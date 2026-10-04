import cmath
import itertools
import math

def elements(factors):
    return list(itertools.product(*[range(n) for n in factors]))

def add(a, b, factors):
    return tuple((x+y) % n for x, y, n in zip(a, b, factors))

def sub(a, b, factors):
    return tuple((x-y) % n for x, y, n in zip(a, b, factors))

def order(a, factors):
    if all(x == 0 for x in a):
        return 1
    z = tuple(0 for _ in factors)
    cur = z
    for k in range(1, math.prod(factors) + 1):
        cur = add(cur, a, factors)
        if cur == z:
            return k
    raise AssertionError("order not found")

def char(b, x, factors):
    phase = sum((bi*xi)/n for bi, xi, n in zip(b, x, factors))
    return cmath.exp(2j*math.pi*phase)

def predicted(m):
    c = 0.0 if m % 2 == 0 else math.sin(math.pi/(2*m))
    L = 2*(1-c)
    U = 2*(1+c)
    rho = (1+c)/(1-c)
    D = 2*math.sqrt(1-c*c)
    return L, U, rho, D

def optimized(E, factors):
    dual = elements(factors)
    bestL = 0.0
    bestU = float("inf")
    bestR = float("inf")
    bestD = 0.0
    basis_count = 0
    x, y = E
    for b0, b1 in itertools.combinations(dual, 2):
        a = char(b0, x, factors)
        b = char(b1, x, factors)
        c = char(b0, y, factors)
        d = char(b1, y, factors)
        inner = a.conjugate()*b + c.conjugate()*d
        s = abs(inner)
        L = 2 - s
        U = 2 + s
        det = abs(a*d - b*c)
        if L > 1e-11:
            basis_count += 1
            rho = U/L
            bestL = max(bestL, L)
            bestU = min(bestU, U)
            bestR = min(bestR, rho)
            bestD = max(bestD, det)
    assert basis_count > 0
    return bestL, bestU, bestR, bestD

groups = [(n,) for n in range(2, 17)]
groups += [(2,2), (2,4), (2,6), (3,3)]

checks = 0
for factors in groups:
    G = elements(factors)
    for E in itertools.combinations(G, 2):
        d = sub(E[1], E[0], factors)
        m = order(d, factors)
        got = optimized(E, factors)
        want = predicted(m)
        for a, b in zip(got, want):
            assert abs(a-b) < 2e-9, (factors, E, m, got, want)
        checks += 1

for m in range(2, 101):
    L, U, rho, D = predicted(m)
    if m % 2 == 0:
        assert abs(rho - 1.0) < 1e-14
    else:
        tangent = math.tan(math.pi/4 + math.pi/(4*m))**2
        assert abs(rho - tangent) < 2e-12
        if m == 3:
            assert abs(rho - 3.0) < 2e-12

print(f"checked_two_point_sets={checks}")
print("VERIFY_OK")
