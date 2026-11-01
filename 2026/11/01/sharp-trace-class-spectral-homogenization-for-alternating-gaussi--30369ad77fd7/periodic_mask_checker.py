"""Numerical arithmetic consistency checks for the alternating-annulus Fock trace theorem.
Scientific proof is analytical; finite evaluations here are corroborative only.
"""
import mpmath as mp
mp.mp.dps=65
pi=mp.pi
F=lambda z: 1/((1-z)*(1+mp.exp(z-1)))
q=1/(1-1j*pi)
assert abs(abs(q)-1/mp.sqrt(1+pi*pi))<mp.mpf('1e-60')
count=0
coeffs=mp.taylor(F,0,80)
for n in range(25):
    lam=coeffs[n]
    # Independent real-integral evaluation by summing ring contributions.
    direct=mp.fsum((mp.gammainc(n+1,2*j,2*j+1)/mp.factorial(n) for j in range(100)))
    assert abs(lam-direct)<mp.mpf('1e-48'),(n,lam,direct)
    count+=1
    fourier=mp.mpf('0.5')+(2/pi)*mp.fsum(mp.im((1-1j*pi*k)**(-n-1))/k for k in range(1,200,2))
    assert abs(lam-fourier)<(mp.mpf('2')/(pi**(n+2)*(n+1))*mp.mpf('198')**(-n-1)+mp.mpf('1e-58')), (n,lam,fourier)
    count+=1
    if n>=8:
       lead=(2/pi)*mp.im(q**(n+1))
       error=abs((lam-mp.mpf('0.5'))-lead)
       assert error<mp.mpf('2')*((1+9*pi*pi)**(-mp.mpf(n+1)/2)),(n,error)
       count+=1
assert abs(mp.fsum(coeffs[n]-mp.mpf('0.5') for n in range(81))-mp.mpf('0.25'))<mp.mpf('1e-35')
count+=1
for z in (mp.mpf('.5'),mp.mpf('.83'),mp.mpf('.93')):
    lhs=F(z)-mp.mpf('0.5')/(1-z)
    sumval=mp.fsum((coeffs[n]-mp.mpf('0.5'))*z**n for n in range(31))
    assert abs(lhs-sumval)<mp.mpf('2e-15')
    count+=1
print('PASS',count,'checks')
print('lambda_0',mp.nstr(F(0),20))
print('rho',mp.nstr(abs(q),20),'theta',mp.nstr(mp.arg(q),20))
print('trace',mp.nstr(mp.mpf('.25'),20))
