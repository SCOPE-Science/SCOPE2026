"""Unit-test the exact thit() logic (t1min < p2max) against brute-force has()."""
import itertools, random

def std(p):
    s = sorted(p); r = {v:i+1 for i,v in enumerate(s)}
    return tuple(r[v] for v in p)

T1=(1,2,3,6,5,4); T2=(3,2,1,6,5,4)

def has(b, j, T):
    m = len(b)-1
    for idx in itertools.combinations(range(m+1), 6):
        if j not in idx: continue
        if std([b[i] for i in idx]) == T:
            return True
    return False

def thit(b, m, j):
    INF = 10**9
    t1 = INF; t2 = INF; p2 = -1
    if j >= 3:
        for i2 in range(1, j):
            pre = any(b[i1] < b[i2] for i1 in range(i2))
            if not pre: continue
            smin = min([b[i3] for i3 in range(i2+1, j) if b[i3] > b[i2]] or [INF])
            t1 = min(t1, smin)
        for i1 in range(j):
            if b[i1] >= t2: continue
            found = False
            for i2 in range(i1+1, j):
                if b[i2] >= b[i1]: continue
                if any(b[i3] < b[i2] for i3 in range(i2+1, j)):
                    found = True; break
            if found: t2 = min(t2, b[i1])
    if j+2 <= m:
        for k1 in range(j+1, m):
            p2 = max([p2] + [b[k2] for k2 in range(k1+1, m+1) if b[k2] < b[k1]])
    return (t1 < p2), (t2 < p2)

random.seed(1)
bad = 0
for trial in range(5000):
    m = random.randint(1, 10)
    vals = random.sample(range(1, m+1), m)
    j = random.randint(0, m)
    b = tuple(vals[:j] + [m+1] + vals[j:])
    for T, k in ((T1, 0), (T2, 1)):
        if has(b, j, T) != thit(b, m, j)[k]:
            bad += 1; print("MISMATCH", b, j, T, has(b, j, T), thit(b, m, j)); break
print("done, mismatches:", bad)
