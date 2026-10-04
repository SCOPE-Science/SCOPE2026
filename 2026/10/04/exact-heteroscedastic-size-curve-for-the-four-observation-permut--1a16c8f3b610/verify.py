import itertools, math

def size_curve(k):
    if not (k > 0):
        raise ValueError("k must be positive")
    q = ((math.sqrt(1 + 2*k) - math.sqrt(k)) * (math.sqrt(k + 2) - 1)) / (1 + k)
    return 4 * math.atan(q) / math.pi

def perm_p(x1, x2, y1, y2):
    vals = [x1, x2, y1, y2]
    obs = abs((x1+x2-y1-y2)/2)
    stats = []
    for A in itertools.combinations(range(4), 2):
        B = [i for i in range(4) if i not in A]
        stats.append(abs((vals[A[0]]+vals[A[1]]-vals[B[0]]-vals[B[1]])/2))
    return sum(t >= obs - 1e-15 for t in stats) / len(stats)

assert abs(size_curve(1) - 1/3) < 1e-14
for k in [0.01, 0.1, 0.25, 0.5, 2, 4, 10, 100]:
    assert abs(size_curve(k) - size_curve(1/k)) < 2e-14
    assert 1/3 < size_curve(k) < 1/2
assert size_curve(1e12) > 0.4995
examples = [((-3,-2,1,4), True),((2,5,-4,-1), True),((-3,2,-1,4), False),((-4,3,-2,5), False)]
for (x1,x2,y1,y2), sep in examples:
    got = abs(perm_p(x1,x2,y1,y2)-1/3) < 1e-15
    assert got == sep
print("VERIFY_OK")
