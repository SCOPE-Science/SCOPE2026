#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

def invariants(a, enumerate_vertices=True):
    a=tuple(sorted(map(Fraction,a), reverse=True))
    d=len(a)
    assert d>=2 and len(set(a))>1
    mean=sum(a,Fraction(0))/d
    s=Fraction(0)
    A=[]
    for x in a:
        s+=x
        A.append(s)
    q=[]
    for k in range(1,d):
        delta=A[k-1]-k*mean
        assert delta>0
        ck2=Fraction(k*(d-k),d)
        q.append(delta*delta/ck2)
    rin2=min(q)
    rout2=sum((x-mean)*(x-mean) for x in a)
    contacts=tuple(k+1 for k,z in enumerate(q) if z==rin2)
    if enumerate_vertices:
        vals={
            sum((x-mean)*(x-mean) for x in p)
            for p in set(permutations(a))
        }
        assert vals=={rout2}
    return rin2,rout2,contacts

cases=0
for d in range(2,8):
    examples=[
        list(range(d,0,-1)),
        [d]+[0]*(d-1),
        [2*d-i*i for i in range(d)],
        [3 if i<d//2 else -2 for i in range(d)],
    ]
    for a in examples:
        if len(set(a))>1:
            invariants(a, True)
            cases+=1

for d in range(2,13):
    a=[d+1-2*i for i in range(1,d+1)]
    rin2,rout2,contacts=invariants(a, False)
    assert rin2==d*(d-1)
    assert rout2==Fraction(d*(d*d-1),3)
    if d==2:
        assert contacts==(1,)
    else:
        assert contacts==(1,d-1)
    cases+=1

print(f"VERIFY_OK schur-horn-radii exact_cases={cases} generic_dimensions=2..7 standard_dimensions=2..12")
