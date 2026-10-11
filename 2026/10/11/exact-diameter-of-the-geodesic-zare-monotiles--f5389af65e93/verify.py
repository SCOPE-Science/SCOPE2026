from fractions import Fraction
import math

def vertices(q):
    delta = Fraction(1, q*q)
    r = Fraction(q+1, q)
    lower = [(Fraction(k)*delta, Fraction(1)) for k in range(q+2)]
    upper = [(r*Fraction(j)*delta, r) for j in range(q+1)]
    return lower, upper

def cosh_dist(p, z):
    x,y = p
    X,Y = z
    return Fraction(1) + ((x-X)**2 + (y-Y)**2) / (2*y*Y)

for q in range(2, 101):
    lower, upper = vertices(q)
    V = lower + upper
    values = {}
    best = None
    pairs = set()
    for i in range(len(V)):
        for j in range(i+1, len(V)):
            c = cosh_dist(V[i], V[j])
            if best is None or c > best:
                best = c
                pairs = {(i,j)}
            elif c == best:
                pairs.add((i,j))

    c_low = Fraction(1) + Fraction((q+1)**2, 2*q**4)
    c_up = Fraction(1) + Fraction(1, 2*q*q)
    c_cross = Fraction(1) + Fraction(2*q*q + 2*q + 1, 2*q**3*(q+1))
    assert c_low > c_up
    assert c_cross - c_low == Fraction(q**3-q**2-2*q-1, 2*q**4*(q+1))

    if q == 2:
        assert best == c_low
        # lower endpoints: indices 0 and q+1
        assert pairs == {(0, q+1)}
        closed = Fraction(41,32)
        assert best == closed
    else:
        assert best == c_cross
        # V0-Wq and V_{q+1}-W0
        first_upper = len(lower)
        expected = {(0, first_upper+q), (q+1, first_upper)}
        assert pairs == expected

# Exact sign transition.
assert 2**3 - 2**2 - 2*2 - 1 < 0
assert 3**3 - 3**2 - 2*3 - 1 > 0
for q in range(2,100):
    p = q**3-q**2-2*q-1
    pn = (q+1)**3-(q+1)**2-2*(q+1)-1
    assert pn-p == 3*q*q + q - 2 > 0

# Numerical asymptotic sanity checks.
for q in (100, 1000, 10000):
    x = (2*q*q+2*q+1)/(2*q**3*(q+1))
    D = math.acosh(1+x)
    A = 2*math.atan(1/(2*q*q))
    assert abs(q*D-math.sqrt(2)) < 1e-4
    assert abs(D/math.sqrt(A)-math.sqrt(2)) < 1e-4

print("VERIFY_OK")
print("exact_vertex_pair_sweep=q=2..100")
print("branch=q2_lower_endpoints;q>=3_opposite_cross_endpoints")
print("asymptotic_constant=sqrt(2)")
