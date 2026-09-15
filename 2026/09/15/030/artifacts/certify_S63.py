"""Certify S(g) = sum_chi chi(g)^3/chi(1) for all 74 classes of PSp_6(3).
Unlike floats, certify EXACTLY using cyclotomic arithmetic in Q(E(39))? Values involve E(3) and E(13).
chi(g)^3/chi(1): terms are Z-linear combos of E(3)^a * E(13)^b-type products. Since 3 and 13 coprime, work in
Q(E(39)) with exact integer-coefficient polynomial arithmetic mod Phi_39. Simpler robust approach:
exact representation as dict {(a,b): coef} for E(3)^a E(13)^b, reduced via relations. Even simpler and fully rigorous:
compute S(g) in two independent ways: (i) high-precision complex (50 digits via mpmath-free long double? use fractions of sympy exact cyclotomics),
(ii) sympy exact with primitive roots (RootOf unity) and simplify to zero/nonzero.
Here: use sympy with exp(2*pi*I*k/n) exact? sympy has primitive_root / exp; use sympy.nsimplify? Better: represent each value as element of Q(zeta_39) exactly as polynomial in zeta_39.
E(3) = zeta_39^13, E(13) = zeta_39^3. All table entries are Z-linear combos of powers of zeta_39. chi(g)^3 expands to Z-combo of zeta_39 powers; divide by degree (rational). Sum -> element of Q(zeta_39). Reduce mod Phi_39 (degree 24) to normal form; check zero/nonzero by exact integer arithmetic.
"""
import re, math, json
from fractions import Fraction

PHI39_DEG = 24  # phi(39)=phi(3)*phi(13)=2*12

def eval_terms(expr):
    expr = expr.replace(' ', '').replace('\n', '')
    if expr == '': return [], Fraction(0)
    terms = []; const = Fraction(0)
    for term in expr.replace('-', '+-').split('+'):
        if term == '': continue
        m = re.fullmatch(r'(-?\d*)\*?E\((\d+)\)(?:\^(\d+))?', term)
        if m:
            cs, ns, ks = m.groups()
            coef = 1 if cs in ('', None) else (-1 if cs == '-' else int(cs))
            terms.append((coef, int(ns), int(ks) if ks else 1))
        else:
            const += Fraction(term)
    return terms, const

def to_z39(expr, gal13=1, conj3=False):
    """Convert expr to polynomial in zeta_39 as dict {exp: Fraction}. zeta_39 = E(39).
    E(3)^k = zeta_39^(13k); E(13)^k = zeta_39^(3*gal13*k); conj3: apply E(3)^k->E(3)^{-k} for generated E(3) rows."""
    terms, const = eval_terms(expr)
    d = {0: const}
    for coef, n, k in terms:
        if n == 3:
            kk = (-k) % 3 if conj3 else (k % 3)
            e = (13 * kk) % 39
        elif n == 13:
            e = (3 * ((gal13 * k) % 13)) % 39
        elif n == 1:
            e = 0
        else:
            raise ValueInError(f'unsupported order {n}')
        d[e] = d.get(e, Fraction(0)) + Fraction(coef)
    return {e: c for e, c in d.items() if c != 0}

class ValueError(Exception): pass
class InError(Exception): pass

def split_top(s):
    assert s[0] == '[' and s[-1] == ']'
    inner = s[1:-1]
    parts, depth, cur = [], 0, ''
    for c in inner:
        if c == '(': depth += 1; cur += c
        elif c == ')': depth -= 1; cur += c
        elif c == ',' and depth == 0: parts.append(cur); cur = ''
        else: cur += c
    parts.append(cur)
    return parts

blk = open('output/irr_S63.txt').read()
rows = []
depth = 0; start = None
for idx, c in enumerate(blk):
    if c == '[':
        if depth == 1: start = idx
        depth += 1
    elif c == ']':
        depth -= 1
        if depth == 1 and start is not None:
            rows.append(blk[start:idx+1]); start = None

# Build table as (exprs, gal13, conj3) per row
table = []
for r in rows:
    if r.startswith('[GALOIS'):
        exprs, g13, c3 = table[-1]
        has13 = any('E(13)' in p for p in exprs)
        table.append((exprs, 2 if has13 else 1, False if has13 else True))
    else:
        table.append((split_top(r), 1, False))
assert len(table) == 74

NCOL = len(table[0][0])
# degrees
degs = []
for exprs, g13, c3 in table:
    t, c = eval_terms(exprs[0])
    assert not t
    degs.append(int(c))

