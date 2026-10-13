"""Finite computational checks for bounded-morphism endomorphisms of crown Heyting algebras.

Usage: python3 verify.py
Only the standard Python library is required.
"""
from collections import Counter
from itertools import product
from math import factorial


def crown(m):
    """M_i=i; B_i=m+i; M_i < B_{i-1},B_i (indices modulo m)."""
    assert m >= 3
    return tuple((i, (m + i - 1) % m + m, m + i) if i < m else (i,)
                 for i in range(2 * m))


def upsets(up):
    n = len(up)
    return tuple(mask for mask in range(1 << n)
                 if all((not (mask >> i) & 1) or all((mask >> j) & 1 for j in up[i])
                        for i in range(n)))


def is_p_morphism(f, up):
    return all({f[j] for j in up[i]} == set(up[f[i]]) for i in range(len(f)))


def lazy_path_trace(length, steps):
    """Trace of (I+Adj(path with steps edges))^length, integer DP."""
    n = steps + 1
    return sum(_walkreturn(n, v, length) for v in range(n))


def _walkreturn(n, v, length):
    t = [0] * n
    t[v] = 1
    for _ in range(length):
        t = [t[i] + (t[i-1] if i > 0 else 0) +
             (t[i+1] if i+1 < n else 0) for i in range(n)]
    return t[v]


def central_trinomial(m):
    return sum(factorial(m) // (factorial(j)**2 * factorial(m-2*j))
               for j in range(m//2 + 1))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def lucas(n):
    a,b=2,1
    for _ in range(n):
        a,b=b,a+b
    return a


def from_top_labels(t, m):
    """Construct the only possible bounded map extending images of all maxima."""
    z = []
    for i in range(m):
        x,y = t[(i-1)%m],t[i]
        if x == y:
            z.append(m+x)
        elif (y-x)%m == 1:
            z.append(y)  # low y has maxima B_(y-1) and B_y
        elif (x-y)%m == 1:
            z.append(x)
        else:
            return None
    return tuple(z) + tuple(m+v for v in t)


def rank_by_image(f, full):
    preimages = {sum(1 << i for i,t in enumerate(f) if (mask >> t)&1) for mask in full}
    rank = len(preimages)
    image_set = set(f)
    image_upsets = {mask & sum(1<<j for j in image_set) for mask in full}
    assert rank == len(image_upsets)
    return rank


def verify_m(m):
    up = crown(m)
    all_upsets = upsets(up)
    # Independent brute-force determination of admissible maximum-row labelings.
    hist = Counter()
    count = 0
    for t in product(range(m), repeat=m):
        f = from_top_labels(t, m)
        if f is None: continue
        assert is_p_morphism(f, up)
        count += 1
        r = rank_by_image(f, all_upsets)
        hist[r] += 1
    predicted = Counter({2:m, lucas(2*m):2*m})
    # Exact counts by closed lazy walks covering a prescribed path interval.
    traces = {k:lazy_path_trace(m,k) for k in range(m//2+1)}
    for k in range(1,m//2+1):
        h = traces[k] - 2*traces[k-1] + (traces[k-2] if k>=2 else 0)
        assert h>0
        predicted[fibonacci(2*k+3)] = m*h
    assert count == m*(central_trinomial(m)+2), (m,count)
    assert hist == predicted, (m, hist, predicted)
    if m<=4:
        # All possible upsets are enumerated independently; the cycle count is direct.
        assert len(upsets(up)) == lucas(2*m)
        for t in product(range(m),repeat=m):
            f=from_top_labels(t,m)
            if f is None: continue
            us=all_upsets
            for a in us:
                for b in us:
                    imp=sum(1<<i for i in range(2*m)
                            if all((not ((a>>j)&1)) or ((b>>j)&1) for j in up[i]))
                    pre=lambda z:sum(1<<i for i,z0 in enumerate(f) if (z>>z0)&1)
                    assert pre(imp) == sum(1<<i for i in range(2*m)
                                            if all(not ((pre(a)>>j)&1) or ((pre(b)>>j)&1)
                                                   for j in up[i]))
    print('CROWN',m,'endomorphisms',count,'ranks',dict(sorted(hist.items())))
    return count


def brute_small():
    m=3
    up = crown(m)
    p=0
    monotone=0
    for f in product(range(2*m), repeat=2*m):
        if any(f[j] not in up[f[i]] for i in range(2*m) for j in up[i]):
            continue
        monotone+=1
        if is_p_morphism(f,up):p+=1
    assert monotone == 234 and p == 27
    print('BRUTE_FULL_MAPPING',m,'monotone',monotone,'bounded',p)


def main():
    brute_small()
    for m in range(3,8):verify_m(m)
    print('VERIFY_OK')

if __name__=='__main__':main()
