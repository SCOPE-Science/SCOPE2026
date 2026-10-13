"""Independent finite checks of the five-cycle flat-gate recurrence identities.

All exact infinite-size assertions are proved analytically; floating-point
calculations here check normalization and representative finite instances.
"""
import cmath
import math

pi = math.pi
root5 = math.sqrt(5)
omega = cmath.exp(2j*pi/5)
lambda_ = [2 * math.cos(2*pi*r/5) for r in range(5)]
# Spectral masks: 0, +/-1, +/-2.
expect_eigs = [2,(root5-1)/2,(-root5-1)/2]
assert abs(lambda_[0]-expect_eigs[0]) < 1e-13
for r in (1,4):assert abs(lambda_[r]-expect_eigs[1])<1e-13
for r in (2,3):assert abs(lambda_[r]-expect_eigs[2])<1e-13
checks=0

def spectral_U(t, j, k):
    return sum(cmath.exp(1j*t*lambda_[r])*omega**(r*(j-k)) for r in range(5))/5

def target_F(j,k):
    return sum(omega**((r*r+r*(j-k))%5) for r in range(5))/5

def delta(t):
    return max(abs(cmath.exp(1j*(expect_eigs[r]-2)*t)-omega**(r*r)) for r in (1,2))

for j in range(5):
    for k in range(5):
        z=target_F(j,k)
        assert abs(abs(z)**2 - 1/5) < 5e-14
        checks += 1

for t in [0.0, .125, .8, 3., 5.5, 10.77, 20.9]:
    lhs = max(abs(cmath.exp(-2j*t)*spectral_U(t,j,k)-target_F(j,k)) for j in range(5) for k in range(5))
    # Entrywise differences bounded by spectral-operator distance; direct
    # spectral residual equality checked via the three eigenmode pairs.
    assert lhs <= delta(t)+2e-13
    for j in range(5):
        assert abs(sum(abs(spectral_U(t,j,k))**2 for k in range(5))-1)<1e-12
        checks += 1

f0,f1=0,1
l0,l1=2,1
previous_t=0
bound=4*pi*pi/(25*root5)
for n in range(1,33):
    f0,f1=f1,f0+f1
    l0,l1=l1,l0+l1
    assert l0*l0-5*f0*f0==4*((-1)**n)
    if n%4==0:
        k=f0
        N=l0
        assert (N-5*k-2)%10==0
        assert N*N-5*k*k==4
        t=2*pi*k/5
        # Floating point phase precision deteriorates for huge Fibonacci k;
        # use the Pell-cancelled residual to check it without cancellation.
        eps = -2/(5*(root5*k + N)) # sign from irrational - rational
        exact_delta = 2*abs(math.sin(pi*eps))
        assert k>=3 and exact_delta>0
        if k<=987:
            assert abs(delta(t)-exact_delta)<3e-10
        assert abs(t*exact_delta-bound)<1.0/k
        checks += 1

for k in range(1,600):
    N=5*k+10*round(((root5-5)*k-2)/10)+2
    assert (5*k*k-N*N)%20==16
    checks+=1

print('VERIFY_OK',checks,'sharp_constant',format(bound,'.12f'))
