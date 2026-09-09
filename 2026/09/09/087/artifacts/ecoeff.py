"""Ordered-partition enumeration of X_{C_{n,k}} m-expansion, then exact conversion to e-basis."""
import sys
sys.path.insert(0, 'output/artifacts')
from sym import partitions, e_basis_monomial_matrix, invert_matrix
from ellzey import build
from fractions import Fraction
from collections import defaultdict
import itertools

def ordered_partitions_blocks(n):
    """Generate ordered set partitions as lists of blocks (each block a tuple), covering all ranks 0..l-1.
    Recursive: assign vertex v=0..n-1 either to existing block or new block at each rank position.
    We generate by: for each set partition (via restricted growth strings) and each permutation of blocks."""
    # restricted growth strings
    def rgs(n):
        if n == 0:
            yield [];
            return
        for rest in rgs(n - 1):
            m = max(rest) + 1 if rest else 0
            for b in range(m + 1):
                yield rest + [b]
    for rg in rgs(n):
        nb = max(rg) + 1 if rg else 0
        blocks0 = [None]*nb
        for b in range(nb):
            blocks0[b] = tuple(v for v in range(n) if rg[v] == b)
        for perm in itertools.permutations(range(nb)):
            yield [blocks0[perm[i]] for i in range(nb)]

