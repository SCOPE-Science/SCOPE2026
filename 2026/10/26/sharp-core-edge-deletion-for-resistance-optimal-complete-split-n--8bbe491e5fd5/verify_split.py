"""Finite checks of the complete-split-graph conductance theorem.

Requires NumPy and SymPy. This file only tests finite instances;
the all-size conclusion is established by the accompanying proof.
"""
import math
import numpy as np
import sympy as sp


def optimal(r, s, B):
    n = r + s
    H = math.sqrt(n * r * (r + 1) / (n - 1))
    ratio = max((H - s) / r, 0.0)
    b = B / (r * s + r * (r - 1) * ratio / 2)
    return ratio * b, b


def edges(r, s):
    return ([(i, j, 'clique') for i in range(r) for j in range(i + 1, r)] +
            [(i, j, 'cross') for i in range(r) for j in range(r, r + s)])


def laplacian(r, s, weights):
    n = r + s
    L = np.zeros((n,n))
    for (i, j, kind), w in zip(edges(r,s),weights):
        L[i,i] += w
        L[j,j] += w
        L[i,j] -= w
        L[j,i] -= w
    return L


def Kirchhoff(L):
    n = len(L)
    return n * (np.trace(np.linalg.inv(L + np.ones((n,n)) / n)) - 1)


def predicted(r,s,B):
    a,b = optimal(r,s,B)
    n=r+s
    return n*(r-1)/(r*a+s*b) + s*(n-1)/(r*b)


def assert_close(actual, predicted, tol=2e-8):
    assert abs(actual-predicted) <= tol * (1 + abs(predicted)), (actual, predicted)


def run():
    spectral=0
    optimizer=0
    asymmetric=0
    rng=np.random.default_rng(20261024)
    for r in range(2,10):
        for s in range(1,12):
            for B in (1.0, 3.0):
                n=r+s
                a,b=optimal(r,s,B)
                ee=edges(r,s)
                weights=np.array([a if z=='clique' else b for _,_,z in ee])
                assert_close(weights.sum(),B)
                L=laplacian(r,s,weights)
                actual=np.linalg.eigvalsh(L)
                theoretical=sorted([0.0]+[r*a+s*b]*(r-1)+[r*b]*(s-1)+[n*b])
                assert np.allclose(actual,theoretical,rtol=1e-8,atol=1e-9)
                spectral+=1
                assert_close(Kirchhoff(L),predicted(r,s,B))
                for ratio in [0.0,0.025,0.1,0.2,0.5,1,2,5,10,50]:
                    bb=B/(r*s+r*(r-1)*ratio/2)
                    aa=ratio*bb
                    candidate=np.array([aa if z=='clique' else bb for _,_,z in ee])
                    assert Kirchhoff(laplacian(r,s,candidate)) >= predicted(r,s,B)-1e-7
                    optimizer+=1
                if n<=11:
                    for _ in range(12):
                        candidate=rng.gamma(1.0,1.0,len(ee))
                        candidate *= B/candidate.sum()
                        assert Kirchhoff(laplacian(r,s,candidate)) >= predicted(r,s,B)-1e-7
                        asymmetric+=1
                assert (a < 1e-12) == (s>=r+1)
    # Independently verify symbolic generalized Laplacian eigenvalue factors
    symbols=0
    a,b,z=sp.symbols('a b z')
    for r,s in [(2,1),(2,2),(2,3),(3,2),(3,4),(4,2)]:
        ee=edges(r,s)
        L=sp.zeros(r+s)
        for i,j,kind in ee:
            w=a if kind=='clique' else b
            L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
        pol=sp.factor(L.charpoly(z).as_expr())
        expected=sp.factor(z*(z-r*a-s*b)**(r-1)*(z-r*b)**(s-1)*(z-(r+s)*b))
        assert sp.expand(pol-expected)==0
        symbols+=1
    # Exact rational Kirchhoff checks at support-transition boundaries.
    rational=0
    for r,s,B in [(2,3,1),(3,4,7),(4,5,2),(2,1,5),(3,1,2)]:
        a_f,b_f=optimal(r,s,B)
        if s>=r+1:
            a=sp.Rational(0);b=sp.Rational(B,r*s)
        elif s==1:
            a=b=sp.Rational(2*B,(r+1)*r)
        else:continue
        n=r+s;L=sp.zeros(n)
        for i,j,kind in edges(r,s):
            w=a if kind=='clique' else b
            L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
        exact=n*(sp.trace((L+sp.ones(n)/n).inv())-1)
        expected=sp.Rational(n*(r-1),1)/(r*a+s*b)+sp.Rational(s*(n-1),r)/b
        assert exact==expected,(r,s,exact,expected)
        rational+=1
    print('PASS',{'spectral_and_optimal':spectral,'symmetric_objective_comparisons':optimizer,'asymmetric_budget_comparisons':asymmetric,'symbolic_factors':symbols,'exact_rational_Kirchhoff':rational})

if __name__=='__main__':run()
