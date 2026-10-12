from math import gcd
from functools import reduce

# Basis of Pic(S): C0, Gamma, e01,...,e06,e11,...,e16.
N = 14

def vec(C=0, G=0, **kw):
    z = [0]*N
    z[0], z[1] = C, G
    for b in (0,1):
        for i in range(1,7):
            z[2+6*b+i-1] = kw.get(f"e{b}{i}", 0)
    return z

def add(*vs):
    return [sum(x) for x in zip(*vs)]

def neg(v): return [-x for x in v]
def sub(a,b): return [x-y for x,y in zip(a,b)]

def dot(a,b):
    # C0^2=-3, C0.Gamma=1, Gamma^2=0; exceptional basis is orthogonal with square -1.
    s = -3*a[0]*b[0] + a[0]*b[1] + a[1]*b[0]
    for i in range(2,N):
        s -= a[i]*b[i]
    return s

all_exc = {f"e{b}{i}":-1 for b in (0,1) for i in range(1,7)}
F = vec(C=2, G=6, **all_exc)
C0 = vec(C=1)
A = vec(C=1,G=3,e01=-1,e11=-1,e12=-1,e13=-1,e14=-1,e15=-1)
B = vec(C=1,G=3,e01=-1,e02=-1,e03=-1,e04=-1,e05=-1,e11=-1)
E0 = [vec(**{f"e0{i}":1, f"e0{i+1}":-1}) for i in range(1,6)]
E1 = [vec(**{f"e1{i}":1, f"e1{i+1}":-1}) for i in range(1,6)]
Rinf = sub(F,C0)
e06 = vec(e06=1)
e16 = vec(e16=1)

assert F == add(A,B,*E0,*E1)
assert dot(F,F) == 0
assert dot(A,A) == dot(B,B) == -3
assert all(dot(e,e) == -2 for e in E0+E1)
assert dot(C0,C0) == -3 and dot(Rinf,Rinf) == -3
assert dot(e06,F) == 1 and dot(e16,F) == 1

# Vertical lattice generators: F; one component C0 of the infinity fiber;
# and eleven independent components from the t=0 fiber.
cols = [F,C0,A,*E0,*E1]
M = [[cols[j][i] for j in range(13)] for i in range(14)]

def det_bareiss(A):
    A = [row[:] for row in A]
    n = len(A)
    if n == 0: return 1
    sign = 1
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            swap = next((r for r in range(k+1,n) if A[r][k] != 0), None)
            if swap is None: return 0
            A[k], A[swap] = A[swap], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j] = (A[i][j]*pivot - A[i][k]*A[k][j]) // prev
        for i in range(k+1,n): A[i][k] = 0
        prev = pivot
    return sign*A[-1][-1]

def minor(rows, cols_):
    return [[M[i][j] for j in cols_] for i in rows]

# Rank 13: at least one maximal minor is nonzero. The gcd of all 14 maximal
# minors is 12, hence the product of the 13 Smith invariant factors is 12.
maximal = []
for omit in range(14):
    rows = [i for i in range(14) if i != omit]
    maximal.append(det_bareiss(minor(rows, range(13))))
g13 = reduce(gcd, (abs(x) for x in maximal), 0)
assert g13 == 12

# A 12x12 minor is unimodular. Thus the product of the first 12 Smith factors is 1.
rows12 = [0,2,3,4,5,6,7,8,9,10,11,12]
cols12 = [0,1,2,3,4,5,6,8,9,10,11,12]
d12 = det_bareiss(minor(rows12, cols12))
assert abs(d12) == 1

# Therefore SNF is 1^12,12, and the cokernel is Z plus Z/12.
print("fiber_relation=OK")
print("component_intersections=OK")
print("section_degree=1")
print("maximal_minors=" + ",".join(map(str,maximal)))
print("gcd_13x13_minors=12")
print("unimodular_12x12_minor=1")
print("smith_invariants=1,1,1,1,1,1,1,1,1,1,1,1,12")
print("picard_mod_vertical=Z+Z/12")
print("VERIFY_OK")
