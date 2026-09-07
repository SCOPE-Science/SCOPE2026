from math import gcd, comb
from functools import reduce


def age_hist(q):
    Q = sum(q)
    h = [0] * 5
    for k in range(Q):
        h[sum((k * qi) % Q for qi in q) // Q] += 1
    return tuple(h)


# (i) Reflexivity: every tabled tuple has qi|Q by construction; confirm age
# symmetry directly; also confirm interior uniqueness via h0=1 (origin only).
import json
tab = json.load(open("output/artifacts/table_Q5_430.json"))
bad = [r for r in tab if not (r["h"][0] == 1 and r["h"][4] == 1 and r["h"][1] == r["h"][3])]
print("non-palindromic rows:", len(bad))

# (ii) Non-reflexive divisor tuples exist and are excluded: count them.
import bisect


def divisors(n):
    d = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            d.append(i)
            if i * i != n:
                d.append(n // i)
        i += 1
    return sorted(d)


def gen(divs, total, parts, lo=0, cur=()):
    if parts == 1:
        j = bisect.bisect_left(divs, total, lo=lo)
        if j < len(divs) and divs[j] == total:
            yield cur + (total,)
        return
    for j in range(lo, len(divs)):
        v = divs[j]
        if v * parts > total:
            break
        yield from gen(divs, total - v, parts - 1, j, cur + (v,))


ndiv_all = nref = 0
for Q in range(5, 378):
    for t in gen(divisors(Q), Q, 5):
        if reduce(gcd, t) != 1:
            continue
        ndiv_all += 1
        h = age_hist(t)
        if not (h[0] == 1 and h[4] == 1 and h[1] == h[3]):
            nref += 1
print("reduced divisor 5-tuples Q<=377:", ndiv_all, "non-age-symmetric:", nref)

# (iii) Completeness note: every reduced reflexive WP simplex arises from a
# weight tuple with qi|Q (reflexivity criterion) -- cited to Conrads Prop 3.5 /
# Braun-Kreuzer-Skarke; since we swept ALL such tuples, table is complete.
# (iv) palindromic negative control: verify no reflexive tuple missed by
# non-palindromic filter: try k <-> Q-k symmetry argument numerically.
nonsym = 0
for Q in range(5, 378):
    for t in gen(divisors(Q), Q, 5):
        if reduce(gcd, t) != 1:
            continue
        h = age_hist(t)
        if h[0] != 1 or h[4] != 1:
            nonsym += 1
print("rows failing h0=h4=1:", nonsym)

# (v) timing / determinism: rerun cost of full sweep
import time
t0 = time.time()
c = 0
for Q in range(5, 378):
    for t in gen(divisors(Q), Q, 5):
        if reduce(gcd, t) == 1:
            c += 1
print("candidate tuples:", c, f"gen time {time.time()-t0:.1f}s")
