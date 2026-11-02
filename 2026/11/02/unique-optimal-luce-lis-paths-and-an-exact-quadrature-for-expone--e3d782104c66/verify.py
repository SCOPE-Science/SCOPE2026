"""Reproducible checks of the exponential-weight Luce LIS quadrature.

Requires Python 3, NumPy and SciPy.  Numerical tests corroborate, but do not
replace, the infinite-dimensional optimality and asymptotic proofs.
"""
import math
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def g(y):
    if y >= 1:
        return 0.
    return -(1.-y)*math.log1p(-y)

def quantities(beta):
    if beta == 0:
        return .5, 1., 1., .5
    m = math.sqrt(beta / math.e)
    z0 = 1. - 1. / math.e
    def integrals(C):
        def d(y): return math.sqrt(max(0., C*C - beta*g(y)))
        def form(y,typ):
            z=d(y)
            if typ == 0: return 1. / (2.*z*(C+z))
            if typ == 1: return 1. / (2.*z)
            return 1./(2.*(C+z))
        return tuple(quad(lambda y:form(y,k), 0., 1., points=[z0],
                          epsabs=4.e-10, limit=300)[0] for k in range(3))
    lower = m*(1.+1.e-12)
    upper = max(2., 3.*m)
    check(integrals(lower)[0]>1., 'finite-parameter root must exceed threshold')
    while integrals(upper)[0]>=1.: upper *=2
    C=brentq(lambda x:integrals(x)[0]-1.,lower,upper,xtol=2.e-14)
    T,K,R=integrals(C)
    return C,K,T,R

def run():
    table=[]
    for beta in [0., .01, .05, .1, .5, 1., 2., 4., 6., 8., 10.]:
        C,K,T,R = quantities(beta)
        check(abs(T-1.)<1.e-7, 'time normalization')
        check(abs((C+R)-K)<1.e-7, 'dual endpoint identity')
        check(C*C>=beta/math.e -1.e-11, 'spectral admissibility')
        check(K>=1.-1.e-11, 'uniform-weight lower benchmark')
        def flow(t,y):
            yy=min(max(float(y[0]),0.),1.)
            d=math.sqrt(max(0.,C*C-beta*g(yy)))
            return [2.*d*(C+d)]
        sol=solve_ivp(flow,(0.,1.),[0.],rtol=5.e-10,atol=5.e-11,
                      t_eval=[0.,.2,.4,.6,.8,1.])
        check(sol.success, 'smooth optimizer IVP')
        check(abs(sol.y[0,-1]-1.)<2.e-6, 'optimizer endpoint')
        for j in range(5):
            check(sol.y[0,j] < sol.y[0,j+1], 'strictly increasing optimal path')
        for alpha in [.2,.4,.6,.8,1.,1.2,1.5,2.,3.,5.]:
            # A monotone competitor y=1-(1-t)^alpha.
            def integrand(t):
                z=1.-t
                yy=1.-z**alpha
                return math.sqrt(alpha*z**(alpha-1.)+beta*g(yy))
            A=quad(integrand,0.,1.,epsabs=1.e-9,limit=200)[0]
            check(A<K+1.e-7,'competitor exceeds variational maximum')
        table.append((beta,C,K))
    check(abs(table[0][1]-.5)<1.e-12 and abs(table[0][2]-1.)<1.e-12,
          'uniform limit')
    for beta,C,K in table[1:5]:
        check(abs((K-1.)/beta-.125)<.013, 'small beta slope')
    for beta,C,K in table[-3:]:
        check(K>C and K< C+1./(2.*C)+1.e-8,'large-beta bracket')
    print('VERIFICATION PASSED')
    print('Assertions:',CHECKS)
    print('beta             C_beta          K_beta')
    for beta,C,K in table:
        print('%6g    %.10f    %.10f'%(beta,C,K))
    print('Tests are finite consistency checks; global optimality and limiting'
          ' asymptotics rely on the mathematical proof.')

if __name__=='__main__':run()
