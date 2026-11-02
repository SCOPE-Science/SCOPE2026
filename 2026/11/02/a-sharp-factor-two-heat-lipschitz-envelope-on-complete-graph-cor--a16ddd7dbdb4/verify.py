"""Independent finite graph heat and transport checks for complete-graph coronas.

Requires only Python 3 standard library. These finite checks corroborate, but do
not replace, the all-order analytical proof in RESULT.md.
"""
from math import exp, sqrt, log
from fractions import Fraction
from itertools import product


def graph(n):
    # Core vertices 0..n-1, pendant vertices n..2n-1.
    adj = [[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(i+1,n):
            adj[i][j] = adj[j][i] = 1
        adj[i][n+i] = adj[n+i][i] = 1
    return adj


def heat_row(n, origin, t):
    adj = graph(n)
    size = 2*n
    # Maximal vertex degree is n. Uniformization stochastic matrix P.
    p = [[(1 if i == j else 0) + (adj[i][j] - (sum(adj[i]) if i == j else 0))/n
          for j in range(size)] for i in range(size)]
    row = [0.0]*size
    row[origin] = 1.0
    out = [0.0]*size
    coefficient = exp(-n*t)
    k = 0
    while True:
        for j in range(size):
            out[j] += coefficient*row[j]
        if k > n*t and coefficient < 2e-18:
            break
        row = [sum(row[i]*p[i][j] for i in range(size)) for j in range(size)]
        k += 1
        coefficient *= (n*t)/k
        if k > 1000:
            raise AssertionError('uniformization did not converge')
    assert abs(sum(out)-1) < 4e-14
    return out


def tau(n,t):
    d=sqrt(n*n+4)
    alpha=(n+2-d)/2
    beta=(n+2+d)/2
    x=exp(-alpha*t)
    y=exp(-beta*t)
    p=((beta-n-1)*x+(n+1-alpha)*y)/d
    q=(x-y)/d
    r=((beta-1)*x+(1-alpha)*y)/d
    return p,q,r


def formulas(n,t):
    p,q,r=tau(n,t)
    leaf=(n-1)/n*(2*r+(n-2)*q)-(n-2)/n*exp(-2*t)
    core=r+(3-n)*q
    return leaf,core


def transport(mu,n):
    # Exact minimum-cost flow formula on K_n with n pendant leaves.
    return (sum(abs(mu[n+i]) for i in range(n)) +
            sum(abs(mu[i]+mu[n+i]) for i in range(n))/2)


def integer_potentials(n):
    # Exhausts integral 1-Lipschitz potentials after fixing core 0 at 0.
    # The unit graph-Lipschitz polytope has integral vertices because its
    # difference-constraint matrix is totally unimodular.
    for tail in product((-1,0,1),repeat=n-1):
        core=(0,)+tail
        if max(core)-min(core)>1:
            continue
        for shifts in product((-1,0,1),repeat=n):
            yield core+tuple(core[i]+shifts[i] for i in range(n))


def checks():
    cases=0
    edge_tests=0
    for n in range(2,13):
        adj=graph(n)
        for t in (0.004,0.03,0.1,0.25,0.7):
            rows=[heat_row(n,i,t) for i in range(2*n)]
            w_leaf,w_core=formulas(n,t)
            mu_leaf=[rows[n][i]-rows[0][i] for i in range(2*n)]
            mu_core=[rows[0][i]-rows[1][i] for i in range(2*n)]
            assert abs(transport(mu_leaf,n)-w_leaf) < 2e-12,(n,t,'leaf')
            assert abs(transport(mu_core,n)-w_core) < 2e-12,(n,t,'core')
            assert (w_leaf > w_core) == (n>=3),(n,t,'winner')
            assert max(w_leaf,w_core) < 2
            # Independently check all edges, not just representatives.
            for i in range(2*n):
                for j in range(i+1,2*n):
                    if adj[i][j]:
                        mu=[rows[i][k]-rows[j][k] for k in range(2*n)]
                        value=transport(mu,n)
                        expected=w_core if j<n else w_leaf
                        assert abs(value-expected)<2e-12,(n,t,i,j,value,expected)
                        edge_tests+=1
            cases+=1
    dual_tests=0
    for n in range(2,6):
        potentials=list(integer_potentials(n))
        adj=graph(n)
        for t in (0.03,0.4):
            rows=[heat_row(n,i,t) for i in range(2*n)]
            for i in range(2*n):
                for j in range(i+1,2*n):
                    if adj[i][j]:
                        mu=[rows[i][k]-rows[j][k] for k in range(2*n)]
                        dual=max(sum(f[k]*mu[k] for k in range(2*n)) for f in potentials)
                        assert abs(dual-transport(mu,n))<2e-12,(n,i,j,t)
                        dual_tests+=1
    # Taylor coefficient in the formula is n-3, compare a finite difference.
    for n in range(2,13):
        h=1.e-7
        fd=(formulas(n,h)[0]-1)/h
        assert abs(fd-(n-3))< 5e-5,(n,fd)
    # Large-order approximation to the universal sharp envelope.
    for n in (100,1000,10000):
        t=log(n)/n
        leaf,core=formulas(n,t)
        assert leaf<2 and leaf>2-15*log(n)/n,(n,leaf)
    print('CHECK_OK complete_corona_n=2..12 time_cases=%d edge_transport_checks=%d' % (cases,edge_tests))
    print('CHECK_OK independent_integer_KR_dual_cases=%d' % dual_tests)
    print('CHECK_OK onset_derivative=n_minus_3 limiting_envelope=2')

if __name__ == '__main__':
    checks()
