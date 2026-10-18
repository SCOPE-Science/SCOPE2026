"""Exact-rational tests for the planar orthogonal two-gradient robustness theorem.
No third-party dependencies. Run: python verify.py
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def dot(u, v):
    return sum(x*y for x,y in zip(u,v))

def norm2(u):
    return dot(u,u)

def projection(a,b):
    # Closest vector in the closed segment [a,b] to the origin.
    d = tuple(y-x for x,y in zip(a,b))
    t = -dot(a,d) / norm2(d) if norm2(d) else F(0)
    t = max(F(0),min(F(1),t))
    return tuple(a[i]+t*d[i] for i in range(2))

# Exhaust the exact rational grid of admissible perturbation pairs.
# Distances are compared by squared rational arithmetic, not floats.
D=8
E=[(F(i,D),F(j,D)) for i,j in product(range(-4,5), repeat=2)]
for A,B in [(F(1),F(1)),(F(2),F(1)),(F(1),F(3)),(F(3),F(2))]:
    rad=min(A,B)/2
    es=[e for e in E if norm2(e)<rad*rad]
    for e1,e2 in product(es, repeat=2):
        h1=(A+e1[0],e1[1]); h2=(e2[0],B+e2[1])
        p=projection(h1,h2)
        assert p[0]>0 and p[1]>0, (A,B,e1,e2,p)
        checks+=1

# Shared-error grid: use the exact equivalent squared bound
# d^2=A^2 B^2/(A^2+B^2).
for A,B in [(F(1),F(1)),(F(2),F(1)),(F(1),F(3)),(F(3),F(2))]:
    d2=A*A*B*B/(A*A+B*B)
    for e in E:
        if norm2(e)<d2:
            p=projection((A+e[0],e[1]),(e[0],B+e[1]))
            assert p[0]>0 and p[1]>0,(A,B,e,p)
            checks+=1

# At the independent-error threshold (A>=B), task 1 is not descended.
for A,B in [(F(1),F(1)),(F(2),F(1)),(F(3),F(2))]:
    d=B/2
    h1=(A,d);h2=(F(0),B-d)
    p=projection(h1,h2)
    assert p==h2 and p[0]==0
    assert norm2((h1[0]-A,h1[1]))==d*d
    assert norm2((h2[0],h2[1]-B))==d*d
    checks+=4

# The shared-error threshold translates the noiseless closest point to 0.
for A,B in [(F(1),F(1)),(F(2),F(1)),(F(1),F(3))]:
    p0=projection((A,F(0)),(F(0),B))
    e=(-p0[0],-p0[1]); p=projection((A+e[0],e[1]),(e[0],B+e[1]))
    assert p==(0,0)
    assert norm2(e)==A*A*B*B/(A*A+B*B)
    checks+=2

# Explicit superthreshold strict-ascent witnesses, rational arithmetic.
# For A>=B, choose d>B/2, then a sufficiently small negative first
# coordinate in h2. The exact endpoint test is verified here.
for A,B in [(F(1),F(1)),(F(2),F(1)),(F(3),F(2))]:
    d=B*F(3,5)
    tiny=B*F(1,1000)
    h1=(A,d);h2=(-tiny,B-d)
    p=projection(h1,h2)
    assert p==h2 and p[0]<0
    assert norm2((h2[0],h2[1]-B)) < (B*F(61,100))**2
    checks+=3

print(f"PASS {checks} exact-rational assertions/cases")
