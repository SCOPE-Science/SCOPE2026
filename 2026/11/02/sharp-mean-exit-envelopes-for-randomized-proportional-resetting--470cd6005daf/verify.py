"""Numerical checks of symmetric first-exit moments for random contraction resets."""
import math
import numpy as np
from scipy.sparse import diags, lil_matrix
from scipy.sparse.linalg import spsolve


def exit_formula(x, L, D, r, factors, cutoff=150, return_terms=False):
    """factors is a list of (multiplicative factor, probability)."""
    moments = lambda j: sum(prob * a ** (2*j) for a, prob in factors)
    term = L * L / (2 * D)
    value = term * (1 - (x/L)**2)
    vals = [term]
    for n in range(2, cutoff + 1):
        j = n - 1
        term *= (r/D) * (1-moments(j)) * L**2 / ((2*n)*(2*n-1))
        value += term * (1 - (x/L)**(2*n))
        vals.append(term)
        if abs(term) < 1e-14 * abs(value):
            break
    return (value, vals) if return_terms else value


def numerical_generator(x, L, D, r, factors, gridsize=1001):
    # Finite-difference BVP for the full nonlocal generator.
    mesh = np.linspace(-L, L, gridsize)
    h = mesh[1]-mesh[0]
    N = gridsize - 2
    M = lil_matrix((N, N))
    rhs = np.ones(N)
    for i, y in enumerate(mesh[1:-1]):
        M[i, i] += 2*D/h**2+r
        if i > 0: M[i, i-1] -= D/h**2
        if i < N-1: M[i, i+1] -= D/h**2
        for a, prob in factors:
            at = a*y
            w = (at+L)/h
            lo = int(min(gridsize-2, max(0, math.floor(w))))
            frac = w-lo
            for k, alpha in ((lo,1-frac),(lo+1,frac)):
                if 1 <= k <= gridsize-2:
                    M[i, k-1] -= r*prob*alpha
    solution = spsolve(M.tocsr(), rhs)
    ix = int(round((x+L)/h))
    return solution[ix-1] if 0<ix<gridsize-1 else 0.0


def check():
    count = 0
    L,D,r=1.3,0.7,2.4
    q=0.36
    b=math.sqrt(q)
    protocols = {
        "fixed": [(b,1.)],
        "mixed": [(0.,0.2),(b,0.375),(1.,0.425)],  # q different; compare only BVP
        "bernoulli": [(0.,1-q),(1.,q)],
        "signed": [(-0.6,0.5),(0.6,0.5)],
    }
    for name,p in protocols.items():
        for x in (0.,.26,.65,-.26):
            exact = exit_formula(x,L,D,r,p)
            numerical = numerical_generator(x,L,D,r,p,gridsize=801)
            assert abs(numerical-exact) < 8.0e-4, (name,x,exact,numerical)
            count+=1
        if name == 'signed':
            assert abs(exit_formula(0.,L,D,r,p)-exit_formula(0.,L,D,r,protocols['fixed']))<1e-12
            count+=1
    for q in (.03,.1,.3,.6,.85,.97):
        for r in (.05,.5,1.,10.,50.):
            b=math.sqrt(q)
            fixed = exit_formula(0.,1.,1.,r,[(b,1.)])
            bern = exit_formula(0.,1.,1.,r,[(0.,1-q),(1.,q)])
            half = exit_formula(0.,1.,1.,r,[(0.,(1-q)/2), (b, 1./2), (1.,q/2)]) # E[A²]=q
            assert bern+1e-12 < half < fixed-1e-12,(q,r,bern,half,fixed)
            benchmark=(math.cosh(math.sqrt(r*(1-q)))-1)/(r*(1-q))
            assert abs(bern-benchmark)<2e-10*max(1.,benchmark)
            count+=2
    for r in (.01,.1,1.,4.):
        for q in (.1,.4,.8):
            v=exit_formula(0.,1.,1.,r,[(math.sqrt(q),1.)])
            v0=exit_formula(0.,1.,1.,r,[(0.,1.)])
            assert .5 < v < v0
            count+=1
    q=.4
    p=math.prod(1-q**j for j in range(1,200))
    r=10000
    value=exit_formula(0.,1.,1.,r,[(math.sqrt(q),1.)],cutoff=400)
    asym=p*math.exp(math.sqrt(r))/(2*r)
    assert abs(value/asym-1)<.002,(value,asym)
    count+=1
    # Weak reset: finite difference coefficient isolates Var(A²).
    q=.36
    p = [(0.,.4),(math.sqrt(q/.6),.6)]
    assert abs(sum(x*x*pr for x,pr in p)-q)<1e-12
    for r in (.1,.05,.02):
        fixed=exit_formula(0.,1.,1.,r,[(math.sqrt(q),1.)])
        randomized=exit_formula(0.,1.,1.,r,p)
        var_a2 = sum(x**4*pr for x,pr in p)-q*q
        pred=r*r*(1-q)*var_a2/720
        assert abs((fixed-randomized)/pred-1) < .1,(r,fixed-randomized,pred)
        count+=1
    print(f'PASS: {count} finite-difference, strict-bound, special-case, asymptotic checks')

if __name__=='__main__': check()
