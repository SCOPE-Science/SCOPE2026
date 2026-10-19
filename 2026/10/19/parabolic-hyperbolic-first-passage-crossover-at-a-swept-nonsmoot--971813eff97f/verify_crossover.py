"""Standalone numerical consistency checks for a scalar discrete border-fold law.
Only standard Python modules required. No external data or hidden artifacts.
"""
import math

def initial(a):
    n0=math.ceil(1/(1-a))
    v0=n0/(1-a)-1/(1-a)**2
    return n0, v0

def crossing_exact(eps,delta,a,L):
    n,v=initial(a)
    assert v>=-1e-10
    v=max(0.0,v)
    while eps*v < L:
        v=(1+delta)*v+n
        n+=1
        assert n < 10000000
    return n,eps*v

def H(k,t):
    if k==0: return t*t/2
    z=k*t
    return (math.expm1(z)-z)/(k*k)

def find_T(k,L):
    lo=0.; hi=1.
    while H(k,hi)<L: hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if H(k,mid)<L:lo=mid
        else: hi=mid
    return (lo+hi)/2

if __name__=='__main__':
    a=.4; L=1.
    for k in [0,.25,1.,2.,5.]:
        T=find_T(k,L)
        print('kappa=',k,'T=',T)
        for eps in [1e-3,1e-4,1e-5,1e-6,1e-7]:
            delta=k*math.sqrt(eps)
            n,x=crossing_exact(eps,delta,a,L)
            print(' ',eps,'N=',n,'sqrt(eps)*N=',n*math.sqrt(eps),'err=',n*math.sqrt(eps)-T, 'overshoot',x-L)
            assert abs(n*math.sqrt(eps)-T)<.15
    for power in [.3,.4]:
        print('hyperbolic-near-neutral: delta=eps^',power)
        for eps in [1e-5,1e-7,1e-9]:
            delta=eps**power
            n,_=crossing_exact(eps,delta,a,L)
            r=n*math.log1p(delta)-math.log(L*delta*delta/eps)
            print(' ',eps,'residual log=',r)
            assert abs(r)<.5

# Exact-rational independent checks of the branch change and the finite sum.
def exact_rational_tests():
    from fractions import Fraction as F
    for a in (F(1, 2), F(2, 5), F(2, 3), F(7, 10)):
        q = 1 - a
        n0 = (q.denominator + q.numerator - 1) // q.numerator
        v0 = F(n0, 1) / q - 1 / (q * q)
        for delta in (F(0), F(1, 5), F(3, 7)):
            b = 1 + delta
            n = -12
            v = F(n, 1) / q - 1 / (q * q)
            while n < 40:
                if n <= n0:
                    assert v == F(n, 1) / q - 1 / (q * q)
                else:
                    s = sum(F(j, 1) * b**(n-1-j) for j in range(n0, n))
                    assert v == b**(n-n0) * v0 + s
                    t = (b**n - 1 - n*delta)/(delta*delta) if delta else F(n*(n-1), 2)
                    assert t == sum(F(j, 1) * b**(n-1-j) for j in range(n))
                v = (a if v <= 0 else b)*v + n
                n += 1
    print('Exact-rational branch and closed-form checks: passed')

if __name__ == '__main__':
    exact_rational_tests()
