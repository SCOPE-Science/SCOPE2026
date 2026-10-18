"""Standalone checks for fastest symmetric stochastic mixing on the cone of a crown graph.

Requires Python >=3.9 with sympy and numpy. Analytic proof is supplied separately.
"""
from fractions import Fraction as F
import numpy as np
import sympy as sp


def formula(m):
    a=F(1,2*m)
    b=F(2*m-1,m*(3*m-4))
    t=F(2*m-1,2*(3*m-4))
    return a,b,t


def matrix(m,a,b,rational=False):
    n=2*m+1
    zero=F(0) if rational else 0.
    p=[[zero for _ in range(n)] for _ in range(n)]
    for i in range(m):
        p[0][i+1]=p[i+1][0]=a
        p[0][i+m+1]=p[i+m+1][0]=a
        for j in range(m):
            if i!=j:
                p[i+1][j+m+1]=p[j+m+1][i+1]=b
    for i in range(n):
        p[i][i]=1-sum(p[i][j] for j in range(n) if j!=i)
    return p


def exact_tests():
    ct=0
    for m in range(4,31):
        a,b,t=formula(m)
        p=matrix(m,a,b,rational=True)
        assert all(sum(row)==1 for row in p)
        assert all(v>=0 for row in p for v in row)
        assert p[0][0]==0
        assert p[1][1]>0
        assert 1-(2*m+1)*a==-F(1,2*m)
        assert 1-a-2*(m-1)*b==-t
        assert 1-a-(m-2)*b==t
        assert 1-a-m*b==F(m-4,m)*t
        assert abs(1-(2*m+1)*a)<=t
        assert abs(1-a-m*b)<=t
        assert 2*m*a==1
        assert b>0
        assert t==F(m,3*m-4)*(1-a)
        ct+=12
    return ct


def full_spectrum_tests():
    ct=0
    for m in range(4,40):
        a,b,t=formula(m)
        eigen=np.linalg.eigvalsh(np.array(matrix(m,float(a),float(b))))
        target=sorted([1.,-1/(2*m),-float(t)]+[float(t)]*(m-1)+[float(F(m-4,m)*t)]*(m-1))
        assert len(eigen)==len(target)
        assert np.max(np.abs(eigen-np.array(target)))<2e-12,(m,eigen,target)
        assert abs(max(abs(eigen[:-1]))-float(t))<2e-12
        ct+=2
    return ct


def sympy_tests():
    ct=0
    z=sp.symbols('z')
    for m in range(4,9):
        a,b,t=formula(m)
        pp=sp.Matrix(matrix(m,sp.Rational(a.numerator,a.denominator),sp.Rational(b.numerator,b.denominator),True))
        cp=sp.factor(pp.charpoly(z).as_expr())
        pred=(z-1)*(z+sp.Rational(1,2*m))*(z+sp.Rational(t.numerator,t.denominator))*(z-sp.Rational(t.numerator,t.denominator))**(m-1)*(z-sp.Rational(m-4,m)*sp.Rational(t.numerator,t.denominator))**(m-1)
        assert sp.simplify(cp-pred)==0,(m,cp,pred)
        ct+=1
    return ct


def perturbation_tests():
    rng=np.random.default_rng(70271)
    ct=0
    for m in range(4,11):
        n=2*m+1
        a,b,t=formula(m)
        edges=[(0,i) for i in range(1,n)]+[(i+1,m+j+1) for i in range(m) for j in range(m) if i!=j]
        for _ in range(120):
            rr=rng.random(len(edges))
            deg=np.zeros(n)
            for (u,v),x in zip(edges,rr):deg[u]+=x;deg[v]+=x
            rr*=min(1.,np.min(1/deg))
            pp=np.zeros((n,n))
            for (u,v),x in zip(edges,rr): pp[u,v]=pp[v,u]=x
            np.fill_diagonal(pp,1-pp.sum(axis=1))
            eig=np.linalg.eigvalsh(pp)
            assert abs(eig[-1]-1)<2e-12
            assert max(abs(eig[:-1]))>=float(t)-3e-12
            ct+=1
    return ct


if __name__=='__main__':
    print('Exact rational identities:',exact_tests())
    print('Full-matrix spectral tests:',full_spectrum_tests())
    print('Exact symbolic characteristic-polynomial tests:',sympy_tests())
    print('Random feasible matrix comparisons:',perturbation_tests())
    print('All checks passed. Sampling is supplementary, not an infinite-family proof.')
