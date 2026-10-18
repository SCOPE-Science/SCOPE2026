"""Reproducibility checks for degree-two stochastic Laplacian filters.
Requires Python 3, NumPy and SciPy. Run: python verify_quadratic_biclique.py
Only finite tests are performed; the theorem's all-parameter scope uses its proof.
"""
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog

checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def formula(p, q):
    assert 2 <= p <= q
    if p == 2 or (p - 2)*q <= p*p:
        beta = F(2, p*(p+3*q))
        alpha = beta*(2*p+q)
        tau = F(q-p, p+3*q)
        regime='alternating'
    else:
        beta = F(1, q*(2*p-1))
        alpha = beta*(q+2*p)
        tau = F((p-1)*q-p*p, q*(2*p-1))
        regime='holding-saturated'
    return alpha, beta, tau, regime

def exact_values(p,q,alpha,beta):
    N=p+q
    return tuple(F(1)-alpha*l+beta*l*l for l in (p,q,N))

def feasible(p,q,alpha,beta):
    N=p+q
    return (beta>=0 and alpha>=N*beta
            and 1-alpha*p+beta*p*(p+1)>=0
            and 1-alpha*q+beta*q*(q+1)>=0)

def independent_lp(p,q):
    N=p+q
    A=[]; rhs=[]
    for l in (p,q,N):
        A.append([-l,l*l,-1]);rhs.append(-1)
        A.append([l,-l*l,-1]);rhs.append(1)
    A.append([-1,N,0]);rhs.append(0)
    A.append([p,-p*(p+1),0]);rhs.append(1)
    A.append([q,-q*(q+1),0]);rhs.append(1)
    out=linprog([0,0,1],A_ub=A,b_ub=rhs,
                bounds=[(None,None),(None,None),(0,None)],method='highs',
                options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    assert out.success, (p,q,out.message)
    return out.x

# Exact algebraic identity checks across two branches and the equality boundary.
for p in range(2,19):
    for q in range(p,101):
        a,b,t,regime=formula(p,q)
        check(feasible(p,q,a,b),(p,q,'nonnegative'))
        u,v,w=exact_values(p,q,a,b)
        check(u==t and w==t,(p,q,'extreme modes'))
        check(abs(v)<=t,(p,q,'middle mode'))
        check(t>=0 and t<1,(p,q,'contraction'))
        check(a-(p+q)*b==p*b,(p,q,'cross-probability'))
        if regime=='alternating':
            check(v==-t,(p,q,'alternating mode'))
        else:
            check(v==F(-1,2*p-1),(p,q,'saturated mode'))
            check(1-a*q+b*q*(q+1)==0,(p,q,'zero high-degree holding'))
        x,y,z=independent_lp(p,q)
        check(abs(z-float(t))<1e-8,(p,q,'LP objective'))
        check(abs(x-float(a))<1e-7 and abs(y-float(b))<1e-7,(p,q,'LP coefficients'))

# Matrix-level checks compute the entire stochastic kernel separately.
for p in range(2,8):
    for q in range(p,14):
        N=p+q
        A=np.zeros((N,N))
        A[:p,p:]=1
        A[p:,:p]=1
        L=np.diag(A.sum(axis=1))-A
        a,b,t,regime=formula(p,q)
        K=np.eye(N)-float(a)*L+float(b)*(L@L)
        ev=np.linalg.eigvalsh(K)
        check(np.max(np.abs(K-K.T))<1e-12,(p,q,'symmetry'))
        check(np.min(K)>=-1e-12,(p,q,'entrywise positivity'))
        check(np.max(np.abs(K.sum(axis=1)-1))<1e-12,(p,q,'row sums'))
        check(np.max(np.abs(ev[:-1]))<=float(t)+1e-10,(p,q,'SLEM'))
        check(abs(np.max(np.abs(ev[:-1]))-float(t))<1e-10,(p,q,'sharp SLEM'))
        check(abs(ev[-1]-1)<1e-12,(p,q,'trivial eig'))
        lp=independent_lp(p,q)
        check(np.max(np.abs(lp[:2]-[float(a),float(b)]))<1e-7,(p,q,'LP matrix agreement'))

# Check that two individually stochastic first-order steps cannot match the
# limiting quadratic filter for unbalanced part sizes, using their p-eigenmode.
for p in range(2,9):
    for q in (3*p,10*p,30*p):
        a,b,t,_=formula(p,q)
        lower=(1-F(p,q))**2
        check(t<lower,(p,q,'quadratic improves any pair of stochastic Euler factors'))

print(f'PASS: {checks} verification assertions; finite checks do not prove the infinite theorem.')
