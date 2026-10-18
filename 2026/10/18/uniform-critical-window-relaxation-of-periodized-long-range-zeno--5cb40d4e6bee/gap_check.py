"""Numerical checks for a periodized power-law lattice jump generator.

Requires Python 3 and mpmath. Run: python gap_check.py
"""
from mpmath import mp

mp.dps = 36

def dispersion(n, m, p, kappa=1):
    theta = 2*mp.pi*m/n
    return 2*kappa*(mp.zeta(p) - mp.re(mp.polylog(p, mp.exp(1j*theta))))

def direct_matrix_gap(n, p, kappa=1):
    weights = [mp.mpf(0)]
    for r in range(1,n):
        weights.append(kappa*n**(-p)*(mp.zeta(p,mp.mpf(r)/n) + mp.zeta(p,1-mp.mpf(r)/n)))
    gen = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            gen[i,j] = weights[(j-i)%n]
        gen[i,i] = -sum(weights)
    # Matrix is real symmetric; verify Fourier eigenvectors rather than numerical diagonalization.
    for m in range(n):
        vec = mp.matrix([mp.exp(2j*mp.pi*m*j/n) for j in range(n)])
        lam = dispersion(n,m,p,kappa)
        resid = max(abs(t) for t in (gen*vec + lam*vec))
        assert resid < mp.mpf('3e-27'), (n,p,m,resid)
    lam = [dispersion(n,m,p,kappa) for m in range(1,n)]
    assert min(lam) >= lam[0] - mp.mpf('2e-28')
    return n-1

checks=0
for n in (5,7,10,14):
    for p in (mp.mpf('2.7'),mp.mpf('3'),mp.mpf('3.4')):
        checks+=direct_matrix_gap(n,p)

for n in (80,220,640,1800):
    gap=dispersion(n,1,mp.mpf(3))
    approx=4*mp.pi**2/n**2*(mp.log(n)-mp.log(2*mp.pi)+mp.mpf(3)/2)
    err=abs(gap-approx)
    # The next term is O(n^-4), not merely O(n^-2).
    assert err*n**4 < 90, (n,err*n**4)
    checks+=1

for z in (-2, -1, 0, 1, 2):
    def F(w):
        return (1-mp.exp(-w))/w if w else mp.mpf(1)
    last=None
    for n in (250,500,1000,2000,5000):
        p=3+mp.mpf(z)/mp.log(n)
        gap=dispersion(n,1,p)
        scaled=gap*n**2/(4*mp.pi**2*mp.log(n))
        error=abs(scaled/F(mp.mpf(z))-1)
        if last is not None:
            assert error<last, (z,n, error,last)
        last=error
        checks+=1

print('PASS',checks,'independent Fourier/matrix/asymptotic checks; high-precision arithmetic',mp.dps)
