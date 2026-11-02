"""Reproducible exact checks of the three-season stage-projection identity."""
from fractions import Fraction as F
from itertools import permutations
from random import Random


def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def mat(f,s,t):
    return ((F(0),f),(s,t))

def tr(a): return a[0][0]+a[1][1]
def det2(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def det3(rows):
    (a,b,c),(d,e,f),(g,h,i)=rows
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def period(P,order):
    a=((F(1),F(0)),(F(0),F(1)))
    for j in order: a=mm(P[j],a)
    return a

# Fully symbolic proof support: the trace identity and determinant equality.
import sympy as S
f1,f2,f3,s1,s2,s3,t1,t2,t3=S.symbols('f1 f2 f3 s1 s2 s3 t1 t2 t3')
p=[S.Matrix([[0,f],[s,t]]) for f,s,t in zip((f1,f2,f3),(s1,s2,s3),(t1,t2,t3))]
T123=S.trace(p[2]*p[1]*p[0]); T132=S.trace(p[1]*p[2]*p[0]);
V=S.Matrix([[f1,s1,t1],[f2,s2,t2],[f3,s3,t3]])
assert S.expand(T123-T132-V.det())==0
assert S.expand(T123-(t1*t2*t3+s1*f3*t2+s3*f2*t1+s2*f1*t3))==0
assert S.expand(T132-(t1*t2*t3+s1*f2*t3+s2*f3*t1+s3*f1*t2))==0
assert S.expand((p[2]*p[1]*p[0]).det()+f1*s1*f2*s2*f3*s3)==0
print('Symbolic trace, determinant and recruitment-loop identities: PASS')

rng=Random(20261027)
num=0
for _ in range(500):
    ff=[F(rng.randint(1,20),rng.randint(1,10)) for _ in range(3)]
    ss=[F(rng.randint(1,19),20) for _ in range(3)]
    tt=[F(rng.randint(1,19),20) for _ in range(3)]
    p=[mat(ff[i],ss[i],tt[i]) for i in range(3)]
    left=period(p,(0,1,2));right=period(p,(0,2,1));
    assert tr(left)-tr(right)==det3(list(zip(ff,ss,tt)))
    assert det2(left)==det2(right)==-(ff[0]*ss[0]*ff[1]*ss[1]*ff[2]*ss[2])
    group1=set();group2=set()
    for order in permutations(range(3)):
        T=tr(period(p,order))
        if order in ((0,1,2),(1,2,0),(2,0,1)): group1.add(T)
        else: group2.add(T)
    assert len(group1)==len(group2)==1
    assert group1=={tr(left)} and group2=={tr(right)}
    num+=4
print('Exact rational identity checks (500 datasets, four properties each):',num)

ff=[F(3,5),F(6,5),F(12,5)]
ss=[F(1,4),F(1,2),F(3,4)]
tt=[F(2,5)]*3
p=[mat(ff[i],ss[i],tt[i]) for i in range(3)]
L=period(p,(0,1,2));R=period(p,(0,2,1))
assert det3(list(zip(ff,ss,tt)))==F(-3,50)
assert tr(L)==F(98,125) and tr(R)==F(211,250)
assert det2(L)==det2(R)==F(-81,500)
assert F(1)-tr(L)+det2(L)==F(27,500)>0
assert F(1)-tr(R)+det2(R)==F(-3,500)<0
print('Viability reversal example: PASS, P123 trace:',tr(L),'P132 trace:',tr(R),'common det:',det2(L))
print('All checks passed.')

# Projective seasonal composition: independent exact-rational replay of the
# nonlinear iteration and its cycle-compressed matrix-power identity.
def mv(a,x): return tuple(sum(a[i][j]*x[j] for j in range(2)) for i in range(2))
def dot(c,x): return sum(c[i]*x[i] for i in range(2))
def vv(x,n): return tuple(a/n for a in x)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def transpose_mv(c,P): return tuple(sum(c[i]*P[i][j] for i in range(2)) for j in range(2))
def season(x,P,c): return vv(mv(P,x),1+dot(c,x))
cs=[(F(1,5),F(1,7)),(F(2,9),F(3,11)),(F(1,3),F(2,5))]
checks=0
for order in ((0,1,2),(0,2,1)):
    mats=[p[i] for i in order]
    cov=[cs[i] for i in order]
    M=period(p,order)
    C=add(add(cov[0],transpose_mv(cov[1],mats[0])),transpose_mv(cov[2],mm(mats[1],mats[0])))
    for xinit in ((F(3,2),F(1,3)),(F(0),F(3)),(F(1),F(0))):
        x=xinit
        power=((F(1),F(0)),(F(0),F(1)))
        geometric=(F(0),F(0))
        for cycle in range(1,8):
            for P,c in zip(mats,cov): x=season(x,P,c)
            geometric=add(geometric,mv(power,xinit))
            power=mm(M,power)
            expected=vv(mv(power,xinit),1+dot(C,geometric))
            assert x==expected
            checks+=1
print('Nonlinear seasonal composition and exact multicycle formula:',checks,'PASS')
print('All checks passed.')
