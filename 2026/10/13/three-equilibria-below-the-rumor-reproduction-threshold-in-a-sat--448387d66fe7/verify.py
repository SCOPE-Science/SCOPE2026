"""Exact rational checks for a subthreshold multiplicity example.
Run with Python >=3.10: python verify.py. No third-party packages.
The general argument is given in RESULT.md; this file checks its finite algebra.
"""
from fractions import Fraction as F
from itertools import permutations

# Dense polynomials in z, coefficient order ascending.
def add(a,b):
    return trim([ (a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b))) ])
def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def R(n,d=[F(1)]): return (n,d)
def r_add(a,b): return R(add(mul(a[0],b[1]),mul(b[0],a[1])),mul(a[1],b[1]))
def r_neg(a): return R(neg(a[0]),a[1])
def r_sub(a,b): return r_add(a,r_neg(b))
def r_mul(a,b): return R(mul(a[0],b[0]),mul(a[1],b[1]))
def r_div(a,b): return R(mul(a[0],b[1]),mul(a[1],b[0]))
def const(x): return R([F(x)])
def r_scale(a,x): return r_mul(a,const(x))
def r_same(a,b): return all(x==0 for x in sub(mul(a[0],b[1]),mul(b[0],a[1])))
def val(p,z): return sum(x*z**i for i,x in enumerate(p))

z=R([F(0),F(1)])
S=r_div(r_mul(z,R([F(9),F(4)])),R([F(2),F(2)]))
T1=r_div(r_scale(S,10),r_add(const(1),S))
T2=r_div(r_scale(z,F(5,2)),r_add(const(1),z))
D=r_add(T1,T2)
L=r_add(r_add(r_scale(S,F(1577,4000)),r_scale(z,F(1,1000))),r_scale(D,F(1,1000)))
H=r_sub(r_sub(r_div(r_scale(L,28),r_add(const(1),L)),r_scale(S,3)),T1)
Q=[F(-477856),F(-2085860),F(3804560),F(10628853),F(8092284),F(2586288),F(303168)]
den=mul(mul([F(2),F(2)],[F(2),F(11),F(4)]),[F(16000),F(133162),F(290103),F(158680),F(25264)])
claimed=R(neg(mul(mul([F(0),F(1)],[F(-1),F(4)]),Q)),den)
assert r_same(H,claimed), 'equilibrium elimination identity does not hold'
assert val(Q,F(1,4))==-561250
assert val(Q,F(1,2))==F(10802295,8)
assert [x>0 for x in Q[::-1]]==[True,True,True,True,True,False,False]

params={'b':F(28),'d':F(1),'h1':F(1),'h2':F(1),'h3':F(1),
 'k1':F(1),'k2':F(1),'r1':F(1),'r2':F(1),
 'sigma1':F(10),'sigma2':F(5,2),
 'alpha1':F(1577,4000),'alpha2':F(1,1000),'alpha3':F(1,1000)}
p=params
eta1=p['d']+p['h1']+p['h2']+p['sigma1']/p['k1']
eta2=p['d']+p['h3']+p['sigma2']/p['k2']
R0=(p['b']/p['d'])/eta1*(p['alpha1']+p['alpha2']*p['h2']/eta2+
    (p['alpha3']/p['d'])*(p['sigma1']/p['k1']+p['sigma2']*p['h2']/(p['k2']*eta2)))
assert R0==F(102067,117000) and R0<1

def dynamics(v):
    U,S,C,D=v
    LL=p['alpha1']*S+p['alpha2']*C+p['alpha3']*D
    t1=p['sigma1']*S/(p['k1']+p['r1']*S)
    t2=p['sigma2']*C/(p['k2']+p['r2']*C)
    return (p['b']-(p['d']+LL)*U,
            LL*U-(p['d']+p['h1']+p['h2'])*S-t1,
            p['h2']*S-(p['d']+p['h3'])*C-t2,
            t1+t2-p['d']*D)

e1=(F(20),F(1),F(1,4),F(11,2));e0=(F(28),F(0),F(0),F(0))
assert all(x>0 for x in e1)
assert sum(e1)<p['b']/p['d']
assert dynamics(e1)==(0,0,0,0) and dynamics(e0)==(0,0,0,0)

def jac(v):
    U,S,C,D=v
    LL=p['alpha1']*S+p['alpha2']*C+p['alpha3']*D
    t1p=p['sigma1']*p['k1']/(p['k1']+p['r1']*S)**2
    t2p=p['sigma2']*p['k2']/(p['k2']+p['r2']*C)**2
    return [ [-p['d']-LL,-p['alpha1']*U,-p['alpha2']*U,-p['alpha3']*U],
             [LL,p['alpha1']*U-(p['d']+p['h1']+p['h2'])-t1p,p['alpha2']*U,p['alpha3']*U],
             [F(0),p['h2'],-(p['d']+p['h3'])-t2p,F(0)],
             [F(0),t1p,t2p,-p['d']] ]

def det(M):
    n=len(M);out=F(0)
    for q in permutations(range(n)):
        crossings=sum(q[i]>q[j] for i in range(n) for j in range(i+1,n))
        term=F(-1 if crossings%2 else 1)
        for i in range(n): term*=M[i][q[i]]
        out+=term
    return out

def char_value(M,l):
    return det([[F(l if i==j else 0)-M[i][j] for j in range(4)] for i in range(4)])

def cp0(l): return (l+1)*(2000*l**3+14922*l*l+29955*l+14933)/2000
def cp1(l): return (l+1)*(1000*l**3+2615*l*l-3801*l-898)/1000
for t in range(5):
    assert char_value(jac(e0),F(t))==cp0(F(t))
    assert char_value(jac(e1),F(t))==cp1(F(t))
assert 14922*29955>2000*14933
assert cp1(0)!=0 and cp1(F(2))>0 and cp1(F(0))<0
print('VERIFY_OK')
