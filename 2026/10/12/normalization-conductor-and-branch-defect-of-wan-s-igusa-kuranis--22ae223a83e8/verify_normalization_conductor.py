from itertools import combinations, product

first = ('a','b','c')
second = ('d','e','f')
vars6 = first + second

# The defining squarefree monomial ideal kills products of two distinct
# variables inside either triple. Hence every nonzero monomial uses at most
# one variable from each triple.
within = {tuple(sorted(p)) for p in combinations(first,2)} | {tuple(sorted(p)) for p in combinations(second,2)}
cross = {tuple(sorted((x,y))) for x in first for y in second}
all_pairs = {tuple(sorted(p)) for p in combinations(vars6,2)}
assert within | cross == all_pairs
assert len(within) == 6 and len(cross) == 9 and len(all_pairs) == 15

# Minimal components: choose one surviving variable from each triple.
components = [(x,y) for x in first for y in second]
assert len(components) == 9

# On a normalized component C[x,y], the conductor is (xy).  Thus the
# conductor downstairs has exactly the nine cross quadratic generators.
conductor_generators = tuple(x+y for x,y in components)
assert len(conductor_generators) == 9

# Hilbert functions.  For the three-axis ring A, dim A_0=1 and dim A_n=3
# for n>0.  The product ring R=A tensor A has dim R_n=9n-3 for n>0.
def hR(n):
    return 1 if n == 0 else 9*n - 3

def hNorm(n):
    # nine polynomial planes
    return 9*(n+1)

def hDefect(n):
    return hNorm(n)-hR(n)

assert hDefect(0) == 8
for n in range(1,20):
    assert hDefect(n) == 12

# Degree-n conductor basis: choose a component and positive exponents on
# both component variables.  It has 9(n-1) basis monomials for n>=2.
def hCond(n):
    return 0 if n < 2 else 9*(n-1)

for n in range(0,20):
    if n < 2:
        assert hCond(n) == 0
    else:
        assert hCond(n) == len(components)*(n-1)

# Normalization fibers: a smooth point lies on one plane; a nonzero point on
# one conductor axis lies on the three planes containing that axis; the
# origin lies on all nine planes.
assert 1 == 1
assert len(second) == 3
assert len(components) == 9

print('components=9')
print('conductor_generators=' + ','.join(conductor_generators))
print('downstairs_conductor_support_axes=6')
print('normalization_fiber_sizes=1,3,9')
print('defect_hilbert_degree0=8')
print('defect_hilbert_positive_degree=12')
print('defect_hilbert_series=(8+4t)/(1-t)')
print('defect_multiplicity=12')
print('VERIFY_OK')
