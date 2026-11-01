"""High-precision finite tests of cycle Gaussian Fourier assertions.
Requires mpmath. This is supporting computation, not proof of the limits.
"""
import mpmath as mp
mp.mp.dps = 100

def witness_index(n):
    m = n // 2
    if n % 2 == 0:
        return m if m % 2 == 0 else m-1
    return m if m % 2 == 0 else m-1

def eigenvalue(n, j, t):
    return mp.fsum(mp.exp(-t * min(r, n-r)**2) *
                   mp.cos(2*mp.pi*j*r/n) for r in range(n))

def theta(theta, t):
    return mp.sqrt(mp.pi/t) * mp.fsum(
        mp.exp(-(theta+2*mp.pi*k)**2/(4*t)) for k in range(-5, 6))

def truncated_difference(n, j, t):
    return theta(2*mp.pi*j/n, t)-eigenvalue(n, j, t)

def analytic_positive_ratio(n, t):
    return (2*mp.sqrt(t/mp.pi)/(1-mp.exp(-t*n)) *
            mp.exp(mp.pi**2/(4*t)-t*n**2/4))

for n in (40,41,42,43,80,81,82,83,120,121,122,123):
    j=witness_index(n)
    low=(mp.pi-mp.mpf('0.5'))/n
    high=(mp.pi+mp.mpf('0.5'))/n
    lv=eigenvalue(n,j,low)
    hv=eigenvalue(n,j,high)
    assert lv<0, (n,'low',lv)
    assert hv>0, (n,'high',hv)
    assert analytic_positive_ratio(n,high)<1, (n,'uniform positive bound')
    assert truncated_difference(n,j,low)>0, (n,'tail sign')
    print('n=%3d j=%3d low_eigen=%s high_eigen=%s' %
          (n,j,mp.nstr(lv,8),mp.nstr(hv,8)))

for n in (12,13,14,15):
    for j in (0,1,n//2):
        t=mp.mpf('0.7')
        v=eigenvalue(n,j,t)
        # Verify an actual matrix-vector product against a Fourier eigenvector.
        f=[mp.exp(2j*mp.pi*j*b/n) for b in range(n)]
        for a in (0,2,n-1):
            product=mp.fsum(mp.exp(-t*min((a-b)%n,(b-a)%n)**2)*f[b]
                            for b in range(n))
            assert abs(product-v*f[a]) < mp.mpf('1e-85')
print('PASS: witness negativity, high-parameter positivity, and matrix Fourier checks')
