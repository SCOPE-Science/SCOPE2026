from fractions import Fraction as F
from decimal import Decimal, getcontext
from math import sqrt

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def check_matrix(t):
    t2=t*t; t3=t2*t
    M=[[t2,t2-t,t2-t],[-t3+t2,-t3+2*t2,-t3+2*t2-t],[-t3+2*t2-t,-t3+3*t2-2*t,-t3+3*t2-3*t+1]]
    tr=sum(M[i][i] for i in range(3))
    c2=(M[0][0]*M[1][1]-M[0][1]*M[1][0]+M[0][0]*M[2][2]-M[0][2]*M[2][0]+M[1][1]*M[2][2]-M[1][2]*M[2][1])
    A=2*t3-6*t2+3*t-1
    assert -tr==A and c2==t3 and det3(M)==0
for n in range(1,13): check_matrix(F(n,17))

def add(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c
def scale(a,s): return [x*s for x in a]
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c
def sub(a,b): return add(a,scale(b,F(-1)))
def power(a,n):
    c=[F(1)]
    for _ in range(n): c=mul(c,a)
    return c
T=[F(0),F(1)]; A=[F(-1),F(3),F(-6),F(2)]; P=[F(1),F(-4),F(12),F(-16),F(4)]
one_minus_t=[F(1),F(-1)]; t3=power(T,3)
assert sub(mul(A,A),scale(t3,F(4)))==mul(power(one_minus_t,2),P)
D0=[F(1),F(-4),F(2)]; minus_t2=[F(0),F(0),F(-1)]
lhs=add(add(mul(minus_t2,minus_t2),mul(mul(A,minus_t2),D0)),mul(t3,mul(D0,D0)))
rhs=mul(mul(power(T,2),power(one_minus_t,2)),power([F(-1),F(2)],2))
assert lhs==rhs
left=[1,-1,-1,1,-1]; right=[-1,-1,1,1,-1]
def variations(s): return sum(a!=b for a,b in zip(s,s[1:]))
assert variations(left)==3 and variations(right)==2 and variations(left)-variations(right)==1

def Af(x): return 2*x**3-6*x**2+3*x-1
def dA(x): return 6*x*x-12*x+3
def disc(x): return Af(x)**2-4*x**3
def qplus(x): return (-Af(x)+sqrt(disc(x)))/2
def dq(x):
    q=qplus(x); return -(dA(x)*q+3*x*x)/sqrt(disc(x))
assert dq(0.25)<0 and dq(0.55)<0 and abs(qplus(0.5)-0.5)<1e-15

getcontext().prec=70
D=Decimal
def pd(x): return D(4)*x**4-D(16)*x**3+D(12)*x**2-D(4)*x+D(1)
lo,hi=D(0),D(1)
for _ in range(260):
    mid=(lo+hi)/2
    if pd(mid)>0: lo=mid
    else: hi=mid
t=(lo+hi)/2
ratio=t/(D(1)-t); rate=t*t.sqrt()
assert abs(t-D('0.59479552536573240762811017973187120674298829867841')) < D('1e-49')
assert abs(ratio-D('1.4678898250138705587178878253361993763197457026030')) < D('1e-48')
assert abs(rate-D('0.45872408071180430759625059940434272212532682893460')) < D('1e-49')
print('VERIFY_OK')
print('t_star='+str(t))
print('rho_over_a='+str(ratio))
print('spectral_factor='+str(rate))
