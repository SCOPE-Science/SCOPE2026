"""Finite-dimensional verification of a three-dot load-discharge crossover.
Run: python verify.py
Requires numpy and scipy. Analytic arguments are in RESULT.md.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq
from scipy.special import expit

CHECKS = 0

def check(test, message):
    global CHECKS
    CHECKS += 1
    if not bool(test):
        raise AssertionError(message)


def model(delta, omega=1., gamma=.1, temp=1., c=4.5):
    H = np.array([[delta, -omega, 0.], [-omega, 0., -omega], [0., -omega, 0.]])
    energies, vectors = np.linalg.eigh(H)
    mu = energies[2] - c * temp
    overlaps = vectors[0,:]**2
    fermi = expit((mu - energies)/temp)
    incoming = gamma * overlaps * fermi
    outgoing = gamma * overlaps * expit((energies-mu)/temp)
    Q = np.zeros((4,4))
    for j in range(3):
        Q[1+j,0] = incoming[j]
        Q[0,1+j] = outgoing[j]
    Q[np.diag_indices(4)] = -np.sum(Q,axis=0)
    Z = 1+sum(np.exp((mu-energies)/temp))
    stat = np.r_[1., np.exp((mu-energies)/temp)] / Z
    ch = math.cosh(omega/temp)
    initial = np.array([1.,math.exp(omega/temp),math.exp(-omega/temp),ch])/(1+3*ch)
    def work(t):
        return float((expm(Q*t)@initial)[0] - initial[0])
    return Q,initial,stat,incoming,outgoing,work,mu,energies,overlaps


def run():
    f=expit(-4.5)
    c=math.cosh(1)
    p0=1/(1+3*c)
    m=(1+c)/(1+3*c)
    theta_star=math.log((1-f)*m/p0)/(1-f)
    check(theta_star>0,'positive return-scale root')
    check((1-f)*m>p0,'positive extraction plateau')
    check(math.isclose(theta_star,0.9325745931819455,rel_tol=2e-13),'critical number')
    print('limit f=',f,'theta_star=',theta_star)
    errors=[]
    root_errors=[]
    for delta in [40,60,80,100,150,200,300,500]:
        Q,p,pi,ins,outs,work,mu,en,u=model(delta)
        check(np.allclose(Q.sum(axis=0),0.,atol=1e-14),'column conservation')
        check(np.all(ins>0) and np.all(outs>0),'irreducible contact')
        check(np.allclose(Q@pi,np.zeros(4),atol=1e-13),'Gibbs stationarity')
        check(np.allclose(ins*pi[0],outs*pi[1:],rtol=1e-11,atol=1e-14),'detailed balance')
        check(abs(sum(pi)-1)<1e-12,'Gibbs normalization')
        check(np.allclose(p.sum(),1.),'initial normalization')
        check(np.allclose(u.sum(),1.),'endpoint spectral completeness')
        check(work(100)>0,'short finite extraction')
        check(pi[0]<p0,'negative accumulated output after equilibration')
        check(math.isclose(u[0]*delta**2,0.5,rel_tol=0.08),'low-branch overlap ground')
        check(math.isclose(u[1]*delta**2,0.5,rel_tol=0.08),'low-branch overlap excited')
        check(u[2]>0.99,'detuned state localization')
        scale=delta**2/.1
        for theta in (0.2,0.4,0.65,0.85,theta_star,1.1,1.5,2.,3.):
            approx=(1-f)*m*math.exp(-(1-f)*theta)-p0
            actual=work(theta*scale)
            check(abs(actual-approx)<0.006,'slow scaled limiting profile')
            check(abs(actual-approx)*delta**2<8.,'second-order convergence envelope')
        r=brentq(lambda th:work(th*scale),.6,1.4,xtol=5e-12)
        check(abs(r-theta_star)<.07,'critical time quadratic limit')
        root_errors.append((delta,r,r-theta_star))
        errors.append((delta,work(theta_star*scale)))
    for (_,__,a),(_,___,b) in zip(root_errors,root_errors[1:]):
        check(abs(b)<abs(a),'root error decreases with detuning')
    for (_,a),(_,b) in zip(errors,errors[1:]):
        check(abs(b)<abs(a),'crossover profile error decreases')
    print('roots (detuning, scaled root, error):',root_errors)
    print('profile at theta_star:',errors)
    print('PASS:',CHECKS,'deterministic assertions')

if __name__ == '__main__': run()