def e_coeffs(n, k):
    arcs, adj = build(n, k)
    arcs_set = set(arcs)
    # m-expansion: key type tuple -> dict power->count (asc distribution)
    from collections import Counter
    mdist = defaultdict(Counter)
    total = 0
    for oblocks in ordered_partitions_blocks(n):
        total += 1
        rank = [0]*n
        for r, B in enumerate(oblocks):
            for v in B: rank[v] = r
        # properness: no edge inside block
        ok = True
        for B in oblocks:
            for a in range(len(B)):
                for b in range(a+1, len(B)):
                    if adj[B[a]][B[b]]: ok = False; break
                if not ok: break
            if not ok: break
        if not ok: continue
        asc = sum(1 for (u, v) in arcs if rank[u] < rank[v])
        mu = tuple(sorted((len(B) for B in oblocks), reverse=True))
        mdist[mu][asc] += 1
    parts = list(partitions(n))
    pidx = {tuple(p): i for i, p in enumerate(parts)}
    # E matrix per-monomial: a = E c. a_mu = sum over colorings of type mu / (number of monomials of type mu)? 
    # Careful: m_mu = sum of distinct monomials; coefficient a_mu(t) as defined = sum over ordered partitions of type mu.
    # Each ordered partition with l blocks corresponds to l! ... hmm: m_mu monomial x_1^{mu_1}...: assignments of distinct colors to blocks.
    # Ordered partition (B_0<...<B_{l-1}) with ranks: choosing distinct colors c_0<...? No: ordered partition already fixes total order of blocks;
    # actual colorings with values in P projecting to this ordered partition: choose strictly increasing values v_0<...<v_{l-1} in P.
    # Infinitely many! But X groups them: each gives same monomial type with different exponents pattern? No—
    # x^kappa = prod x_{v_r}^{|B_r|}: as values vary, these are distinct monomials of type mu, each appearing once.
    # So coefficient of each monomial of type mu in X = sum over bijections blocks->positions? For a fixed monomial x_1^{mu_{pi1}}...,
    # the preimage is the set of ordered partitions consistent... Standard: coefficient per monomial = #{ordered partitions mapping}.
    # Since symmetric, per-monomial coeff a_mu^{mono} = (total ordered-partition weight of type mu) / (number of distinct monomials assignments...).
    # Number of ordered partitions of type mu (as unlabeled block collections with sizes mu) = n! / (prod mu_i! prod mult!) * l! ... 
    # Simpler: a_mu^{mono}(t) = W_mu(t) / M_mu where W = our mdist sum (each ordered partition counted once) and M_mu = n!/(prod mu_i! prod_c mult_c(mu)!)... 
    # Let's verify: monomials of type mu in variables P infinite: each corresponds to assignment of distinct values to labeled slots? 
    # Standard identity: m_mu = sum over distinct exponent patterns. Coefficient extraction: X = sum_mu W_mu(t) * (sum over increasing value choices)? 
    # Actually X = sum_{oblocks} sum_{v_0<...<v_{l-1}} t^{asc(oblocks)} x_{v_0}^{|B_0|}... — inner sum over increasing tuples =: m_{sizes in order}. Summing over all block orders gives (mult!/l! ...) m_mu.
    # Precisely: for fixed type mu with distinct part values, each unordered collection {blocks} yields l! ordered versions, and sum_{orders} sum_{increasing values} = m_mu (each monomial once per matching of block sizes to values...). If mu has repeated parts, overcount by mult!.
    # So X = sum_mu [W_mu^{sym}(t)] m_mu where W_mu^{sym} = (sum of t^{asc} over ordered partitions of type mu, modulo stabilizer)/... let's just compute:
    # m_mu has distinct monomials; each monomial x_{v_1}^{mu_1}...x_{v_l}^{mu_l} (v_i distinct) arises from ordered partitions where block of size mu_i gets value v_{pi}... 
    # The clean statement: per-monomial coefficient a_mu(t) = (1/(l! / mult... )) hmm. Easiest: compute per-monomial coeff by dividing W_mu by (number of ordered partitions per monomial).
    # Each monomial of type mu: positions of values fixed; blocks must be assigned to values with matching sizes. #assignments = (prod_c mult_c(mu)!) ... no wait.
    # Let's think concretely: monomial M = x_1^3 x_2^2 x_3^1 (mu=(3,2,1), all distinct). Colorings kappa with x^kappa = M: color class sizes fixed per value: class of 1 has size 3, of 2 size 2, of 3 size 1. Ordered partitions (B_0,B_1,B_2) with |B_0|=3,|B_1|=2,|B_2|=1 biject with these colorings (B_i = kappa^{-1}(i+1)). Different size patterns give different monomials. So #ordered partitions of exact size sequence (3,2,1) in order = #colorings with that exact class-size sequence = per-monomial coeff summed over asc weights. Our mdist[(3,2,1)] aggregates over ALL orders of sizes (3,2,1),(3,1,2),... So per-monomial coeff a_{(3,2,1)} = (sum over ordered partitions with sizes exactly (mu_1,...,mu_l) in that order)/1 ... but by symmetry all orders have equal total weight? NO — asc weight depends on order! t^{asc} differs across orders. Hmm, but X is symmetric so per-monomial coeffs for different size-to-value assignments must be related... Actually m_mu symmetric: coefficient is same for all monomials of type mu. Monomial x_1^3 x_2^1 x_3^2 (sizes (3,1,2)) has coefficient = sum over ordered partitions with exact sizes (3,1,2) weighted. For X symmetric these two sums must be EQUAL as polynomials (nontrivial!). So a_mu = (total W_mu)/(number of distinct size orders) = W_mu / (l!/prod mult!). Good — division is exact.
    from math import factorial
    from collections import Counter as C
    amat = {}
    for mu in parts:
        tmu = tuple(mu)
        W = mdist.get(tmu, C())
        l = len(mu); c = C(mu)
        norders = factorial(l)
        for v in c.values(): norders //= factorial(v)
        amat[tmu] = defaultdict(Fraction)
        for pwr, cnt in W.items():
            amat[tmu][pwr] = Fraction(cnt, norders)
    # check integrality
    for mu in parts:
        for pwr, v in amat[tuple(mu)].items():
            assert v.denominator == 1, (mu, pwr, v)
    # build per-power vectors and solve
    maxdeg = max((max(d.keys()) if d else 0) for d in mdist.values())
    _, E = e_basis_monomial_matrix(n, q=n)
    Einv = invert_matrix(E)
    # a_vec[j] poly, c = Einv^T? Convention: E[mu][lam] with a_mu = sum_lam E[mu][lam] c_lam. So c = E^{-1} a.
    import copy
    cpolys = {tuple(lam): defaultdict(Fraction) for lam in parts}
    for pwr in range(maxdeg + 1):
        avec = [amat[tuple(mu)].get(pwr, Fraction(0)) for mu in parts]
        # c = Einv * a
        cvec = [sum(Einv[i][j] * avec[j] for j in range(len(parts))) for i in range(len(parts))]
        for i, lam in enumerate(parts):
            if cvec[i] != 0: cpolys[tuple(lam)][pwr] = cvec[i]
    return cpolys, mdist, total

if __name__ == '__main__':
    n, k = int(sys.argv[1]), int(sys.argv[2])
    cpolys, mdist, total = e_coeffs(n, k)
    print(f"n={n} k={k} orderedBell-scan={total}")
    for lam in sorted(cpolys):
        d = dict(cpolys[lam])
        if d: print(lam, dict(sorted(d.items())))
        else: print(lam, 0)
