"""Build integral cellular chain complex of the free D5 quotient of Hom(C5,Kq).
All computations use exact integer arithmetic and the product-of-simplices CW structure.
"""
from itertools import product
from collections import Counter

def actions(n=5):
    # old position -> new position
    return [tuple((i+k)%n for i in range(n)) for k in range(n)]+[tuple((k-i)%n for i in range(n)) for k in range(n)]

def action(cell,perm):
    vals=[None]*5
    for i,p in enumerate(perm): vals[p]=cell[i]
    return tuple(vals)

def oriented_sign(cell,perm):
    # induced sign permutation of factors, each factor dimension |S|-1
    dims=[x.bit_count()-1 for x in cell]
    flips=sum(dims[i]*dims[j] for i in range(5) for j in range(i+1,5) if perm[i]>perm[j])
    return -1 if flips%2 else 1

def compute(q=5):
    ms=range(1,1<<q)
    comp={x:[y for y in ms if not x&y] for x in ms}
    orbits={}
    aa=actions()
    cells=Counter()
    def gen(c):
        if len(c)==5:
            if c[0]&c[4]:return
            cc=tuple(c)
            canon=min(action(cc,g) for g in aa)
            orbits.setdefault(canon,None)
            cells[sum(x.bit_count()-1 for x in cc)]+=1
            return
        for x in (ms if not c else comp[c[-1]]):
            if len(c)==4 and x&c[0]:continue
            gen(c+[x])
    gen([])
    reps=sorted(orbits, key=lambda cc:(sum(x.bit_count()-1 for x in cc),cc))
    bydim={d:[cc for cc in reps if sum(x.bit_count()-1 for x in cc)==d] for d in sorted(set(sum(x.bit_count()-1 for x in cc) for cc in reps))}
    lookup={cell:(d,i) for d,li in bydim.items() for i,cell in enumerate(li)}
    boundaries={}
    for d,li in bydim.items():
        if not d:continue
        cols=[]
        for cc in li:
            chain=Counter()
            dim_before=0
            for j,x in enumerate(cc):
                elem=[k for k in range(q) if x>>k&1]
                if len(elem)>=2:
                    for k,t in enumerate(elem):
                        fc=tuple((x^(1<<t)) if h==j else cc[h] for h in range(5))
                        can,perm=min((action(fc,g),g) for g in aa)
                        if lookup[can][0]!=d-1:raise Exception('degree mismatch')
                        s=(-1 if (dim_before+k)%2 else 1)*oriented_sign(fc,perm)
                        chain[lookup[can][1]]+=s
                dim_before+=len(elem)-1
            cols.append({i:c for i,c in chain.items() if c})
        boundaries[d]=cols
    return cells,bydim,boundaries

def sparse_rank_mod2(cols):
    piv={}
    for c in cols:
        v=0
        for r,a in c.items():
            if a%2:v^=1<<r
        while v:
            p=v.bit_length()-1
            if p not in piv:piv[p]=v;break
            v^=piv[p]
    return len(piv)

def sparse_rank_modp(cols,p):
    piv={}
    for c in cols:
        v={r:a%p for r,a in c.items() if a%p}
        while v:
            i=max(v)
            if i not in piv:
                factor=pow(v[i],-1,p)
                piv[i]={r:(a*factor)%p for r,a in v.items()}
                break
            fac=v[i]
            for r,a in piv[i].items():
                t=(v.get(r,0)-fac*a)%p
                if t:v[r]=t
                else:v.pop(r,None)
    return len(piv)

def chain_check(boundaries):
    for d in range(2,1+max(boundaries)):
        if d not in boundaries or d-1 not in boundaries:continue
        for col in boundaries[d]:
            r=Counter()
            for i,a in col.items():
                for j,b in boundaries[d-1][i].items():r[j]+=a*b
            if any(r.values()):return False,d,r
    return True


