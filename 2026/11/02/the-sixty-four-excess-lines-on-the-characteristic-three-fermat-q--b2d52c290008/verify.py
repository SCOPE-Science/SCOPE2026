"""Exact verification of a partition of lines on the characteristic-three Fermat quartic.

Python 3 with SymPy.  F9 is represented as F3[u]/(u*u+1).
The computation exhausts all F9 rational projective points and Hermitian
isotropic generator lines; completeness over an algebraic closure then follows
from the established sharp geometric count of 112 lines.
"""
from itertools import product, combinations
from collections import Counter
import sympy as sp

F = range(9)
def add(x,y):
    return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
def mul(x,y):
    a,b=x%3,x//3; c,d=y%3,y//3
    return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
def fpow(x,n):
    z=1
    for _ in range(n):z=mul(z,x)
    return z
def inv(x):return fpow(x,7)
def norm(v):
    i=next(j for j,x in enumerate(v) if x)
    return tuple(mul(x,inv(v[i])) for x in v)
def herm(x,y):
    s=0
    for a,b in zip(x,y):s=add(s,mul(fpow(a,3),b))
    return s
assert all(mul(x,inv(x))==1 for x in range(1,9))
vec={norm(v) for v in product(F,repeat=4) if any(v)}
points=sorted(v for v in vec if herm(v,v)==0)
assert len(points)==280

def line_points(x,y):
    return frozenset({norm(tuple(add(a,mul(t,b)) for a,b in zip(x,y)))
                     for t in F}|{y})
lines=set()
for x,y in combinations(points,2):
    if herm(x,y)==0:
        lines.add(line_points(x,y))
lines=sorted(lines,key=lambda L:tuple(sorted(L)))
assert len(lines)==112
assert all(len(L)==10 for L in lines)

# Three pairings of coordinates, with each of two ratios a,b satisfying a^4=b^4=-1.
roots=[a for a in F if fpow(a,4)==2]
assert len(roots)==4
classical=set()
for pairs in (((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))):
    (i,j),(k,l)=pairs
    for a,b in product(roots,repeat=2):
        L=frozenset(v for v in points if v[i]==mul(a,v[j]) and v[k]==mul(b,v[l]))
        assert len(L)==10 and L in lines
        classical.add(L)
assert len(classical)==48
excess=[L for L in lines if L not in classical]
assert len(excess)==64
classical=sorted(classical,key=lambda L:tuple(sorted(L)))

# Pairwise intersections of distinct lines are at most one rational point.
def meets(A,B):return int(bool(A & B))
assert all(len(A&B)<=1 for i,A in enumerate(lines) for B in lines[i+1:])
assert all((sum(meets(L,M) for M in classical if M!=L),
            sum(meets(L,M) for M in excess if M!=L))==(14,16) for L in classical)
assert all((sum(meets(L,M) for M in classical if M!=L),
            sum(meets(L,M) for M in excess if M!=L))==(12,18) for L in excess)

A=sp.Matrix([[meets(L,M) if L!=M else 0 for M in excess] for L in excess])
t=sp.Symbol('T')
cp=sp.factor(A.charpoly(t).as_expr())
wanted=(t-18)*(t-2)**43*(t+2)**6*(t+6)**12*(t+10)**2
assert sp.expand(cp-wanted)==0
G=A-2*sp.eye(64)
assert G.rank()==21

# The diagonal fourth-root and coordinate permutation symmetries act transitively
# on the 48 classical lines, and preserve the excess set. One representative suffices.
L=classical[0]
v=sp.Matrix([meets(L,M) for M in excess])
aug=G.row_join(v).col_join(sp.Matrix([[*v,-2]]))
assert aug.rank()==22

# Arithmetic Frobenius is x -> x^3 and preserves the partition.
frob=lambda L:frozenset(tuple(fpow(c,3) for c in v) for v in L)
assert all(frob(L) in lines for L in lines)
assert sum(frob(L)==L for L in excess)==8
assert sum(frob(L)==L for L in classical)==0
assert all(frob(frob(L))==L for L in lines)

print('SURFACE_F9_POINTS=280;TOTAL_F9_LINES=112')
print('CLASSICAL_48_EXCESS_64=OK')
print('EQUITABLE_MEETING_QUOTIENT=((14,16),(12,18))')
print('EXCESS_INDUCED_CHARACTERISTIC_POLYNOMIAL=',cp)
print('EXCESS_INTERSECTION_GRAM_RANK=21')
print('CLASSICAL_LINE_ADJOINED_GRAM_RANK=22')
print('FROBENIUS_FIXED_EXCESS=8;FROBENIUS_FIXED_CLASSICAL=0')
print('VERIFY_OK')
