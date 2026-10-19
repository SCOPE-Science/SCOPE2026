"""Reproduce the corona grounding threshold calculations.

Dependencies: Python 3, NumPy, SciPy, SymPy.
This program checks finite cases and algebraic identities; the proof in RESULT.md
establishes the theorem for all admissible base graphs and budgets.
"""
import itertools
import numpy as np
from scipy.optimize import brentq, minimize, minimize_scalar
import sympy as sp

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def laplacian(n, edges):
    L = np.zeros((n,n), dtype=float)
    for i,j in edges:
        L[i,i] += 1
        L[j,j] += 1
        L[i,j] -= 1
        L[j,i] -= 1
    return L

def core_types():
    out=[]
    for m in range(3,9):
        out.append((f'clique_{m}', laplacian(m,itertools.combinations(range(m),2))))
        out.append((f'cycle_{m}', laplacian(m,[(i,(i+1)%m) for i in range(m)])))
    for d in (2,3):
        m=2**d
        out.append((f'cube_{d}',laplacian(m,[(i,i^(1<<k)) for i in range(m) for k in range(d) if i<i^(1<<k)])))
    for p in (2,3,4):
        m=2*p
        out.append((f'biclique_{p}', laplacian(m,((i,j) for i in range(p) for j in range(p,2*p)))))
    return out

def full_laplacian(L):
    m=L.shape[0]
    return np.block([[L+np.eye(m), -np.eye(m)],[-np.eye(m),np.eye(m)]])

def phi(z, eigs):
    return (2-z)*sum(float(e)/(float(e)+z) for e in eigs[1:])-len(eigs)

def logdet(M):
    sign,logabs=np.linalg.slogdet(M)
    if sign<=0:return -np.inf
    return float(logabs)

z=sp.symbols('z',positive=True)
m=sp.symbols('m',integer=True,positive=True)
expr=sp.factor((2-z)*(m-1)*m/(m+z)-m)
check(sp.simplify(expr.subs(z,(m-2)/m))==0,'clique threshold identity')
check(sp.simplify(m*((m-2)/m)/(1-(m-2)/m)-m*(m-2)/2)==0,'clique budget identity')
check(sp.simplify((2-z)*(2*sp.Integer(2)/(2+z)+sp.Integer(4)/(4+z))-4 + 4*(3*z*z+8*z-4)/((z+2)*(z+4)))==0, 'C4 resolvent identity')

for name,L in core_types():
    n=len(L)
    eig=np.linalg.eigvalsh(L)
    check(abs(eig[0])<1e-9 and eig[1]>1e-8, f'{name}: connected')
    check(eig[-1]<n+1e-8, f'{name}: eigen bound')
    A0=brentq(lambda a:phi(a,eig), 1e-12, 1-1e-12,xtol=1e-14)
    B0=n*A0/(1-A0)
    check(0<B0<=n*(n-2)/2+1e-8,f'{name}: maximum threshold')
    is_clique=name.startswith('clique') or name=='cycle_3'
    check((abs(B0-n*(n-2)/2)<1e-7)==is_clique,f'{name}: sharp equality')
    for multiplier in (0.2,0.73,1.0,1.27,2.2):
        B=B0*multiplier
        s=B/n
        def theoretical(y):
            a=s-y+y/(1+y)
            return n*np.log1p(y)+np.sum(np.log(eig+a))
        def derivative(y):
            a=s-y+y/(1+y)
            return n/(1+y)+(-1+1/(1+y)**2)*np.sum(1/(eig+a))
        Lf=full_laplacian(L)
        for y in (0.0, s*.13, s*.41, s*.75, s):
            gains=np.concatenate([np.full(n,s-y),np.full(n,y)])
            value=logdet(Lf+np.diag(gains))
            check(abs(value-theoretical(y))<5e-9,f'{name}: Schur determinant identity')
        check(abs(derivative(s)-phi(s/(1+s),eig))<4e-8,f'{name}: endpoint spectral condition')
        check(abs(derivative(0)-n)<4e-8,f'{name}: positive leaf derivative')
        ans=minimize_scalar(lambda y:-theoretical(y),bounds=(0,s), method='bounded', options={'xatol':1e-13})
        yopt=s if B<=B0+1e-9 else brentq(derivative,0,s,xtol=1e-13)
        check(abs(theoretical(yopt)+ans.fun)<1e-6,f'{name}: global reduced maximizer: {multiplier} delta={theoretical(yopt)+ans.fun}')
        check((derivative(s)>=-1e-9)==(B<=B0+1e-9),f'{name}: regime')
        # Explicit KKT gradients of the unrestricted matrix criterion.
        gains=np.concatenate([np.full(n,s-yopt),np.full(n,yopt)])
        inverse=np.linalg.inv(Lf+np.diag(gains))
        grad=np.diag(inverse)
        check(max(grad[:n])-min(grad[:n])<1e-8 and max(grad[n:])-min(grad[n:])<1e-8,f'{name}: orbit gradients')
        if yopt < s-1e-10:
            check(abs(grad[0]-grad[n])<1e-8,f'{name}: interior KKT')
        else:
            check(grad[0]<=grad[n]+1e-8,f'{name}: boundary KKT')
        if name in ('clique_4','cycle_4','biclique_3'):
            # Independent unrestricted random allocations check numerical optimality.
            rng=np.random.default_rng(int(1e5*multiplier)+n)
            target=logdet(Lf+np.diag(gains))
            for _ in range(12):
                weights=rng.dirichlet(np.ones(2*n))*B
                check(logdet(Lf+np.diag(weights))<=target+1e-7,f'{name}: unrestricted competitor')
            x0=np.full(2*n,B/(2*n))
            fit=minimize(lambda v:-logdet(Lf+np.diag(v)),x0,method='SLSQP',bounds=[(0,B)]*(2*n),
                constraints=[{'type':'eq','fun':lambda v:np.sum(v)-B}], options={'maxiter':500,'ftol':1e-11})
            check(fit.success,f'{name}: SLSQP convergence {fit.message}')
            check(abs(-fit.fun-target)<3e-7,f'{name}: unrestricted numerical optimum')

print('VERIFY_OK',checks)
