"""Exact-arithmetic diagnostics for the quartic complete-edge Walsh inequality.

The all-dimensional proof is algebraic and is given in RESULT.md. These finite
checks replay the identities and the direct expectation independently.
Run with: python3 verify.py
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, prod
from random import Random


def edge_data(n):
    edges = list(combinations(range(n), 2))
    cycles = []
    for i, j, k, l in combinations(range(n), 4):
        cycles += [((i,j),(j,k),(k,l),(i,l)),
                   ((i,j),(j,l),(k,l),(i,k)),
                   ((i,k),(j,k),(j,l),(i,l))]
    assert len(cycles) == 3 * comb(n, 4)
    return edges, cycles


def exact_expectation(a, n):
    return Fraction(sum(sum(coeff * e[i] * e[j] for (i,j),coeff in a.items()) ** 4
                        for e in product((-1,1), repeat=n)), 2**n)


def combinatorial_moment(a, edges, cycles):
    b = {e:a[e]**2 for e in edges}
    return (3 * sum(b.values())**2 - 2 * sum(x*x for x in b.values())
            + 24 * sum(prod(a[e] for e in c) for c in cycles))


def certificate(a, n, edges, cycles):
    m = comb(n,2)
    b = {e:a[e]**2 for e in edges}
    B = sum(b.values())
    alpha = Fraction(12,n-1)
    beta = Fraction(12*(n-3),n-1)
    lam1 = Fraction(2*(3*n*n-14*n+17),n-1)
    r = Fraction(15*n*n-63*n+68,n*(n-1))
    A = sum((a[c[0]]*a[c[1]]-a[c[2]]*a[c[3]])**2 +
            (a[c[1]]*a[c[2]]-a[c[3]]*a[c[0]])**2 for c in cycles)
    D = sum((a[c[0]]*a[c[2]]-a[c[1]]*a[c[3]])**2 for c in cycles)
    s = [sum(b[(min(i,j),max(i,j))] for j in range(n) if j!=i)
         for i in range(n)]
    u = [Fraction(si,1)-Fraction(2*B,n) for si in s]
    u = [ui/(n-2) for ui in u]
    v = {e:Fraction(b[e],1)-Fraction(B,m)-u[e[0]]-u[e[1]] for e in edges}
    assert sum(u)==0
    assert all(sum(v[(min(i,j),max(i,j))] for j in range(n) if j!=i)==0
               for i in range(n))
    norm1 = sum((u[i]+u[j])**2 for i,j in edges)
    norm2 = sum(z*z for z in v.values())
    assert norm1 + norm2 == sum((Fraction(b[e],1)-Fraction(B,m))**2 for e in edges)
    RHS = alpha*A + beta*D + lam1*norm1 + 2*norm2
    LHS = r*B*B - combinatorial_moment(a,edges,cycles)
    assert LHS == RHS, (n,a,LHS,RHS)
    assert LHS >= 2*sum((Fraction(b[e],1)-Fraction(B,m))**2 for e in edges)
    return r, LHS


def test(n):
    E,C = edge_data(n)
    uniform = {e:1 for e in E}
    r, deficit = certificate(uniform,n,E,C)
    assert deficit==0
    assert combinatorial_moment(uniform,E,C) == r*len(E)**2
    for e0 in E:
        if e0 != E[0]: continue
        sparse={e:int(e==e0) for e in E}
        assert combinatorial_moment(sparse,E,C)==1
        certificate(sparse,n,E,C)
    rng=Random(8463801+n)
    for _ in range(9):
        a={e:rng.randint(-4,4) for e in E}
        assert exact_expectation(a,n) == combinatorial_moment(a,E,C)
        certificate(a,n,E,C)
    switching={e:3*((-1)**e[0])*((-1)**(e[1]//2)) for e in E}
    certificate(switching,n,E,C)
    # Verify row-zero Kneser eigenspaces by direct combinatorial summation.
    q=[Fraction(i+1,1)-Fraction(n+1,2) for i in range(n)]
    g={e:q[e[0]]+q[e[1]] for e in E}
    for e in E:
        val=sum(g[f] for f in E if not set(e).intersection(f))
        assert val == -(n-3)*g[e]
    print('EXACT_OK', n, 'dimension',len(E),'cycles',len(C),'sharp_fourth_ratio',r)


if __name__=='__main__':
    for n in (6,7,8):test(n)
    print('VERIFY_OK')
