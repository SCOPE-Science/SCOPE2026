from fractions import Fraction as F
import math

def add(p, q):
    n = max(len(p), len(q))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out

def scale(p, c):
    return [c*x for x in p]

def shift(p):
    return [F(0)] + p

A = [
    [],
    [F(1,4)],
    [F(3,32), F(9,32)],
    [F(1932,2197), F(-7200,2197), F(7296,2197)],
    [F(439,216), F(-8), F(3680,513), F(-845,4104)],
    [F(-8,27), F(2), F(-3544,2565), F(1859,4104), F(-11,40)],
]
b4 = [F(25,216), F(0), F(1408,2565), F(2197,4104), F(-1,5), F(0)]
b5 = [F(16,135), F(0), F(6656,12825), F(28561,56430), F(-9,50), F(2,55)]

stages = []
for i in range(6):
    s = [F(1)]
    for j in range(i):
        s = add(s, scale(shift(stages[j]), A[i][j]))
    stages.append(s)

def stability(weights):
    r = [F(1)]
    for i,w in enumerate(weights):
        r = add(r, scale(shift(stages[i]), w))
    return r

R4 = stability(b4)
R5 = stability(b5)
want4 = [F(1),F(1),F(1,2),F(1,6),F(1,24),F(1,104)]
want5 = [F(1),F(1),F(1,2),F(1,6),F(1,24),F(1,120),F(1,2080)]
assert R4 == want4, (R4, want4)
assert R5 == want5, (R5, want5)

n = max(len(R4), len(R5))
E = [(R5[i] if i < len(R5) else F(0)) - (R4[i] if i < len(R4) else F(0))
     for i in range(n)]
assert E == [F(0),F(0),F(0),F(0),F(0),F(-1,780),F(1,2080)]

def peval(p, x):
    s = F(0)
    for c in reversed(p):
        s = s*x + c
    return s

z = F(8,3)
common = F(1613,117)
assert peval(R4,z) == common
assert peval(R5,z) == common
assert peval(E,z) == 0

# E'(8/3)
Ep = sum(F(i)*E[i]*z**(i-1) for i in range(1,len(E)))
assert Ep == F(1024,15795)

# Sixth Taylor partial sum is already strictly above the common RK value.
fact = 1
t6 = F(0)
for j in range(7):
    if j:
        fact *= j
    t6 += z**j / fact
assert t6 == F(462973,32805)
assert t6 - common == F(139264,426465) > 0

q = float(common) * math.exp(-8.0/3.0)
assert 0.0 < q < 1.0
vals = {n: 1.0-q**n for n in (1,50,100)}
assert abs(vals[1] - 0.0420785741677019) < 1e-14
assert abs(vals[50] - 0.8834548079916271) < 1e-13
assert abs(vals[100] - 0.9864172182197315) < 1e-13

print("VERIFY_OK")
