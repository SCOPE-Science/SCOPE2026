"""Deterministic checks for golden-ratio linearized Steiner spectral estimates.

Scientific diagnostics supplement the analytic proof; no finite test proves the limiting theorem.
"""
import math
import mpmath as mp
mp.mp.dps = 90
phi=(1+mp.sqrt(5))/2
beta=1/phi

def fibs(limit):
    a,b=1,2
    while a<=limit:
        yield a
        a,b=b,a+b

def exact_at_N(N,sigma):
    # Continuous Fourier frequency infimum evaluated at resonant Fibonacci modes.
    ss=mp.mpf(sigma)
    q=2
    k=3
    best=mp.inf
    winner=None
    while q < 10*N**(1/3)+1000:
        loss=ss*q-(N-1)*mp.log(abs(mp.cos(mp.pi*mp.power(phi,-k))))
        if loss<best:
            best=loss;winner=(k,q)
        k+=1
        a=mp.fib(k)
        q=int(a)
    return best,winner

def H(sigma,s):
    a=mp.mpf(sigma)/mp.sqrt(5)
    b=mp.pi**2/2
    return min(a*phi**(j-mp.mpf(s))+b*phi**(-2*(j-mp.mpf(s))) for j in range(-8,9))

checks=0
for k in range(3,25):
    q=int(mp.fib(k))
    error=abs(q*beta-int(mp.fib(k-1)))
    assert mp.almosteq(error, phi**(-k),rel_eps=mp.mpf("1e-65"))
    checks+=1
# Confirm minimal distance to integers for all integers below next denominator.
for k in range(3,16):
    q=int(mp.fib(k)); qnext=int(mp.fib(k+1))
    target=abs(q*beta-mp.nint(q*beta))
    assert all(abs(m*beta-mp.nint(m*beta))>target-mp.mpf('1e-70') for m in range(q+1,qnext))
    checks+=1
# Exact spectral optimizer on a finite range of Fourier modes.
for N in (2,3,5,10,100,1000,100000):
    for sigma in ('0.1','0.7','1.0','2.5'):
        fibloss,which=exact_at_N(N,sigma)
        brute=min(mp.mpf(sigma)*m-(N-1)*mp.log(abs(mp.cos(mp.pi*m*beta))) for m in range(2,701))
        assert mp.almosteq(fibloss,brute,rel_eps=mp.mpf('1e-65'))
        checks+=1
# Periodic envelope constants and fluctuations.
for sigma in ('0.2','1','3'):
    a=mp.mpf(sigma)/mp.sqrt(5);b=mp.pi**2/2
    low=3*mp.power(a*a*b/4,mp.mpf(1)/3)
    high=2*mp.power(a*a*b,mp.mpf(1)/3)
    vals=[H(sigma,mp.mpf(j)/1000) for j in range(1000)]
    assert min(vals)>=low-mp.mpf('1e-60')
    assert max(vals)<=high+mp.mpf('1e-60')
    assert abs(min(vals)-low)<mp.mpf('0.00002')
    assert abs(max(vals)-high)<mp.mpf('0.005')
    checks+=4
print('PASSED',checks,'diagnostic checks')
print('Low/high for sigma=1:',mp.nstr(3*mp.power((1/mp.sqrt(5))**2*(mp.pi**2/2)/4,mp.mpf(1)/3),22),mp.nstr(2*mp.power((1/mp.sqrt(5))**2*(mp.pi**2/2),mp.mpf(1)/3),22))
for s in ('0','0.25','0.5','0.75'):
    for j in (8,12,16):
        N=max(2,int(mp.nint(phi**(3*(j+mp.mpf(s))))))
        v,who=exact_at_N(N,1)
        print('phase',s,'index',j,'N',N,'scaled',mp.nstr(v/(mp.mpf(N-1)**(mp.mpf(1)/3)),16),'predicted',mp.nstr(H(1,s),16),'mode',who)
