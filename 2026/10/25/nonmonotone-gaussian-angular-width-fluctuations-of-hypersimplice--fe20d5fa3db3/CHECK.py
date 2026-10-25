from fractions import Fraction as F
from math import factorial, isqrt

def Iadd(a,b): return a[0]+b[0],a[1]+b[1]
def Ineg(a): return -a[1],-a[0]
def Isub(a,b): return Iadd(a,Ineg(b))
def Imul(a,b):
    s=[x*y for x in a for y in b]
    return min(s),max(s)
def Ic(v): return F(v),F(v)
def Iscale(a,v): return Imul(a,Ic(v))
def Isquare(a):
    if a[0]<=0<=a[1]: return F(0), max(a[0]**2,a[1]**2)
    return min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2)

def atan_sum(x,n):
    return sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n+1)),F(0))
a5=(atan_sum(F(1,5),61),atan_sum(F(1,5),60))
a239=(atan_sum(F(1,239),61),atan_sum(F(1,239),60))
pi_interval=Isub(Iscale(a5,16),Iscale(a239,4))
q=(F(1,2*pi_interval[1]),F(1,2*pi_interval[0]))
S=10**36
floor=lambda r:isqrt((r.numerator*S*S)//r.denominator)
c=(F(floor(q[0]),S),F(floor(q[1])+1,S))

def exp_neg(t,n=70):
    return sum(((-t)**j/F(factorial(j)) for j in range(n+1)),F(0))
def int_exp(z,n=70):
    return sum(((-1)**j*z**(2*j+1)/F((2*j+1)*2**j*factorial(j)) for j in range(n+1)),F(0))
def Vinterval(z):
    t=z*z/2
    ep=(exp_neg(t,71),exp_neg(t,70))
    integral=(int_exp(z,71),int_exp(z,70))
    phi=Imul(c,ep)
    a=Isub(Ic(F(1,2)),Imul(c,integral))
    m=Isub(phi,Iscale(a,z))
    B=Isub(Iscale(a,1+z*z),Iscale(phi,z))
    v=Isub(Isub(Iscale(B,2),Iscale(Isquare(m),4)),Iscale(Isquare(phi),2))
    return v

def decimal_bounds(v,digits=15):
    base=10**digits
    return ((v[0].numerator*base)//v[0].denominator,
            -( (-v[1].numerator*base)//v[1].denominator))
if __name__=='__main__':
    print('pi bracket width',float(pi_interval[1]-pi_interval[0]))
    for z in [F(0), F(1,2), F(1), F(3,2),F(2)]:
        v=Vinterval(z)
        print('z',z,'bound',float(v[0]),float(v[1]),'scaled15', decimal_bounds(v))
    vv={z:Vinterval(z) for z in [F(0),F(1,2),F(1),F(3,2),F(2)]}
    assert vv[F(1)][1]<vv[F(3,2)][0]
    assert vv[F(2)][1]<vv[F(3,2)][0]
    assert vv[F(1,2)][0]>vv[F(1)][1]
    print('CERTIFIED_VARIANCE_NONMONOTONE')

    # Exact support comparison for the hypersimplex; no probabilistic approximation.
    from itertools import combinations
    for n in range(4,9):
        v=[F((i*i+7*i+3)%17-8, 5) for i in range(n)]
        for k in range(1,n//2+1):
            objective=[sum(v[i] for i in S) for S in combinations(range(n),k)]
            sorted_v=sorted(v)
            direct=max(objective)-min(objective)
            order=sum(sorted_v[-k:])-sum(sorted_v[:k])
            assert direct==order
    print('CERTIFIED_FINITE_SUPPORT_IDENTITY')
