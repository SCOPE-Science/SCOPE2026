"""Independent lattice-resolvent checks for a gated Brownian search.

Requirements: Python 3, numpy, scipy. The continuous result is analytic;
these finite-chain checks are supporting numerical tests, not its proof.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def sensitivity(a, alpha, beta):
    k = math.sqrt(alpha + beta)
    q = beta / alpha
    f = a * (a - 2) * (5 * a*a - 10*a + 4) / 24
    F = (k*k*math.cosh(k)*(a-a*a/2-1/3)
         +math.cosh(k*(1-a))-math.cosh(k)/2
         -k/(2*math.sinh(k)))
    return f + q * F/(k**3 * math.sinh(k))


def lattice_derivative(a, alpha, beta, N):
    """Differentiate the exact finite-chain resolvent at r=0.

    Open gate at site 0 is absorbing; closed gate at site 0 and
    both states at site N are reflecting. Positional resets leave gate unchanged.
    """
    a_idx = round(a*N)
    assert 0 < a_idx < N
    states = [(i,gate) for i in range(N+1) for gate in range(2)
              if not (i==0 and gate==1)]
    ids = {state:j for j,state in enumerate(states)}
    G = lil_matrix((len(states), len(states)), dtype=float)
    h2 = N*N
    for j,(i,gate) in enumerate(states):
        moves = []
        if i==0:
            moves.append(((1,gate),2*h2))
        elif i==N:
            moves.append(((N-1,gate),2*h2))
        else:
            moves.extend([((i-1,gate),h2),((i+1,gate),h2)])
        moves.append(((i,1-gate), alpha if gate==0 else beta))
        for dest,rate in moves:
            G[j,j] -= rate
            if dest in ids: G[j,ids[dest]] += rate
    A = (-G).tocsc()
    m = spsolve(A, np.ones(len(states)))
    rhs = np.array([m[ids[(a_idx,g)]]-m[j] for j,(i,g) in enumerate(states)])
    n = spsolve(A,rhs)
    return (beta*n[ids[(a_idx,0)]]+alpha*n[ids[(a_idx,1)]])/(alpha+beta)


def main():
    num = 0
    for alpha,beta in [(1,1),(.2,3),(3,.2),(.02,.03),(5,12)]:
        for a in [.125,.25,.375,.5,.625,.75,.875]:
            exact = sensitivity(a,alpha,beta)
            n1 = lattice_derivative(a,alpha,beta,160)
            n2 = lattice_derivative(a,alpha,beta,320)
            extrap = (4*n2-n1)/3
            assert abs(extrap-exact)<2.5e-4, (a,alpha,beta,exact,extrap)
            num+=1
    lower=1-1/math.sqrt(3)
    upper=1-1/math.sqrt(5)
    for k in [.12,.3,1,2,4,8,12]:
        for q in [.01,.1,1,10,100]:
            alpha=k*k/(1+q); beta=k*k-alpha
            f=lambda a:sensitivity(a,alpha,beta)
            root=brentq(f,lower,upper,xtol=1e-13)
            assert lower<root<upper
            assert f(root-1e-5)<0<f(root+1e-5)
            num+=3
    for k in [.12,.3,1,2,4,8,12]:
        roots=[]
        for q in [.01,.1,1,10,100]:
            alpha=k*k/(1+q);beta=k*k-alpha
            roots.append(brentq(lambda a:sensitivity(a,alpha,beta),lower,upper))
        assert all(x>y for x,y in zip(roots,roots[1:])), roots
        num+=1
    # Independent coefficient sign tests for the two sharp universal endpoints.
    for n in range(2,25):
        for b,sgn in [(1/math.sqrt(3),-1),(1/math.sqrt(5),1)]:
            S=(1+b)**(2*n+1)+(1-b)**(2*n+1)
            P=S-2**(2*n)+(1-3*b*b)*2**(2*n-1)*(2*n)*(2*n+1)/6
            assert P*sgn>0, (n,b,P)
            num+=1
    print(f'PASS {num} numerical checks; root thresholds in ({lower:.12f},{upper:.12f}).')

if __name__=='__main__': main()
