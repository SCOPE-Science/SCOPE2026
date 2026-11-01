#!/usr/bin/env python3
"""Self-contained exact/integer-interval verification for harmonic sampling on a truncated cube.

All finite-degree positivity tests use outward-rounded integer intervals;
no floating point is used. Runs with Python >=3.9, standard library only.
"""
from math import isqrt
from fractions import Fraction as F

Q=10**220
R=isqrt(2*Q*Q)-Q
assert 0<R<Q and (R+Q)**2 <= 2*Q*Q < (R+Q+1)**2

# Choose representatives with first coordinate positive, in three blocks.
V=[]
for pos in range(3):
    for sy,sz in ((-1,-1),(-1,1),(1,-1),(1,1)):
        t=[(0,1),(0,sy),(0,sz)]
        if pos == 0: t[0]=(1,1)
        elif pos == 1: t[1]=(1,sy)
        else: t[2]=(1,sz)
        V.append(t)
assert len(V)==12

def coefs(i,j):
    """Numerator A*r^2+B*r+C of normalized dot product."""
    a=b=c=0
    for (k,x),(l,y) in zip(V[i],V[j]):
        if k+l==2: a+=x*y
        elif k+l==1: b+=x*y
        else: c+=x*y
    return (a,b,c)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def integer(n):return I(n*Q)
    @staticmethod
    def zero():return I(0)
    def __add__(a,b):return I(a.lo+b.lo,a.hi+b.hi)
    def __sub__(a,b):return I(a.lo-b.hi,a.hi-b.lo)
    def __mul__(a,b):
        z=[x*y for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(z)//Q,-((-max(z))//Q))
    def times(a,n):
        if n>=0:return I(a.lo*n,a.hi*n)
        return I(a.hi*n,a.lo*n)
    def divint(a,n):
        assert n>0
        return I(a.lo//n,-((-a.hi)//n))
    def __truediv__(a,b):
        assert b.lo>0 or b.hi<0
        z=[(x,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        lows=[(Q*x)//y for x,y in z]
        ups=[-((-Q*x)//y) for x,y in z]
        return I(min(lows),max(ups))

def t_interval(coeff):
    a,b,c=coeff
    N=a*R*R+b*R*Q+c*Q*Q
    D=2*Q*Q+R*R
    # For every r>=0 the normalized-point derivative has norm sqrt(2)/(r*r+2);
    # hence |d(dot)/dr|<=2*sqrt(2)/(r*r+2)<=sqrt(2)<2.
    # Both chosen r proxies bracket the exact algebraic r within 1/Q.
    return I(Q*N//D-2,-((-Q*N)//D)+2)

# P_n(t), outward-rounded with no unverified floating-point operation.
def polynomial_values(t, nmax):
    A=[I.integer(1),t]
    for n in range(2,nmax+1):
        A.append((t*A[-1].times(2*n-1)-A[-2].times(n-1)).divint(n))
    return A

keys={(i,j):coefs(i,j) for i in range(12) for j in range(i+1,12)}
ps={k:polynomial_values(t_interval(k),161) for k in set(keys.values())}

def matrix(n):
    m=[[I.integer(1) if i==j else ps[keys[min(i,j),max(i,j)]][n] for j in range(12)] for i in range(12)]
    return m

def verify_pd(m,ids):
    pivots=[]; L=[]
    for i in ids:
        li=[]
        for t,j in enumerate(ids[:len(pivots)]):
            w=m[i][j]
            for z in range(t):
                w=w-li[z]*L[t][z]*pivots[z]
            li.append(w/pivots[t])
        d=m[i][i]
        for z in range(len(pivots)):
            d=d-li[z]*li[z]*pivots[z]
        if d.lo<=0:return False,(i,d.lo,d.hi)
        L.append(li);pivots.append(d)
    return True,min(p.lo for p in pivots)

low_sets={
0:[11],1:[11,4,1],2:[11,6,0,8,7],3:[11,4,1,9,0,7,10],
4:[11,7,3,5,0,10,4,9,2],
5:[11,4,1,7,8,2,10,5,9,6,0]
}
for n,ss in low_sets.items():
    assert len(ss)==2*n+1
    ok,detail=verify_pd(matrix(n),ss)
    assert ok,(n,detail)

for n in range(6,162):
    if n==9:
        ok,detail=verify_pd(matrix(n),[i for i in range(12) if i not in (0,4)])
    else:ok,detail=verify_pd(matrix(n),list(range(12)))
    assert ok,(n,detail)

# Algebraic proof for the two null vectors at n=9 in Q(sqrt(2)).
class A:
    __slots__=('a','b')
    def __init__(self,a,b=0):self.a=F(a);self.b=F(b)
    def __add__(x,y):return A(x.a+y.a,x.b+y.b)
    def __sub__(x,y):return A(x.a-y.a,x.b-y.b)
    def __mul__(x,y):return A(x.a*y.a+2*x.b*y.b,x.a*y.b+x.b*y.a)
    def __truediv__(x,y):
        den=y.a*y.a-2*y.b*y.b
        return A((x.a*y.a-2*x.b*y.b)/den,(x.b*y.a-x.a*y.b)/den)
    def __eq__(x,y):return (x.a,x.b)==(y.a,y.b)
    def __repr__(x):return f'({x.a})+({x.b})sqrt2'

def P9(a,b,c):
    r=A(-1,1)
    t=(A(a)*r*r+A(b)*r+A(c))/(A(2)+r*r)
    u,v=A(1),t
    for n in range(2,10):u,v=v, (A(2*n-1)*t*v-A(n-1)*u)/A(n)
    return v

K={k:P9(*k) for k in set(keys.values())}
def getK(i,j):return A(1) if i==j else K[keys[min(i,j),max(i,j)]]
W=[]
for pos in range(3):
    W.append([V[i][1][1]*V[i][2][1] if i//4==pos else 0 for i in range(12)])
for i in range(12):
    for j in (0,1):
        acc=A(0)
        for u in range(12):acc=acc+getK(i,u)*A(W[j][u]-W[j+1][u])
        assert acc==A(0),(i,j,acc)

# A parameter-uniform, exact polynomial identity for the degree-nine
# coordinate-position contrast. The degree-nine Legendre numerator is
# (12155*N^9 -25740*N^7*D^2 +18018*N^5*D^4 -4620*N^3*D^6
#  +315*N*D^8)/(128*D^9), N=a*r^2+b*r+c, D=r^2+2.
def padd(x,y):
    z=[0]*max(len(x),len(y))
    for i,v in enumerate(x):z[i]+=v
    for i,v in enumerate(y):z[i]+=v
    return z
def pmul(x,y):
    z=[0]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    return z
def ppow(x,n):
    y=[1]
    for _ in range(n):y=pmul(y,x)
    return y
def pscale(x,s):return [s*v for v in x]
def numerator9(co):
    a,b,c=co
    N=[c,b,a]; D=[2,0,1]
    Z=[0]
    for power,cf in ((9,12155),(7,-25740),(5,18018),(3,-4620),(1,315)):
        Z=padd(Z,pscale(pmul(ppow(N,power),ppow(D,9-power)),cf))
    return Z
H={key:numerator9(key) for key in set(keys.values())}
def sumblock(i,j):
    S=[0]
    for a in range(4):
        for b in range(4):
            u=4*i+a;v=4*j+b
            weight=W[i][u]*W[j][v]
            h=[128]*1 if u==v else H[keys[min(u,v),max(u,v)]]
            if u==v: h=pscale(ppow([2,0,1],9),128)
            S=padd(S,pscale(h,weight))
    return S
# Subtract normalized 3-by-3 compressed diagonal/off-diagonal entries;
# since the compression divides by 4, the numerator difference is S/512.
S=padd(sumblock(0,0),pscale(sumblock(0,1),-1))
for i in range(3):
    for j in range(3):
        assert sumblock(i,j)==sumblock(0,0) if i==j else sumblock(i,j)==sumblock(0,1)
factors=pmul(ppow([0,1],2),pmul(ppow([-1,0,1],2),
        pmul(ppow([-1,-2,1],2),ppow([-1,2,1],2))))
assert S[:len(factors)]==pscale(factors,128*19305) and not any(S[len(factors):])

# The other Archimedean ratio r=1+sqrt(2) has the same two
# algebraically forced null directions, and has rank exactly ten.
R_small=R
R=isqrt(2*Q*Q)+Q
ps_big={k:polynomial_values(t_interval(k),9) for k in set(keys.values())}
ps_saved=ps
ps=ps_big
ok,detail=verify_pd(matrix(9),[i for i in range(12) if i not in (0,4)])
assert ok,detail
ps=ps_saved
R=R_small

# Bernstein's uniform bound: |P_n(t)| <= sqrt(2/(pi*(n+1/2)*sqrt(1-t^2))).
# |t|<sqrt(3)/2 => sqrt(1-t^2)>1/2; pi>3.
# For n>=162, row sum <= 11 sqrt(4/(3(n+1/2)))<1.
assert 11**2*4 < 3*(2*162+1)//2
for key in set(keys.values()):
    if key==coefs(0,0):continue
    t=t_interval(key)
    assert 4*max(t.lo*t.lo,t.hi*t.hi) < 3*Q*Q,(key,t.lo,t.hi)
print('TRUNCATED_CUBE_HARMONIC_INTERVAL_CERTIFICATE_OK 0..5=1,3,5,7,9,11; 9=10; other_ge6=12; tail_ge162; exact_cubic_orbit_resonances')
