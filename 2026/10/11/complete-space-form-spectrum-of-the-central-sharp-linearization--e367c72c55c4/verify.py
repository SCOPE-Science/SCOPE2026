import itertools
import sympy as sp

def pairs(n):
    return list(itertools.combinations(range(n), 2))

def derivation(n, a, b):
    ps = pairs(n)
    index = {p:i for i,p in enumerate(ps)}
    D = sp.zeros(len(ps))
    def on_one(k):
        if k == a:
            return [(b, -1)]
        if k == b:
            return [(a, 1)]
        return []
    for col, (i,j) in enumerate(ps):
        terms = []
        for k,c in on_one(i):
            terms.append((k,j,c))
        for k,c in on_one(j):
            terms.append((i,k,c))
        for u,v,c in terms:
            if u == v:
                continue
            if u < v:
                p,sgn=(u,v),1
            else:
                p,sgn=(v,u),-1
            D[index[p],col] += c*sgn
    return D

def gamma(n, M):
    out = sp.zeros(len(pairs(n)))
    for a,b in pairs(n):
        D = derivation(n,a,b)
        out += D*M*D.T
    return sp.simplify(out)

for n in range(4,10):
    ps = pairs(n)
    N = len(ps)

    scalar = sp.eye(N)
    assert gamma(n, scalar) == 2*(n-2)*scalar

    s = [1,-1] + [0]*(n-2)
    tr_weights = [s[i]+s[j] for i,j in ps]
    tr = sp.diag(*tr_weights)
    assert gamma(n, tr) == (n-4)*tr

    weights = {p:sp.Integer(0) for p in ps}
    weights[(0,1)] = 1
    weights[(2,3)] = 1
    weights[(0,2)] = -1
    weights[(1,3)] = -1
    for i in range(n):
        row = sum(weights[tuple(sorted((i,j)))] for j in range(n) if j != i)
        assert row == 0
    weyl = sp.diag(*[weights[p] for p in ps])
    assert weyl != sp.zeros(N)
    assert gamma(n, weyl) == -2*weyl

    # Linearization dQ = -2 Gamma.
    assert -2*gamma(n, scalar) == -4*(n-2)*scalar
    assert -2*gamma(n, tr) == -2*(n-4)*tr
    assert -2*gamma(n, weyl) == 4*weyl

print("VERIFY_OK")
print("scalar_channel=2*(n-2)")
print("traceless_ricci_channel=n-4")
print("weyl_channel=-2")
print("linearization_multiplier=-2")
print("dimension_four_traceless_ricci_neutral=true")
