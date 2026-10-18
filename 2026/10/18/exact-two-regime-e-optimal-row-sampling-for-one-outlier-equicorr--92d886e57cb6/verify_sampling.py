#!/usr/bin/env python3
"""Independent algebraic and matrix checks for two-class Kaczmarz probabilities."""
from fractions import Fraction as F
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

checks = 0

def check(statement, message):
    global checks
    assert bool(statement), message
    checks += 1

m, c, r = sp.symbols('m c r', positive=True)
a = (1+(m-1)*c)/m
b = 1-a
delta = a-r*r
p0 = sp.factor((a+r)/(1+a+2*r))
q0 = (1-p0)/m
L0 = sp.factor(delta/(1+a+2*r))
p1 = sp.factor(c*(1-c)/(m*(c-r*r)+c*(1-c)))
q1 = (1-p1)/m
L1 = sp.factor(q1*(1-c))
trace = lambda p: a + b*p
det = lambda p: delta*p*(1-p)

check(sp.simplify(L0**2-trace(p0)*L0+det(p0))==0, 'stationary eigenvalue equation')
check(sp.simplify(b*L0-delta*(1-2*p0))==0, 'stationary derivative')
check(sp.simplify(L1**2-trace(p1)*L1+det(p1))==0, 'crossing eigenvalue equation')
check(sp.simplify((1-c)*q1-L1)==0, 'crossing transverse mode')
check(sp.factor(sp.together(L0-(1-c)*q0)) == sp.factor((m*(c-r*r)-r*(1-c))/(m*(1+a+2*r))), 'phase discriminant')
check(sp.simplify(p1.subs(r,c)-1/(m+1))==0,'uniform at equiangularity')
check(sp.simplify(p0-1/(m+1)-(m-1)*(c+r)/((m+1)*(1+a+2*r)))==0, 'special row boosted in smooth regime')

# Exact characteristic checks and independent numerical optimization.
rational_cases=0
for M in range(2,10):
    for C in [F(1,40),F(1,10),F(1,5),F(2,5),F(3,5),F(4,5)]:
        for R in [F(1,40),F(1,20),F(1,10),F(1,5),F(3,10),F(2,5),F(1,2),F(3,5)]:
            if M*R*R >= 1+(M-1)*C: continue
            cm, rm = sp.Rational(C.numerator,C.denominator),sp.Rational(R.numerator,R.denominator)
            aa=(1+(M-1)*cm)/M
            v=M*(cm-rm*rm)-rm*(1-cm)
            branch='cross' if v>=0 else 'smooth'
            pp=sp.factor((cm*(1-cm))/(M*(cm-rm*rm)+cm*(1-cm))) if branch=='cross' else sp.factor((aa+rm)/(1+aa+2*rm))
            qq=(1-pp)/M
            ll=sp.factor((1-cm)*qq) if branch=='cross' else sp.factor((aa-rm*rm)/(1+aa+2*rm))
            check(0<pp<1 and qq>0 and ll>0, 'positivity')
            Gram=sp.Matrix(M+1,M+1,lambda i,j: 1 if i==j else (rm if min(i,j)==0 else cm))
            P=sp.diag(pp,*([qq]*M))
            check(sp.factor((P*Gram-ll*sp.eye(M+1)).det())==0, 'exact eigenvalue')
            # The full matrix is independent of the two-mode reduced calculation.
            G=np.array(Gram,dtype=float)
            pp_f=float(pp); ll_f=float(ll)
            probs=np.array([pp_f]+[(1-pp_f)/M]*M)
            def eigval(z):
                z=np.asarray(z)
                return np.linalg.eigvalsh(np.sqrt(z)[:,None]*G*np.sqrt(z)[None,:])[0]
            check(abs(eigval(probs)-ll_f)<3e-11, 'full spectrum')
            one=minimize_scalar(lambda x: -eigval([x]+[(1-x)/M]*M),bounds=(1e-10,1-1e-10),method='bounded',options={'xatol':1e-13})
            check(abs(-one.fun-ll_f)<5e-9, 'independent scalar optimizer')
            rng=np.random.default_rng(120000+M*10000+int(C*1000)*10+int(R*1000))
            for _ in range(4):
                contender=rng.dirichlet(np.ones(M+1))
                check(eigval(contender)<=ll_f+1e-10,'asymmetric competitor')
            rational_cases+=1

# One-step conditional Euclidean error identity using row Gram Cholesky.
for M,C,R in [(3,.3,.1),(4,.08,.3),(6,.5,.4),(8,.25,.1)]:
    if M*R*R >= 1+(M-1)*C: continue
    G=np.full((M+1,M+1),C)
    np.fill_diagonal(G,1.)
    G[0,1:]=R; G[1:,0]=R
    U=np.linalg.cholesky(G)
    v=M*(C-R*R)-R*(1-C)
    alpha=(1+(M-1)*C)/M
    p=C*(1-C)/(M*(C-R*R)+C*(1-C)) if v>=0 else (alpha+R)/(1+alpha+2*R)
    weights=np.array([p]+[(1-p)/M]*M)
    S=U.T@np.diag(weights)@U
    vals,vecs=np.linalg.eigh(S)
    z=vecs[:,0]
    observed=sum(weights[i]*np.linalg.norm(z - U[i]*float(U[i]@z))**2 for i in range(M+1))
    check(abs(observed-(1-vals[0]))<1e-12,'sharp Kaczmarz projection identity')

print(f'PASS {checks} assertions; {rational_cases} rational parameter instances')
