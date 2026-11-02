"""Rigorous fixed-point integer intervals for the two-step multi-searcher restart cutoff.
All assertions are integer/rational inequalities; tails are bounded analytically.
"""
from fractions import Fraction as F
SCALE=10**32
M=10000
lo=hi=SCALE
# m indexes pair of original discrete times 2m and 2m+1
parts={n:[0,0,0,0] for n in range(5,10)}
for m in range(M):
    for n,z in parts.items():
        z[0]+=2*lo**n
        z[1]+=2*hi**n
        z[2]+=(4*m+1)*lo**n
        z[3]+=(4*m+1)*hi**n
    a=2*m+3;b=2*m+4
    lo=lo*a//b
    hi=(hi*a+b-1)//b

def bounds(n):
    a,b,c,d=parts[n]
    unit=SCALE**n
    # q_m^n <= C*m^{-n/2}, C=3 for n<=7 and 4 for n>=8.
    C=3 if n<=7 else 4
    # Exponent-free, rational, deliberately generous bounds for m>=M:
    # n=5: 2C/(1.5)(M-1)^(-1.5) <= 4/(M-1)*1/100;
    # h <= 5C/.5*(M-1)^(-.5) <=30/99.
    if n==5:
        tailmu=F(4,99*(M-1))
        tailh=F(30,99)
    elif n==6:
        tailmu=F(3,(M-1)**2) # 2*3/(2)=3
        tailh=F(15,M-1) # 5*3/(1)=15
    elif n==7:
        tailmu=F(4,(M-1)**2) # upper bound (M-1)^-2.5
        tailh=F(10,(M-1)) # upper bound (M-1)^-1.5
    elif n==8:
        tailmu=F(4,(M-1)**3)
        tailh=F(10,(M-1)**2)
    else:
        tailmu=F(4,(M-1)**3)
        tailh=F(10,(M-1)**2)
    mu_l=F(a,unit);mu_u=F(b,unit)+tailmu
    h_l=F(c,unit);h_u=F(d,unit)+tailh
    D_l=h_l+mu_u-mu_u**2
    D_u=h_u+mu_l-mu_l**2
    return mu_l,mu_u,h_l,h_u,D_l,D_u
for n in range(5,10):
    ml,mu,hl,hu,dl,du=bounds(n)
    print(n,'mu approx',float((ml+mu)/2),'h approx',float((hl+hu)/2),'D bounds',(float(dl),float(du)))
    if n in (5,6):assert dl>0
    if n in (7,8):assert du<0
assert bounds(9)[3]<2
# Inductive Wallis inequality used to control the tails:
# C_m^2 <= 1/(3m+1), m>=0; from 4(m+1)^2(3m+1)-(2m+1)^2(3m+4)=m.
for m in range(10000):
    assert 4*(m+1)**2*(3*m+1)-(2*m+1)**2*(3*m+4)==m
# q_m <=2/sqrt(3m) for m>=1. When n>=9, h_n<=h_9<2<=mu_n^2-mu_n.
print('PASS: strict small-reset benefit N<=6 and strict small-reset harm N>=7')
