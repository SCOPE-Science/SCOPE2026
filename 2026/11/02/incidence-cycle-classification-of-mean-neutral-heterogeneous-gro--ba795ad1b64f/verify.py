"""Exact checks for incidence-cycle balance in directed group opinion dynamics.

Requires sympy >= 1.12. This tests finite instances and algebraic identities;
the all-hypergraph classification is established by the accompanying proof.
"""
from itertools import combinations
from random import Random
from sympy import Matrix, Rational, eye, zeros, symbols, factor, simplify


def projection(n, edges, weights, contributions):
    assert len(edges) == len(weights) == len(contributions)
    w = zeros(n)
    for e, weight, gamma in zip(edges, weights, contributions):
        e = tuple(e)
        k = len(e)
        assert k >= 2 and len(set(e)) == k and weight > 0
        assert set(gamma) == set(e)
        assert simplify(sum(gamma.values()) - 1) == 0 and all(val.is_positive is not False for val in gamma.values())
        c = 2 * weight / (k - 1)
        for i in e:
            for j in e:
                if i != j:
                    w[i, j] += c * gamma[j]
    laplacian = zeros(n)
    for i in range(n):
        for j in range(n):
            laplacian[i, j] = -w[i, j] if i != j else sum(w[i, k] for k in range(n))
    return laplacian


def incidence_matrix(n, edges):
    columns = [(j, v) for j, e in enumerate(edges) for v in e]
    a = zeros(n + len(edges), len(columns))
    for k, (j, v) in enumerate(columns):
        a[v, k] = 1
        a[n+j, k] = -1
    return a, columns


def component_count(n, edges):
    total = n + len(edges)
    parent = list(range(total))
    def root(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k
    for j, e in enumerate(edges):
        for v in e:
            a,b = root(v),root(n+j)
            parent[a] = b
    return len({root(i) for i in range(total)})


def checks():
    d = symbols('d', real=True)
    one = Rational(1, 1)
    third = Rational(1, 3)
    edges = [(0,1,2), (1,2,3)]
    gamma = [
        {0: third, 1: third+d, 2: third-d},
        {1: third-d, 2: third+d, 3: third},
    ]
    l = projection(4, edges, [one, one], gamma)
    o = (eye(4) + l).inv()
    expected = Matrix([
        [Rational(23,35), Rational(1,7)+d/5, Rational(1,7)-d/5, Rational(2,35)],
        [Rational(1,7), Rational(11,21), Rational(4,21), Rational(1,7)],
        [Rational(1,7), Rational(4,21), Rational(11,21), Rational(1,7)],
        [Rational(2,35), Rational(1,7)-d/5, Rational(1,7)+d/5, Rational(23,35)],
    ])
    assert all(simplify(v) == 0 for v in o-expected)
    assert all(simplify(sum(l[i,j] for i in range(4))) == 0 for j in range(4))
    assert all(simplify(sum(o[i,j] for i in range(4))-1) == 0 for j in range(4))
    for x, sign in ((Matrix([1,1,0,0]),1), (Matrix([1,0,1,0]),-1)):
        z = o*x
        p = factor(sum((v-sum(z)/4)**2 for v in z))
        assert simplify(p - (18*d*d + 54*sign*d + 53)/225) == 0
        assert factor(p.subs(d, Rational(1,6))) == (Rational(5,18) if sign == 1 else Rational(89,450))
        assert simplify(sum(z) - sum(x)) == 0
    # Independent nonuniform mean-neutral cycle with unequal hyperedge weights.
    h1, h2, amplitude = Rational(2), Rational(3), Rational(1, 5)
    unequal_gammas = [
        {0: third, 1: (1 + amplitude/h1)/3, 2: (1 - amplitude/h1)/3},
        {1: (1 - amplitude/h2)/3, 2: (1 + amplitude/h2)/3, 3: third},
    ]
    unequal_l = projection(4, edges, [h1, h2], unequal_gammas)
    unequal_o = (eye(4) + unequal_l).inv()
    assert all(sum(unequal_l[i,j] for i in range(4)) == 0 for j in range(4))
    assert all(sum(unequal_o[i,j] for i in range(4)) == 1 for j in range(4))
    assert unequal_l != unequal_l.T
    # The role inequalities are sharp along this single cycle direction.
    assert min(h1, h2) > amplitude
    # Strict positivity of the roles is ensured at all sampled parameter values.
    rng = Random(20261027)
    total = 0
    for n in range(3,8):
        subsets = [s for k in range(2,min(n,4)+1) for s in combinations(range(n),k)]
        for _ in range(35):
            m = rng.randint(1,min(6,len(subsets)))
            es = rng.sample(subsets,m)
            contributions=[]
            weights=[]
            for e in es:
                raw = [rng.randint(1,7) for _ in e]
                contributions.append(dict(zip(e, (Rational(t,sum(raw)) for t in raw))))
                weights.append(Rational(rng.randint(1,5), rng.randint(1,5)))
            lap=projection(n,es,weights,contributions)
            omega=(eye(n)+lap).inv()
            a,cols=incidence_matrix(n,es)
            cyclo = len(cols)-n-m+component_count(n,es)
            assert len(cols)-a.rank()==cyclo
            q=[]
            for ei,v in cols:
                k=len(es[ei]); c=2*weights[ei]/(k-1)
                q.append(c*(k*contributions[ei][v]-1))
            qq=Matrix(q)
            assert all(z==0 for z in a[n:,:]*qq)
            for i in range(n):
                assert simplify(sum(lap[j,i] for j in range(n)) + (a*qq)[i]) == 0
            balanced=all(z==0 for z in a*qq)
            assert balanced == all(simplify(sum(omega[j,i] for j in range(n))-1)==0 for i in range(n))
            assert all(simplify(sum(omega[i,j] for j in range(n))-1)==0 for i in range(n))
            total+=1
    print('PASS: two-triple symbolic resolvent and both exact polarization formulas')
    print(f'PASS: {total} exact-rational hypergraphs; balance, incidence nullity, and equilibrium mean')

if __name__=='__main__':
    checks()
