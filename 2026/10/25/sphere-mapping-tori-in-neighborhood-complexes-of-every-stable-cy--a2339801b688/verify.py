#!/usr/bin/env python3
"""Finite cross-checks for cyclic-power open-neighborhood nerves.
All claims for unbounded k,n require the paper's symbolic proof.
"""
from itertools import combinations

def faces_of_neighborhood(k, n):
    f=[]
    for i in range(n):
        vs={ (i+d)%n for d in range(-k,k+1) if d }
        f.append(frozenset(vs))
    return f

def beta_modp(k,n,p):
    facets=faces_of_neighborhood(k,n)
    faces=[set() for _ in range(2*k)]
    for facet in facets:
        v=sorted(facet)
        for r in range(1,len(v)+1):
            faces[r-1].update(combinations(v,r))
    fs=[sorted(s) for s in faces]
    ranks=[]
    for d in range(1,2*k):
        idx={f:i for i,f in enumerate(fs[d-1])}
        pivots={}
        for simplex in fs[d]:
            col={idx[simplex[:i]+simplex[i+1:]]:(-1 if i%2 else 1)%p for i in range(len(simplex))}
            while col:
                pv=min(col)
                if pv not in pivots:
                    factor=pow(col[pv],-1,p)
                    pivots[pv]={u:(a*factor)%p for u,a in col.items()}
                    ranks.append(None) if False else None
                    break
                coef=col[pv]
                for u,a in pivots[pv].items():
                    v=(col.get(u,0)-coef*a)%p
                    if v: col[u]=v
                    else: col.pop(u,None)
        ranks.append(len(pivots))
    ranks=[0]+ranks+[0]
    return [len(fs[d])-ranks[d]-ranks[d+1] for d in range(len(fs))]

def local_nerve(k):
    f={i:{j for j in range(i-k,i+k+1) if j!=i} for i in range(-2*k-2,k+2)}
    # Complete intersection of the first k+1 facets vanishes; each k-fold one lives.
    assert not set.intersection(*(f[i] for i in range(k+1)))
    for skipped in range(k+1):
        common=set.intersection(*(f[i] for i in range(k+1) if i!=skipped))
        assert skipped in common
    # The adding-one-more-facet intersection has cone apex 0, translated to center k.
    apex=0
    new=f[k]
    previous=[f[i]&new for i in range(-k,k)]
    assert all((apex in s) or (s <= (f[k]&f[-1])) for s in previous)
    # Direct robust star condition by generating the intersection simplices.
    inter=set()
    for i in range(-k,k):
        a=list(f[i]&new)
        for r in range(1,len(a)+1):
            inter.update(map(frozenset,combinations(a,r)))
    assert all((apex in s) or (s | {apex} in inter) for s in inter)
    # Additional-window nerve: precisely the two consecutive k-faces are absent.
    centers=list(range(k+2))
    for omitted in centers:
        face=set.intersection(*(f[i] for i in centers if i!=omitted))
        assert bool(face)==(0<omitted<k+1), (k,omitted,face)
    assert not set.intersection(*(f[i] for i in centers))

for k in range(2,8):
    local_nerve(k)
    print('LOCAL_NERVE_OK',k)
for k in range(2,6):
    for n in [4*k+1,4*k+2]:
        b101=beta_modp(k,n,101)
        target=[0]*len(b101)
        target[0]=1
        target[1]+=1
        if (k*n)%2==0:
            target[k-1]+=1
            target[k]+=1
        assert b101==target,(k,n,b101,target)
        if (k*n)%2:
            b2=beta_modp(k,n,2)
            t2=[0]*len(b2);t2[0]=1;t2[1]+=1;t2[k-1]+=1;t2[k]+=1
            assert b2==t2,(k,n,b2,t2)
        print('FINITE_HOMOLOGY_OK',k,n,b101)
print('VERIFY_OK_ALL_POWER_CYCLE_NEIGHBORHOODS')
