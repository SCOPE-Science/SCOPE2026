"""Finite checks for sharp endpoint norms of fractional path Laplacians.

Run with Python 3 and mpmath: python CHECK.py
Numerical checks are finite illustrations; proofs are in RESULT.md.
"""
import math
import mpmath as mp

mp.mp.dps = 60
COUNT = 0

def close(x,y,atol=mp.mpf('1e-36'),rtol=mp.mpf('1e-30')):
    global COUNT
    assert abs(x-y) < atol+rtol*max(abs(x),abs(y)), (x,y,abs(x-y))
    COUNT += 1

def spectral_diagonal(n, alpha, i):
    a=mp.mpf(alpha)
    return mp.fsum([(4*mp.sin(mp.pi*k/(2*n))**2)**a * (2/mp.mpf(n)) *mp.cos(mp.pi*k*(i+mp.mpf('0.5'))/n)**2 for k in range(1,n)])

def coefficient(m,a):
    a=mp.mpf(a)
    if m==0:return mp.gamma(2*a+1)/mp.gamma(a+1)**2
    return -mp.gamma(2*a+1)*mp.sin(mp.pi*a)/mp.pi *mp.gamma(m-a)/mp.gamma(m+a+1)

def spectral_entry(n,alpha,i,j):
    a=mp.mpf(alpha)
    return mp.fsum([(4*mp.sin(mp.pi*k/(2*n))**2)**a * (2/mp.mpf(n)) *mp.cos(mp.pi*k*(i+mp.mpf('0.5'))/n)*mp.cos(mp.pi*k*(j+mp.mpf('0.5'))/n) for k in range(1,n)])

def main():
    global COUNT
    for n in range(2,13):
        for alpha in ('0.17','0.5','0.83'):
            v=[spectral_diagonal(n,alpha,i) for i in range(n)]
            for i in range(n):
                close(v[i],v[n-1-i])
                if 0<i<n-1:
                    assert v[i] > v[0]
                    COUNT+=1
            for i in range(n//2):
                if i+1 <= (n-1)//2:
                    assert v[i+1]>v[i]
                    COUNT+=1
            for i in range(n):
                row=mp.fsum(spectral_entry(n,alpha,i,j) for j in range(n))
                close(row,0)
                for j in range(n):
                    if i!=j:
                        assert spectral_entry(n,alpha,i,j)<0
                        COUNT+=1
                normrow=mp.fsum(abs(spectral_entry(n,alpha,i,j)) for j in range(n))
                close(normrow,2*v[i])
            assert abs(max(v)-v[(n-1)//2])<mp.mpf('1e-50')
            COUNT+=1
    # Gamma Fourier coefficient formula: independent high-precision quadrature.
    for alpha in ('0.17','0.5','0.83'):
        for m in range(0,12):
            integral=mp.quad(lambda t:(4*mp.sin(t/2)**2)**mp.mpf(alpha)*mp.cos(m*t)/mp.pi,[0,mp.pi])
            close(integral,coefficient(m,alpha))
    # Exact odd-path formula for the square root of the path Laplacian.
    for n in range(3,32,2):
        v=spectral_diagonal(n,mp.mpf('0.5'),n//2)
        close(2*v,4/mp.mpf(n)*mp.cot(mp.pi/(2*n)))
    # First and second finite-size terms, for both parities.
    for alpha in ('0.25','0.5','0.8'):
        a=mp.mpf(alpha);s=1+2*a
        kap=mp.gamma(2*a+1)*mp.sin(mp.pi*a)/mp.pi
        b=a*(a+1)*(2*a+1)/6
        c0=coefficient(0,a)
        lead=4*kap*mp.zeta(s)
        corr_odd=4*kap*b*mp.zeta(s+2)
        corr_even=corr_odd+2*kap*s*(s+1)*(1-2**(-s-2))*mp.zeta(s+2)
        for n in (31,32,63,64,127,128):
            norm=2*spectral_diagonal(n,a,(n-1)//2)
            second=(2*c0-norm-lead*n**(-s))*n**(s+2)
            target=corr_odd if n%2 else corr_even
            assert abs(second-target)<mp.mpf('0.09')*(32/mp.mpf(n))**2
            COUNT+=1
    # Zero-order logarithmic crossover (uniform estimate at finite n).
    for lam in ('0.0','0.5','2.0'):
        for n in (100,300,1000):
            a=mp.mpf('0.3')/(mp.log(n)**2) if lam=='0.0' else mp.mpf(lam)/mp.log(n)
            c0=coefficient(0,a)
            norm=2*spectral_diagonal(n,a,(n-1)//2)
            ratio=n*(2*c0-norm)
            kap=mp.gamma(2*a+1)*mp.sin(mp.pi*a)/mp.pi
            approximation=4*kap*mp.zeta(1+2*a)*n**(-2*a)
            assert abs(ratio-approximation)<mp.mpf('0.00003')*(mp.mpf(100)/n)**2
            COUNT+=1
    print('PASS',COUNT,'finite checks')

if __name__=='__main__':main()
