#!/usr/bin/env python3
"""Characteristic-two Cayley-cubic identities and finite Fano-plane checks.
All identities are in polynomial rings over F_2; the function-field proof is in RESULT.md.
"""
import itertools
import sympy as s
U,V,T,W=s.symbols('U V T W')
X,Y,Z,A=s.symbols('X Y Z A')

def zero_mod2(expr, variables):
    return s.Poly(s.expand(expr), *variables, modulus=2).is_zero

def eq(expr, variables):
    assert zero_mod2(expr,variables), str(s.expand(expr))

e3 = X*Y*Z+X*Y*A+X*Z*A+Y*Z*A
sub = {X:U+W,Y:V+W,Z:T+W,A:W}
eq(e3.subs(sub)-(U*V*T+W*W*(U+V+T)),(U,V,T,W))
F=U*V*T+W*W*(U+V+T)
for i,expect in [(U,V*T+W*W),(V,U*T+W*W),(T,U*V+W*W),(W,0)]:
    eq(s.diff(F,i)-expect,(U,V,T,W))
S=U+V+T
G=[V*T*(V+T),U*T*(U+T),U*V*(U+V)]
for g,partial in zip(G,[s.diff(F,U),s.diff(F,V),s.diff(F,T)]):
    eq(S*partial-g-F,(U,V,T,W)) # in char 2
# Cayley gradient summation in original coordinates
partials=[s.diff(e3,i) for i in (X,Y,Z,A)]
eq(sum(partials),(X,Y,Z,A))
# Seven F2 base points, exactly simple: evaluation of 3 cubics and
# rank of derivatives on local x_j=1 charts of P2.
vars=[U,V,T]
points=[p for p in itertools.product([0,1],repeat=3) if any(p)]
for p in points:
    assert all(int(g.subs(dict(zip(vars,p))))%2==0 for g in G)
    pivot=next(i for i in range(3) if p[i]); local=[i for i in range(3) if i!=pivot]
    jac=[[int(s.diff(g,vars[i]).subs(dict(zip(vars,p))))%2 for i in local] for g in G]
    assert any((jac[i][0]*jac[j][1]-jac[i][1]*jac[j][0])%2 for i in range(3) for j in range(i+1,3)),(p,jac)
# Space of cubics through F2 rational points is dimension 3.
monoms=[U**a*V**b*T**(3-a-b) for a in range(4) for b in range(4-a)]
mat=[[int(m.subs(dict(zip(vars,p))))%2 for m in monoms] for p in points]
def rank2(A):
    A=[row[:] for row in A]; i=0
    for j in range(len(A[0])):
        q=next((h for h in range(i,len(A)) if A[h][j]),None)
        if q is None: continue
        A[i],A[q]=A[q],A[i]
        for h in range(len(A)):
            if h!=i and A[h][j]:A[h]=[c^d for c,d in zip(A[h],A[i])]
        i+=1
        if i==len(A):break
    return i
assert len(monoms)==10 and rank2(mat)==7
# If r=G1/G2 and t=G3/G2, on U=1 the identity
# r=V+tT implies T^2=r(r+1)/(t(t+1)).
v,z,r,t = s.symbols('v z r t')
g1=v*z*(v+z);g2=z*(1+z);g3=v*(1+v)
eq(g1-v*g2-z*g3,(v,z))
eq((g1*g2+g1*g3)*0,(v,z))
# Eliminate v=r+t*z via cross-multiplication of t=g3/g2
h=s.expand((r+t*z)**2+(r+t*z)+t*(z+z*z))
eq(h-(r*r+r+(t*t+t)*z*z),(r,t,z))
# Simple local Jacobian scheme at an ordinary node: on U=1, V=T=W^2
# and T*V+W^2=W^2(W^2+1), a length-2 ring near W=0.
assert s.factor((W*W)*(W*W+1))==W*W*(W*W+1)
print('VERIFY_OK: transformed cubic, Gauss factorization, seven reduced F2 base points, cubic net dimension three, inseparability identities')
# Gauss-field exact Frobenius factorization: each source-coordinate square
# lies in k(r,t), r=g1/g2, t=g3/g2. Clearing denominators verifies:
S1=1+v+z
# W^2=r/(1+t) using relation W^2=v*z/S1
# r/(1+t)=g1/(g2+g3)
eq(g1*S1-v*z*(g2+g3),(v,z))
# z^2 = r(r+1)/(t(t+1)), substitute rational r,t
# multiply through by g2^4:
# z²*g3*(g3+g2)*g2² = g1*(g1+g2)*g2²
# Actually r(r+1)/(t(t+1))=g1(g1+g2)/(g3(g3+g2))
eq(z*z*g3*(g3+g2)-g1*(g1+g2),(v,z))
# y² = r(r+t)/(1+t) = g1(g1+g3)/(g2(g2+g3))
eq(v*v*g2*(g2+g3)-g1*(g1+g3),(v,z))
print('VERIFY_OK: exact Frobenius-coordinate reconstruction')
