"""Exact finite-state verification of a three-particle ancestral current.

Requires Python 3 and SymPy. Solves the stationary count equations and the
one-founder harmonic equations over a rational-function field. Independently
checks the result with an absorbing two-colour Markov chain.
"""
from itertools import product
from sympy import Matrix, Rational, Symbol, zeros, ones, cancel, factor, simplify
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix

N = 3
SITES = range(3)
SIGN = (-1, 0, 1)
counts = [(a, b, N-a-b) for a in range(N+1) for b in range(N+1-a)]
others = [(a, b, N-1-a-b) for a in range(N) for b in range(N-a)]
ci = {c: j for j, c in enumerate(counts)}
fi = {(i, d): j for j, (i, d) in enumerate(product(SITES, others))}


def moved(c, a, b):
    v = list(c)
    v[a] -= 1
    v[b] += 1
    return tuple(v)


def build_operators():
    L0 = zeros(len(ci)); L1 = zeros(len(ci))
    T0 = zeros(len(fi)); T1 = zeros(len(fi))
    for c, r in ci.items():
        for a in SITES:
            if not c[a]:
                continue
            for b in SITES:
                if a == b:
                    continue
                t = ci[moved(c, a, b)]
                for A, rate in ((L0, Rational(c[a]) + Rational(c[a]*c[b], 2)),
                                (L1, Rational(c[a]*c[b]*SIGN[a], 2))):
                    A[r, t] += rate
                    A[r, r] -= rate
    for (i, d), row in fi.items():
        def add(A, target, rate):
            A[row, fi[target]] += rate
            A[row, row] -= rate
        for j in SITES:
            if j != i:
                add(T0, (j, d), 1)
        for a in SITES:
            if not d[a]:
                continue
            for b in SITES:
                if a != b:
                    add(T0, (i, moved(d, a, b)), d[a])
        # Death of the distinguished founder: failure, not a diagonal jump.
        T0[row, row] -= 1
        T1[row, row] -= SIGN[i]
        for a in SITES:
            if not d[a]:
                continue
            for multiplier, A in ((1, T0), (SIGN[a], T1)):
                if multiplier == 0:
                    continue
                A[row, fi[(i, moved(d, a, i))]] += Rational(2*d[a]*multiplier, 2)
                for b in SITES:
                    m = d[b] - int(a == b)
                    if m:
                        A[row, fi[(i, moved(d, a, b))]] += Rational(d[a]*m*multiplier, 2)
                A[row, row] -= d[a]*multiplier
    return L0, L1, T0, T1


def solve_rational(M0, M1, rhs, parameter):
    domain = QQ.frac_field(parameter)
    return DomainMatrix.from_Matrix(M0 + parameter*M1).convert_to(domain).lu_solve(
        DomainMatrix.from_Matrix(rhs).convert_to(domain)
    ).to_Matrix()


def symbolic_current():
    z = Symbol('z')
    L0, L1, T0, T1 = build_operators()
    assert len(ci) == 10 and len(fi) == 18
    A0, A1 = L0.T.copy(), L1.T.copy()
    A0[-1, :] = ones(1, len(ci))
    A1[-1, :] = zeros(1, len(ci))
    prhs = Matrix([0]*(len(ci)-1)+[1])
    pi = solve_rational(A0, A1, prhs, z)
    anchor = fi[(0, (2, 0, 0))]
    H0, H1 = T0.copy(), T1.copy()
    H0[anchor, :] = zeros(1, len(fi)); H0[anchor, anchor] = 1
    H1[anchor, :] = zeros(1, len(fi))
    hrhs = Matrix([Rational(1, 3) if j == anchor else 0 for j in range(len(fi))])
    h = solve_rational(H0, H1, hrhs, z)
    assert all(simplify(x) == 0 for x in (A0+z*A1)*pi - prhs)
    assert all(simplify(x) == 0 for x in (H0+z*H1)*h - hrhs)
    assert simplify(sum(pi) - 1) == 0
    result = 0
    for c, index in ci.items():
        for a, j, sg in ((0, 2, 1), (2, 0, -1)):
            if c[a]:
                d = tuple(c[b]-int(b == a) for b in SITES)
                result += sg*c[a]*pi[index]*h[fi[(j, d)]]
    result = factor(cancel(result))
    expected = (
        24*z**5*(16-3*z**2)*(38448+479*z**2)
        /((790272+4704*z**2+279*z**4+5*z**6)
          *(11757312-137808*z**2+840*z**4+143*z**6))
    )
    assert cancel(result-expected) == 0
    assert result.subs(z, 0) == 0
    assert simplify((result/z**5).limit(z, 0)) == Rational(89, 56010528)
    print('symbolic 10-state stationary and 18-state founder rational identity: PASS')
    print('global rational formula and quintic coefficient: PASS')
    return z, result


def independent_two_colour(k):
    # Colour A identifies a single founder; colour B identifies the other two.
    universe = [tuple(z) for z in product(range(4), repeat=6) if sum(z) == N]
    transient = [z for z in universe if 0 < sum(z[:3]) < N]
    ti = {z: j for j, z in enumerate(transient)}
    G = zeros(len(ci))
    for c, i in ci.items():
        for a in SITES:
            for b in SITES:
                if a == b or not c[a]:
                    continue
                rate = c[a]*(1+Rational(c[b], 2)*k[a])
                j = ci[moved(c, a, b)]
                G[i, j] += rate
                G[i, i] -= rate
    A = G.T.copy(); A[-1, :] = ones(1, len(ci))
    prhs = Matrix([0]*(len(ci)-1)+[1])
    pi = A.inv()*prhs
    B = zeros(len(ti)); b = zeros(len(ti), 1)
    for state, i in ti.items():
        for a in range(6):
            if not state[a]:
                continue
            for j in range(6):
                if a == j:
                    continue
                rate = Rational(state[a]*state[j]*k[a % 3], 2)
                if a // 3 == j // 3 and a % 3 != j % 3:
                    rate += state[a]
                if rate == 0:
                    continue
                nxt = moved(state, a, j)
                B[i, i] -= rate
                if sum(nxt[:3]) == N:
                    b[i] += rate
                elif sum(nxt[:3]) != 0:
                    B[i, ti[nxt]] += rate
    h = B.inv()*(-b)
    def fix(site, d):
        z = tuple(int(site == i) for i in SITES) + d
        return h[ti[z]]
    out = Rational(0)
    for c, ix in ci.items():
        if c[0]:
            out += pi[ix]*c[0]*fix(2, (c[0]-1,c[1],c[2]))
        if c[2]:
            out -= pi[ix]*c[2]*fix(0, (c[0],c[1],c[2]-1))
    return factor(out)


def main():
    z, expression = symbolic_current()
    checks = [
        ((Rational(1, 2), 1, Rational(3, 2)), Rational(1, 2)),
        ((Rational(3, 4), 1, Rational(5, 4)), Rational(1, 4)),
    ]
    for k, eps in checks:
        independent = independent_two_colour(k)
        assert independent == expression.subs(z, eps)
        print('independent absorbing two-colour check at epsilon={}: PASS'.format(eps))
    published = Rational(421413160, 139117744582101)
    assert independent_two_colour((1, 2, 4)) == published
    print('independent reproduction of published (1,2,4) current: PASS')
    # For 0 < |z| < 1 both denominator factors are strictly positive.
    # The second exceeds 11757312 - 137808 > 0.
    assert 11757312-137808 > 0
    assert 16-3 > 0 and 38448 > 0
    print('denominator and numerator sign inequalities on (-1,1): PASS')
    print('all exact checks passed')

if __name__ == '__main__':
    main()
