#!/usr/bin/env python3
"""Independent finite checks of dual p-morphism and retraction rank spectra.
Only standard-library Python is required. Usage: python3 verify.py.
"""
from collections import Counter
from itertools import product, combinations_with_replacement
from math import comb, factorial


def surj(n,k):
    if k > n or k < 1:
        return 0
    return sum((-1)**(k-j)*comb(k,j)*j**n for j in range(k+1))


def theoretical(shape):
    m=len(shape)
    q=[[surj(a,c)*surj(b,d) for c,d in shape] for a,b in shape]
    E=Counter(); I=Counter(); supportE=Counter(); supportI=Counter()
    for mask in range(1,1<<m):
        J=[j for j in range(m) if mask>>j & 1]
        count=0
        for sub in range(1<<len(J)):
            L=[j for k,j in enumerate(J) if sub>>k&1]
            weight=1
            for i in range(m):
                weight*=sum(q[i][j] for j in L)
            count+=(-1)**(len(J)-len(L))*weight
        idem=1
        for i in range(m):
            if i not in J:
                idem*=sum(q[i][j] for j in J)
        if count:
            supportE[mask]=count
            E[2**sum(shape[j][0]*shape[j][1] for j in J)]+=count
        if idem:
            supportI[mask]=idem
            I[2**sum(shape[j][0]*shape[j][1] for j in J)]+=idem
    return E,I,supportE,supportI


def worlds(shape):
    vertices=[]
    for comp,(a,b) in enumerate(shape):
        for x in range(a):
            for y in range(b):
                vertices.append((comp,x,y))
    n=len(vertices)
    row_masks=[]; col_masks=[]
    for comp,x,y in vertices:
        row_masks.append(sum(1<<t for t,(k,u,v) in enumerate(vertices) if k==comp and u==x))
        col_masks.append(sum(1<<t for t,(k,u,v) in enumerate(vertices) if k==comp and v==y))
    return vertices,row_masks,col_masks


def check_bounded(f,rs,cs):
    n=len(f)
    for x in range(n):
        a=b=0
        for y in range(n):
            if rs[x]>>y&1: a|=1<<f[y]
            if cs[x]>>y&1: b|=1<<f[y]
        if a!=rs[f[x]] or b!=cs[f[x]]:return False
    return True


def direct(shape,algebra=False):
    vs,rs,cs=worlds(shape); n=len(vs)
    E=Counter(); I=Counter(); sE=Counter(); sI=Counter(); maps=[]
    def modal_diamond(mask, rels):
        return sum(1<<x for x in range(n) if mask&rels[x])
    for f in product(range(n),repeat=n):
        bounded=check_bounded(f,rs,cs)
        if algebra and n<=5:
            # A direct Boolean-power-set test of preservation of both diamonds.
            preimage=[sum(1<<x for x in range(n) if mask>>f[x]&1)
                      for mask in range(1<<n)]
            preserves=True
            for rel in (rs,cs):
                for mask in range(1<<n):
                    if preimage[modal_diamond(mask,rel)] != modal_diamond(preimage[mask],rel):
                        preserves=False;break
                if not preserves:break
            assert preserves==bounded, (shape,f,preserves,bounded)
        if not bounded:continue
        vals=set(f)
        assert all(set(f[x] for x in range(n) if vs[x][0]==i)
                   ==set(x for x in range(n) if vs[x][0]==j)
                   for i in range(len(shape)) for j in [vs[f[next(t for t in range(n) if vs[t][0]==i)]][0]])
        mask=0
        for v in vals: mask|=1<<vs[v][0]
        E[2**len(vals)]+=1;sE[mask]+=1
        idem=all(f[f[x]]==f[x] for x in range(n))
        if idem:
            I[2**len(vals)]+=1;sI[mask]+=1
        maps.append((f,idem))
    return E,I,sE,sI,len(maps)


def minimal_supports(shape):
    m=len(shape)
    types=set(shape)
    minima={u for u in types if not any(v!=u and v[0]<=u[0] and v[1]<=u[1] for v in types)}
    expected_count=2**sum(t not in minima for t in shape)
    for t in minima:
        expected_count*=2**sum(u==t for u in shape)-1
    valid=[]
    for mask in range(1,1<<m):
        if all(any(shape[j]==t for j in range(m) if mask>>j&1) for t in minima):
            valid.append(mask)
    assert len(valid)==expected_count
    return set(valid),minima