def integer_unit_reduce(columns,nrows, verbose=False):
    """Unimodular Schur reduction of all unit entries, preserving nonunit Smith factors.
    Only altered presentation, no homology inference without full residual SNF.
    """
    import heapq,time
    tt=__import__('time').monotonic()
    cols=[dict(c) for c in columns]
    rows=[set() for _ in range(nrows)]
    for j,c in enumerate(cols):
        for i,v in c.items():
            if not v:raise AssertionError('zero entry')
            rows[i].add(j)
    aliveC=set(range(len(cols)));aliveR=set(range(nrows))
    nums=0;mx=1;growth=0
    while True:
        best=None;cost=float('inf')
        # degree one rows are always cost zero, and cheap to choose
        for i in aliveR:
            if len(rows[i])==1:
                j=next(iter(rows[i]));x=cols[j][i]
                if abs(x)==1: best=(i,j);break
        if best is None:
            for j in aliveC:
                if len(cols[j])==1:
                    i=next(iter(cols[j]));x=cols[j][i]
                    if abs(x)==1:best=(i,j);break
        if best is None:
            for j in aliveC:
                c=cols[j]
                if not c:continue
                for i,v in c.items():
                    if abs(v)==1:
                        t=(len(c)-1)*(len(rows[i])-1)
                        if t<cost:
                            cost=t;best=(i,j)
                            if not cost:break
                if cost==0:break
        if best is None:break
        i,j=best;sgn=cols[j][i]
        row_neighbors=[(k,cols[k][i]) for k in rows[i] if k!=j]
        col_neighbors=[(h,v) for h,v in cols[j].items() if h!=i]
        # all Schur updates
        for k,b in row_neighbors:
            cb=cols[k]
            for h,a in col_neighbors:
                nv=cb.get(h,0)-a*b*sgn
                if nv:
                    cb[h]=nv;rows[h].add(k)
                    mx=max(mx,abs(nv))
                else:
                    cb.pop(h,None);rows[h].discard(k)
            cb.pop(i,None)
        # remove pivot column/row
        for h,a in col_neighbors:rows[h].discard(j)
        rows[i].clear();cols[j].clear()
        aliveC.remove(j);aliveR.remove(i)
        nums+=1
        if verbose and nums%200==0:print('pivots',nums,'residual',len(aliveR),len(aliveC),'max',mx,'t',round(__import__('time').monotonic()-tt,2),flush=True)
    remaining_cols=[]
    active_rows=sorted(aliveR);rowmap={i:k for k,i in enumerate(active_rows)}
    for j in sorted(aliveC):remaining_cols.append({rowmap[i]:v for i,v in cols[j].items()})
    return nums,remaining_cols,len(active_rows),mx



def verify_integral_homology():
    from functools import reduce
    from math import gcd
    for q,cell_expect,unit_expect,torsion_expect in [
        (4,(240,780,840,300),(23,54,29),(0,4,0)),
        (5,(1020,5700,13000,15000,8750,2070),(101,468,831,667,206),(0,2,0,5,2)),
    ]:
        original,bydim,boundaries=compute(q)
        assert tuple(original[d] for d in range(len(original)))==cell_expect
        assert tuple(len(bydim[d]) for d in range(len(original)))==tuple(x//10 for x in cell_expect)
        # Every product cell has a free orbit under the ten dihedral symmetries.
        group=actions()
        for rep in (x for arr in bydim.values() for x in arr):
            assert len({action(rep,g) for g in group})==10
        assert chain_check(boundaries) is True
        units=[];torsion=[];ranks=[]
        for d in range(1,len(original)):
            u,residual,nr,mx=integer_unit_reduce(boundaries[d],len(bydim[d-1]))
            entries=[v for col in residual for v in col.values()]
            gram=reduce(gcd,entries,0)
            units.append(u);torsion.append(gram)
            nonzero=[c for c in residual if c]
            if nonzero:
                base=nonzero[0]
                # Exact residual rank-one certificate: all nonzero columns equal base or -base.
                assert all(c==base or c=={i:-v for i,v in base.items()} for c in nonzero)
                assert len(set(map(abs,entries)))==1 and gram in (2,4,5)
                ranks.append(u+1)
            else:
                ranks.append(u)
        assert tuple(units)==unit_expect,(q,units)
        assert tuple(torsion)==torsion_expect,(q,torsion)
        if q==4:
            assert ranks==[23,55,29]
            print('CONTROL_Q4: quotient ranks',ranks,'torsion in H1 = Z/4',flush=True)
        else:
            assert ranks==[101,469,831,668,207]
            assert [len(bydim[d])- (0 if d==0 else ranks[d-1])-(0 if d==5 else ranks[d]) for d in range(6)]==[1,0,0,1,0,0]
            print('HOM_C5_K5: original cells',cell_expect,'quotient cells',tuple(len(bydim[d]) for d in range(6)))
            print('HOM_C5_K5: unit pivots',units,'nonunit invariant factors',torsion,'integer ranks',ranks)
            print('HOM_C5_K5: H0=Z H1=Z/2 H2=0 H3=Z+Z/5 H4=Z/2 H5=0')
    print('PENTAGON_DIHEDRAL_INTEGRAL_HOMOLOGY_OK')

if __name__ == '__main__':
    verify_integral_homology()
