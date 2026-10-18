#!/usr/bin/env python3
"""Exact rational checks for the hub-augmentation resistance theorem.

Requires Python 3 and SymPy. All assertions use exact arithmetic.
The arbitrary-size result follows from the accompanying proof, not testing.
"""
from fractions import Fraction
from itertools import combinations
import sympy as S

checks=0

def check(value):
    global checks
    if not value:
        raise AssertionError('Exact identity failed')
    checks+=1

def laplacian(n, weights):
    L=S.zeros(n)
    for u,v,w in weights:
        L[u,u]+=w;L[v,v]+=w
        L[u,v]-=w;L[v,u]-=w
    return L

def objective(n,weights):
    L=laplacian(n,weights)
    one=S.ones(n,1)
    X=L+one*one.T/S.Integer(n)
    return S.factor(n*(S.trace(X.inv())-1))

def graph_cases():
    yield 4,[(0,1)],'one chord'
    yield 5,[(0,1),(1,2),(2,3)],'path'
    yield 4,[(0,1),(1,2),(2,3),(3,0)],'cycle4'
    yield 5,[(i,(i+1)%5) for i in range(5)],'cycle5'
    yield 6,[(i,(i+1)%6) for i in range(6)],'cycle6'
    yield 6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)],'two triangles'
    yield 6,[(0,1),(2,3),(4,5)],'matching'
    yield 4,list(combinations(range(4),2)),'clique4'

for N,H,title in graph_cases():
    n=N+1;B=S.Integer(1);a=B/N
    base=[(0,u+1,a) for u in range(N)]
    k0=objective(n,base)
    check(k0==N**3)
    # Effective-resistance objective derivatives at the uniform star.
    for u,v in H:
        d=S.symbols('d', positive=True)
        weight_base=[(0,w+1,a-S.Rational(3,2)*d/N) for w in range(N)]
        pert=weight_base+[(u+1,v+1,d)]
        expr=objective(n,pert)
        slope=S.simplify(S.diff(expr,d).subs(d,0))
        # All nonspoke costs are 3/2 < 2(N+1)/N.
        check(slope== S.Rational(3,2)*N**3-2*(N+1)*N**2)
    # Arbitrary extra-edge prices: compare explicit first variation.
    for t in [S.Rational(3,2), 2*S.Rational(N+1,N), S.Integer(3)]:
        u,v=H[0]; d=S.symbols('d')
        pert=[(0,w+1,a-t*d/N) for w in range(N)]+[(u+1,v+1,d)]
        exact=S.diff(objective(n,pert),d).subs(d,0)
        check(S.simplify(exact-N**2*(t*N-2*(N+1)))==0)
    # Vertex/edge-transitive cases have invariant spectral formula.
    degs=[sum(1 for u,v in H if z==u or z==v) for z in range(N)]
    if len(set(degs))==1:
        d=S.Rational(degs[0]);E=len(H)
        H_L=laplacian(N,[(u,v,S.Integer(1)) for u,v in H]);
        # Invariant weighted graph and eigenvalue predictions.
        a0=S.Rational(2,5);b0=S.Rational(1,7)
        weighted=[(0,w+1,a0) for w in range(N)]+[(u+1,v+1,b0) for u,v in H]
        K=objective(n,weighted)
        predicted=1/a0+(N+1)*S.trace((a0*S.eye(N)+b0*H_L).inv())-(N+1)/(a0)
        # Trace of H inverse includes N zero-mode: subtract once.
        check(S.simplify(K-predicted)==0)
        lams=list(H_L.eigenvals().items()); 
        moment1=S.trace(H_L);moment2=S.trace(H_L**2)
        check(moment1==N*d)
        check(S.simplify(moment2-N*d*(d+1))==0)
        q=S.symbols('q',real=True); x=S.symbols('x',real=True)
        G=1+(N+1)*(S.trace((S.eye(N)+x*H_L).inv())-1)
        f=S.cancel((1+q*x)*G)
        q0=S.Rational(N+1,N)*d
        Tc=2*S.Rational(N+1,N)
        check(S.factor(S.diff(f,x).subs(x,0).subs(q,S.Rational(E,N)*Tc))==0)
        check(S.factor(S.diff(f,x,2).subs(x,0).subs(q,q0))==2*(N+1)*d*(N-d))
        t=S.symbols('t',real=True)
        slope_in_x=S.factor(S.diff(f,x).subs(x,0).subs(q,t*S.Rational(d,2)))
        check(S.simplify(slope_in_x - S.Rational(N**2,2)*d*(t-Tc))==0)
        onset=S.Rational(N**2,4*(N+1)*(N-d))
        check(onset == S.factor(S.diff(slope_in_x,t)/S.diff(f,x,2).subs(x,0).subs(q,q0)))
        improvement=S.factor(S.Rational(N)*S.diff(slope_in_x,t)**2/(2*S.diff(f,x,2).subs(x,0).subs(q,q0)))
        check(improvement==S.Rational(N**5,16)*d/((N+1)*(N-d)))
        # The second onset coefficient detects the number of triangles.
        T=S.trace((d*S.eye(N)-H_L)**3)/6
        A0=S.diff(f,x,2).subs(x,0).subs(q,q0)
        A1= -S.diff(S.diff(f,x,2).subs(x,0).subs(q,t*d/2),t)
        B0=S.diff(f,x,3).subs(x,0).subs(q,q0)/2
        D=S.simplify(-(A1*onset+B0*onset**2)/A0)
        D_formula=-S.Integer(N)**3 * (d**2*(N*(7-2*N)-(N+4)*d)+18*N*T)/(32*(N+1)**2*d*(N-d)**3)
        check(S.simplify(D-D_formula)==0)

print(f'VERIFY_OK {checks} exact rational/symbolic identities on 8 graph families')
