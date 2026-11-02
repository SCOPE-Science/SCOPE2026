"""Independent finite checks from digital definition of cyclic uniform morphisms.
Enumerated finite prefixes provide a comparison, not a global proof."""

def source_at(n, r):
    k = r + 1
    s = 0
    while n:
        n, digit = divmod(n, k)
        if digit == r: s = (s + 1) % 3
    return s

def discrepancy(r, m):
    z = [1, 0, 0]
    for _ in range(m):
        z = [r*z[i] + z[(i-1)%3] for i in range(3)]
    return max(z)-min(z), z

def prediction(r, m):
    return 2 + r * sum(discrepancy(r, j)[0] for j in range(m))

def prefix_range(r,m):
    n = (r+1)**m
    pairs = set()
    j = 0
    last = source_at(0, r)
    while len(pairs) != 9:
        j += 1
        cur = source_at(j, r)
        pairs.add((last, cur))
        last = cur
        assert j < 100000
    length = (j+2)*n
    counts = [0]*(length+1)
    for i in range(length):
        counts[i+1] = counts[i] + (source_at(i,r) == 0)
    counts_at_n = [counts[i+n]-counts[i] for i in range(length-n+1)]
    return min(counts_at_n), max(counts_at_n)

if __name__ == '__main__':
    for r in range(4, 10):
        for m in range(0,5 if r in (4,5) else 4):
            mn,mx=prefix_range(r,m)
            pred=prediction(r,m)
            print(f'r={r} m={m} n={(r+1)**m} range=[{mn},{mx}] abelian={mx-mn+1} predicted={pred}')
            assert mx-mn+1==pred
        for t in range(1,15):
            g,z=discrepancy(r,3*t)
            mid = (z[0]-z[1])*(z[0]-z[2]) < 0
            assert (g%2==0) == mid
    print('PASS: all finite checks; these do not replace the infinite proof')
