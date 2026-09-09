"""Exact Murnaghan-Nakayama engine (beta-set rim hooks) + class-algebra Kronecker sums."""
import sys, math, functools, itertools
sys.setrecursionlimit(100000)

_fact = [1]
def fact(n):
    while len(_fact) <= n:
        _fact.append(_fact[-1]*len(_fact))
    return _fact[n]

def partitions(n, max_part=None):
    """All integer partitions of n as descending tuples."""
    if max_part is None: max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(max_part, n), 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest

def z_of(mu):
    """Centralizer size z_mu = prod i^{m_i} m_i! ."""
    from collections import Counter
    c = Counter(mu)
    z = 1
    for part, m in c.items():
        z *= part**m * fact(m)
    return z

def rim_hook_children(lam, h):
    """All (sub-partition, height) after removing a rim hook of size h (beta-set method)."""
    if h == 0:
        return [(lam, 0)]
    if not lam:
        return []
    if sum(lam) < h:
        return []
    r = len(lam)
    beta = [lam[i] + r - 1 - i for i in range(r)]
    S = set(beta)
    res = []
    for i, b in enumerate(beta):
        nb = b - h
        if nb < 0 or nb in S:
            continue
        newbeta = sorted(S - {b} | {nb}, reverse=True)
        mu = tuple(newbeta[j] - (r - 1 - j) for j in range(r))
        assert all(mu[j] >= mu[j+1] for j in range(r-1)), (lam, h, mu)
        mu = tuple(x for x in mu if x > 0)
        ht = sum(1 for c in beta if nb < c < b)
        res.append((mu, ht))
    return res

def make_chi():
    @functools.lru_cache(maxsize=None)
    def chi(lam, mu):
        # lam, mu: tuples; |lam| == |mu| required (mu nonempty or both empty)
        if not mu:
            return 1 if not lam else 0
        if not lam:
            return 0
        m = mu[0]
        rest = mu[1:]
        s = 0
        for sub, ht in rim_hook_children(lam, m):
            v = chi(sub, rest)
            if v:
                s += -v if (ht & 1) else v
        return s
    return chi

def hook_dim(lam):
    n = sum(lam)
    r = len(lam)
    denom = 1
    for i, row in enumerate(lam):
        for j in range(row):
            hook = row - j + sum(1 for k in range(i+1, r) if lam[k] > j) - 1 + 1
            # hook = arm + leg + 1
            hook = (row - j - 1) + sum(1 for k in range(i+1, r) if lam[k] > j) + 1
            denom *= hook
    return fact(n) // denom

def kronecker(lam, mu_, nu, n, chi=None, log=None):
    """g(lam,mu_,nu) = (1/n!) sum_classes |C| chi_lam chi_mu chi_nu. Exact int."""
    if chi is None:
        chi = make_chi()
    S = 0
    fn = fact(n)
    for cl in partitions(n):
        a = chi(tuple(lam), cl)
        if a == 0: continue
        b = chi(tuple(mu_), cl)
        if b == 0: continue
        c = chi(tuple(nu), cl)
        if c == 0: continue
        z = z_of(cl)
        term, rem = divmod(fn, z)
        assert rem == 0
        t = term * a * b * c
        S += t
        if log is not None:
            log.append((cl, z, a, b, c, t))
    assert S % fn == 0, (lam, mu_, nu, S)
    return S // fn
