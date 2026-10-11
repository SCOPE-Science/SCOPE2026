"""Self-contained exact-rational interval sign certificate for a Gabor frame obstruction.
No third-party packages or floating-point correctness assumptions.
"""
from fractions import Fraction as Q
from math import factorial

S=10**32

def bounds(v):
    return (v.numerator*S//v.denominator, -((-v.numerator*S)//v.denominator))

def I(a,b=None):
    if b is None:b=a
    return bounds(Q(a)) if b==a else (Q(a).numerator*S//Q(a).denominator,-((-Q(b).numerator*S)//Q(b).denominator))

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    pp=[u*v for u in x for v in y]
    return (min(pp)//S,-((-max(pp))//S))
def div(x,y):
    assert y[0]>0
    f=[Q(u,v) for u in x for v in y]
    return (min(z.numerator*S//z.denominator for z in f), max(-((-z.numerator*S)//z.denominator) for z in f))
def q(x):return bounds(Q(x))

def atan_n(y,n):return sum((Q(-1 if k%2 else 1,2*k+1)*y**(2*k+1) for k in range(n)), Q(0))
# Each even truncation underestimates arctan(y), the following odd truncation overestimates it.
aL,aU=atan_n(Q(1,5),32),atan_n(Q(1,5),33)
bL,bU=atan_n(Q(1,239),32),atan_n(Q(1,239),33)
piL,piU=16*aL-4*bU,16*aU-4*bL
assert Q(3141592653589793238462,10**21)<piL and piU<Q(3141592653589793238464,10**21)
pmid=(piL+piU)/2
pErr=(piU-piL)/2
P=I(piL,piU)

def e_minus(z):
    # 50 terms: ends negative (k=49); 51 terms: ends positive (k=50).
    lower=sum(((-z)**k/Q(factorial(k)) for k in range(50)),Q(0))
    upper=lower+z**50/Q(factorial(50))
    err=pErr*Q(z)/pmid   # argument z=pmid*positive rational, derivative |(e^-x)'|<=1
    return I(lower-err,upper+err)

def cosine(z):
    # 35 terms through k=34, positive; 36 terms ends negative and is lower.
    approx=sum(((-1)**k*z**(2*k)/Q(factorial(2*k)) for k in range(35)),Q(0))
    rem=z**70/Q(factorial(70))
    err=pErr*Q(z)/pmid   # derivative |sin|<=1
    return I(approx-rem-err,approx+rem+err)

cs={k:cosine(pmid*k/10) for k in range(11)}
cs[0]=q(1);cs[10]=q(-1)


def value_h(k,beta):
    result=q(0)
    for a,c in [(1,Q(-1,12)),(2,Q(1,3)),(3,Q(-1,4))]:
        t=e_minus(pmid*a*beta/2)
        numerator=sub(q(1),mul(t,t))
        denominator=sub(add(q(1),mul(t,t)),mul(q(2),mul(t,cs[k])))
        assert denominator[0]>0,(k,beta,denominator)
        result=add(result,mul(q(c/Q(a)),div(numerator,denominator)))
    return mul(mul(P,q(beta/4)),result)

def determinant(beta):
    h={k:value_h(k,beta) for k in range(11)}
    twice=lambda x:mul(q(2),x)
    B=[
      [h[0],twice(h[4]),twice(h[8])],
      [h[10],twice(h[6]),twice(h[2])],
      [twice(h[5]),twice(add(h[1],h[9])),twice(add(h[3],h[7]))]
    ]
    X=B
    return add(sub(mul(X[0][0],sub(mul(X[1][1],X[2][2]),mul(X[1][2],X[2][1]))),
                   mul(X[0][1],sub(mul(X[1][0],X[2][2]),mul(X[1][2],X[2][0])))),
               mul(X[0][2],sub(mul(X[1][0],X[2][1]),mul(X[1][1],X[2][0]))))

def asdec(k): return '%.19g'%(k/S)
if __name__=='__main__':
    for beta in [Q(3,20), Q(7,20)]:
        lo,hi=determinant(beta)
        print('beta=',beta,'det lower=',asdec(lo),'upper=',asdec(hi), 'SIGN=', 'POSITIVE' if lo>0 else 'NEGATIVE' if hi<0 else 'UNCERTIFIED')
    assert determinant(Q(3,20))[0] > q(Q(21035,10**10))[1]
    assert determinant(Q(3,20))[1] < q(Q(21036,10**10))[0]
    assert determinant(Q(7,20))[0] > q(Q(-56824,10**10))[1]
    assert determinant(Q(7,20))[1] < q(Q(-56823,10**10))[0]
    print('CERTIFIED: determinant changes sign, hence a rank-deficient 4x5 fiber exists')
