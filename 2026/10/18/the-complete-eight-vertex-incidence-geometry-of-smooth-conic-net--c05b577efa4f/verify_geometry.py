#!/usr/bin/env python3
"""Independent F8 projective-point verification of Frobenius triangles."""
from itertools import product,combinations
from collections import Counter

def mul(a,b):
    p=0
    while b:
        if b&1:p^=a
        a<<=1
        if a&8:a^=11
        b>>=1
    return p

def pw(a,n):
    t=1
    for _ in range(n):t=mul(t,a)
    return t

def norm(P):
    k=next(x for x in P if x)
    inv=pw(k,6)
    return tuple(mul(x,inv) for x in P)

def frob(P):return norm(tuple(mul(x,x) for x in P))
points=sorted({norm(t) for t in product(range(8),repeat=3) if any(t)})
assert len(points)==73

def det(A,B,C):
    R=(A,B,C)
    v=0
    for k in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)):
        v^=mul(mul(R[0][k[0]],R[1][k[1]]),R[2][k[2]])
    return v

triples=set()
for P in points:
    if frob(P)!=P:
        T=frozenset((P,frob(P),frob(frob(P))))
        assert len(T)==3
        triples.add(T)
assert len(triples)==22
noncollinear=sorted([tuple(sorted(T)) for T in triples if det(*tuple(T))],key=str)
assert len(noncollinear)==8

def conic(F,P):
    x,y,z=P
    t=(mul(x,x),mul(y,y),mul(z,z),mul(x,y),mul(x,z),mul(y,z))
    return __import__('functools').reduce(lambda acc,k:acc^t[k],(i for i in range(6) if F>>i&1),0)

def singular_over_f8(F):
    a,b,c,d,e,f=((F>>i)&1 for i in range(6))
    for x,y,z in points:
        if conic(F,(x,y,z))==0 and (d*y ^ e*z)==0 and (d*x ^ f*z)==0 and (e*x ^ f*y)==0:
            return True
    return False

smooth={F for F in range(1,64) if not singular_over_f8(F)}
assert len(smooth)==28
incidence={T:frozenset(F for F in smooth if all(conic(F,P)==0 for P in T)) for T in noncollinear}
assert all(len(v)==7 for v in incidence.values())
assert all(sum(F in v for v in incidence.values())==2 for F in smooth)
assert all(len(A&B)==1 for A,B in combinations(incidence.values(),2))
assert len({frozenset(v) for v in incidence.values()})==8
F2points=[P for P in points if frob(P)==P]
assert len(F2points)==7
assert all(sum(conic(F,P)==0 for P in F2points)==3 for F in smooth)
unique_pencils=set()
for T,forms in incidence.items():
    for P in F2points:
        membership=frozenset(F for F in forms if conic(F,P)==0)
        assert len(membership)==3
        unique_pencils.add(membership)
assert len(unique_pencils)==56
assert all(sum(sum(conic(F,P)==0 for F in pencil)==3 for P in F2points)==1 for pencil in unique_pencils)
print('projective_F8_points',len(points))
print('degree_three_Frobenius_triples',len(triples))
print('collinear_triples',len(triples)-len(noncollinear))
print('noncollinear_triples',len(noncollinear))
print('smooth_conics_direct_F8_singularity_test',len(smooth))
print('smooth_conics_through_each_triangle',Counter(map(len,incidence.values())))
print('triangles_per_smooth_conic',Counter(sum(F in v for v in incidence.values()) for F in smooth))
print('common_conic_per_two_triangles',Counter(len(A&B) for A,B in combinations(incidence.values(),2)))
print('smooth_pencils_by_triangle_and_rational_point',len(unique_pencils))
print('rational_common_basepoint_count_per_pencil',Counter(sum(all(conic(F,P)==0 for F in pencil) for P in F2points) for pencil in unique_pencils))