def main():
    shapes=[((1,1),),((1,2),),((2,1),),((2,2),),
            ((1,1),(1,1)),((1,2),(2,1)),((1,1),(1,2)),
            ((1,1),(2,1)),((1,1),(1,1),(1,1)),
            ((1,1),(1,2),(2,1)),((1,2),(1,2)),
            ((1,1),(2,2)),((1,1),(1,1),(1,2)),
            ((1,1),(1,1),(1,1),(1,1)),
            ((1,1),(1,1),(1,1),(1,1),(1,1)),
            ((1,3),(2,1)),((1,1),(1,2),(1,2)),
            ((1,1),(1,1),(1,1),(1,2)),
            ((1,2),(2,1),(1,1))]
    total_functions=0; maps=0; tested=0; direct_algebra=0
    for shape in shapes:
        n=sum(a*b for a,b in shape)
        e,i,se,si=theoretical(shape)
        d_e,d_i,d_se,d_si,k=direct(shape,algebra=n<=5)
        assert (e,i,se,si)==(d_e,d_i,d_se,d_si), (shape,e,d_e,i,d_i)
        valid,_=minimal_supports(shape)
        assert valid==set(si)==set(se), (shape,valid,se,si)
        total_functions+=n**n;maps+=k;tested+=1
        if n<=5: direct_algebra+=n**n
    big=((1,2),(1,2),(2,1),(2,2))
    E,I,Se,Si=theoretical(big)
    assert E=={16:64,64:128,256:64,1024:64}
    assert I=={16:16,64:6,256:4,1024:1}
    assert sum(E.values())==320 and sum(I.values())==27
    valid,_=minimal_supports(big)
    assert len(valid)==6 and set(Se)==set(Si)==valid
    shapes_more=[((1,2),(2,1),(2,2)),((1,3),(2,2),(3,1),(3,3)),
                 ((1,1),(1,1),(2,2)),((1,2),(1,2),(1,2),(2,1),(3,3))]
    for shape in shapes_more:
        e,i,se,si=theoretical(shape)
        valid,_=minimal_supports(shape)
        assert set(se)==set(si)==valid
        assert sum(e.values()) == __import__('math').prod(sum(surj(a,c)*surj(b,d) for c,d in shape) for a,b in shape)
    print('VERIFY_OK',tested,'direct_shape_cases',total_functions,'direct_function_tables',
          maps,'bounded_maps',direct_algebra,'direct_algebra_candidate_checks',
          len(shapes_more)+1,'larger_symbolic_support_checks',
          'example_320_endomorphisms_27_idempotents')


def theoretical_nd(shape):
    m=len(shape)
    q=[[__import__('math').prod(surj(a,b) for a,b in zip(shape[i],shape[j]))
        for j in range(m)] for i in range(m)]
    E=Counter();I=Counter();SE=Counter();SI=Counter()
    for mask in range(1,1<<m):
        J=[j for j in range(m) if mask>>j&1]
        count=0
        for sub in range(1<<len(J)):
            L=[j for u,j in enumerate(J) if sub>>u&1]
            w=__import__('math').prod(sum(q[i][j] for j in L) for i in range(m))
            count+=(-1)**(len(J)-len(L))*w
        idem=__import__('math').prod(sum(q[i][j] for j in J)
                                  for i in range(m) if i not in J)
        degree=2**sum(__import__('math').prod(shape[j]) for j in J)
        if count: E[degree]+=count;SE[mask]=count
        if idem: I[degree]+=idem;SI[mask]=idem
    return E,I,SE,SI


def direct_nd(shape):
    d=len(shape[0]);assert d>=3
    vertices=[]
    for comp,dims in enumerate(shape):
        for coords in product(*[range(k) for k in dims]):
            vertices.append((comp,coords))
    n=len(vertices);relations=[]
    for t in range(d):
        relations.append([sum(1<<j for j,(c2,y) in enumerate(vertices)
                  if c2==c1 and all(x[k]==y[k] for k in range(d) if k!=t))
                  for c1,x in vertices])
    E=Counter();I=Counter();SE=Counter();SI=Counter();count=0
    for f in product(range(n),repeat=n):
        if any({f[y] for y in range(n) if rel[x]>>y&1} !=
               {y for y in range(n) if rel[f[x]]>>y&1}
               for rel in relations for x in range(n)):
            continue
        count+=1
        image=set(f);mask=0
        for j in image:mask|=1<<vertices[j][0]
        degree=2**len(image)
        E[degree]+=1;SE[mask]+=1
        if all(f[f[x]]==f[x] for x in range(n)):
            I[degree]+=1;SI[mask]+=1
    return E,I,SE,SI,count,n**n


def test_nd():
    cases=[((1,1,2),),((1,1,2),(1,2,1)),
           ((1,1,1),(1,1,2),(1,2,1)),
           ((1,1,2),(2,1,1)),((2,1,2),),
           ((1,1,1),(2,2,1))]
    total=0;maps=0
    for shape in cases:
        e,i,se,si=theoretical_nd(shape)
        de,di,dse,dsi,k,nfunc=direct_nd(shape)
        assert (e,i,se,si)==(de,di,dse,dsi), (shape,e,de,i,di)
        total+=nfunc;maps+=k
    print('ND_VERIFY_OK',len(cases),'three_modal_shapes',total,'direct_tables',maps,'bounded_maps')


def exhaustive_normal_form_example():
    shape=((1,2),(1,2),(2,1),(2,2))
    vertices,rows,cols=worlds(shape);index={v:i for i,v in enumerate(vertices)}
    choices=[]
    for source,(a,b) in enumerate(shape):
        opts=[]
        for target,(c,d) in enumerate(shape):
            for f in product(range(c),repeat=a):
                if len(set(f))!=c:continue
                for g in product(range(d),repeat=b):
                    if len(set(g))!=d:continue
                    opts.append((target,f,g))
        choices.append(opts)
    E=Counter();I=Counter(); seen=set()
    for selected in product(*choices):
        f=[]
        for comp,x,y in vertices:
            target,p,q=selected[comp]
            f.append(index[(target,p[x],q[y])])
        f=tuple(f)
        assert f not in seen
        seen.add(f)
        assert check_bounded(f,rows,cols)
        exponent=2**len(set(f))
        E[exponent]+=1
        if all(f[f[x]]==f[x] for x in range(len(f))): I[exponent]+=1
    e,i,_,_=theoretical(shape)
    assert E==e and I==i and len(seen)==320
    print('LARGE_EXAMPLE_OK',len(seen),'distinct_structural_maps_rechecked')

if __name__=='__main__':
    main()
    test_nd()
    exhaustive_normal_form_example()
