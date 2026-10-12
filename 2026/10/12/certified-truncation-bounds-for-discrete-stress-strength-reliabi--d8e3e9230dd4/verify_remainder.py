import math


def survival_ge(k, alpha, theta, beta):
    """DAPW P(X>=k), with the continuous alpha=1 extension."""
    a = theta ** (k ** beta)
    if abs(alpha - 1.0) < 1e-14:
        return a
    return alpha/(alpha-1.0) * (-math.expm1(-a*math.log(alpha)))


def pmf(x, alpha, theta, beta):
    return survival_ge(x,alpha,theta,beta)-survival_ge(x+1,alpha,theta,beta)


def cdf(x, alpha, theta, beta):
    if x < 0:
        return 0.0
    return 1.0-survival_ge(x+1,alpha,theta,beta)


def term(x, alpha, theta1, beta1, theta2, beta2):
    return pmf(x,alpha,theta1,beta1)*cdf(x-1,alpha,theta2,beta2)

# Published Scenario 4.
alpha=0.3
theta1=0.4
beta1=0.2
theta2=0.4
beta2=2.0
K=4041

increment=term(K,alpha,theta1,beta1,theta2,beta2)
upper=survival_ge(K+1,alpha,theta1,beta1)
# A rigorous monotone lower bound can use F_Y(1), avoiding extreme-tail arithmetic.
fy1=cdf(1,alpha,theta2,beta2)
lower=fy1*upper

assert increment < 1e-6
assert abs(increment-9.99890871234167e-7) < 5e-18
assert abs(upper-0.00416841458563916) < 2e-16
assert abs(fy1-0.986585024146203) < 2e-15
assert lower > 0.0041
assert upper/lower < 1.02
assert lower/increment > 4000.0

# Reconstruct the partial sum.
rk=sum(term(x,alpha,theta1,beta1,theta2,beta2) for x in range(K+1))
assert abs(rk-0.2497120830577852) < 2e-15

# Large-cutoff consistency replay: direct remainder must lie inside the certificate.
M=250000
r_direct=sum(term(x,alpha,theta1,beta1,theta2,beta2) for x in range(K+1,M+1))
residual_after_M=survival_ge(M+1,alpha,theta1,beta1)
# direct truncated remainder plus its own remaining survival must fit the main upper bound
assert r_direct <= upper + 1e-15
assert r_direct + residual_after_M <= upper + 1e-12
assert r_direct + residual_after_M >= lower - 2e-5

# Distribution-free theorem replay on a few small finite distributions.
examples=[
    ([0.2,0.3,0.5],[0.6,0.4],0),
    ([0.1,0.2,0.3,0.4],[0.1,0.2,0.7],1),
]
for px,py,K0 in examples:
    def Fy(j):
        if j<0:return 0.0
        return sum(py[:min(j+1,len(py))])
    R=sum(px[x]*Fy(x-1) for x in range(len(px)))
    Rk=sum(px[x]*Fy(x-1) for x in range(min(K0+1,len(px))))
    tail=sum(px[K0+1:])
    assert Fy(K0)*tail - 1e-15 <= R-Rk <= tail + 1e-15

print('VERIFY_OK')
