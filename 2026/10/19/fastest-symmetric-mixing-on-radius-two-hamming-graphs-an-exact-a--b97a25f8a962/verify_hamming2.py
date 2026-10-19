"""Reproducible exact-spectrum checks for radius-two Hamming fastest mixing.

Run: python verify_hamming2.py
Dependencies for optional independent optimization: numpy, scipy.
The exact checks use Python's standard-library Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

checks=0

def check(condition, message):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(message)


def optimal(q,d):
    if q<2 or d<2:
        raise ValueError('q and d must be at least two')
    u=q-1
    if d==2:
        return F(2*u,q*q),F(u*u,q*q),F(1,q*q),F(0)
    if d==3 and q<=4:
        return F(6*u*(4-q),7*q*q),F(12*u*u,7*q*q),F(q*q-6*q+12,7*q*q),F(1,7)
    if q==2:
        return F(2,d+1),F(d-1,d+1),F(0),F(d-3,d+1)
    return F(0),F(1),F(0),F(1)-F(2*q,d*u)


def eigen(q,d,k,a,b,h):
    u=q-1
    f1=F(1)-F(q*k,u*d)
    f2=F(1)-F(2*q*k,u*d)+F(q*q*k*(k-1),u*u*d*(d-1))
    return h+a*f1+b*f2


def exact_tests():
    for d in range(2,37):
        for q in range(2,33):
            a,b,h,mu=optimal(q,d)
            check(a>=0 and b>=0 and h>=0 and a+b+h==1,(q,d,'stochastic'))
            check(eigen(q,d,0,a,b,h)==1,(q,d,'constant'))
            vals=[eigen(q,d,k,a,b,h) for k in range(1,d+1)]
            check(max(map(abs,vals))==mu,(q,d,'exact SLEM',vals,mu))
            if d>=4:
                baseline=F(d-1,d+1) if q==2 else F(1)-F(q,d*(q-1))
                check(F(1)-mu==2*(F(1)-baseline),(q,d,'factor-two gap'))
            if d==3 and q<=4:
                check(vals==[F(1,7),F(-1,7),F(1,7)],(q,d,'three contacts'))
    print('Exact rational formula and boundary tests passed.')


def independent_lp_tests():
    try:
        from scipy.optimize import linprog
        import numpy as np
    except ImportError:
        print('Optional SciPy/Numpy LP tests skipped (packages not installed).')
        return
    for d in range(2,22):
        for q in list(range(2,19))+[20,25,50,100]:
            u=q-1
            k=np.arange(1,d+1,dtype=float)
            f1=1-q*k/(u*d)
            f2=1-2*q*k/(u*d)+q*q*k*(k-1)/(u*u*d*(d-1))
            A=np.r_[np.c_[-(1-f1),-(1-f2),-np.ones(d)],np.c_[1-f1,1-f2,-np.ones(d)],[[1,1,0]]]
            B=np.r_[-np.ones(d),np.ones(d),1]
            res=linprog([0,0,1],A_ub=A,b_ub=B,bounds=[(0,None)]*3,method='highs')
            check(res.success,(q,d,'LP failed'))
            a,b,h,mu=optimal(q,d)
            check(abs(res.fun-float(mu))<2e-9,(q,d,'LP value',res.fun,mu))
    print('Independent three-variable LP checks passed.')
    for d in range(2,6):
        for q in range(2,8):
            if q**d>512:continue
            states=list(product(range(q),repeat=d));size=len(states)
            a,b,h,mu=optimal(q,d)
            p=np.zeros((size,size))
            for i,x in enumerate(states):
                for j,y in enumerate(states):
                    dist=sum(x[t]!=y[t] for t in range(d))
                    if dist==0:p[i,j]=float(h)
                    elif dist==1:p[i,j]=float(a/F(d*(q-1)))
                    elif dist==2:p[i,j]=float(b/F(comb(d,2)*(q-1)**2))
            check(np.max(abs(p.sum(axis=1)-1))<3e-14,(q,d,'row sums'))
            ev=np.linalg.eigvalsh(p)
            check(abs(ev[-1]-1)<1e-10,(q,d,'Perron'))
            check(abs(max(abs(ev[0]),abs(ev[-2]))-float(mu))<2e-10,(q,d,'matrix eigenspectrum'))
    print('Full transition-matrix spectral checks passed.')

if __name__=='__main__':
    exact_tests()
    independent_lp_tests()
    print(f'PASS: {checks} assertions')
