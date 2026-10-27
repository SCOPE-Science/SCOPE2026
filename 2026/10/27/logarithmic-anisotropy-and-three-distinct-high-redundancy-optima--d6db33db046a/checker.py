#!/usr/bin/env python3
"""Numerical checks for explicit normalized exponential-Gabor frame-bound formulas.
Requires mpmath. These checks are corroboration, not a proof of global optimality.
"""
import mpmath as mp
mp.mp.dps = 90

def quantities(n, eta):
    n, eta = mp.mpf(n), mp.mpf(eta)
    u = eta/n
    aa = mp.tanh(eta/2)*(u/mp.sinh(u) - eta/mp.sinh(eta))
    bb = mp.coth(eta/2)*(u*mp.coth(u) + eta/mp.sinh(eta))
    return aa, bb, bb/aa

def optimum(n, mode):
    n=mp.mpf(n)
    key={'A':0,'B':1,'K':2}[mode]
    c={'A':6,'B':3,'K':4}[mode]
    estimate=2*mp.log(n)+mp.log(c)
    return mp.findroot(lambda x: mp.diff(lambda y: quantities(n,y)[key],x),
                       (estimate-mp.mpf('.15'),estimate+mp.mpf('.15')))

def check():
    count=0
    for n in (20,50,100,1000,10000,100000):
        n=mp.mpf(n); L=2*mp.log(n)
        roots={key:optimum(n,key) for key in ('A','B','K')}
        assert roots['B']<roots['K']<roots['A']; count+=1
        for key,c in [('A',3),('K',4),('B',6)]:
            root=roots[key]
            q=quantities(n,root)
            assert q[0]>0 and q[1]>q[0]
            count+=1
        for key,c in [('A',6),('B',3),('K',4)]:
            err=abs(roots[key]-(L+mp.log(c)))
            assert err < 7*(L**3)/(n*n)
            count+=1
        etaK=roots['K']; exact=quantities(n,etaK)[2]
        uK=L+mp.log(4)
        pred=1+(uK**2/2+uK+1)/n**2
        assert abs(exact-pred) < 20*L**4/n**4
        count+=1
        a=quantities(n,roots['A'])[0]
        uA=L+mp.log(6)
        predA=1-(uA**2/6+(uA+1)/3)/n**2
        assert abs(a-predA) < 20*L**4/n**4
        count+=1
        b=quantities(n,roots['B'])[1]
        uB=L+mp.log(3)
        predB=1+(uB**2/3+mp.mpf(2)/3*(uB+1))/n**2
        assert abs(b-predB) < 20*L**4/n**4
        count+=1
        sq=quantities(n,mp.sqrt(n))[2]
        assert sq>exact
        count+=1
    # Verify critical rescaled landscape against the limiting c profiles.
    n=mp.mpf(10**30); L=2*mp.log(n)
    base=quantities(n,L)
    for c in (-mp.mpf('2'),-mp.mpf('1'),mp.mpf(0),mp.mpf(1),mp.mpf(2),mp.mpf(3)):
        q=quantities(n,L+c)
        profile=((2-c/3-2*mp.exp(-c)),
                 (mp.mpf(2)*c/3+2*mp.exp(-c)-2),
                 (c+4*mp.exp(-c)-4))
        for k in range(3):
            val=(n*n/L)*(q[k]-base[k]); assert abs(val-profile[k])<mp.mpf('.3')
            count+=1
    # Exact reconstruction of the condition quotient from normalized bounds.
    n=mp.mpf(13); eta=mp.mpf('3.45'); aa,bb,kap=quantities(n,eta)
    x=eta/n
    alt=mp.coth(eta/2)**2 * (x*mp.coth(x)+eta/mp.sinh(eta))/(x/mp.sinh(x)-eta/mp.sinh(eta))
    assert mp.almosteq(kap,alt);count+=1
    print('PASS', count, 'numerical assertions; finite evidence only')

if __name__=='__main__': check()