# Exact arithmetic in Z[zeta_39]: represent poly as dict exp->Fraction; multiply via convolution mod x^39-1, then reduce mod Phi_39.
# Reduction mod Phi_39(x) = Phi_3(x^13)/...? Simpler: Phi_39(x) = Phi_13(x^3)/Phi_13(x)? Hmm. Easiest exact reduction:
# Use relation zeta_39^39=1 then reduce exponents >= 39, then use the two relations:
#   1 + zeta_3 + zeta_3^2 = 0  i.e. 1 + z^13 + z^26 = 0, and
#   1 + zeta_13 + ... + zeta_13^12 = 0 i.e. sum_{j=0..12} z^{3j} = 0.
# These two generate the full relation ideal? The relation lattice: a polynomial f(z) vanishes at zeta_39 iff f in (Phi_39).
# Reducing via the two subfield relations gives a normal form? The set {z^i : ... } — dimension check: quotient by both relations:
# start 39 dims; first relation (times z^k, k=0..12?) gives 13 relations but dependent... Safer: reduce using integer linear algebra:
# compute normal form by finding, for the exponent vector, its projection onto basis of Q(zeta)^dual via exact Galois traces?
# Alternative rigorous zero-test: S(g) != 0 iff Tr_{Q(zeta)/Q}(S(g) * zeta^j) != 0 for some j. Traces computable combinatorially without normal forms:
# Tr(zeta^e) = mu(39/gcd(39,e)) * phi(39)/phi(39/gcd(39,e)). Then S(g)=sum_e c_e zeta^e is zero iff all 39 traces t_j = Tr(S zeta^j) vanish.
# And S(g) as computed: expand chi^3 then divide by degree — all exact Fractions. Compute t_j exactly. Zero-test + nonzero certificate.
def trace_z39(e):
    e %= 39
    if e == 0: return Fraction(PHI39_DEG)
    import math
    g = math.gcd(39, e)
    m = 39 // g  # order of zeta^e
    # Tr = mu(m) * phi(39)/phi(m)
    def mu(n):
        f = {}
        d = 2
        nn = n
        while d*d <= nn:
            if nn % d == 0:
                c = 0
                while nn % d == 0: nn //= d; c += 1
                if c > 1: return 0
                f[d] = 1
            d += 1 if d == 2 else 2
        if nn > 1: f[nn] = 1
        return -1 if len(f) % 2 else 1
    def phi(n):
        r = n; nn = n; d = 2
        while d*d <= nn:
            if nn % d == 0:
                while nn % d == 0: nn //= d
                r -= r // d
            d += 1 if d == 2 else 2
        if nn > 1: r -= r // nn
        return r
    return Fraction(mu(m) * (PHI39_DEG // phi(m)))

# sanity: Tr(1)=24; sum of all 39 traces-weighted... check orthogonality of trace pairing later via results.
assert trace_z39(0) == 24 and trace_z39(13) == trace_z39(26) == -12 and trace_z39(3) == -2 and trace_z39(1) == 1, [trace_z39(e) for e in [0,13,26,3,1,39]]

def poly_mul_mod39(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = (e1 + e2) % 39
            out[e] = out.get(e, Fraction(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}

# Precompute each table entry as z39-poly
T = []
for exprs, g13, c3 in table:
    T.append([to_z39(p, g13, c3) for p in exprs])

# Compute S(g) polys: S(g) = sum_chi chi(g)^3 / chi(1)
S = []
for g in range(NCOL):
    acc = {}
    for i in range(74):
        v = T[i][g]
        v2 = poly_mul_mod39(v, v)
        v3 = poly_mul_mod39(v2, v)
        d = degs[i]
        for e, c in v3.items():
            acc[e] = acc.get(e, Fraction(0)) + c / d
    S.append({e: c for e, c in acc.items() if c != 0})

# Zero test via traces: t_j(g) = Tr(S(g) z^j) for j=0..38; S(g)=0 iff all zero.
results = []
for g in range(NCOL):
    ts = []
    for j in range(39):
        t = Fraction(0)
        for e, c in S[g].items():
            t += c * trace_z39(e + j)
        ts.append(t)
    is_zero = all(t == 0 for t in ts)
    results.append((g+1, is_zero, ts))
    print(f'class {g+1}: S==0? {is_zero}  t0={ts[0]}')

nzero = sum(1 for _, z, _ in results if z)
print('zero classes:', nzero)
json.dump([{'class': c, 'is_zero': z, 't0': str(t[0])} for c, z, t in results], open('output/S63_trace_results.json', 'w'), indent=1)
