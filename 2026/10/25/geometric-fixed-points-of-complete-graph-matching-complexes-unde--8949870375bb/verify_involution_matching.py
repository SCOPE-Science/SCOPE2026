"""Independent finite checks for involution-fixed matching complexes.

Standard-library only; not a proof for unbounded parameters.
"""
from itertools import combinations
from math import prod


def orbit_model(m, r):
    """Edge orbits whose union is a matching under m two-cycles and r fixed points."""
    n = 2*m+r
    def tau(i):
        return i ^ 1 if i < 2*m else i
    unseen = set(combinations(range(n),2))
    out=[]
    while unseen:
        e=min(unseen)
        e2=tuple(sorted((tau(e[0]),tau(e[1]))))
        o=frozenset((e,e2))
        unseen-=o
        support=[v for edge in o for v in edge]
        if len(support)==len(set(support)):
            out.append((tuple(sorted(o)),frozenset(support)))
    return sorted(out)


def all_faces(model):
    faces=[()]
    for i in range(len(model)):
        addition=[]
        support_i=model[i][1]
        for face in faces:
            if not any(model[j][1] & support_i for j in face):
                addition.append(face+(i,))
        faces.extend(addition)
    return faces


def rank_mod2(columns):
    pivots={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p]=x
                break
    return len(pivots)


def reduced_betti(model):
    allf=all_faces(model)
    bysize={k:sorted(f for f in allf if len(f)==k) for k in range(len(model)+1)}
    bysize={k:v for k,v in bysize.items() if v}
    rank={}
    for k in range(1,max(bysize)+1):
        idx={f:i for i,f in enumerate(bysize[k-1])}
        cols=(sum(1<<idx[f[:a]+f[a+1:]] for a in range(k)) for f in bysize[k])
        rank[k]=rank_mod2(cols)
    betti={k-1:len(faces)-rank.get(k,0)-rank.get(k+1,0)
           for k,faces in bysize.items() if k>=1}
    return {i:v for i,v in betti.items() if v}, len(allf)


def target(m,r):
    if m%2:
        return {}
    if m==0:
        return reduced_betti(orbit_model(0,r))[0]
    k=m//2
    a=prod(2*(2*j-1) for j in range(1,k+1))
    if r<=1:
        return {k-1:a}
    if r==2:
        return {}
    smaller,_=reduced_betti(orbit_model(0,r))
    return {d+k:a*b for d,b in smaller.items()}


def check_support(m,r):
    model=orbit_model(m,r)
    labels=set(range(2*m+r))
    assert all(len(o)==1 or len(o)==2 for o,_ in model)
    assert all(all(x in labels for edge in o for x in edge) for o,_ in model)
    assert len(model)==m*m+r*(r-1)//2
    for orbit,support in model:
        if len(orbit)==1:
            e=orbit[0]
            assert (e[0]<2*m and e[1]==(e[0]^1)) or (e[0]>=2*m)
        else:
            assert len(support)==4
            assert {v//2 for v in support} <= set(range(m))
            assert len({v//2 for v in support})==2


for m,r in [(1,0),(2,0),(3,0),(4,0),(1,3),(2,1),(2,2),(2,3),(2,4),
            (2,5),(3,4),(4,2),(4,3),(4,4)]:
    check_support(m,r)
    got, faces=reduced_betti(orbit_model(m,r))
    expect=target(m,r)
    assert got==expect, (m,r,got,expect)
    print('case',m,r,'faces',faces,'reduced_mod2',got)

for m in (5,6,7,8):
    check_support(m,0)
    model=orbit_model(m,0)
    count_by_size=[0]*(m+1)
    for f in all_faces(model):
        count_by_size[len(f)]+=1
    reduced_chi=-sum((-1)**k*count_by_size[k] for k in range(m+1))
    expected=0 if m%2 else ((-1)**(m//2-1))*prod(2*(2*j-1) for j in range(1,m//2+1))
    assert reduced_chi==expected,(m,reduced_chi,expected)
    print('Euler',m,'faces',sum(count_by_size),'reduced_chi',reduced_chi)
print('MATCHING_INVOLUTION_FIXED_COMPLEX_VERIFIED')
