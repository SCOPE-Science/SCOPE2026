from math import gcd
from functools import reduce


def age_hist(q):
    Q = sum(q)
    h = [0] * 5
    for k in range(Q):
        s = sum((k * qi) % Q for qi in q)
        a = s // Q
        h[a] += 1
    return tuple(h)


def divs(n):
    return [d for d in range(1, n + 1) if n % d == 0]


D = divs(42)
pairs = [(u, v) for u in D for v in D if u <= v and gcd(u, v) == 1]
print("num pairs:", len(pairs))
rows = []
for (u, v) in pairs:
    m = u + v
    q = tuple(sorted((u, v, 6 * m, 14 * m, 21 * m)))
    Q = sum(q)
    assert Q == 42 * m, (q, Q, m)
    assert all(Q % qi == 0 for qi in q)
    assert reduce(gcd, q) == 1
    h = age_hist(q)
    exc = h[2] - 3 * h[1]
    rows.append((Q, (u, v, m), q, h, exc))
rows.sort()
nviol = 0
for r in rows:
    print("Q=%4d (u,v,m)=%s q=%s h=%s excess=%d %s" %
          (r[0], r[1], r[2], r[3], r[4], "VIOL" if r[4] > 0 else ""))
    if r[4] > 0:
        nviol += 1
print("violators:", nviol, "max excess:", max(r[4] for r in rows))
