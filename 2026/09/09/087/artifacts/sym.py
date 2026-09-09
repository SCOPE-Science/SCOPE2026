"""Exact symmetric-function toolkit (stdlib only): partitions, e-basis monomial expansion, exact solve."""
from fractions import Fraction

def partitions(n, max_part=None):
    if n == 0:
        yield [];
        return
    if max_part is None: max_part = n
    for f in range(min(max_part, n), 0, -1):
        for rest in partitions(n - f, f):
            yield [f] + rest

def monomials_nvars(nvars, deg):
    # compositions of deg into nvars parts
    if nvars == 1:
        yield (deg,); return
    for a in range(deg + 1):
        for rest in monomials_nvars(nvars - 1, deg - a):
            yield (a,) + rest

def type_of(exp):
    return tuple(sorted((a for a in exp if a > 0), reverse=True))

def e_basis_monomial_matrix(n, q=None):
    """Return (parts, E) where E[mu][lam] = coeff of m_mu in e_lam (q variables, q>=n)."""
    if q is None: q = n
    parts = list(partitions(n))
    pidx = {tuple(p): i for i, p in enumerate(parts)}
    # enumerate monomials, group representatives not needed: expand e_k then products directly aggregated by type
    # First compute e_k as dict type->coeff-per-monomial? e_k = sum_{|S|=k} prod x_i: each squarefree monomial coeff 1.
    # e_lam = product of e_{li}. Expand over exponent vectors in q vars via DP over variables.
    from collections import defaultdict
    # Represent symmetric poly by dict: type-tuple -> total weight summed over all monomials of that type
    # i.e. store W_mu = sum of coeffs over monomials of type mu. Then per-monomial a_mu = W_mu / N_mu.
    # For E we want per-monomial coeffs E_{mu,lam}. Compute W then divide.
    def Nmon(mu, q):
        # number of monomials in q vars with type mu
        from math import factorial
        l = len(mu)
        # multiplicities of each part size
        from collections import Counter
        c = Counter(mu)
        denom = 1
        for v in c.values(): denom *= factorial(v)
        # choose which variables used + assign: q! / ((q-l)! prod mult!)
        return factorial(q) // (factorial(q - l) * denom)
    # expand each e_lam by brute force over subsets
    import itertools
    E = [[Fraction(0)] * len(parts) for _ in range(len(parts))]
    for j, lam in enumerate(parts):
        # product over factors: each factor e_{li} = sum of subsets size li. Expand: iterate over tuples of subsets
        # brute force: subsets list per factor
        subs = []
        for li in lam:
            subs.append(list(itertools.combinations(range(q), li)))
        # exponent accumulation
        W = defaultdict(int)
        # iterate product (could be big: for q=8, e_4^2 = 70^2=4900, fine; worst e_2^4 = 28^4=614k, ok in py? borderline)
        def rec(fi, exp):
            if fi == len(lam):
                mu = type_of(exp)
                W[mu] += 1
                return
            for S in subs[fi]:
                e2 = list(exp)
                for v in S: e2[v] += 1
                rec(fi + 1, tuple(e2))
        rec(0, tuple([0] * q))
        for mu, w in W.items():
            E[pidx[mu]][j] = Fraction(w, Nmon(mu, q))
    return parts, E

def invert_matrix(M):
    n = len(M)
    A = [[M[i][j] for j in range(n)] for i in range(n)]
    I = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if A[i][c] != 0)
        A[c], A[piv] = A[piv], A[c]; I[c], I[piv] = I[piv], I[c]
        d = A[c][c]
        for j in range(n): A[c][j] /= d; I[c][j] /= d
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                for j in range(n): A[i][j] -= f * A[c][j]; I[i][j] -= f * I[c][j]
    return I

def solve_e(a_vec, Einv):
    n = len(a_vec)
    return [sum(Einv[i][j] * a_vec[j] for j in range(n)) for i in range(n)]
