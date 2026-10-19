"""Independent numerical checks of Fourier-mode renewal aging formulas.
Run: python check.py (Python >=3.10, mpmath >=1.2).
"""
from itertools import combinations
from math import sin, cos, pi, isclose
import mpmath as mp

mp.mp.dps=240
checks=0

def verify(test, message):
    global checks
    if not bool(test):
        raise AssertionError(message)
    checks += 1

def phi_weights(L):
    return [sin(2*pi*(x+.5)/L) for x in range(L)]

# Independent finite-state generator calculation: unit-rate bond exchanges.
for L in (4,6,8,10,12):
    weights=phi_weights(L)
    eig=2*(1-cos(2*pi/L))
    init=sum(weights[:L//2])
    verify(isclose(init,1/sin(pi/L),rel_tol=1e-13,abs_tol=1e-13), f'initial amplitude {L}')
    for subset in combinations(range(L), L//2):
        state=set(subset)
        val=sum(weights[x] for x in state)
        generator=0.
        for x in range(L):
            y=(x+1)%L
            if (x in state)!=(y in state):
                generator += (weights[y]-weights[x]) if x in state else (weights[x]-weights[y])
        verify(abs(generator+eig*val)<2e-11, f'Fourier generator L={L} state={subset}')

def psi_hat(s, a, b):
    # Direct integral of Pareto(alpha=a, cutoff=b).
    return a*(b*s)**a*mp.gammainc(-a,b*s,mp.inf)

def H(s,a,b):
    return (1-psi_hat(s,a,b))/s

def cov_hat(s,a,b,lam):
    mu=a*b/(a-1)
    ht=H(lam,a,b)
    mean=ht/mu
    expression=(lam*ht*H(lam+s,a,b)/(1-psi_hat(s,a,b))-H(2*lam,a,b))/(mu*(lam-s))
    return expression-mean**2/s

def full_two_part(s,a,b,lam):
    # Independently evaluate no-reset and at-least-one-reset paths.
    mu=a*b/(a-1)
    Nh=(H(lam+s,a,b)-H(2*lam,a,b))/(mu*(lam-s))
    Bh=(psi_hat(s,a,b)-psi_hat(lam,a,b))/(mu*(lam-s))
    Gh=H(lam+s,a,b)/(1-psi_hat(s,a,b))
    return Nh+Bh*Gh

for a,b,lam,s in [(mp.mpf('1.25'),mp.mpf('0.7'),mp.mpf('2'),mp.mpf('.11')),
                  (mp.mpf('1.5'),mp.mpf('1'),mp.mpf('.7'),mp.mpf('.09')),
                  (mp.mpf('1.9'),mp.mpf('3'),mp.mpf('1.4'),mp.mpf('.37')),
                  (mp.mpf('2'),mp.mpf('1'),mp.mpf('.3'),mp.mpf('.07')),
                  (mp.mpf('3.25'),mp.mpf('1.7'),mp.mpf('1.3'),mp.mpf('.13'))]:
    mu=a*b/(a-1)
    m=H(lam,a,b)/mu
    direct=full_two_part(s,a,b,lam)
    combined=cov_hat(s,a,b,lam)+m*m/s
    verify(mp.almosteq(direct,combined,rel_eps=mp.mpf('1e-70')),f'renewal decomposition {a}')
    # Independent one-dimensional integral for stationary first moment.
    survival=lambda u: 1 if u<b else (b/u)**a
    integral=mp.quad(lambda u:mp.exp(-lam*u)*survival(u),[0,b,mp.inf])/mu
    verify(mp.almosteq(m,integral,rel_eps=mp.mpf('1e-55')),f'stationary mean {a}')

# Check small-s covariance transform singularities and exact universal constants.
for a in [mp.mpf('1.2'),mp.mpf('1.5'),mp.mpf('1.8')]:
    for b,lam in [(mp.mpf('1'),mp.mpf('2')), (mp.mpf('.7'),mp.mpf('.4'))]:
        mu=a*b/(a-1)
        m=H(lam,a,b)/mu
        coeff=m*m*b**(a-1)/a*mp.gamma(2-a)  # Laplace of covariance tail
        ratios=[]
        for exponent in (6,12,20,28):
            s=mp.power(10,-exponent)
            val=cov_hat(s,a,b,lam)*s**(2-a)/coeff
            verify(mp.isfinite(val) and val>0,f'positive singular covariance {a}')
            ratios.append(val)
        verify(abs(ratios[-1]-1)<mp.mpf('.005'), f'power-law coefficient {a} {b}: {ratios[-1]}')
        verify(abs(ratios[-1]-1)<abs(ratios[0]-1),f'power-law convergence {a}')

for b,lam in [(mp.mpf('1'),mp.mpf('.7')), (mp.mpf('3'),mp.mpf('2'))]:
    a=mp.mpf('2')
    mu=2*b
    m=H(lam,a,b)/mu
    for exponent in (40,60):
        s=mp.power(10,-exponent)
        ratio=cov_hat(s,a,b,lam)/(m*m*b/2*mp.log(1/s))
        verify(abs(ratio-1)<mp.mpf('.05'),f'logarithmic boundary {b} {exponent}: {ratio}')

# For alpha > 2, the zero-frequency covariance is finite rather than singular.
for a in (mp.mpf('2.4'), mp.mpf('3.5')):
    b=mp.mpf('1')
    lam=mp.mpf('1.3')
    x=cov_hat(mp.mpf('1e-16'),a,b,lam)
    y=cov_hat(mp.mpf('1e-22'),a,b,lam)
    verify(mp.isfinite(y) and abs(x-y)<mp.mpf('.00005')*max(1,abs(y)),f'finite variance regime {a}')

print('PASS',checks,'independent assertions')
for a in ['1.2','1.5','1.8','2','2.4']:
    aa=mp.mpf(a); b=mp.mpf('1'); lam=mp.mpf('2')
    m=H(lam,aa,b)/(aa*b/(aa-1))
    print('alpha=',a,'reset-age mode mean=',mp.nstr(m,13))
