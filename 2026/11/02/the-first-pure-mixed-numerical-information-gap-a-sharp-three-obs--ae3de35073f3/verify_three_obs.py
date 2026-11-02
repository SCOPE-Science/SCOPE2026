"""Direct arithmetic spot checks for a three-observable information example.

The analytic theorem is proved in RESULT.md; finite sampling here checks its
matrix normalization and the exact attainment construction, not maximality.
"""
import cmath
import math
import random


def expectations(x):
    a, b, c = x
    w = a.conjugate() * b
    return (2 * w.real, 2 * w.imag, abs(a) ** 2 - abs(b) ** 2), (
        abs(a) ** 2 + abs(b) ** 2 - abs(c) ** 2
    )


def spinor(n):
    nx, ny, nz = n
    theta = math.acos(max(-1.0, min(1.0, nz)))
    phi = math.atan2(ny, nx)
    return (math.cos(theta / 2), cmath.exp(1j * phi) * math.sin(theta / 2))


def witness(eps):
    length = math.sqrt(sum(e * e for e in eps))
    if length == 0:
        return (0j, 0j, 1 + 0j)
    r = min(1.0, length)
    u, v = spinor(tuple(e / length for e in eps))
    return (math.sqrt(r) * u, math.sqrt(r) * v, math.sqrt(1 - r) + 0j)


def qubit_states_with_same_difference(a, b):
    # a,b Bloch vectors, lengths <= 1. Return unit vectors u,v with u-v=a-b.
    delta = tuple(u-v for u,v in zip(a,b))
    delta_norm = math.sqrt(sum(x*x for x in delta))
    if delta_norm < 1e-13:
        return (1.0,0.0,0.0), (1.0,0.0,0.0)
    direction = tuple(x/delta_norm for x in delta)
    pivot = (1.0,0.0,0.0) if abs(direction[0]) < .9 else (0.0,1.0,0.0)
    dot = sum(pivot[i]*direction[i] for i in range(3))
    orth = tuple(pivot[i]-dot*direction[i] for i in range(3))
    norm = math.sqrt(sum(t*t for t in orth))
    orth = tuple(t/norm for t in orth)
    length = math.sqrt(max(0,1-delta_norm**2/4))
    u = tuple(delta[i]/2+length*orth[i] for i in range(3))
    v = tuple(-delta[i]/2+length*orth[i] for i in range(3))
    return u,v


def run():
    rng = random.Random(260421)
    checks = 0
    for _ in range(5000):
        x = [rng.gauss(0,1)+1j*rng.gauss(0,1) for j in range(3)]
        t = math.sqrt(sum(abs(v)**2 for v in x))
        x = [v/t for v in x]
        a,b = expectations(x)
        r = abs(x[0])**2+abs(x[1])**2
        assert abs(math.sqrt(sum(z*z for z in a))-r) < 5e-13
        assert abs(b-(2*r-1)) < 5e-13
        checks += 2
    for _ in range(5000):
        eps = tuple(5 * rng.random() if rng.random() < .5 else .01*rng.random() for j in range(3))
        x = witness(eps)
        a,b = expectations(x)
        r = min(1.0,math.sqrt(sum(e*e for e in eps)))
        assert abs(sum(abs(c)**2 for c in x)-1)<5e-13
        assert all(abs(a[j])<=eps[j]+1e-12 for j in range(3))
        assert abs(b+1-2*r)<5e-13
        checks+=3
    for _ in range(5000):
        def bloch():
            direction=[rng.gauss(0,1) for _ in range(3)]
            length=math.sqrt(sum(z*z for z in direction))
            radius=rng.random()
            return [radius*z/length for z in direction]
        a,b=bloch(),bloch()
        u,v=qubit_states_with_same_difference(a,b)
        assert abs(sum(c*c for c in u)-1)<5e-13
        assert abs(sum(c*c for c in v)-1)<5e-13
        assert all(abs((u[j]-v[j])-(a[j]-b[j]))<5e-13 for j in range(3))
        checks+=3
    # Exact rational Bloch/mixed witnesses: Pauli traces vanish for I_2/2 and e3e3^*.
    # The diagonal target has values +1 and -1, giving the full spectral spread 2.
    for eps in [(0,0,0),(.1,.1,.1),(0,.2,0),(.5,.4,.7),(1,0,0),(4,5,6)]:
        x=witness(eps)
        v,b=expectations(x)
        delta=2*min(1,math.sqrt(sum(c*c for c in eps)))
        assert abs((b+1)-delta)<5e-13
        assert all(abs(v[j])<=eps[j]+1e-12 for j in range(3))
        checks+=2
    print('PASS',checks,'finite assertions: Pauli moment identity, witness saturation, qubit difference replacement')

if __name__ == '__main__':
    run()
