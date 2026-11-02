"""Reproducibility checks for a two-channel cyclic Gabor-frame potential identity.

Finite checks support the separately written all-order proof; they do not certify it.
Run with: python3 CHECK.py
"""
import cmath
import math
import random

COUNT = 0


def near(x, y, tol=2e-8):
    global COUNT
    COUNT += 1
    if abs(x-y) > tol * max(1.0, abs(x), abs(y)):
        raise AssertionError((x, y))


def direct_potential(n, abc, gap):
    """Build the 2n complex vectors and the frame operator directly."""
    g = list(abc) + [0j] * (n-3)
    s = [[0j for _ in range(n)] for _ in range(n)]
    for m in (0, gap):
        for k in range(n):
            v = [g[(i-k)%n] * cmath.exp(2j*math.pi*m*i/n) for i in range(n)]
            for i in range(n):
                for j in range(n):
                    s[i][j] += v[i]*v[j].conjugate()
    potential = sum(abs(s[i][j])**2 for i in range(n) for j in range(n))
    return potential, s


def formula_potential(n, abc, gap):
    a, b, c = abc
    t = math.cos(math.pi * gap/n)**2
    c1 = a*b.conjugate() + b*c.conjugate()
    c2 = a*c.conjugate()
    return 4*n + 8*n*(abs(c1)**2*t + abs(c2)**2*(2*t-1)**2)


def direct_fourier_eigenvalues(n, abc, gap):
    a, b, c = abc
    return [
        sum(abs(a+b*cmath.exp(2j*math.pi*(j-m)/n)
                  +c*cmath.exp(4j*math.pi*(j-m)/n))**2
            for m in (0,gap))
        for j in range(n)]


def candidate_gaps(n, u, v, w):
    aa = v*v*(u-w)**2
    bb = (u*w)**2
    tau = max(0, (4*bb-aa)/(8*bb))
    ts = [(d, math.cos(math.pi*d/n)**2) for d in range(1,n//2+1)]
    dist = min(abs(t-tau) for d,t in ts)
    return {d for d,t in ts if abs(abs(t-tau)-dist) < 1e-12}


rng = random.Random(253)
for n in range(5, 16):
    for rep in range(4):
        abc = [complex(rng.uniform(-1,1), rng.uniform(-1,1)) for _ in range(3)]
        norm = math.sqrt(sum(abs(z)**2 for z in abc))
        abc = [z/norm for z in abc]
        for gap in range(1, n//2+1):
            potential, s = direct_potential(n, abc, gap)
            near(potential, formula_potential(n, abc, gap))
            eig = direct_fourier_eigenvalues(n, abc, gap)
            near(potential, sum(l*l for l in eig))
            near(sum(s[i][i].real for i in range(n)), 2*n)

for n in range(5, 36):
    for rep in range(35):
        raw = [rng.uniform(.1, 2) for _ in range(3)]
        norm = math.sqrt(sum(x*x for x in raw))
        u,v,w = (x/norm for x in raw)
        # Choose phases with ac / b^2 negative, attaining the sharp phase minimum.
        abc = (u, v, -w)
        values = {d: formula_potential(n, abc, d) for d in range(1,n//2+1)}
        optimum = min(values.values())
        predicted = candidate_gaps(n, u, v, w)
        for d, val in values.items():
            near(val >= optimum-1e-9, True)
            near(abs(val-optimum)<1e-9, d in predicted)
        # Any other phase can only worsen, with possible equality at antipodal gaps.
        for _ in range(2):
            phase = rng.uniform(-math.pi, math.pi)
            alternative = (u, v, w*cmath.exp(1j*phase))
            for d, val in values.items():
                near(formula_potential(n, alternative, d) >= val-1e-9, True)

for n in (8, 12, 16, 20):
    xyz = (1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
    potential, S = direct_potential(n, xyz, n//4)
    near(potential, 4*n)
    for i in range(n):
        for j in range(n):
            near(S[i][j], 2 if i==j else 0)

for n in (6, 8, 10, 12, 16, 22):
    xyz = (1/math.sqrt(3),)*3
    for d in range(1,n//2+1):
        t=math.cos(math.pi*d/n)**2
        near(formula_potential(n,xyz,d), 4*n+(8*n/9)*(1+4*t*t))
    near(formula_potential(n,xyz,n//2), 44*n/9)
    near(formula_potential(n,xyz,n//2-1)-formula_potential(n,xyz,n//2),
         (32*n/9)*math.sin(math.pi/n)**4)

print('CHECK_OK assertions=' + str(COUNT))
