#!/usr/bin/env python3
import itertools
import math
import sympy as sp

x0,x1,x2,x3 = sp.symbols('x0 x1 x2 x3')
y0,y1,y2,y3 = sp.symbols('y0 y1 y2 y3')
A,B,C,D = sp.symbols('A B C D')

# Equation (4) of Di Gennaro--Ilardi--Miro-Roig--Szemberg--Szpond,
# written with parameter coordinates A,B,C,D and ambient coordinates x0,...,x3.
F = (
  3*A*D*(C**2-B**2)*x0**2*x1*x2
 +3*B*D*(A**2-C**2)*x0*x1**2*x2
 +3*C*D*(B**2-A**2)*x0*x1*x2**2
 +3*A*C*(B**2-D**2)*x0**2*x1*x3
 +3*B*C*(D**2-A**2)*x0*x1**2*x3
 +3*D*C*(A**2-B**2)*x0*x1*x3**2
 +3*A*B*(D**2-C**2)*x0**2*x2*x3
 +3*C*B*(A**2-D**2)*x0*x2**2*x3
 +3*D*B*(C**2-A**2)*x0*x2*x3**2
 +3*B*A*(C**2-D**2)*x1**2*x2*x3
 +3*C*A*(D**2-B**2)*x1*x2**2*x3
 +3*D*A*(B**2-C**2)*x1*x2*x3**2
 +C*D*(D**2-C**2)*x0*x1*(x0**2-x1**2)
 +B*D*(B**2-D**2)*x0*x2*(x0**2-x2**2)
 +B*C*(C**2-B**2)*x0*x3*(x0**2-x3**2)
 +A*D*(D**2-A**2)*x1*x2*(x1**2-x2**2)
 +A*C*(A**2-C**2)*x1*x3*(x1**2-x3**2)
 +A*B*(B**2-A**2)*x2*x3*(x2**2-x3**2)
)

Fs = sp.expand(F.subs({A:1,B:2,C:4,D:8})/6)
assert Fs != 0

# The sixteen projective B4 points: four coordinate points and e_i +/- e_j.
pts=[]
for i in range(4):
    v=[0]*4; v[i]=1; pts.append(tuple(v))
for i in range(4):
    for j in range(i+1,4):
        for s in (1,-1):
            v=[0]*4; v[i]=1; v[j]=s; pts.append(tuple(v))
assert len(pts)==16 and len(set(pts))==16
for p in pts:
    assert sp.expand(Fs.subs(dict(zip((x0,x1,x2,x3),p)))) == 0

# Send P=[1:2:4:8] to [1:0:0:0].
G = sp.expand(Fs.subs({x0:y0,x1:2*y0+y1,x2:4*y0+y2,x3:8*y0+y3}))
f = (84*y1**3*y2 - 10*y1**3*y3 - 48*y1**2*y2*y3
     -84*y1*y2**3 + 120*y1*y2**2*y3 - 48*y1*y2*y3**2
     +10*y1*y3**3 + y2**3*y3 - y2*y3**3)
assert sp.expand(G-f)==0
assert y0 not in f.free_symbols

# Exact interpolation dimension: quartics through B4 with a quadruple point at P.
vars4=(x0,x1,x2,x3); Ys=(y0,y1,y2,y3)
mons=[]
for e in itertools.product(range(5), repeat=4):
    if sum(e)==4:
        mons.append(e)
assert len(mons)==35
rows=[]
for p in pts:
    rows.append([math.prod(p[i]**e[i] for i in range(4)) for e in mons])
subsP={x0:y0,x1:2*y0+y1,x2:4*y0+y2,x3:8*y0+y3}
for ey in itertools.product(range(5), repeat=4):
    if sum(ey)==4 and ey[0]>0:
        target=math.prod(Ys[i]**ey[i] for i in range(4))
        row=[]
        for e in mons:
            m=math.prod(vars4[i]**e[i] for i in range(4))
            tr=sp.Poly(sp.expand(m.subs(subsP)),*Ys,domain=sp.QQ)
            row.append(tr.coeff_monomial(target))
        rows.append(row)
M=sp.Matrix(rows)
assert M.shape==(36,35)
assert M.rank()==34
assert 35-M.rank()==1

# Smoothness of the projectivized tangent cone C=V(f) in P^2.
grad=[sp.diff(f,v) for v in (y1,y2,y3)]
for patch in (y1,y2,y3):
    others=[v for v in (y1,y2,y3) if v!=patch]
    polys=[sp.expand(g.subs(patch,1)) for g in grad]
    gb=sp.groebner(polys,*others,order='lex',domain=sp.QQ)
    assert len(gb.polys)==1 and gb.polys[0].as_expr()==1

# Numerical geometry of a smooth plane quartic exceptional section.
deg=4
genus=(deg-1)*(deg-2)//2
E2=-deg
# (a+1)E^2 = 2g-2
discrepancy=sp.Rational(2*genus-2,E2)-1
assert genus==3
assert E2==-4
assert discrepancy==-2

print('VERIFY_OK')
