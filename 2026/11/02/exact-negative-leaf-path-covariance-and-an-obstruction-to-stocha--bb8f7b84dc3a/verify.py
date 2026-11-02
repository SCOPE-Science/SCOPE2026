"""Independent exact checks of leaf-count and internal-path covariance in BSTs."""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
from math import factorial

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

# First exact approach: recurrences for joint moments and covariance.
N = 100
p = [F(0) for _ in range(N + 1)]
l = [F(0) for _ in range(N + 1)]
a = [F(0) for _ in range(N + 1)]
l2 = [F(0) for _ in range(N + 1)]
l[1] = l2[1] = 1
for n in range(2, N + 1):
    p[n] = (2 * sum(p[:n]) + n*(n-1)) / n
    l[n] = (2 * sum(l[:n])) / n
    a[n] = (2 * sum(a[:n]) + 2 * sum(p[k]*l[n-1-k] for k in range(n))
            + 2*(n-1)*sum(l[:n])) / n
    l2[n] = (2*sum(l2[:n]) + 2*sum(l[k]*l[n-1-k] for k in range(n))) / n
    check(l[n] == F(n+1, 3))
    check(a[n] - p[n]*l[n] == -F(n*n+n-6, 9*n))
    if n >= 4:
        check(l2[n]-l[n]**2 == F(2*(n+1),45))

# Independent full distribution recurrence: exact convolution of child BSTs.
dist = [None] * 9
dist[0] = {(0, 0): F(1)}
dist[1] = {(1, 0): F(1)}
for n in range(2, 9):
    count = Counter()
    for k in range(n):
        for (lk, pk), x in dist[k].items():
            for (lj,pj), y in dist[n-1-k].items():
                count[(lk+lj,pk+pj+n-1)] += x*y/F(n)
    dist[n] = dict(count)
    check(sum(dist[n].values()) == 1)
    ep = sum(F(pp)*v for (ll,pp),v in dist[n].items())
    el = sum(F(ll)*v for (ll,pp),v in dist[n].items())
    epl = sum(F(ll*pp)*v for (ll,pp),v in dist[n].items())
    check((ep,el,epl) == (p[n],l[n],a[n]))

# Third independent computation: enumerate all insertion permutations,
# build each tree without using either recurrence or distribution convolution.
def stats(perm):
    nodes = [[perm[0], -1, -1]]
    path = 0
    for key in perm[1:]:
        at = 0
        depth = 0
        while True:
            side = 1 if key < nodes[at][0] else 2
            depth += 1
            nxt = nodes[at][side]
            if nxt < 0:
                nodes[at][side] = len(nodes)
                nodes.append([key,-1,-1])
                path += depth
                break
            at = nxt
    leaves = sum(node[1] == -1 and node[2] == -1 for node in nodes)
    return leaves,path

for n in range(1,9):
    counts = Counter(stats(perm) for perm in permutations(range(n)))
    check(sum(counts.values()) == factorial(n))
    check({k:F(v,factorial(n)) for k,v in counts.items()} == dist[n])
    ep = sum(F(pp*c,factorial(n)) for (ll,pp),c in counts.items())
    el = sum(F(ll*c,factorial(n)) for (ll,pp),c in counts.items())
    epl = sum(F(ll*pp*c,factorial(n)) for (ll,pp),c in counts.items())
    check((ep,el,epl) == (p[n],l[n],a[n]))
    if n == 7:
        for leaf,total,cut10,cut11 in [(3,2880,0,1040),(4,272,80,80)]:
            check(sum(c for (ll,pp),c in counts.items() if ll==leaf) == total)
            check(sum(c for (ll,pp),c in counts.items() if ll==leaf and pp<=10) == cut10)
            check(sum(c for (ll,pp),c in counts.items() if ll==leaf and pp<=11) == cut11)
        check(F(80,272) > F(0,2880))
        check(F(80,272) < F(1040,2880))

print(f"PASS: {checks} exact assertions; moment recurrences through n={N}, "
      "two independent full-distribution methods through n=8, and n=7 CDF reversal")
