"""Exact finite support and Walsh-certificate checks for the five-vertex cut polytope.
Scientific proof for arbitrary graphs is in RESULT.md; this executable verifies the base algebra.
"""
from itertools import combinations
from fractions import Fraction
E = list(combinations(range(5),2))
W = [tuple(i for i in range(4) if m >> i & 1) for m in range(16)]
V = [tuple(int(((m >> i) & 1) != ((m >> j) & 1)) for i,j in E) for m in range(16)]
assert len(set(V)) == 16
A = []
for w in W:
    indicator = tuple(int((i in w) != (j in w)) for i,j in E)
    q = sum(indicator)
    a = tuple(1-2*t for t in indicator)
    vals = [sum(aj*vj for aj,vj in zip(a,v)) for v in V]
    assert set(vals).issubset(set(range(-q,7-q)))
    assert min(vals)==-q and max(vals)==6-q
    assert sum(a)==10-2*q
    assert Fraction(sum(a),2)==5-q
    assert Fraction(5-q+q, (6-q)-(5-q))==5
    A.append(a)
assert sum(len([1 for w in W if len(w)==k]) for k in range(5))==16
assert sum(sum(int((i in w)!=(j in w)) for i,j in E) for w in W)==80
assert all(sum(row[j] for row in A)==0 for j in range(10))
assert all(sum(A[w][i]*A[w][j] for w in range(16))==(16 if i==j else 0) for i in range(10) for j in range(10))
for tri in combinations(range(5),3):
    T=list(combinations(tri,2))
    for w in [tuple(),(tri[0],),(tri[1],),(tri[2],)]:
        d=[int((i in w)!=(j in w)) for i,j in T]
        a=tuple(1-2*t for t in d)
        q=sum(d)
        vals=[sum(a[t]*v[E.index(edge)] for t,edge in enumerate(T)) for v in V]
        assert min(vals)==-q and max(vals)==2-q
        assert Fraction(sum(a),2)==Fraction(3,2)-q
        assert Fraction(Fraction(3,2),Fraction(1,2))==3
print('VERIFY_OK: 16 pentagon switches, 40 triangle switches, exact support extrema and full Walsh orthogonality.')
# Strict two-clique-sum of K5 and a triangle: 6 vertices, 12 edges.
E6=E+[(0,5),(1,5)]
assert len(E6)==12
T=[(0,1),(0,5),(1,5)]
K5_switches=[]
for w in W:
    d=[int((i in w)!=(j in w)) for i,j in E]
    K5_switches.append((tuple(1-2*t for t in d),6-sum(d)))
T_switches=[]
for w in [tuple(),(0,),(1,),(5,)]:
    d=[int((i in w)!=(j in w)) for i,j in T]
    T_switches.append((tuple(1-2*t for t in d),2-sum(d)))
centers=[(Fraction(1,2),Fraction(1,2)), (Fraction(13,24),Fraction(11,24))]
for u,v in centers:
    c={e:Fraction(1,2) for e in E}
    c[(0,5)],c[(1,5)]=u,v
    for mask in range(32):
        x={e:Fraction(int(((mask>>i)&1)!=((mask>>j)&1))) for e in E6 for i,j in [e]}
        z={e:c[e]-(x[e]-c[e])/5 for e in E6 for i,j in [e]}
        for a,b in K5_switches:
            assert sum(ai*z[e] for ai,e in zip(a,E))<=b
        for a,b in T_switches:
            assert sum(ai*z[e] for ai,e in zip(a,T))<=b
print('VERIFY_OK: two distinct centers of the 12-dimensional K5-triangle edge-clique-sum satisfy all 32 reflected cut vertices.')
