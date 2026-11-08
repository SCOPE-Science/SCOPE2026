"""Exact and independent numerical checks for enclosing balls of sparse Cayley-box polytopes.

Run: python3 check.py. Requires Python's standard library; optional SciPy adds
an independent nonlinear minimax comparison.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose


def solution(d,a,b):
    a,b=F(a),F(b)
    if b<a:
        L=d*a*a+F(1,d)
        V=F(d-1,d)
        q=(L-V)/(2*L)
        c=q*a
        t=(1-q)/d
        R2=V+q*q*L
        active='all_alpha_and_zero_tops'
    else:
        L=d*(a-b/d)**2+F(1,d)
        V=F(d-1,d)*(b*b+1)
        q=max(F(0), (L-V)/(2*L))
        c=q*a+(1-q)*b/d
        t=(1-q)/d
        R2=V+q*q*L
        active=('beta_tops_only' if L<V else
                'beta_tops_and_all_alpha')
    return c,t,R2,q,active


def dist2(x,y,c,t):
    return sum((z-c)**2 for z in x)+sum((z-t)**2 for z in y)


def exact_checks():
    checked=0; vertices=0
    for d in range(3,11):
      for aa in range(1,8):
       for bb in range(1,8):
        a,b=F(aa),F(bb)
        c,t,R2,q,active=solution(d,aa,bb)
        assert 0 <= q < 1 and R2>0
        assert 0<=t<=F(1,d)
        if b<a:
            assert c>b/2
        else:
            assert c<b/2
        # All explicitly described vertices of the Cayley sum, including 2^d cube vertices.
        zero=(F(0),)*d
        for bits in product((F(0),a),repeat=d):
            z=dist2(bits,zero,c,t)
            should=(active.endswith('all_alpha') or active=='all_alpha_and_zero_tops') and all(v==a for v in bits)
            assert (z==R2)==should, (d,a,b,'cube',bits,z,R2,active)
            assert z<=R2
            checked+=1;vertices+=1
        for j in range(d):
            ej=tuple(F(1) if k==j else F(0) for k in range(d))
            x_beta=tuple(b if k==j else F(0) for k in range(d))
            zb=dist2(zero,ej,c,t)
            zc=dist2(x_beta,ej,c,t)
            if b<a:
                assert zb==R2 and zc<R2
            else:
                assert zb<R2 and zc==R2
            checked+=2;vertices+=2
        # Positive support weights with barycenter equal to the center.
        if b<a:
            wcube=q; wtop=(1-q)/d
            assert c==wcube*a and t==d*wtop/d
            assert wcube>0 and wtop>0
        else:
            wcube=q; wtop=(1-q)/d
            assert c==wcube*a + wtop*b
            assert t==wtop
            assert wcube>=0 and wtop>0
        checked+=5
        assert R2==max([dist2(bits,zero,c,t) for bits in product((F(0),a),repeat=d)]+[dist2(zero,tuple(F(1) if k==j else F(0) for k in range(d)),c,t) for j in range(d)]+[dist2(tuple(b if k==j else F(0) for k in range(d)),tuple(F(1) if k==j else F(0) for k in range(d)),c,t) for j in range(d)])
        checked+=1
    print('Exact rational checks:',checked,'vertex comparisons:',vertices)
    return checked


def independent_numeric():
    try:
        import scipy.optimize as opt
        import numpy as np
    except ImportError:
        print('SciPy not installed: optional independent optimizer skipped')
        return
    checks=0
    for d in (3,4,5,6,8,10):
      for a,b in ((1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(1,4),(3,7),(6,1),(2,5),(5,2)):
        c,t,R2,_,_=solution(d,a,b)
        def f(z):
            cc,tt=z
            return max(d*cc*cc+d*tt*tt,
                d*(a-cc)**2+d*tt*tt,
                d*cc*cc+1-2*tt+d*tt*tt,
                d*cc*cc+b*b-2*b*cc+1-2*tt+d*tt*tt)
        # Independent minimization of the four raw vertex-orbit distances.
        res=opt.minimize(lambda z:z[2],np.array([float(c),float(t),float(R2)+1]),
                constraints=[{'type':'ineq','fun':lambda z,i=i: z[2] - [d*z[0]**2+d*z[1]**2,
                d*(a-z[0])**2+d*z[1]**2,
                d*z[0]**2+1-2*z[1]+d*z[1]**2,
                d*z[0]**2+b*b-2*b*z[0]+1-2*z[1]+d*z[1]**2][i]} for i in range(4)],
                method='SLSQP', options={'ftol':1e-10,'maxiter':300})
        assert res.success and abs(res.x[2]-float(R2))<1e-5, (d,a,b,res.message,res.x,R2)
        assert abs(res.x[0]-float(c))<1e-4 and abs(res.x[1]-float(t))<1e-4, (d,a,b,res.x,c,t)
        checks+=1
    print('Independent SLSQP orbit-minimax cases:',checks)

if __name__ == '__main__':
    exact_checks()
    independent_numeric()
