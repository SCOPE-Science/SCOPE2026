"""Reproduce finite-temperature aggregate asymptotics in two-resource congestion games.

Only the Python standard library is required.  Numerical quadrature checks do not
replace the proof of the all-parameter asymptotic theorem.
"""
import math

N = 8192
LOG2 = math.log(2.0)
C = math.pi * math.pi / 6.0
checks = 0


def logistic(x, y, sigma):
    a = (x-y)/sigma
    if a >= 0:
        z = math.exp(-a)
        return z/(1+z)
    z = math.exp(a)
    return 1/(1+z)


def moments(y, sigma):
    total, weighted = 0.0, 0.0
    for j in range(N+1):
        x = j/N
        v = logistic(x, y, sigma)
        weight = 1 if j in (0,N) else 4 if j%2 else 2
        total += weight*v
        weighted += weight*x*v
    return total/(3*N), weighted/(3*N)


def equilibrium(theta, lam, gam, sigma):
    e0=theta*theta/2
    t=theta+lam*theta*e0-gam*(1-theta)*(0.5-e0)
    def residual(y):
        m,e=moments(y,sigma)
        return y + lam*m*e - gam*(1-m)*(0.5-e) - t
    lo,hi=-2.0,3.0
    for _ in range(56):
        mid=(lo+hi)/2
        if residual(mid)<0:lo=mid
        else:hi=mid
    y=(lo+hi)/2
    return y,*moments(y,sigma)


def test(condition, message):
    global checks
    checks+=1
    if not condition:raise AssertionError(message)


for theta in (0.25,0.5,0.75):
    for lam in (0.2,1.0,2.0):
        for gam in (0.0,0.2,0.4):
            e0=theta*theta/2
            a=1+lam*e0+gam*(0.5-e0)
            b=lam*theta+gam*(1-theta)
            denom=a+theta*b
            cm=-C*b/denom
            ce=C*a/denom
            test(denom>=1 and cm<=0 and ce>0, 'sign/order')
            coeff_errors=[]
            for sigma in (0.018,0.012):
                y,m,e=equilibrium(theta,lam,gam,sigma)
                test(0<y<1 and 0<m<1 and 0<e<.5, 'physical aggregates')
                em=abs((m-theta)/sigma**2-cm)
                ee=abs((e-e0)/sigma**2-ce)
                coeff_errors.append(em+ee)
                test(em<0.014 and ee<0.014, 'quadratic coefficients')
            test(coeff_errors[1]<coeff_errors[0]+2e-5, 'second-order refinement')

# Non-potential example: h_1(M,E)=2ME, h_2=0, theta=1/2, t=5/8.
# The first moment of membership moves downward, while its weighted version
# moves upward, and the total assignment probability moves at order sigma.
for sigma in (0.025, 0.018, 0.012):
    y,m,e=equilibrium(0.5,2.0,0.0,sigma)
    cm=-2*math.pi**2/21
    ce=5*math.pi**2/42
    test(abs((m-0.5)/sigma**2-cm)<0.002, 'witness mass')
    test(abs((e-0.125)/sigma**2-ce)<0.002, 'witness weighted demand')
    # Exact finite-interval L1 formula computed from stable softplus functions.
    def softplus(z):return math.log1p(math.exp(-abs(z)))+max(z,0.0)
    l1=sigma*(softplus((0.5-y)/sigma)+softplus((y-0.5)/sigma))
    # Endpoints are 1/2 away; remaining tails are exponentially small.
    test(abs(l1/sigma-2*LOG2)<0.0002, 'linear L1 coefficient')
    test(m<0.5 and e>0.125, 'opposite drift')
print(f'PASS: {checks} independent numerical assertions using composite Simpson and bisection.')
