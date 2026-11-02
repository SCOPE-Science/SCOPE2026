"""Exact reproducibility checks for two-guru discounted delegation forests.

Run with Python 3.10+ (standard library only).
"""
from fractions import Fraction
from itertools import product
from math import prod


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_eval(a, x):
    value = Fraction(0)
    for c in reversed(a):
        value = value * x + c
    return value


def m_polynomial(m):
    assert m >= 1
    out = [0, 1]
    out = mul(out, [1, -1])
    for j in range(1, 2*m):
        out = mul(out, [-j, 2*m])
    return out


def level_profiles(coeffs):
    assert coeffs[0] == 0
    assert sum(coeffs) == 0
    a = [1] + [1 + max(c, 0) for c in coeffs[1:]]
    b = [1] + [1 + max(-c, 0) for c in coeffs[1:]]
    assert sum(a) == sum(b)
    assert all(x >= 1 for x in a+b)
    assert [x-y for x, y in zip(a,b)] == coeffs
    return a, b


def rooted_tree_from_levels(level_counts):
    # Every positive level profile is feasible: attach each new vertex
    # to the first vertex at its preceding depth.
    parents, depth, prior = [-1], [0], [0]
    for d, count in enumerate(level_counts[1:], 1):
        new = list(range(len(parents), len(parents) + count))
        parents.extend([prior[0]] * count)
        depth.extend([d] * count)
        prior = new
    for v in range(1, len(parents)):
        assert depth[parents[v]] == depth[v] - 1
        p, steps = v, 0
        while p:
            p = parents[p]
            steps += 1
            assert steps <= len(parents)
        assert steps == depth[v]
    return parents, depth


def accuracy(w1, w2):
    q1, q2 = Fraction(4, 5), Fraction(3, 5)
    if w1 > w2:
        return q1
    if w1 < w2:
        return q2
    return (q1 + q2) / 2



