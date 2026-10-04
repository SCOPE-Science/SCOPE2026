#!/usr/bin/env python3
import sympy as sp

u,v,w,t,a,s = sp.symbols('u v w t a s')
x,y,z = sp.symbols('x y z')
Fxy = x**4 - 2*x**2*y**2 + y**4 + 2*x**2*z**2 + 2*y**2*z**2 + z**4 - 4*z**2
F = (u**2+w**2)*(v**2+w**2)-4*w**2

assert sp.expand(F.subs({u:x+y,v:x-y,w:z})-Fxy) == 0
Fu,Fv,Fw = [sp.diff(F,q) for q in (u,v,w)]
assert sp.expand(Fu-2*u*(v**2+w**2)) == 0
assert sp.expand(Fv-2*v*(u**2+w**2)) == 0
assert sp.expand(Fw-2*w*(u**2+v**2+2*w**2-4)) == 0

G = sp.groebner([F,Fu,Fv,Fw,1-t*w], t,u,v,w, order='lex', domain=sp.QQ)
assert any(p.as_expr() == 1 for p in G.polys)

for repl in ({u:0,w:0},{v:0,w:0}):
    assert sp.expand(F.subs(repl)) == 0
    assert all(sp.expand(g.subs(repl)) == 0 for g in (Fu,Fv,Fw))

Hvv = sp.diff(F,v,2).subs({u:a,v:0,w:0})
Hvw = sp.diff(F,v,w).subs({u:a,v:0,w:0})
Hww = sp.diff(F,w,2).subs({u:a,v:0,w:0})
assert sp.simplify(Hvv*Hww-Hvw**2 - 4*a**2*(a**2-4)) == 0

A = (a+s)**2+w**2
assert sp.expand(F.subs(u,a+s) - (A*v**2+(A-4)*w**2)) == 0
S = -(A-4)/A
for av, expected in [(2,-1),(-2,1)]:
    assert sp.simplify(sp.diff(S,s).subs({a:av,s:0,w:0})) == expected
    assert sp.simplify((F.subs(u,a+s)/A - (v**2-S*w**2)).subs(a,av)) == 0

Delta = sp.expand((u**2+v**2-4)**2 - 4*u**2*v**2)
assert sp.expand(Delta - (((u+v)**2-4)*((u-v)**2-4))) == 0
assert Delta.subs({u:0,v:0}) == 16

W,U,V = sp.symbols('W U V')
origin_nf = W**2-U**2*V**2
assert sp.expand(origin_nf - (W-U*V)*(W+U*V)) == 0
for branch in (W-U*V, W+U*V):
    assert sp.diff(branch,W).subs({W:0,U:0,V:0}) == 1

print('VERIFY_OK')
