#!/usr/bin/env python3
import json, os
from fractions import Fraction
from math import comb

HERE=os.path.dirname(os.path.abspath(__file__))
CERT=json.load(open(os.path.join(HERE,'inequality_certificate.json'),encoding='utf-8'))

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); c=[Fraction(0) for _ in range(n)]
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)

def neg(a): return [-v for v in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,u in enumerate(a):
      for j,v in enumerate(b): c[i+j]+=u*v
    return trim(c)
def scale(a,s): return trim([v*s for v in a])
def eq(a,b): return trim(a)==trim(b)
def xp(k,coef=1):
    a=[Fraction(0)]*(k+1); a[k]=Fraction(coef); return a

def rf_add(A,B):
    an,ad=A; bn,bd=B
    return (add(mul(an,bd),mul(bn,ad)),mul(ad,bd))
def rf_neg(A): return (neg(A[0]),A[1])
def rf_sub(A,B): return rf_add(A,rf_neg(B))
def rf_mul(A,B): return (mul(A[0],B[0]),mul(A[1],B[1]))
def rf_scale(A,s): return (scale(A[0],Fraction(s)),A[1])
def rf_pow(A,k):
    R=([Fraction(1)],[Fraction(1)])
    for _ in range(k): R=rf_mul(R,A)
    return R

def cycle_factor(L):
    # polynomial in y: coefficient 0 and coefficient L are rational functions in x
    den=sub([Fraction(1)],xp(2*L))
    out=[None]*6
    out[0]=([Fraction(1)],den)
    if L<=5: out[L]=(xp(L),den)
    return out

def yp_mul(A,B):
    C=[None]*6
    for i,a in enumerate(A):
      if a is None: continue
      for j,b in enumerate(B):
        if b is None or i+j>5: continue
        v=rf_mul(a,b)
        C[i+j]=v if C[i+j] is None else rf_add(C[i+j],v)
    return C

def yp_for_cycles(cycles):
    A=[None]*6; A[0]=([Fraction(1)],[Fraction(1)])
    for L in cycles: A=yp_mul(A,cycle_factor(L))
    return A

B=[None]*6
for weight,cycles in [(1,[1,1,1,1,1]),(15,[1,2,2]),(20,[1,1,3]),(24,[5])]:
    Y=yp_for_cycles(cycles)
    for r,v in enumerate(Y):
      if v is None: continue
      v=rf_scale(v,Fraction(weight,60))
      B[r]=v if B[r] is None else rf_add(B[r],v)

one_minus_x=([Fraction(1),Fraction(-1)])
inv1mx_den=one_minus_x
corr1=(xp(1),sub([Fraction(1)],xp(2)))
corr2=([Fraction(1)],sub([Fraction(1)],xp(2)))
H0=(rf_add(B[2],B[3])[0],mul(rf_add(B[2],B[3])[1],inv1mx_den))
T1=rf_sub(rf_add(B[1],B[4]),corr1)
H1=(T1[0],mul(T1[1],inv1mx_den))
T2=rf_sub(rf_add(B[0],B[5]),corr2)
H2=(T2[0],mul(T2[1],inv1mx_den))
D={'D01':rf_sub(H0,H1),'D12':rf_sub(H1,H2)}

# verify certificate reduced rational functions and period identities
period=60; order=6
base=sub([Fraction(1)],xp(period))
period_factor=[Fraction(1)]
for _ in range(order): period_factor=mul(period_factor,base)
for name,A in D.items():
    entry=CERT['differences'][name]
    cn=[Fraction(v) for v in entry['numerator']]
    cd=[Fraction(v) for v in entry['denominator']]
    P=[Fraction(v) for v in entry['period_numerator']]
    # A == cn/cd
    assert eq(mul(A[0],cd),mul(cn,A[1]))
    # P == (cn/cd)*(1-x^60)^6
    assert eq(mul(P,cd),mul(cn,period_factor))

    # residue positivity for coefficients of P/(1-x^60)^6
    for r in range(period):
        terms={}
        for e,p in enumerate(P):
            if p and e%period==r: terms[e//period]=p
        if not terms: continue
        U=max(terms)
        # Polynomial in s for t=s+U: sum p_u * C(s+U-u+5,5).
        poly=[Fraction(0)]
        for u,p in terms.items():
            q=[Fraction(1)]
            a=U-u
            for j in range(1,6): q=mul(q,[Fraction(a+j),Fraction(1)])
            q=scale(q,p/Fraction(120))
            poly=add(poly,q)
        assert len(poly)<=6 and all(c>0 for c in poly)
        # finite pre-shift coefficients
        for t in range(U):
            n=r+period*t
            val=Fraction(0)
            for u,p in terms.items():
                if u<=t: val += p*comb(t-u+5,5)
            if n>=4: assert val>0

# F4 arithmetic: bits a+b*w, w^2=w+1.
def fadd(a,b): return a^b
def fmul(a,b):
    a0=a&1; a1=(a>>1)&1; b0=b&1; b1=(b>>1)&1
    c0=(a0*b0)^(a1*b1)
    c1=(a0*b1)^(a1*b0)^(a1*b1)
    return c0|(c1<<1)
def fsq(a): return fmul(a,a)
def matadd(A,B): return [[fadd(A[i][j],B[i][j]) for j in range(2)] for i in range(2)]
def contrib(v):
    return [[fmul(v[i],fsq(v[j])) for j in range(2)] for i in range(2)]
def rank2(A):
    if all(A[i][j]==0 for i in range(2) for j in range(2)): return 0
    det=fadd(fmul(A[0][0],A[1][1]),fmul(A[0][1],A[1][0]))
    return 2 if det else 1
w=2; w2=fsq(w)
pts=[(1,0),(0,1),(1,1),(1,w),(1,w2)]
Cs=[contrib(v) for v in pts]
Z=[[0,0],[0,0]]
for mask in range(32):
    A=Z
    s=0
    for i in range(5):
        if mask>>i&1:
            A=matadd(A,Cs[i]); s+=1
    expected=0 if s in (0,5) else 1 if s in (1,4) else 2
    assert rank2(A)==expected

# direct Burnside coefficient census and initial counts
N=20
def fixed_counts(cycles):
    a=[[0]*6 for _ in range(N+1)]; a[0][0]=1
    for L in cycles:
        b=[[0]*6 for _ in range(N+1)]
        for n0 in range(N+1):
          for r0 in range(6):
            v=a[n0][r0]
            if not v: continue
            m=0
            while n0+L*m<=N:
                r=r0+(L if m%2 else 0)
                if r<=5:b[n0+L*m][r]+=v
                m+=1
        a=b
    return a
agg=[[0]*6 for _ in range(N+1)]
for weight,cycles in [(1,[1,1,1,1,1]),(15,[1,2,2]),(20,[1,1,3]),(24,[5])]:
    F=fixed_counts(cycles)
    for n in range(N+1):
      for r in range(6):agg[n][r]+=weight*F[n][r]
for n in range(N+1):
  for r in range(6):
    assert agg[n][r]%60==0; agg[n][r]//=60
M0=[agg[n][2]+agg[n][3] for n in range(N+1)]
M1=[agg[n][1]+agg[n][4]-(1 if n%2 else 0) for n in range(N+1)]
M2=[agg[n][0]+agg[n][5]-(1 if n%2==0 else 0) for n in range(N+1)]
I=[[sum(M[:n+1]) for n in range(N+1)] for M in (M0,M1,M2)]
for row in CERT['initial_counts']:
    n=row['n']
    assert (I[0][n],I[1][n],I[2][n])==(row['hull0'],row['hull1'],row['hull2'])
print('VERIFY_OK')
