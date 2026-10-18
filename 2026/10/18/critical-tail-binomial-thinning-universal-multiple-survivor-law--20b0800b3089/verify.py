"""Reproduce finite thinning identities and the critical-index conditional law.
Scientific reference implementation; requires mpmath >= 1.2.
Run: python verify.py
"""
import math
import mpmath as mp
mp.mp.dps = 55


def rare_tail(a):
    return a*(1-a+a*mp.log(a))/(1-a)**2


def mass_two(a):
    return a*(1-a*a+2*a*mp.log(a))/(2*(1-a)**3)


def mass_integral(a, j):
    return a*mp.quad(lambda v: v**(j-1)*(1-v)/(a+(1-a)*v), [0, .5, 1])


def mass_direct(a, j, ceiling=2500):
    s = mp.mpf(0)
    for x in range(j, ceiling+1):
        s += mp.binomial(x,j)*a**j*(1-a)**(x-j)/(x*(x+1))
    return s


def exact_tv(a):
    return a*((1+a)*mp.log(1/a)-2*(1-a))/(2*(1-a)*(1-a+a*mp.log(a)))

checks=0
for d in (2,3,4,5,7,10,16):
    a = mp.mpf(1)/d
    D = rare_tail(a)
    assert D > 0
    assert mp.almosteq(D, a*mp.quad(lambda v:v/(a+(1-a)*v), [0,.5,1]), rel_eps=mp.mpf('1e-43'))
    checks += 1
    for j in range(2,9):
        integral = mass_integral(a,j)
        direct = mass_direct(a,j)
        assert abs(integral-direct)<mp.mpf('2e-32'), (d,j,integral,direct)
        checks += 1
    p2 = mass_integral(a,2)
    assert abs(p2-mass_two(a))<mp.mpf('1e-40')
    tv = mp.mpf('0.5')-p2/D
    assert abs(tv-exact_tv(a))<mp.mpf('1e-40')
    assert tv>0
    # Strict positive in all dimensions beyond j=2; numerical evidence only.
    assert mass_integral(a,3)/D > mp.mpf(1)/6
    for j in range(2,7):
        current=mass_integral(a,j)/D*j*(j-1)
        next_=mass_integral(a,j+1)/D*(j+1)*j
        assert next_>current
        checks += 1
    checks+=3
for denom in (10**3,10**4,10**5,10**6,10**8):
    a=mp.mpf(1)/denom
    ratio=exact_tv(a)/(a*mp.log(1/a))
    assert abs(ratio-mp.mpf('.5'))<mp.mpf(3)/mp.log(1/a)
    checks+=1
# Binomial-thinning tail identities for arbitrary finite positive-support pmfs.
for pmf in ([mp.mpf(1)/6,mp.mpf(1)/3,mp.mpf(1)/2], [mp.mpf(1)/4]*4):
    for a in (mp.mpf('0.2'),mp.mpf('0.6')):
        mass=[mp.fsum(p*mp.binomial(k+1,j)*a**j*(1-a)**(k+1-j) for k,p in enumerate(pmf) if k+1>=j) for j in range(len(pmf)+1)]
        tail=[mp.fsum(pmf[k-1:] ) for k in range(1,len(pmf)+1)]
        A=mp.fsum(tail[k-1]*(1-a)**(k-1) for k in range(1,len(pmf)+1))
        A_prime=mp.fsum((k-1)*tail[k-1]*(1-a)**(k-2) for k in range(2,len(pmf)+1))
        assert abs(mp.fsum(mass[1:])-a*A)<mp.mpf('1e-48')
        assert abs(mp.fsum(mass[2:])-a*a*A_prime)<mp.mpf('1e-48')
        checks+=2
print('PASS:',checks,'independent finite/analytic formula checks')
print('alpha=1e-6 sharp TV ratio',mp.nstr(exact_tv(mp.mpf('0.000001'))/(mp.mpf('0.000001')*mp.log(10**6)),12))
print('Limit and all-alpha statements require the accompanying analytic proof.')
