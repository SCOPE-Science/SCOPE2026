from fractions import Fraction as F
from itertools import combinations

# Exact verifier for the distinguished metric tau = 4/15.
tau = F(4, 15)

# Packing minimum on the diagonal ray.
packing_candidates = [4*tau, 1+tau, F(2), 1+tau/4]
assert min(packing_candidates) == F(16, 15)

# Lower-hole witness from the source theorem, independently rechecked.
h0 = [F(11,30), F(11,30), F(1,15), F(0), F(1)]

def q(v):
    return sum(x*x for x in v[:4]) + tau*v[4]*v[4]

# Enumerate nearby sites. The coordinate box is more than sufficient because
# a coordinate difference of at least 2 already contributes > 27/50.
def d2_to_X(p):
    best = None
    for z1 in range(-2, 3):
      for z2 in range(-2, 3):
       for z3 in range(-2, 3):
        for z4 in range(-2, 3):
         for z5 in range(-2, 3):
          z = (z1,z2,z3,z4,z5)
          if sum(z) % 2 == 0:
            v = [p[i]-F(z[i]) for i in range(5)]
            val = q(v)
            best = val if best is None or val < best else best
          # translated coset D5+(1/2,...,1/2)
          if sum(z) % 2 == 0:
            v = [p[i]-(F(z[i])+F(1,2)) for i in range(5)]
            val = q(v)
            best = val if val < best else best
    return best

assert d2_to_X(h0) == F(27, 50)

# Fundamental-chamber polytope used for the exact covering-radius upper bound.
# Each inequality is a.x <= b, with x=(x1,x2,x3,x4,z).
ineqs = [
    ((0,0,0,0,1), F(1)),
    ((0,0,0,0,-1), F(1)),
    ((15,15,15,-15,-4), F(16)),
    ((5,5,5,5,-4), F(8)),
    ((15,15,15,15,4), F(16)),
    ((30,0,0,0,-8), F(19)),
    ((30,0,0,0,8), F(19)),
    ((1,1,0,0,0), F(1)),
    ((-1,1,0,0,0), F(0)),
    ((0,-1,1,0,0), F(0)),
    ((0,0,-1,1,0), F(0)),
    ((0,0,0,-1,0), F(0)),
]

def solve5(rows):
    A = [[F(c) for c in ineqs[i][0]] + [ineqs[i][1]] for i in rows]
    n = 5
    for col in range(n):
        pivot = next((r for r in range(col,n) if A[r][col]), None)
        if pivot is None:
            return None
        A[col], A[pivot] = A[pivot], A[col]
        piv = A[col][col]
        A[col] = [x/piv for x in A[col]]
        for r in range(n):
            if r == col:
                continue
            f = A[r][col]
            if f:
                A[r] = [A[r][j]-f*A[col][j] for j in range(n+1)]
    return tuple(A[i][n] for i in range(n))

def feasible(x):
    for a,b in ineqs:
        if sum(F(a[i])*x[i] for i in range(5)) > b:
            return False
    return True

verts = set()
for rows in combinations(range(len(ineqs)),5):
    x = solve5(rows)
    if x is not None and feasible(x):
        verts.add(x)

assert len(verts) == 41, len(verts)
vals = [q(list(x)) for x in verts]
assert max(vals) == F(27,50), max(vals)

# Piecewise lower-bound identities used in the global-ray proof.
t0 = F(4,15)
assert 1 + F(41,150)/t0 == F(81,40)
assert (F(8) + 9*t0*t0)/(4+t0) == F(81,40)

# The second-interval bound f(t)=(8+9t^2)/(4+t) is increasing for t>=4/15,
# because its derivative numerator is 9t^2+72t-8 and is already positive at 4/15.
assert 9*t0*t0 + 72*t0 - 8 > 0

# Later intervals have a strict margin above 81/40.
assert F(16)*F(2,3)/(4+F(2,3)) > F(81,40)
assert F(16)/(4+F(2)) > F(81,40)
assert (16+F(4))/(4+F(4)) > F(81,40)
assert 2+F(4,8) > F(81,40)

print('VERIFY_OK')
print('vertices', len(verts))
print('max_squared_radius', f'{max(vals).numerator}/{max(vals).denominator}')
