"""Exact symbolic checks for finite-population Hoeffding factors."""
import sympy as s
from fractions import Fraction
from math import comb

def run():
    u=s.symbols('u',positive=True)
    D=u**2+6*u+3
    V=6*u*(u*u+2*u+3)/D**2
    assert s.simplify(s.diff(V,u)+6*(u*u-3)*(u*u-2*u+3)/D**3)==0
    assert s.simplify(V.subs(u,s.sqrt(3))-(s.sqrt(3)-1)/2)==0
    assert s.Rational(1210,405)<3
    assert s.Rational(26,15)**2>3
    assert s.Rational(11,27)>s.log(s.Rational(3,2))
    # N=6, (m,k)=(2,2)
    D=u**2+8*u+6
    assert s.expand(2*D**2-40*u*(u*u+3*u+6)-2*(u*u-2*u+6)**2)==0
    # N=6, (m,k)=(2,3)
    D=u**2+3*u+1
    assert s.expand(2*D**2-5*u*(3+4*u+3*u*u)-(u-1)**2*(2*u*u+u+2))==0
    # N=6, (m,k)=(3,3)
    D=(u+1)*(u*u+8*u+1)
    V=9*u*(u**4+4*u**3+10*u*u+4*u+1)/D**2
    assert s.simplify(s.Rational(9,20)-V-9*(u-1)**2*(u**4+18*u*u+1)/(20*D**2))==0
    # Hamming-slice probabilities and variance checks for each n <= 6.
    for n in range(2,7):
      for k in range(1,n):
       for m in range(1,n):
        ps=[s.Rational(comb(k,j)*comb(n-k,m-j),comb(n,m))
          if 0<=j<=k and 0<=m-j<=n-k else s.S.Zero
          for j in range(min(k,m)+1)]
        assert sum(ps)==1
        mean=sum(j*p for j,p in enumerate(ps))
        var=sum((j-mean)**2*p for j,p in enumerate(ps))
        assert s.simplify(mean-s.Rational(k*m,n))==0
        assert s.simplify(var-s.Rational(k*m*(n-k)*(n-m),n*n*(n-1)))==0
    # The exact unoptimized finite-sample constants and comparisons.
    L=s.log(s.Rational(3,2))
    c={3:1/s.log(2),4:s.Rational(4,3),5:1/(2*L),6:s.Rational(6,5)}
    # Analytic inequalities used to compare Bernoulli cases.
    assert s.Rational(27,8)<4
    assert s.Rational(2,3)<s.log(2)<s.Rational(3,4)
    assert float(c[3])<1.5 and float(c[4])<13/9
    assert float(c[5])<1.3 and float(c[6])<6*(1/9+1/16+1/25)
    print('PASS: polynomial identities, exact hypergeometric moments (N=2..6), and analytic bounds')

if __name__=='__main__':run()
