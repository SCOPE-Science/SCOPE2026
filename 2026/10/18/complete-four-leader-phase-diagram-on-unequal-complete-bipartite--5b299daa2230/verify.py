"""Exact-rational checks for four equal-gain leaders on K_{2,m}.

Run with Python 3: python verify.py. No third-party packages required.
The infinite size classification is established by the sign arguments in RESULT.md;
the finite checks here independently test its algebra and normalization.
"""
from fractions import Fraction as Q
from itertools import combinations

def target(m, k, i):
    j = 4-i
    A = Q(2-i, m) + Q(i, m+k)
    B = Q(m-j, 2) + Q(j, 2+k)
    A2 = Q(2-i, m*m) + Q(i, (m+k)**2)
    B2 = Q(m-j, 4) + Q(j, (2+k)**2)
    return A+B+(B*A2+A*B2)/(1-A*B)

def inverse_trace(H):
    n=len(H)
    M=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(H)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c]!=0)
        M[p],M[c]=M[c],M[p]
        r=M[c][c]
        M[c]=[x/r for x in M[c]]
        for i in range(n):
            if i != c and M[i][c]:
                r=M[i][c]
                M[i]=[x-r*y for x,y in zip(M[i],M[c])]
    return sum((M[i][n+i] for i in range(n)),Q(0))

def direct(m,k,i):
    n=m+2
    H=[[Q(0) for _ in range(n)] for _ in range(n)]
    for u in range(2):
        for v in range(2,n):
            H[u][u]+=1;H[v][v]+=1;H[u][v]-=1;H[v][u]-=1
    for u in list(range(i))+list(range(2,2+4-i)):
        H[u][u]+=k
    return inverse_trace(H)

def P20(m,k):
    return ((-m*m+10*m-8)*k**3 +(-m**3+6*m*m+48*m-48)*k*k
            +(-4*m**3+44*m*m+24*m-64)*k-4*m**3+24*m*m)

def P01(m,k):
    return ((m**3-7*m*m-14*m+24)*k*k
            +(4*m**3-52*m*m-8*m+48)*k
            +4*m**3-28*m*m-8*m)

def P21(m,k):
    return (2*k**4+(-m*m+13*m-2)*k**3
            +(-m**3+5*m*m+60*m-68)*k*k
            +(-4*m**3+36*m*m+28*m-88)*k
            -4*m**3+20*m*m-8*m)

def winner(m,k):
    values=[target(m,k,i) for i in range(3)]
    best=min(values)
    return tuple(i for i,v in enumerate(values) if v==best)

count=0
for m in range(4,16):
    for k in [Q(1,30), Q(1,4), Q(1,2), Q(1), Q(2), Q(5), Q(10), Q(25)]:
        F=[target(m,k,i) for i in range(3)]
        assert (F[2]-F[0])*8*m*(k+2)*(k+4)*(k+m)==P20(m,k)
        assert (F[0]-F[1])*8*m*(k+2)*(k*m+3*k+8*m)==P01(m,k)
        assert (F[2]-F[1])*2*(k+2)*(k+4)*(k+m)*(k*m+3*k+8*m)==P21(m,k)
        for i in range(3):
            if m<=12 and k in (Q(1,4),Q(2),Q(10)):
                assert direct(m,k,i)==F[i], (m,k,i)
                count+=1

# Rational brackets used for exact root placement arguments.
assert P20(7,Q(1,5))<0<P20(7,Q(1,4))
assert P20(8,Q(1,2))<0<P20(8,Q(3,5))
assert P20(9,Q(1))<0<P20(9,Q(11,10))
assert P20(10,Q(13,5))<0<P20(10,Q(27,10))
assert P20(10,Q(93,10))>0>P20(10,Q(19,2))
assert P01(8,Q(1,10))>0>P01(8,Q(1,5))
assert P01(9,Q(2,5))>0>P01(9,Q(1,2))
assert P01(9,Q(21))<0<P01(9,Q(22))
assert P01(10,Q(1))>0>P01(10,Q(11,10))
assert P01(10,Q(11,2))<0<P01(10,Q(57,10))
assert P21(8,Q(1))<0<P21(8,Q(6,5))
assert P21(9,Q(2))<0<P21(9,Q(9,4))
assert P21(10,Q(4))<0<P21(10,Q(41,10))

# Test each asserted phase with sample rational gains on both sides.
for m,points in {
    4:[(Q(1,100),(0,)),(Q(100),(0,))],
    5:[(Q(1,100),(0,)),(Q(100),(0,))],
    6:[(Q(1,100),(0,)),(Q(100),(0,))],
    7:[(Q(1,10),(2,)),(Q(1),(0,))],
    8:[(Q(1,10),(2,)),(Q(1),(0,))],
    9:[(Q(1,2),(2,)),(Q(2),(0,)),(Q(30),(1,))],
    10:[(Q(2),(2,)),(Q(4),(0,)),(Q(10),(1,))],
    11:[(Q(1),(2,)),(Q(20),(1,))],
    12:[(Q(1),(2,)),(Q(30),(1,))],
}.items():
    for k,expect in points:
        assert winner(m,k)==expect,(m,k,winner(m,k),expect)

for m in range(11,120):
    a=m**3-7*m*m-14*m+24
    b=4*m**3-52*m*m-8*m+48
    c=4*m**3-28*m*m-8*m
    assert a>0 and c>0
    if b<0: assert b*b<4*a*c
    p3=-m*m+13*m-2
    p2=-m**3+5*m*m+60*m-68
    p1=-4*m**3+36*m*m+28*m-88
    p0=-4*m**3+20*m*m-8*m
    assert p2<0 and p1<0 and p0<0
    assert (p3>0)==(m<13)
print('VERIFY_OK exact_inverse_traces=%d rational_phase_and_difference_checks=passed' % count)
