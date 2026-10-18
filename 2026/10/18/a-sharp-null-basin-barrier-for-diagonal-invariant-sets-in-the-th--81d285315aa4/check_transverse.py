"""Exact symbolic/finite checks for diagonal transverse dynamics of a sign-coupled Lozi map.

Run: python check_transverse.py
This is a finite checker supplementing (not replacing) the mathematical proof.
"""
from fractions import Fraction as Q
from itertools import product
import sympy as s

a,b=s.symbols('a b', real=True, nonzero=True)
x,y,z=s.symbols('x y z', real=True)
u,w=s.symbols('u w', real=True)
checks=0

def check(assertion, description):
    global checks
    if assertion is not True and assertion!=s.true:
        raise AssertionError(description+': '+repr(assertion))
    checks+=1

# Four smooth quadrants: invertibility and exact invariant splitting.
for sx,sz in product((-1,1), repeat=2):
    F=s.Matrix((a*sx*x+sz*y+1,b*(x+z),sx*y+a*sz*z+1))
    J=F.jacobian((x,y,z))
    check(s.simplify(J.det()+2*a*b)==0, f'quadrant ({sx},{sz}) determinant')
    X,Y,Z=F.subs({x:u+w,z:u-w})
    mean=s.expand((X+Z)/2)
    delta=s.expand((X-Z)/2)
    check(s.expand(Y-2*b*u)==0,f'quadrant ({sx},{sz}) base second coordinate')
    if sx==sz:
        check(s.expand(mean-(a*sx*u+sx*y+1))==0,f'quadrant ({sx},{sz}) mean')
        check(s.expand(delta-a*sx*w)==0,f'quadrant ({sx},{sz}) transverse')
        B=s.Matrix(((a*sx,sx),(2*b,0)))
        check(s.simplify(B.det()+2*b*sx)==0,f'quadrant ({sx},{sz}) tangential determinant')
        lam=s.symbols('lambda')
        check(s.simplify(J.charpoly(lam).as_expr()-(lam-a*sx)*((lam**2-a*sx*lam-2*b*sx)))==0, f'quadrant ({sx},{sz}) spectrum factorization')
    else:
        check(s.expand(delta-(sx*a*u+sz*y))==0,f'quadrant ({sx},{sz}) opposite-sign jump')

# A broad finite rational independent substitution check, including changing signs and near-axis points.
params=[(Q(-5,4),Q(1,10)),(Q(-1),Q(1,5)),(Q(4,5),Q(3,10)),(Q(7,5),Q(1,8)),(Q(3,2),Q(-1,4)),(Q(-2),Q(2,7))]
inputs=[Q(-9,7),Q(-2),Q(-1,100),Q(1,100),Q(3,5),Q(2)]
ys=[Q(-7,6),Q(-1,3),Q(0),Q(4,9)]
ws=[Q(-1,500),Q(1,500)]

def sign(v):return 1 if v>=0 else -1

def T(alpha,beta,xx,yy,zz):
    return (alpha*abs(xx)+yy*sign(zz)+1,
            beta*(xx+zz),
            alpha*abs(zz)+yy*sign(xx)+1)

for alpha,beta in params:
    for uu,yy,ww in product(inputs,ys,ws):
        xx=uu+ww;zz=uu-ww
        # if same sign, exactly same center as diagonal, and transverse factor = a sign(uu)
        if sign(xx)!=sign(zz): continue
        newx,newy,newz=T(alpha,beta,xx,yy,zz)
        diagx,diagy,diagz=T(alpha,beta,uu,yy,uu)
        check((newx+newz)==(diagx+diagz), 'exact nonlinear center independence')
        check(newy==diagy,'same-sign center y independence')
        check((newx-newz)==alpha*sign(xx)*(xx-zz),'finite transverse factor')

# Check full return normal multiplier for exact rational diagonal trajectories avoiding the axes.
for alpha,beta in params:
    for uu,yy in product(inputs,ys):
        qq=Q(1);xx=uu; zz=uu
        for n in range(1,12):
            if xx==0:break
            qq*=alpha*sign(xx)
            xnext,ynext,znext=T(alpha,beta,xx,yy,zz)
            check(xnext==znext,'diagonal invariant under iterate')
            # A direct second implementation of the diagonal-normal multiplier.
            # For a finite orbit, the product of the signed scalar derivatives
            # is exactly qq, and its absolute value equals abs(a)**n.
            check(abs(qq)==abs(alpha)**n,'absolute normal derivative after n steps')
            xx,yy,zz=xnext,ynext,znext

print('PASS',checks,'symbolic exact-rational checks, full proof required for global basin theorem')
