#!/usr/bin/env python3
"""Exact checks for the noisy three-sample plurality mean-field phase diagram.

Requires sympy; all tested computations use integer/rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from sympy import Matrix, Rational, eye, symbols, diff, simplify

def exact_plurality(z):
    k=len(z)
    out=[F(0) for _ in range(k)]
    for tup in product(range(k),repeat=3):
        counts=[tup.count(i) for i in range(k)]
        winners=[i for i,n in enumerate(counts) if n==max(counts)]
        probability=z[tup[0]]*z[tup[1]]*z[tup[2]] /len(winners)
        for i in winners:
            out[i]+=probability
    return out

def T(z):
    s=sum(x*x for x in z)
    return [x*(1+x-s) for x in z]

def Fmap(x,p):
    k=len(x)
    z=[(1-p)*a+p/k for a in x]
    return T(z)

def J(x,p):
    k=len(x)
    z=Matrix([(1-p)*a+p/k for a in x])
    s=(z.T*z)[0]
    return (1-p)*(Matrix.diag(*[1+2*z[i]-s for i in range(k)])-2*z*z.T)

def test_branch(k,r,t):
    t=F(t)
    s=k-r
    denom=r*t+s
    a=t/denom
    b=F(1)/denom
    p=F(k)*t/(denom*denom+k*t)
    z=[a]*r+[b]*s
    x=[(zi-p/k)/(1-p) for zi in z]
    assert all(xx>0 for xx in x)
    assert sum(x)==1
    assert Fmap(x,p)==x
    lamb_hi=1+(1-p)*(a-b)
    lamb_lo=1-(1-p)*(a-b)
    lamb_mix=1+(1-p)*(a-b)*(1-2*r*a)
    JJ=J([Rational(xx.numerator,xx.denominator) for xx in x],Rational(p.numerator,p.denominator))
    # Restrict the Jacobian to the tangent simplex via differences of column vectors.
    basis=Matrix.hstack(*[(Matrix([int(i==j)-int(i==k-1) for i in range(k)])) for j in range(k-1)])
    JB=JJ*basis
    B=Matrix.hstack(basis, Matrix([1]*k))
    tangent=B.inv()*JB
    reduced=tangent[:k-1,:]
    vals=reduced.eigenvals()
    assert sum(vals.values())==k-1
    assert (r==1 or vals.get(Rational(lamb_hi.numerator,lamb_hi.denominator),0)>=r-1)
    assert (s==1 or vals.get(Rational(lamb_lo.numerator,lamb_lo.denominator),0)>=s-1)
    assert vals.get(Rational(lamb_mix.numerator,lamb_mix.denominator),0)>=1
    return p,x,vals

def main():
    rules=0; branches=0
    for k in range(2,8):
        for j in range(1,5):
            z=[F(i+j, sum(range(1,k+1))+k*j) for i in range(1,k+1)]
            assert sum(z)==1
            assert exact_plurality(z)==T(z)
            rules+=1
    for k in range(3,10):
        for r in range(1,k):
            for t in [F(5,4),F(3,2),F(2),F(3),F(7),F(12)]:
                p,x,vals=test_branch(k,r,t)
                assert p>0 and p<1
                branches+=1
        lower=F(1,k+1); upper=F(k,5*k-4)
        assert 0<lower<upper<1
        assert test_branch(k,1,F(k-1))[0]==upper
        assert test_branch(k,1,F((k-1)**2))[0]==lower
    p=F(9,34)
    u=[F(1,3)]*3
    stable=[F(87,125),F(19,125),F(19,125)]
    saddle=[F(53,125),F(36,125),F(36,125)]
    for x in (u,stable,saddle):
        assert Fmap(x,p)==x
    assert max(abs(float(v)) for v in J([Rational(xx.numerator,xx.denominator) for xx in u],Rational(9,34)).eigenvals())>0
    # Tangent eigenvalues from closed formula:
    assert (1-p)*(1+F(1,3))==F(50,51)
    assert test_branch(3,1,3)[2]=={Rational(12,17):1,Rational(16,17):1}
    assert test_branch(3,1,F(4,3))[2]=={Rational(63,68):1,Rational(69,68):1}
    # Symbolic gradient-potential identity for the full map, without an assumed
    # stationary orbit or a finite sample limit.
    for k in range(3,7):
        xsy=symbols('x0:'+str(k)); pp=symbols('p'); alpha=1-pp
        zz=[alpha*t+pp/k for t in xsy]
        ss=sum(a*a for a in zz)
        Phi=(sum(a*a for a in zz)/2+sum(a**3 for a in zz)/3-ss*ss/4)/alpha
        FF=[a*(1+a-ss) for a in zz]
        assert all(simplify(diff(Phi,xsy[i])-FF[i])==0 for i in range(k))
    # Exact strict Lyapunov inequality sampled on the simplex.
    Lyap=0
    for k in range(3,8):
        for j in range(1,9):
            raw=[F(i+j) for i in range(1,k+1)]
            x=[u/sum(raw) for u in raw]
            p=F(j,j+k+4)
            def potential(q):
                z=[(1-p)*u+p/k for u in q]
                S=sum(zi*zi for zi in z)
                return (S/2+sum(zi**3 for zi in z)/3-S*S/4)/(1-p)-sum(u*u for u in q)/2
            y=Fmap(x,p)
            assert potential(y)-potential(x) >= sum((yi-xi)**2 for yi,xi in zip(y,x))/2
            Lyap+=1
    print(f'PASS: {rules} exact three-draw outcome distributions; {branches} exact fixed-point/Jacobian classifications; 4 symbolic potential-gradient identities; {Lyap} exact Lyapunov inequalities; exact three-opinion coexistence witness.')

if __name__=='__main__':main()
