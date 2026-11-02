"""Standalone exact checks for the S5 observational-quotient census.
Run: python3 checker.py . No third-party modules are needed.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def partitions(n):
    if n == 0:
        yield ()
    else:
        for old in partitions(n - 1):
            for j in range(len(old)):
                t = list(map(tuple, old))
                t[j] += (n-1,)
                yield tuple(t)
            yield old + ((n-1,),)


def bell(n):
    return sum(1 for _ in partitions(n))


def signature(blocks, colors):
    ret = [None]*len(colors)
    for block in blocks:
        s = tuple(sorted(set(colors[i] for i in block)))
        for i in block:
            ret[i] = (s, colors[i])
    return ret


def histogram_direct(n, m):
    ans = Counter()
    for blocks in partitions(n):
        for colors in product(range(m), repeat=n):
            sig = signature(blocks, colors)
            ans[len(set(sig))] += 1
    return ans


def onto(n, s):
    return sum((-1)**(s-j)*comb(s,j)*j**n for j in range(s+1))


def species(nmax, m):
    # A[n][q] = number of structures with n labels and quotient size q.
    a = [Counter() for _ in range(nmax+1)]
    a[0][0] = 1
    for s in range(1, m+1):
        b = [0]*(nmax+1)  # unmarked set of nonempty blocks with support exactly S
        b[0] = 1
        for n in range(nmax):
            b[n+1] = sum(comb(n,j)*onto(j+1,s)*b[n-j] for j in range(n+1))
        for _ in range(comb(m,s)):
            c = [Counter() for _ in range(nmax+1)]
            for n in range(nmax+1):
                for j in range(n+1):
                    coeff = comb(n,j)
                    for old_q, old_count in a[n-j].items():
                        if j == 0:
                            c[n][old_q] += coeff*old_count
                        else:
                            c[n][old_q+s] += coeff*old_count*b[j]
            a = c
    return a


def closure_signatures(blocks, colors, q):
    n = len(colors)
    succ = [None]*n
    for block in blocks:
        for x in block:
            succ[x] = block
    funcs = {tuple(colors), tuple(0 for _ in range(n)), tuple(q-1 for _ in range(n))}
    def imp(a,b):
        return q-1 if a <= b else b
    while True:
        old = len(funcs)
        fs = tuple(funcs)
        for f in fs:
            funcs.add(tuple(min(f[j] for j in succ[i]) for i in range(n)))
            for ell in range(q):
                funcs.add(tuple(q-1 if f[i] == ell else 0 for i in range(n)))
        for x in fs:
            for y in fs:
                funcs.add(tuple(min(a,b) for a,b in zip(x,y)))
                funcs.add(tuple(max(a,b) for a,b in zip(x,y)))
                funcs.add(tuple(imp(a,b) for a,b in zip(x,y)))
        if len(funcs)==old:break
    return tuple(tuple(f[i] for f in sorted(funcs)) for i in range(n))


def check():
    totals = []
    for m in (2,3):
        nmax = 6 if m == 2 else 5
        theory = species(nmax,m)
        for n in range(nmax+1):
            assert sum(theory[n].values()) == m**n * bell(n),(m,n, theory[n])
            if n <= 5:
                observed = histogram_direct(n,m)
                assert theory[n] == observed,(m,n, theory[n],observed)
        totals.append((m,[dict(sorted(theory[n].items())) for n in range(1,nmax+1)]))
    # Independent full semantic closure, including boxed and exact-value-test formulas.
    for q,nmax in ((2,4),(3,3)):
        for n in range(1,nmax+1):
            for blocks in partitions(n):
                for colors in product(range(q), repeat=n):
                    s = signature(blocks,colors)
                    semantic = closure_signatures(blocks,colors,q)
                    for i in range(n):
                        for j in range(n):
                            assert (s[i]==s[j]) == (semantic[i]==semantic[j]),(q,n,blocks,colors,i,j)
    # Independent asymptotic sanity for the exceptional m=2 constant.
    # Number with one prescribed singleton support missing:
    # blocks have 2^j - 1 permitted colorings, because monochromatic-0 is forbidden.
    a=[1];bellrow=[1]
    for n in range(350):
        a.append(sum(comb(n,j)*(2**(j+1)-1)*a[n-j] for j in range(n+1)))
        bellrow.append(sum(comb(n,j)*bellrow[n-j] for j in range(n+1)))
    # Check decay, not an infinite-proof claim.
    assert a[350] < 2**350*bellrow[350]
    print('m=2 and m=3 exact quotient-size distributions')
    for m,rows in totals:
        print('m',m,rows)
    print('S5 full semantic closure checks: q=2, n<=4; q=3, n<=3')
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    check()
