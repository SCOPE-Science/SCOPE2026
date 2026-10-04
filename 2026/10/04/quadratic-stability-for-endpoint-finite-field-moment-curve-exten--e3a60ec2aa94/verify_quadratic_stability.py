from fractions import Fraction
from itertools import product
from math import factorial


def rearrangement_count(t, q):
    counts = [0] * q
    for a in t:
        counts[a] += 1
    out = factorial(len(t))
    for c in counts:
        out //= factorial(c)
    return out


def F(theta, d):
    q = len(theta)
    total = Fraction(0)
    for t in product(range(q), repeat=d):
        prob = Fraction(1)
        for a in t:
            prob *= theta[a]
        total += rearrangement_count(t, q) * prob
    return total


def l2_to_uniform(theta):
    q = len(theta)
    u = Fraction(1, q)
    return sum((x-u)**2 for x in theta)


def balanced(theta, a, b):
    z = list(theta)
    m = (z[a] + z[b]) / 2
    z[a] = m
    z[b] = m
    return tuple(z)


def cases(q):
    raw = []
    raw.append([1] + [0]*(q-1))
    raw.append([1]*q)
    raw.append(list(range(1, q+1)))
    raw.append(list(range(q, 0, -1)))
    raw.append([1 if i < 2 else 0 for i in range(q)])
    raw.append([2*i+1 for i in range(q)])
    seen = set()
    for w in raw:
        s = sum(w)
        if s == 0:
            continue
        th = tuple(Fraction(x, s) for x in w)
        if th not in seen:
            seen.add(th)
            yield th


global_cases = 0
pair_cases = 0
for q in range(2, 5):
    uniform = tuple(Fraction(1, q) for _ in range(q))
    for d in range(2, 6):
        A = F(uniform, d)
        c_global = Fraction(d*(d-1), 2)
        c_pair = Fraction(d*(d-1), 4)
        for theta in cases(q):
            val = F(theta, d)
            gap = A - val
            rhs = c_global * l2_to_uniform(theta)
            assert gap >= rhs, (q, d, theta, gap, rhs)
            if d == 2:
                assert gap == rhs, (q, theta, gap, rhs)
            global_cases += 1
            for a in range(q):
                for b in range(a+1, q):
                    th2 = balanced(theta, a, b)
                    gain = F(th2, d) - val
                    local = c_pair * (theta[a]-theta[b])**2
                    assert gain >= local, (q, d, theta, a, b, gain, local)
                    pair_cases += 1

print(f"VERIFY_OK global_cases={global_cases} pair_cases={pair_cases}")
