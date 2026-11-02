"""Reproduce spectral and independent numerical checks for two-population Kaczmarz E-design.
Requirements: Python 3, numpy, scipy, sympy. No network or external files.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
from scipy.optimize import minimize_scalar
import sympy as sp


def optimum(p,q,c,d):
    assert isinstance(p,int) and isinstance(q,int) and 2<=p<q
    s=1-c; a=c+s/p; b=c+s/q
    assert 0<=c<1 and 0<=d<sqrt(a*b)
    threshold=(-s+sqrt(s*s+4*q*q*a*c))/(2*q)
    if d<=c:
        t=p/(p+q); branch='uniform'
    elif d<threshold:
        R=c*s/(p*(c*a-d*d))
        t=p*R/(p*R+q); branch='contrast-coupled'
    else:
        t=(b+d)/(a+b+2*d); branch='coupled'
    return branch,t,t/p,(1-t)/q,threshold


def gram(p,q,c,d):
    n=p+q
    G=np.full((n,n),d,float)
    G[:p,:p]=c; G[p:,p:]=c
    np.fill_diagonal(G,1.0)
    return G


def direct_min(G,probs):
    w=np.sqrt(np.asarray(probs,dtype=float))
    return np.linalg.eigvalsh((w[:,None]*G)*w[None,:])[0]


def exact_values():
    p,q=2,5
    c=sp.Rational(3,10)
    a=c+(1-c)/p; b=c+(1-c)/q; s=1-c
    threshold=(-s+sp.sqrt(s*s+4*q*q*a*c))/(2*q)
    assert threshold == (sp.sqrt(1999)-7)/100
    checks=0
    expected=[
        (sp.Rational(1,4),'uniform',sp.Rational(2,7),sp.Rational(1,10)),
        (sp.Rational(1,3),'contrast-coupled',sp.Rational(378,1133),sp.Rational(1057,11330)),
        (sp.Rational(2,5),'coupled',sp.Rational(4,9),sp.Rational(1,15)),
        (sp.Rational(1,2),'coupled',sp.Rational(94,209),sp.Rational(18,1045))]
    for d,branch,t,mu in expected:
        if d<=c:
            tcalc=sp.Rational(p,p+q);name='uniform'
        elif d<threshold:
            R=c*s/(p*(c*a-d*d));tcalc=sp.cancel(p*R/(p*R+q));name='contrast-coupled'
        else:
            tcalc=sp.cancel((b+d)/(a+b+2*d));name='coupled'
        assert name==branch and sp.cancel(tcalc-t)==0
        alpha=t/p; beta=(1-t)/q
        G=sp.Matrix([[1 if i==j else (c if (i<p)==(j<p) else d) for j in range(p+q)] for i in range(p+q)])
        X=sp.diag(*([alpha]*p+[beta]*q));z=sp.symbols('z')
        char=sp.factor((X*G).charpoly(z).as_expr())
        A=1+(p-1)*c;B=1+(q-1)*c
        coupled=(z*z-(A*alpha+B*beta)*z+(A*B-p*q*d*d)*alpha*beta)
        factors=sp.factor((z-s*alpha)**(p-1)*(z-s*beta)**(q-1)*coupled)
        assert sp.expand(char-factors)==0
        assert abs(direct_min(np.array(G.tolist(),float),[float(alpha)]*p+[float(beta)]*q)-float(mu))<1e-12
        checks+=1
    print('Exact rational full Gram characteristic-polynomial and optimizer cases:',checks)


def numerical_grid():
    rng=np.random.default_rng(20261025)
    ncases=0;n_random=0; min_adv=1e100
    for p in range(2,7):
      for q in range(p+1,p+5):
       for c in [0.0,.03,.2,.5,.83]:
        s=1-c;a=c+s/p;b=c+s/q
        bound=sqrt(a*b)
        for d in sorted(set([0.0, c/2, c, (c+bound)/2, .94*bound,.999*bound])):
         if d>=bound:continue
         br,t,alpha,beta,thr=optimum(p,q,c,d)
         G=gram(p,q,c,d)
         val=direct_min(G,[alpha]*p+[beta]*q)
         coupled=np.linalg.eigvalsh(np.array([[a*t,d*np.sqrt(t*(1-t))],[d*np.sqrt(t*(1-t)),b*(1-t)]]))[0]
         block_formula=min(s*alpha,s*beta,coupled)
         assert abs(val-block_formula)<3e-12
         f=lambda x: direct_min(G,[x/p]*p+[(1-x)/q]*q)
         op=minimize_scalar(lambda x:-f(x),bounds=(1e-9,1-1e-9),method='bounded',options={'xatol':1e-13})
         assert val+1e-8>=-op.fun, (p,q,c,d,br,val,-op.fun)
         assert abs(t-op.x)<4e-4, (p,q,c,d,br,t,op.x)
         if d<=c: assert br=='uniform'
         if c<d<thr: assert br=='contrast-coupled'
         if d>=thr and d>c: assert br=='coupled'
         for _ in range(24):
          w=rng.dirichlet(np.ones(p+q))
          alt=direct_min(G,w)
          min_adv=min(min_adv,val-alt)
          assert alt<=val+3e-11,(p,q,c,d,alt,val)
          n_random+=1
         ncases+=1
    print('Full-parameter grid and independent scalar-optimization checks:',ncases)
    print('Independent asymmetric probability comparisons:',n_random)
    print('Minimum optimum-minus-random margin (non-strict numerically):',format(min_adv,'.10g'))


def symbolic_certificate():
 a,b,d,t=sp.symbols('a b d t',positive=True)
 k=a*b-d*d;den=a+b+2*d;L=k/den;tc=(b+d)/den
 expression=k*t*(1-t)-L*(b+(a-b)*t)+L*L+k*(t-tc)**2
 assert sp.factor(expression)==0
 print('Symbolic coupled-block maximin determinant certificate: exact zero residual')

if __name__=='__main__':
 symbolic_certificate()
 exact_values()
 numerical_grid()
 print('All checks passed.')
