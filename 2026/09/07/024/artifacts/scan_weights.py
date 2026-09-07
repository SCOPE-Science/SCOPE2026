from math import gcd
from functools import reduce
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

def gen_partitions(divs, total, parts, min_idx=0, cur=()):
    if parts == 1:
        need = total
        j = bisect.bisect_left(divs, need, lo=min_idx)
        if j < len(divs) and divs[j] == need:
            yield cur + (need,)
        return
    for j in range(min_idx, len(divs)):
        v = divs[j]
        if v * parts > total:
            break
        yield from gen_partitions(divs, total - v, parts - 1, j, cur + (v,))

def age_hist_mod(q):
    Q = sum(q)
    h = [0] * 5
    for k in range(Q):
        s = 0
        for qi in q:
            s += (k * qi) % Q
        if s % Q != 0:
            return None
        a = s // Q
        if a > 4:
            return None
        h[a] += 1
    return tuple(h)

if __name__ == "__main__":
    import json
    recs = []
    for Q in range(5, 431):
        divs = divisors(Q)
        for t in gen_partitions(divs, Q, 5):
            g = reduce(gcd, t)
            if g != 1:
                continue
            h = age_hist_mod(t)
            if h is None:
                continue
            if h[0] == 1 and h[4] == 1 and h[1] == h[3]:
                recs.append((Q, t, h))
    print("TOTAL Q<=430:", len(recs))
    print("TOTAL Q<=377:", sum(1 for r in recs if r[0] <= 377))
    viol = [r for r in recs if r[2][2] > 3 * r[2][1]]
    print("VIOLATORS:")
    for r in viol:
        print(r[0], r[1], r[2], "excess=", r[2][2] - 3 * r[2][1])
    eq = [r for r in recs if r[0] <= 377 and r[2][2] == 3 * r[2][1]]
    print("EQUALITY Q<=377:")
    for r in eq:
        print(r[0], r[1], r[2])
    json.dump([{"Q": r[0], "q": list(r[1]), "h": list(r[2])} for r in recs],
              open("output/artifacts/table_Q5_430.json", "w"))
    print("saved")
