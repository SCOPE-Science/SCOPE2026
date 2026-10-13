"""Exact verification of spectral factors and spanning-tree count for line graphs of matching-deleted cliques."""
import math
import sympy as sp
from fractions import Fraction

X=sp.symbols('x')

def edge_list(n,t):
    forbidden={(2*j,2*j+1) for j in range(t)}
    return [(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in forbidden]

def line_laplacian(n,t):
    E=edge_list(n,t)
    m=len(E)
    H=sp.zeros(m)
    for u in range(m):
        for v in range(u):
            if len(set(E[u])&set(E[v])):
                H[u,u]+=1; H[v,v]+=1
                H[u,v]=-1;H[v,u]=-1
    return H

def spectral_factor(n,t):
    if t==0:
        m=n*(n-1)//2
        return sp.Poly(-X*(n-X)**(n-1)*(2*n-2-X)**(m-n),X)
    a=2*t;r=n-a
    x=2*(n-2)-X;y=2*n-3-X;z=2*(n-1)-X
    eAA=a*(a-2)//2; eAB=a*r; eBB=r*(r-1)//2
    U=1-sp.Rational(a-2,1)/x-r/y
    V=1-sp.Rational(a-4,1)/x-r/y
    if r==0:
        T=1-sp.Rational(2*(a-2),1)/x
        expr=x**eAA * U**t * V**(t-1) * T
    else:
        W=1-sp.Rational(r-2,1)/z-a/y
        T=(1-sp.Rational(2*(a-2),1)/x-r/y)*(1-sp.Rational(2*(r-1),1)/z-a/y)-a*r/y**2
        expr=x**eAA*y**eAB*z**eBB*U**t*V**(t-1)*W**(r-1)*T
    return sp.Poly(sp.cancel(expr),X)

def tree_formula(n,t):
    if t==0:
        m=n*(n-1)//2
        return sp.Rational(n**(n-1)*(2*n-2)**(m-n),m)
    a=2*t;r=n-a
    alpha=sp.Rational(n-2,2)
    beta=sp.Rational((n-2)*(n-1),2*n-3)
    gamma=sp.Rational(n-1,2)
    Eaa=a*(a-2)//2; Eab=a*r; Ebb=r*(r-1)//2
    pref=sp.Rational((2*(n-2))**Eaa *(2*n-3)**Eab *(2*(n-1))**Ebb,(n-2)**(2*a)*(n-1)**(2*r))
    if r:
        tw=beta*((a-2)*alpha+r*beta)**t*(a*alpha+r*beta)**(t-1)*(r*gamma+a*beta)**(r-1)
    else:
        tw=sp.Rational(1,n)*((a-2)*alpha)**t*(a*alpha)**(t-1)
    return sp.cancel(pref*tw)

def main():
    ct=0
    for n in range(4,10):
        for t in range(0,n//2+1):
            H=line_laplacian(n,t)
            pred=spectral_factor(n,t)
            direct=H.charpoly(X).as_expr()
            # H.charpoly det(X I - H); our factor det(H-X I); sign (-1)^m
            assert sp.expand(pred.as_expr()-(-1)**H.rows*direct)==0, (n,t,pred.as_expr(),direct)
            T=tree_formula(n,t)
            assert T.is_Integer and T>0, (n,t,T)
            # derivative of det(H-X I) at X=0 = -m*tau(H) if connected
            tau_from_poly=-pred.diff().eval(0)/H.rows
            assert sp.simplify(tau_from_poly-T)==0, (n,t,T,tau_from_poly)
            if H.rows<=26:
                minor=H[:H.rows-1,:H.cols-1].det(method='domain-ge')
                assert minor==T, (n,t,minor,T)
            ct+=1
            print(n,t,H.rows,'tau',T,'lambda_factors',sp.factor(pred.as_expr()),flush=True) if n<=6 else None
    print('VERIFY_OK cases=',ct,'orders=4..9','all_matching_sizes=0..floor(n/2)')
if __name__=='__main__':main()
