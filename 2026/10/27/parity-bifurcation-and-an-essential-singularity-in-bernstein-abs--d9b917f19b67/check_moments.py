"""Independent numerical checks for Bernstein absolute-moment bifurcation.

Install mpmath if needed. Numerical checks illustrate, but do not prove,
the infinitely many degree-dependent analytic statements.
"""
from math import comb
from mpmath import mp

mp.dps = 90

def moment(n, r, p):
    return sum(comb(n,k)*p**k*(1-p)**(n-k)
               *abs(mp.mpf(k)/n-p)**r for k in range(n+1))

def derivative(n,r,delta):
    p=mp.mpf('0.5')+delta
    total=mp.mpf(0)
    for k in range(n+1):
        z=mp.mpf(k)/n-p
        w=comb(n,k)*p**k*(1-p)**(n-k)
        dw_over_w=mp.mpf(k)/p-mp.mpf(n-k)/(1-p)
        contribution=dw_over_w*abs(z)**r
        if z != 0:
            contribution -= r*mp.sign(z)*abs(z)**(r-1)
        total += w*contribution
    return total

def positive_root(n,r):
    left=mp.mpf('1e-75')
    right=mp.mpf('0.04')
    assert derivative(n,r,left)>0 and derivative(n,r,right)<0
    for _ in range(275):
        center=(left+right)/2
        if derivative(n,r,center)>0:
            left=center
        else:
            right=center
    return (left+right)/2

def main():
    for n in [2,4,6,10]:
        b=mp.mpf(comb(n,n//2))/2**n
        expected=mp.log(1+1/(n*b))
        assert abs(moment(n,2,mp.mpf('0.3'))-mp.mpf('0.21')/n)<mp.mpf('1e-65')
        for epsstr in ['0.1','0.05','0.02']:
            epsilon=mp.mpf(epsstr)
            r=2-epsilon
            d=positive_root(n,r)
            measured=epsilon*mp.log(1/d)
            gain=moment(n,r,mp.mpf('0.5')+d)-moment(n,r,mp.mpf('0.5'))
            assert gain>0 and 0<d<mp.mpf('0.04')
            print('n=',n,'epsilon=',epsstr,'displacement=',mp.nstr(d,14),
                  'scaled_log=',mp.nstr(measured,14),
                  'limit=',mp.nstr(expected,14),
                  'gain=',mp.nstr(gain,10))
        print()
    for n in [3,5,9]:
        r=mp.mpf('1.95')
        assert moment(n,r,mp.mpf('0.5'))>moment(n,r,mp.mpf('0.49'))
    print('All sample checks passed. The infinite assertions require the proof.')

if __name__=='__main__':
    main()