def trim(p):
    p = [Fraction(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_divmod(a, b):
    a, b = trim(a), trim(b)
    assert any(b)
    q = [Fraction(0)] * max(1, (len(a)-len(b)+1))
    while len(a) >= len(b) and any(a):
        t = a[-1]/b[-1]
        s = len(a)-len(b)
        q[s] = t
        for k in range(len(b)):
            a[k+s] -= t*b[k]
        a = trim(a)
    return trim(q), a


def poly_gcd(a,b):
    a,b=trim(a),trim(b)
    while any(b):
        _,r = poly_divmod(a,b)
        a,b=b,r
    return [x/a[-1] for x in a] if any(a) else [Fraction(0)]


def interior_root_count(p):
    p=trim(p)
    if len(p)==1: return 0
    while len(p)>1 and p[0]==0:
        p=p[1:]
    # Remove the endpoint root t=1 as often as necessary.
    while len(p)>1 and poly_eval(p,Fraction(1)) == 0:
        q,r=poly_divmod(p,[-1,1])
        assert r==[0]
        p=q
    if len(p)==1: return 0
    derivative=[i*p[i] for i in range(1,len(p))]
    gcd=poly_gcd(p, derivative)
    q,r=poly_divmod(p,gcd)
    assert r==[0]
    p=q
    if len(p)==1: return 0
    derivative=[i*p[i] for i in range(1,len(p))]
    seq=[p,derivative]
    while True:
        _,r=poly_divmod(seq[-2],seq[-1])
        if not any(r): break
        seq.append([-x for x in r])
    def variations(t):
        signs=[]
        for f in seq:
            v=poly_eval(f,t)
            if v: signs.append(1 if v>0 else -1)
        return sum(signs[i] != signs[i-1] for i in range(1,len(signs)))
    return variations(Fraction(0))-variations(Fraction(1))


def check():
    # Universal coefficient realization, then multiple exact sign windows.
    profiles = 0
    samples = 0
    for m in range(1, 5):
        coeffs = m_polynomial(m)
        A, B = level_profiles(coeffs)
        assert poly_eval(coeffs, Fraction(0)) == 0
        assert poly_eval(coeffs, Fraction(1)) == 0
        for j in range(2*m):
            mid = Fraction(2*j+1, 4*m)
            expected = Fraction(4, 5) if j % 2 else Fraction(3, 5)
            assert accuracy(poly_eval(coeffs, mid), 0) == expected
            samples += 1
        for j in range(1, 2*m):
            assert poly_eval(coeffs, Fraction(j, 2*m)) == 0
            samples += 1
        assert len(A) == len(B) == len(coeffs)
        profiles += 1
        if m <= 2:
            pa, da = rooted_tree_from_levels(A)
            pb, db = rooted_tree_from_levels(B)
            assert len(pa) == len(pb) == sum(A)
            for t in (Fraction(0),Fraction(1, 5),Fraction(2, 5),
                      Fraction(3, 5),Fraction(4, 5),Fraction(1)):
                left = sum(t**d for d in da)
                right = sum(t**d for d in db)
                assert left - right == poly_eval(coeffs, t)
                samples += 1

    # An explicit six-voter example: a two-leaf star versus a length-2 chain.
    star = [1, 2]
    chain = [1, 1, 1]
    ps, ds = rooted_tree_from_levels(star)
    pc, dc = rooted_tree_from_levels(chain)
    assert len(ps) + len(pc) == 6
    for t in (Fraction(0), Fraction(1, 20), Fraction(1, 2),
              Fraction(19, 20), Fraction(1)):
        delta = sum(t**d for d in ds) - sum(t**d for d in dc)
        assert delta == t*(1-t)
        assert accuracy(delta,0) == (Fraction(7,10) if t in (0,1) else Fraction(4,5))
        samples += 1

    # Every fixed finite grid is evaded by a rational interval in its complement.
    grid = [Fraction(j, 20) for j in range(21)]
    r, s = Fraction(101, 400), Fraction(103, 400)
    # t(1-t)(400t-101)(103-400t): positive precisely on (r,s).
    Q = mul(mul(mul([0,1],[1,-1]),[-101,400]),[103,-400])
    level_profiles(Q)
    assert not any(r <= t <= s for t in grid)
    assert accuracy(poly_eval(Q, (r+s)/2),0) == Fraction(4,5)
    assert max(accuracy(poly_eval(Q,t),0) for t in grid) == Fraction(7,10)
    samples += len(grid)+1

    # Complete exact census of labeled, cycle-free fixed-delegation forests of
    # order at most five, with exact Sturm root counts for every guru majority.
    forest_count = 0
    signatures = set()
    critical_signatures = 0
    for n in range(1,6):
        for parent in product(range(n), repeat=n):
            roots = [i for i in range(n) if parent[i] == i]
            if not roots:
                continue
            dist, owner = [], []
            ok = True
            for i in range(n):
                v, seen, hops = i, set(), 0
                while parent[v] != v:
                    if v in seen:
                        ok = False; break
                    seen.add(v)
                    v = parent[v]
                    hops += 1
                if not ok: break
                owner.append(roots.index(v)); dist.append(hops)
            if not ok: continue
            forest_count += 1
            levels = [tuple(sum(owner[i] == r and dist[i] == d for i in range(n))
                            for d in range(n)) for r in range(len(roots))]
            signature = tuple(levels)
            signatures.add(signature)
            critical = set()
            for mask in range(1, (1<<len(roots))-1):
                margin = [sum((1 if mask&(1<<r) else -1)*levels[r][d]
                              for r in range(len(roots))) for d in range(n)]
                roots_inside = interior_root_count(margin)
                assert roots_inside <= 1
                if roots_inside:
                    # For n<=5 all nontrivial interior roots come from
                    # t+t^2-1 or 2t-1, up to multiplication by t^k, sign.
                    polynomial = trim(margin)
                    while len(polynomial)>1 and polynomial[0]==0:
                        polynomial = polynomial[1:]
                    polynomial = [v/polynomial[-1] for v in polynomial]
                    critical.add(tuple(polynomial))
            assert len(critical) <= 1, (n,signature,critical)
            critical_signatures += bool(critical)
    assert forest_count > 1000
    print(f"PASS: {profiles} polynomial families; {samples} rational crosschecks; {forest_count} forests on <=5 vertices; {len(signatures)} level signatures; {critical_signatures} forests with a unique interior breakpoint")

if __name__ == '__main__':
    check()
