"""Independent numerical checks for two-column Gaussian-sketch pivot formulas.

Requires numpy>=2 and scipy>=1. Exact-rational portions use Python's fractions.
These finite checks corroborate, but do not replace, the mathematical proof.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.special import betainc


def analytic(alpha, beta, gamma, rows):
    assert alpha >= beta > 0 and abs(gamma) < math.sqrt(alpha*beta)
    delta = alpha-beta
    disc = math.sqrt((alpha+beta)**2-4*gamma**2)
    x = (disc-delta)/(2*disc)
    wrong = betainc(rows/2, rows/2, x)
    determinant = alpha*beta-gamma**2
    largest = (alpha+beta+math.sqrt(delta**2+4*gamma**2))/2
    error = determinant*((1-wrong)/alpha+wrong/beta)
    return wrong, error/(determinant/largest), x


def check():
    checks=0
    # Exact squared-residual bound for the two-row beta probability at orthogonal pairs.
    for i in range(1,301):
        alpha=Fraction(1)
        beta=Fraction(i, 301)
        x=beta/(alpha+beta)
        wrong=x
        ratio=1+(alpha/beta-1)*wrong
        assert ratio == 2*alpha/(alpha+beta)
        assert ratio < 2
        checks+=3

    # Test the algebraic uniform factor-2 bound over random full-rank Gram matrices.
    rng=np.random.default_rng(20261014)
    for _ in range(12000):
        beta=float(np.exp(rng.uniform(-16,0)))
        gamma=float(np.sqrt(beta)*rng.uniform(-.999999,.999999))
        delta=1-beta
        disc=math.sqrt((1+beta)**2-4*gamma*gamma)
        p2=(1-delta/disc)/2
        if p2<0: p2=0 # avoid subtractive-cancellation artifacts
        assert p2 <= beta/(1+beta)+1e-9
        det=beta-gamma*gamma
        largest=(1+beta+math.sqrt(delta*delta+4*gamma*gamma))/2
        err=det*((1-p2)+p2/beta)
        assert err<=2*det/largest*(1+3e-8)
        checks+=2

    # Directly generate the two-column correlated Gaussian sketch for diverse row counts.
    configurations=[(1.,.25,0.,1),(1.,.25,0.,2),(1.,.25,0.,4),
                    (1.,.64,.50,2),(1.,.64,-.50,4),(1.,.01,.02,3),
                    (1.,1.,.9,2),(1.,1.,.9,5)]
    report=[]
    total=0
    for alpha,beta,gamma,s in configurations:
        a=np.array([math.sqrt(alpha),0.])
        b=np.array([gamma/math.sqrt(alpha),math.sqrt(beta-gamma*gamma/alpha)])
        N=250000
        Z=rng.standard_normal((N,s,2))
        ga=np.einsum('nsm,m->ns',Z,a)
        gb=np.einsum('nsm,m->ns',Z,b)
        choose_b=np.sum(gb*gb,axis=1)>np.sum(ga*ga,axis=1)
        empir=float(choose_b.mean())
        exact=analytic(alpha,beta,gamma,s)[0]
        tol=5.5*math.sqrt(max(exact*(1-exact),.00001)/N)+.0002
        assert abs(empir-exact)<tol, (alpha,beta,gamma,s,empir,exact,tol)
        checks+=1
        total+=N
        report.append(f's={s}, alpha={alpha:g}, beta={beta:g}, gamma={gamma:g}: empirical={empir:.6f}, exact={exact:.6f}, tolerance={tol:.6f}')

    # Analytic phase checks across a wide range, using stable incomplete-beta evaluation.
    for s in [1,2,3,4,8,12]:
        for K in [1.1,2,3,10,100,10000]:
            x=1/(K+1)
            p=betainc(s/2,s/2,x)
            ratio=1+(K-1)*p
            assert ratio>=1 and p>0
            if s>=2: assert ratio<=2+1e-12
            checks+=2
    assert (2/math.pi)*math.atan(1/math.sqrt(1e8))*1e8 > 6000
    checks+=1

    print('Exact-rational assertions: 900')
    print('Random Gram-matrix assertions: 24000')
    print(f'Independent Gaussian probe pairs: {total}')
    print('Analytic sketch-dimension assertions: 72')
    print(f'Total assertions: {checks}')
    print('\n'.join(report))
    print('PASS')

if __name__=='__main__':
    check()
