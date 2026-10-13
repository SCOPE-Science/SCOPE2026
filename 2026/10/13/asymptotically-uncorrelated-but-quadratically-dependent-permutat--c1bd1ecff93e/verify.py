#!/usr/bin/env python3
"""Exact finite checks and analytic integral certificates for permutation writhe/inversion dependence.
Requires only Python 3 standard library. Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

def w_inv(p):
    m=len(p)
    n=(m-1)//2
    w=0
    inv=0
    for i in range(m):
        for j in range(i+1,m):
            rise=1 if p[j]>p[i] else -1
            w+=(1 if j-i<=n else -1)*rise
            inv+=(rise==-1)
    return w, inv

def finite_case(m):
    n=(m-1)//2
    sw=sw2=sj=sj2=swj=sw2j2=sw4=0
    ct=0
    for p in permutations(range(m)):
        w,inv=w_inv(p)
        j=4*inv-m*(m-1)
        sw+=w; sw2+=w*w; sj+=j; sj2+=j*j
        swj+=w*j; sw2j2+=w*w*j*j; sw4+=w**4
        ct+=1
    assert ct==factorial(m)
    assert sw==sj==0
    assert F(sw2,ct)==F(m*(m-1),6)
    assert F(sj2,16*ct)==F(m*(m-1)*(2*m+5),72)
    assert F(swj,4*ct)==-F(n*n,6)
    covsq=(F(sw2j2,ct)-F(sw2,ct)*F(sj2,ct))/F(16*m**5)
    known={3:F(0),5:F(19,28125),7:F(131,151263),9:F(2486,2657205)}
    assert covsq==known[m],(m,covsq,known[m])
    # Independent tournament-matrix row balances and a finite Riemann proxy.
    b=[2*i-m+1 for i in range(m)]  # 2*(i+1)-m-1
    A=lambda i,j: (0 if i==j else (1 if (j-i)%m<=n else -1))
    assert all(sum(A(i,j) for j in range(m))==0 for i in range(m))
    Ab=[sum(A(i,j)*b[j] for j in range(m)) for i in range(m)]
    print(f'm={m}: {ct} permutations; cov(W,I)={-F(n*n,6)}; normalized square covariance={covsq}; matrix proxy={F(sum(x*x for x in Ab),m**5)}')

def polyadd(a,b):
    return [((a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))) for i in range(max(len(a),len(b)))]
def polymul(a,b):
    o=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return o
def integrate(poly,lo,hi):
    return sum(v*(hi**(i+1)-lo**(i+1))/F(i+1) for i,v in enumerate(poly))

def integral_checks():
    # Integral of square of h-contraction H(v)(u)=2u(1-u)-1/3.
    h1=[F(-1,3),F(2),F(-2)]
    c1=integrate(polymul(h1,h1),F(0),F(1))
    assert c1==F(1,45)
    # A applied to 2t-1 is the exact triangular function on two half intervals.
    Rleft=[F(-1,2),F(2)]
    Rright=[F(3,2),F(-2)]
    c2=integrate(polymul(Rleft,Rleft),F(0),F(1,2)) + integrate(polymul(Rright,Rright),F(1,2),F(1))
    assert c2==F(1,12)
    assert F(1,2)*c1*c2==F(1,1080)
    print('kernel contractions:',c1,c2,'limit',F(1,1080))

if __name__=='__main__':
    integral_checks()
    for m in (3,5,7,9):finite_case(m)
    print('VERIFY_OK')
