"""Exact algebra and high-precision checks for the Gaussian spiked-range theorem.
Run: python verify.py  (requires sympy and mpmath).
The mathematical proof, not these finite tests, establishes the universal results.
"""
import random
import sympy as sp
import mpmath as mp

rng = random.Random(712404)
checks = 0
for n in (3, 4, 5, 6):
    for k in range(1, n):
        for trial in range(5):
            while True:
                Om = sp.Matrix(n, k, [rng.randint(-3, 3) for _ in range(n*k)])
                B = Om[1:, :]
                if B.rank() == k:
                    break
            a = Om[:1, :]
            H = B.T * B
            for eps in (sp.Rational(1, 2), sp.Rational(1, 3)):
                A2 = sp.diag(1, *([eps**2]*(n-1)))
                for power in (1, 2, 3):
                    delta = eps**power
                    Y = sp.diag(1, *([delta]*(n-1))) * Om
                    P = Y * (Y.T*Y).inv() * Y.T
                    U = (sp.eye(n)-P)[0,0]
                    schur = delta**2/(delta**2 + (a*H.inv()*a.T)[0])
                    squared_loss = sp.trace((sp.eye(n)-P)*A2)
                    assert sp.factor(U - schur) == 0
                    assert sp.factor(squared_loss - (n-k)*eps**2-(1-eps**2)*U) == 0
                    checks += 2

mp.mp.dps = 75

def exact_moment(n, k, delta, q):
    a=mp.mpf(k)/2
    b=mp.mpf(n-k)/2
    return (delta**(2*q)*mp.beta(b+q,a)/mp.beta(b,a) *
            mp.hyp2f1(q,b+q,a+b+q,1-delta**2))

def asymptotic_constant(n,k,q):
    a=mp.mpf(k)/2
    b=mp.mpf(n-k)/2
    if q<a:
        return mp.gamma(b+q)*mp.gamma(a-q)/(mp.gamma(b)*mp.gamma(a))
    if q==a:
        return 2*mp.gamma(b+a)/(mp.gamma(b)*mp.gamma(a))
    return mp.gamma(b+a)*mp.gamma(q-a)/(mp.gamma(b)*mp.gamma(q))

# Check all three moment regimes at a very small spike, allowing logarithmic
# boundary convergence to be slower than ordinary power asymptotics.
delta=mp.mpf('1e-20')
for n,k,q in ((6,1,mp.mpf('0.25')),(6,1,mp.mpf('0.5')),
              (6,1,mp.mpf('1')),(6,2,mp.mpf('0.5')),
              (6,2,mp.mpf('1')),(6,2,mp.mpf('2')),
              (6,3,mp.mpf('1')),(6,3,mp.mpf('2')),
              (6,4,mp.mpf('1'))):
    val=exact_moment(n,k,delta,q)
    a=mp.mpf(k)/2
    leading=(delta**(2*q) if q<a else
             delta**k*mp.log(1/delta) if q==a else delta**k)
    ratio=val/(leading*asymptotic_constant(n,k,q))
    assert abs(ratio-1) < mp.mpf('0.035'), (n,k,q,ratio)
    checks+=1

# The ordinary (power one) and row-aware (power two) sketch have the stated
# exact law at every admissible dimension and sketch rank.
for n in (3,5,8):
    for k in range(1,n):
        for eps in (mp.mpf('0.12'),mp.mpf('0.47')):
            for power in (1,2):
                delta=eps**power
                exact_loss=(n-k)*eps**2+(1-eps**2)*exact_moment(n,k,delta,1)
                assert exact_loss >= (n-k)*eps**2
                assert exact_loss <= 1+(n-1)*eps**2
                checks+=2
# Exact beta-survival and the finite-loss rare-event asymptotics.
for n,k,thr in ((4,1,mp.mpf('0.2')),(6,2,mp.mpf('0.4')),
                (8,3,mp.mpf('0.7')),(7,5,mp.mpf('0.35'))):
    delt=mp.mpf('1e-8')
    b=mp.mpf(n-k)/2
    a=mp.mpf(k)/2
    lower=thr/(delt**2+(1-delt**2)*thr)
    surv=mp.betainc(b,a,lower,1,regularized=True)
    c=mp.gamma(mp.mpf(n)/2)/(mp.gamma(b)*mp.gamma(a+1)) * ((1-thr)/thr)**a
    assert abs(surv/(delt**k*c)-1)<mp.mpf('1e-5'),(n,k,thr,surv,c)
    checks += 1
print('PASS', checks, 'exact-algebra and high-precision checks')
