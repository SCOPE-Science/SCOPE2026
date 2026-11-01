#!/usr/bin/env python3
"""Exact finite verification of rational S5 homology for 3 points on the Petersen graph.

Requires only Python standard library. All computations use integer coefficients,
finite-field Gaussian elimination, and character orthogonality; no floating point.
"""
from itertools import combinations, combinations_with_replacement, product
from collections import Counter, defaultdict
from math import factorial

VERTICES=list(combinations(range(5),2))
VINDEX={s:i for i,s in enumerate(VERTICES)}
EDGES=[(i,j) for i in range(10) for j in range(i+1,10)
       if not set(VERTICES[i]).intersection(VERTICES[j])]
EINDEX={s:i for i,s in enumerate(EDGES)}
INCIDENT=[sorted(i for i,(u,w) in enumerate(EDGES) if v in (u,w)) for v in range(10)]
assert len(VERTICES)==10 and len(EDGES)==15 and all(len(x)==3 for x in INCIDENT)
PARTITIONS=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
EXPECTED_H2=[25,-3,1,-2,0,1,0]
EXPECTED_H1=[6,0,-2,0,0,0,1]


def representative(mu):
    p=[];s=0
    for length in mu:
        p.extend(range(s+1,s+length));p.append(s);s+=length
    return tuple(p)


def graph_action(p):
    vertices=tuple(VINDEX[tuple(sorted((p[a],p[b])))] for a,b in VERTICES)
    edges=tuple(EINDEX[tuple(sorted((vertices[a],vertices[b])))] for a,b in EDGES)
    return vertices,edges


def bases():
    result={}
    for d in range(4):
        result[d]=[(tuple(zip(vs,le)),poly)
          for vs in combinations(range(10),d)
          for le in product((1,2),repeat=d)
          for poly in combinations_with_replacement(range(15),3-d)]
    assert tuple(len(result[d]) for d in range(4))==(680,2400,2700,960)
    return result


def boundaries(basis):
    idx={d:{state:i for i,state in enumerate(basis[d])} for d in range(4)}
    out={}
    for d in range(1,4):
        cols=[]
        for selected,mon in basis[d]:
            c=defaultdict(int)
            for j,(v,leg) in enumerate(selected):
                smaller=selected[:j]+selected[j+1:]
                sign=(-1)**j
                c[idx[d-1][(smaller,tuple(sorted(mon+(INCIDENT[v][leg],))))]]+=sign
                c[idx[d-1][(smaller,tuple(sorted(mon+(INCIDENT[v][0],))))]]-=sign
            cols.append({k:v for k,v in c.items() if v})
        out[d]=cols
    return out


def rank_mod(cols,p):
    pivots={}
    for col in cols:
        a={i:x%p for i,x in col.items() if x%p}
        while a:
            j=max(a)
            b=pivots.get(j)
            if b is None:
                inv=pow(a[j],-1,p)
                pivots[j]={k:x*inv%p for k,x in a.items()}
                break
            factor=a[j]
            for k,x in b.items():
                r=(a.get(k,0)-factor*x)%p
                if r:a[k]=r
                elif k in a:del a[k]
    return len(pivots)


def check_squared_zero(ds):
    for d in (2,3):
        below=ds[d-1]
        for col in ds[d]:
            z=defaultdict(int)
            for i,a in col.items():
                for j,b in below[i].items():z[j]+=a*b
            assert all(v==0 for v in z.values())


def graph_cycles_rank():
    # Every Petersen five-cycle avoids five vertices where the two parked
    # particles can be located. Their classes generate all graph cycles.
    from itertools import permutations
    seen=set();chains=[]
    for t in permutations(range(10),5):
        if any(tuple(sorted((t[i],t[(i+1)%5]))) not in EINDEX for i in range(5)):continue
        rotations=[tuple(t[j:]+t[:j]) for j in range(5)]
        rev=tuple(reversed(t))
        rotations += [tuple(rev[j:]+rev[:j]) for j in range(5)]
        canon=min(rotations)
        if canon in seen:continue
        seen.add(canon)
        co=defaultdict(int)
        for i in range(5):
            a,b=canon[i],canon[(i+1)%5]
            co[EINDEX[tuple(sorted((a,b)))]]+=1 if a<b else -1
        chains.append(dict(co))
    count=len(chains)
    result=rank_mod(chains,3)
    return count,result


