from decimal import Decimal, getcontext
import math
import random
import sys

getcontext().prec = 80
SEED = 20260921
N = 100000

def Wd(q):
    q = Decimal(str(q))
    return 2*q*q/((1-q)*(1+2*q))

def Wmd(q):
    q = Decimal(str(q))
    return q*q/(1-q*q)

def general_witness(q):
    q = Decimal(str(q))
    one = Decimal(1)
    a = q/(1+2*q)
    c = -q*a
    value = one-(a-one)**2/(c-2*a+one)
    return a, c, value

def monotone_witness(q):
    q = Decimal(str(q))
    one = Decimal(1)
    a = q/(1+q)
    c = Decimal(0)
    value = one-(a-one)**2/(c-2*a+one)
    return a, c, value

def W(q):
    return 2*q*q/((1-q)*(1+2*q))

def Wm(q):
    return q*q/(1-q*q)

def accelerated(a, c):
    return 1.0-(a-1.0)**2/(c-2.0*a+1.0)

print("python", sys.version.split()[0])
print("seed", SEED)
print("samples_per_q", N)

for q in ("0.01", "0.1", "0.3", "0.5", "0.64", "0.8", "0.95"):
    a, c, value = general_witness(q)
    assert abs(abs(value)-Wd(q)) < Decimal("1e-60")
    a, c, value = monotone_witness(q)
    assert abs(abs(value)-Wmd(q)) < Decimal("1e-60")
print("high_precision_witnesses PASS")

q0 = (1.0+math.sqrt(17.0))/8.0
q0m = 1.0/math.sqrt(2.0)
assert abs(W(q0)-1.0) < 2e-15
assert abs(Wm(q0m)-1.0) < 2e-15
print("general_nonexpansion_threshold", format(q0, ".16g"))
print("monotone_nonexpansion_threshold", format(q0m, ".16g"))

grid = [i/100000.0 for i in range(1, 100000)]
ratios = [W(q)/(q*q) for q in grid]
minimum = min(ratios)
argmin = grid[ratios.index(minimum)]
assert minimum >= 16.0/9.0-1e-12
print("sampled_min_W_over_q2", format(minimum, ".16g"), "at_q", argmin)

rng = random.Random(SEED)
max_general = 0.0
max_monotone = 0.0

for q in (0.1, 0.3, 0.5, 0.7, 0.9):
    for _ in range(N):
        a = rng.uniform(-q, q)
        lo = max(-q*abs(a), a-q*abs(a-1.0))
        hi = min(q*abs(a), a+q*abs(a-1.0))
        if lo <= hi:
            c = rng.uniform(lo, hi)
            value = abs(accelerated(a, c))
            assert value <= W(q)*(1+1e-11)+1e-13
            max_general = max(max_general, value/W(q))

        a = rng.uniform(0.0, q)
        lo = max(0.0, a-q*(1.0-a))
        hi = min(q*a, a+q*(1.0-a))
        if lo <= hi:
            c = rng.uniform(lo, hi)
            value = abs(accelerated(a, c))
            assert value <= Wm(q)*(1+1e-11)+1e-13
            max_monotone = max(max_monotone, value/Wm(q))

print("max_random_general_ratio_to_bound", format(max_general, ".16g"))
print("max_random_monotone_ratio_to_bound", format(max_monotone, ".16g"))
print("PASS")
