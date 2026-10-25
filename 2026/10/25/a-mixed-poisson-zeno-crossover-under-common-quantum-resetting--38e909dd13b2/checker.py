"""Independent numerical checks for the common-clock Rabi spin counting law.

Requires mpmath >=1.2. Analytic limit statements are proved in RESULT.md;
finite numerical checks do not constitute a proof of an asymptotic theorem.
"""
from math import factorial
import json
import mpmath as mp

mp.mp.dps = 42
assertions = 0

def check(condition, description):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(description)

def close(x,y,tol):
    return abs(x-y) <= mp.mpf(tol)

def p_down(age,Omega,Delta):
    w=mp.sqrt(Omega**2+Delta**2)
    return (Omega/w)**2*mp.sin(w*age)**2

def moments(Omega,Delta,gamma):
    w2=Omega**2+Delta**2
    mu=2*Omega**2/(gamma**2+4*w2)
    p2=24*Omega**4/((gamma**2+4*w2)*(gamma**2+16*w2))
    cov=4*Omega**4*(5*gamma**2+8*w2)/((gamma**2+4*w2)**2*(gamma**2+16*w2))
    return mu,p2,cov

def finite_pgf(N,Omega,Delta,gamma,s):
    return mp.quad(lambda u:mp.exp(-u)*(1-(1-s)*p_down(u/gamma,Omega,Delta))**N,
        [0,1,2,4,8,15,30,55,100,170])

def mixed_pgf(c,s):
    a=(1-s)/c**2
    return mp.quad(lambda u:mp.exp(-u-a*u*u),[0,1,2,4,8,15,30,55,100,170])

def gaussian_erfc_pgf(c,s):
    if s==1:return mp.mpf('1')
    a=(1-s)/c**2
    return mp.sqrt(mp.pi)/(2*mp.sqrt(a))*mp.exp(1/(4*a))*mp.erfc(1/(2*mp.sqrt(a)))

for Omega,Delta,gamma in [('1.3','0.6','2.2'),('0.8','-1.1','0.9'),('1.0','0','3.3')]:
    O,D,G=map(mp.mpf,(Omega,Delta,gamma))
    mu,p2,cov=moments(O,D,G)
    q1=mp.quad(lambda u:mp.exp(-u)*p_down(u/G,O,D),[0,1,2,4,8,15,30,55,100,170])
    q2=mp.quad(lambda u:mp.exp(-u)*p_down(u/G,O,D)**2,[0,1,2,4,8,15,30,55,100,170])
    check(close(q1,mu,'2e-14'), 'first-moment integral')
    check(close(q2,p2,'2e-14'), 'second raw moment integral')
    check(close(cov,p2-mu**2,'2e-35'),'exact covariance simplification')
    check(cov>0,'strict finite-rate collective covariance')

for c in [mp.mpf('0.8'),mp.mpf('1.5'),mp.mpf('2.5')]:
    for s in [mp.mpf('0'),mp.mpf('0.25'),mp.mpf('0.75')]:
        check(close(mixed_pgf(c,s),gaussian_erfc_pgf(c,s),'3e-36'),
              'closed mixed-Poisson generating function')
        for N in [256,1024,4096]:
            O=mp.mpf('1.3'); D=mp.mpf('0.6'); G=c*O*mp.sqrt(N)
            actual=finite_pgf(N,O,D,G,s)
            target=mixed_pgf(c,s)
            check(abs(actual-target)<mp.mpf('0.08'), 'finite-to-critical PGF')
    for k in range(1,7):
        sample=mp.quad(lambda u:mp.exp(-u)*(u*u/c**2)**k,[0,1,2,4,8,15,30,55,100,170])
        exact=mp.factorial(2*k)/c**(2*k)
        check(abs(sample/exact-1)<mp.mpf('1e-22'), 'factorial-moment identity')
    a=2/c**2
    var=a+20/c**4
    check(var>a,'overdispersion')
    check((var/a)>1,'Fano factor')
    check(mixed_pgf(c,mp.mpf('0'))>mp.exp(-a), 'common reset increases zero-count probability')
    for N in [256,1024,4096,16384]:
        O=mp.mpf('1.3');D=mp.mpf('0.6');G=c*O*mp.sqrt(N)
        mu,p2,cov=moments(O,D,G)
        mean=N*mu
        variance=N*mu*(1-mu)+N*(N-1)*cov
        check(abs(mean-a)<mp.mpf('0.12')*256/N, 'critical mean convergence')
        check(abs(variance-var)<mp.mpf('9')*256/N, 'critical variance convergence')
        check(variance>=mean*(1-mu),'positive shared-clock covariance')
        check(abs((N-1)*N*cov-20/c**4)<mp.mpf('9')*256/N, 'quadratic covariance scaling')

O=mp.mpf('1.3');D=mp.mpf('0.6')
for N in [10000,100000,1000000]:
    gamma=O*N**mp.mpf('0.4')
    rho=gamma/(O*mp.sqrt(N))
    mu,p2,cov=moments(O,D,gamma)
    mean=rho**2*N*mu
    second=rho**4*(N*mu+N*(N-1)*p2)
    check(abs(mean-2)<mp.mpf('0.35'), 'subcritical normalized mean')
    check(abs(second-24)<mp.mpf('7'), 'subcritical normalized second moment')
    gamma=O*N**mp.mpf('0.7')
    mu,p2,cov=moments(O,D,gamma)
    check(N*mu<mp.mpf('0.1'), 'supercritical freeze expectation')

print(json.dumps({'assertions_passed':assertions,'status':'passed',
 'critical_example_c1':{'mean':'2','variance':'22','independent_variance':'2',
 'global_zero_probability':mp.nstr(mixed_pgf(mp.mpf('1'),mp.mpf('0')),16),
 'independent_zero_probability':mp.nstr(mp.exp(-2),16)},
 'tools':'mpmath 1.3.0','scope':'finite exact integrals, exact moment identities, asymptotic numerical trends'},indent=2))
