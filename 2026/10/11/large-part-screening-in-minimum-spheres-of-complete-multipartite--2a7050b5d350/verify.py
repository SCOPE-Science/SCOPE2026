#!/usr/bin/env python3
"""Exact finite checks of multipartite stable-set circumballs."""
from fractions import Fraction as Q
from itertools import product


def parts(total, minimum=1):
    if total == 0:
        yield ()
        return
    for a in range(minimum, total + 1):
        for tail in parts(total-a, a):
            yield (a,) + tail


def root(ds):
    k = len(ds)
    assert k >= 3 and min(ds) >= 1
    candidates = []
    for m in range(3, k+1):
        top = sorted(ds, reverse=True)[:m]
        H = sum((Q(1,a) for a in top), Q(0))
        h = Q(m-2,1)/H
        if sum(a>h for a in ds)==m:
            assert sum((max(Q(0), 1-h/Q(a)) for a in ds), Q(0))==2
            candidates.append(h)
    assert len(candidates)==1,(ds,candidates)
    return candidates[0]


def check(ds, exhaustive=False):
    k=len(ds)
    h=root(ds)
    ps=[max(Q(0),(1-h/Q(a)))/2 for a in ds]
    assert sum(ps,Q(0))==1
    active=[i for i,a in enumerate(ds) if a>h]
    m=len(active)
    assert m>=3
    B=sum((a*p*p for a,p in zip(ds,ps)),Q(0))
    R2=B+h
    H=sum((Q(1,ds[i]) for i in active),Q(0))
    A=sum(ds[i] for i in active)
    assert h==Q(m-2)/H
    assert R2==(Q(A)-(Q(m-2)**2)/H)/4

    # Every full-class contact used with positive coefficient is at squared
    # distance R2 and the weighted mean of all full-class points equals c.
    assert all((ps[i]==0 or (B+ds[i]*(1-2*ps[i])==R2)) for i in range(k))
    assert R2>0 and 0<h<max(ds)

    for i,a in enumerate(ds):
        for s in range(a+1):
            d2=B+s*(1-2*ps[i])
            assert d2<=R2
            assert (d2==R2)==(s==a and a>=h)
        if exhaustive:
            # Distances computed from the actual binary vectors, not just by
            # the aggregate formula above.
            c=[p for j,p in enumerate(ps) for _ in range(ds[j])]
            offset=sum(ds[:i]); N=sum(ds)
            for bits in product((0,1), repeat=a):
                v=[0]*N
                v[offset:offset+a]=bits
                actual=sum(((Q(z)-c[t])**2 for t,z in enumerate(v)),Q(0))
                assert actual==B+sum(bits)*(1-2*ps[i])

    # Exact global minimality witness (weighted centers and their variance).
    c=[p for i,p in enumerate(ps) for _ in range(ds[i])]
    N=len(c)
    # The center is the weighted average of contacts v_i.
    witness=[Q(0)]*N
    for i,a in enumerate(ds):
        for j in range(sum(ds[:i]), sum(ds[:i+1])):
            witness[j]+=ps[i]
    assert witness==c
    # Check weighted squared-distance identity at several independent points.
    for y in ([Q(0)]*N, [Q(1,2)]*N, c, [Q(j%3,4) for j in range(N)]):
        lhs=Q(0)
        offset=0
        for i,a in enumerate(ds):
            vi=[Q(0)]*N
            vi[offset:offset+a]=[Q(1)]*a
            lhs+=ps[i]*sum(((vi[t]-y[t])**2 for t in range(N)),Q(0))
            offset+=a
        rhs=R2+sum(((y[t]-c[t])**2 for t in range(N)),Q(0))
        assert lhs==rhs,(ds,y,lhs,rhs)
    return h,R2,ps

profiles=0
for total in range(3,15):
    for ds in parts(total):
        if len(ds)<3:continue
        check(ds,exhaustive=True)
        profiles+=1

# Sharp zero-weight contact boundary and plateau with arbitrary extra parts.
h,r2,p=check((1,2,3,6))
assert h==1 and r2==Q(5,2) and p[0]==0
for many in range(0,31):
    ds=(10,10,10)+(1,)*many
    h,r2,p=check(ds)
    assert h==Q(10,3) and r2==Q(20,3)
    assert p[:3]==[Q(1,3)]*3 and all(x==0 for x in p[3:])

# Different active-count profiles, including ties on the inactive boundary.
for ds in [(1,1,1),(1,5,5,5),(1,2,3,4),(2,3,5,7,11),
           (1,1,10,10,10),(1,2,3,6),(3,3,3,3,3)]:
    check(ds)

print(f'VERIFY_OK multipartite-STAB-circumball exact_profiles={profiles} complete_binary_vertex_enumeration=yes rational_active_set=yes contact_certificate=yes screening_plateau=yes')
