"""Exact checks for the stated random OU batch recursion; Python 3 and SymPy."""
import itertools
import math
import sympy as sp

z = sp.symbols('z', positive=True)
k = sp.symbols('k', integer=True, positive=True)
c = (k - 1) / (2*k)
d_s = (k*k-1)/(12*k*k)
d_b = (k-1)**2*(2*k-1)/(6*k**3)
t = (k-1)*(k-2)/(3*k*k)
a = 1-z+c*z*z
m_s=sp.expand(a*a+d_s*z**4)
m_b=sp.expand(a*a+d_b*z**4)
n_s=sp.expand(2*z*(1-2*c*z+c*z*z))
n_b=sp.expand(n_s+2*z**3*t)
check=lambda expr: (sp.simplify(expr)==0) or (_ for _ in ()).throw(AssertionError(str(expr)))
checks=0
check(m_b-m_s-sp.factor((k-1)*(k-2)*(3*k-1)*z**4/(12*k**3)));checks+=1
check(n_b-n_s-2*z**3*t);checks+=1
check(sp.factor(1-m_s)/z-(2-(1+2*c)*z+2*c*z*z-(c*c+d_s)*z**3));checks+=1
check(sp.factor(1-m_b)/z-(2-(1+2*c)*z+2*c*z*z-(c*c+d_b)*z**3));checks+=1
check(sp.expand(n_s-(1-m_s))-(1-2*c)*z*z-(c*c+d_s)*z**4);checks+=1
for K in range(2,8):
    C=sp.Rational(K-1,2*K)
    # Exact enumeration: both alternatives' multiplier and Gaussian-noise coefficients.
    for kind in ('single','bernoulli'):
        choices=[tuple(int(i==v) for i in range(K)) for v in range(K)] if kind=='single' else list(itertools.product((0,1),repeat=K))
        wt=lambda vec:(sp.Rational(1,K) if kind=='single' else sp.Rational(1,K)**sum(vec)*(1-sp.Rational(1,K))**(K-sum(vec)))
        MM=0;NN=0;MMEAN=0
        for vec in choices:
            w=wt(vec)
            alpha=1-z+z*z*sum(i*vec[i] for i in range(K))/K
            # predictor at i uses Z_0,...,Z_{i-1}; thus noise j has corrections with i>j.
            noise=sp.Rational(2, K)*z*sum((1-z*sum(vec[i] for i in range(j+1,K)))**2 for j in range(K))
            MM+=w*alpha*alpha;NN+=w*noise;MMEAN+=w*alpha
        check(sp.expand(MMEAN-(1-z+C*z*z)));checks+=1
        check(sp.expand(MM-(m_s if kind=='single' else m_b).subs(k,K)));checks+=1
        check(sp.expand(NN-(n_s if kind=='single' else n_b).subs(k,K)));checks+=1
        # Ensure a unique positive zero by derivative bound; 0<Q(0), Q(infty)<0.
        dc=d_s.subs(k,K) if kind=='single' else d_b.subs(k,K)
        cc=c.subs(k,K)
        bound=sp.factor(sp.Rational(1,3)-2*cc)
        assert bound<0
        checks+=1
        # numerical bracketing verifies convenient illustrative values only.
        Q=2-(1+2*cc)*z+2*cc*z*z-(cc*cc+dc)*z**3
        assert Q.subs(z,sp.Rational(1,100))>0 and Q.subs(z,10)<0
        checks+=1
print('verified',checks,'exact symbolic/enumerative assertions')