def direct_traces(vp,ep,basis):
    result=[]
    for d in range(4):
        total=0
        for selected,mon in basis[d]:
            if tuple(sorted(ep[e] for e in mon))!=mon:continue
            sites=[v for v,leg in selected]
            mapped=[vp[v] for v in sites]
            if set(mapped)!=set(sites):continue
            sign=(-1)**sum(mapped[i]>mapped[j] for i in range(d) for j in range(i+1,d))
            original=dict(selected)
            for v,leg in selected:
                target=vp[v]
                need=INCIDENT[target][original[target]]
                src=INCIDENT[v]
                sign*=int(ep[src[leg]]==need)-int(ep[src[0]]==need)
                if not sign:break
            total+=sign
        result.append(total)
    return result


def orbits(perm):
    seen=set();res=[]
    for first in range(len(perm)):
        if first in seen:continue
        cyc=[];j=first
        while j not in seen:
            seen.add(j);cyc.append(j);j=perm[j]
        res.append(cyc)
    return res


def generating_lefschetz(vp,ep):
    # Alternating chain trace: local augmentation traces at vertex cycles,
    # divided by edge-permutation symmetric-power cycle factors.
    coeff=[1,0,0,0]
    for orb in orbits(vp):
        length=len(orb);v=orb[0]
        mapped=list(range(15))
        for _ in range(length):mapped=[ep[x] for x in mapped]
        tr=sum(mapped[e]==e for e in INCIDENT[v])-1
        for i in range(3,length-1,-1):coeff[i]-=tr*coeff[i-length]
    for orb in orbits(ep):
        length=len(orb)
        for i in range(length,4):coeff[i]+=coeff[i-length]
    return coeff[3]


def partitions_of(n,limit=None):
    if n==0:
        yield ();return
    for part in range(min(n,limit if limit is not None else n),0,-1):
        for rest in partitions_of(n-part,part):yield (part,)+rest


def rim_removals(lam,k):
    for nu in partitions_of(sum(lam)-k):
        if len(nu)>len(lam) or any(nu[i]>lam[i] for i in range(len(nu))):continue
        removed={(r,c) for r,m in enumerate(lam) for c in range(nu[r] if r<len(nu) else 0,m)}
        if len(removed)!=k:continue
        if any({(r+1,c),(r,c+1),(r+1,c+1)}<=removed for r,c in removed):continue
        active={next(iter(removed))};stack=list(active)
        while stack:
            r,c=stack.pop()
            for z in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if z in removed and z not in active:active.add(z);stack.append(z)
        if active==removed:
            yield nu,(-1)**(len({r for r,c in removed})-1)


def schur_character(lam,mu):
    if not mu:return int(not lam)
    return sum(s*schur_character(nu,mu[1:]) for nu,s in rim_removals(lam,mu[0]))


def run():
    basis=bases();d=boundaries(basis)
    check_squared_zero(d)
    ranks={p:[rank_mod(d[j],p) for j in (1,2,3)] for p in (2,3,5,7)}
    assert ranks[3]==[679,1715,960]
    assert ranks[2]==[679,1714,960]
    assert ranks[5]==ranks[7]==ranks[3]
    count,crank=graph_cycles_rank()
    assert count==12 and crank==6
    print('chain_dimensions',tuple(len(basis[j]) for j in range(4)))
    print('boundary_ranks',ranks)
    print('boundary_compositions_zero',True)
    print('five_cycles',count,'span_graph_cycle_rank',crank)
    values=[];ones=[];Ls=[]
    for mu in PARTITIONS:
        vp,ep=graph_action(representative(mu))
        direct=direct_traces(vp,ep,basis)
        L=sum((-1)**j*t for j,t in enumerate(direct))
        assert L==generating_lefschetz(vp,ep)
        h1=sum((1 if vp[a]==a else -1) for j,(a,b) in enumerate(EDGES) if ep[j]==j)-sum(vp[v]==v for v in range(10))+1
        h2=L-1+h1
        values.append(h2);ones.append(h1);Ls.append(L)
        print('cycle_type',mu,'chain_traces',tuple(direct),'L',L,'H1',h1,'H2',h2)
    assert values==EXPECTED_H2 and ones==EXPECTED_H1
    decomp={}
    for lam in PARTITIONS:
        chr=[schur_character(lam,mu) for mu in PARTITIONS]
        denom=[]
        for mu in PARTITIONS:
            z=1
            for length,multiplicity in Counter(mu).items():z*=length**multiplicity*factorial(multiplicity)
            denom.append(factorial(5)//z)
        n=sum(denom[j]*chr[j]*values[j] for j in range(7))
        assert n%120==0
        decomp[lam]=n//120
        assert decomp[lam]>=0
    
    assert decomp=={(1,1,1,1,1):0,(2,1,1,1):1,(2,2,1):2,(3,1,1):1,(3,2):1,(4,1):0,(5,):0}
    print('H2_Specht_decomposition',decomp)
    print('full_symmetry_invariant_dimension',decomp[(5,)])
    print('VERIFY_OK')

if __name__=='__main__':run()
