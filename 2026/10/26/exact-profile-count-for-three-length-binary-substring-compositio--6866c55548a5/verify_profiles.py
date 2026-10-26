#!/usr/bin/env python3
"""Exact reproducibility checks for binary substring-composition profiles up to length 3.
Uses only Python standard library. The polynomial identity is exact for every power of z;
finite exhaustive/DP checks are additional independent validation, not its proof.
"""
from itertools import product
from collections import defaultdict

def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return tuple(p) or (0,)
def padd(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)
def pneg(a):return tuple(-v for v in a)
def psub(a,b):return padd(a,pneg(b))
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return trim(c)
def pshift(a,n):
    assert n>=0, (a,n)
    return (0,)*n+tuple(a)
def one_minus(k):
    p=[0]*(k+1);p[0]=1;p[k]=-1
    return tuple(p)

def Fcoef_U(T):
    return (1,-1,1) if T==0 else pshift((1,),T)

def H_common_numerator(A,T,B,U,delta):
    # Coefficient of u**delta in F_(A,T)(u,z) F_(B,U)(u^-1,z).
    # Common denominator: (1-z)^4 (1-z^2)(1-z^3)(1-z^4).
    s=max(B+U,A+T-delta,0)
    J2,J3,J4=one_minus(2),one_minus(3),one_minus(4)
    F0,F1=Fcoef_U(T),Fcoef_U(U)
    terms=[
        pshift(pmul(pmul(F0,F1),pmul(J3,J4)), delta+2*s),
        pneg(pshift(pmul(F0,pmul(J2,J4)), delta-B+1+3*s)),
        pneg(pshift(pmul(F1,pmul(J2,J4)),2*delta-A+1+3*s)),
        pshift(pmul(J2,J3),2*delta-A-B+2+4*s)
    ]
    v=(0,)
    for t in terms:v=padd(v,t)
    return v

J2,J3,J4=(one_minus(i) for i in (2,3,4))
# Enumerate both nonconstant endpoint cases, avoiding double count for the
# central endpoint-status union by inclusion-exclusion.
CASES=[
 (2,0,0,0,1,1), (1,1,0,0,1,1), (0,2,0,0,1,1),
 (0,0,0,2,-1,1), (0,0,1,1,-1,1), (0,0,2,0,-1,1),
 (1,0,0,1,0,1), (0,1,0,1,0,1), (1,0,1,0,0,1),
 (1,1,1,1,0,-1), (0,1,1,0,0,1)
]
N=pmul(pshift((2,),1),pmul(pmul(pmul(one_minus(1),one_minus(1)),one_minus(1)),pmul(J2,pmul(J3,J4))))
for A,T,B,U,d,coef in CASES:
    part=H_common_numerator(A,T,B,U,d)
    N=padd(N,part if coef==1 else pneg(part))
P=(2,-5,6,-4,4,-1,2,-3,2)
TARGET=pmul(pshift(P,1),pmul(J2,J3))
assert N==TARGET, ('polynomial_identity',N,TARGET)
print('EXACT_GF_IDENTITY_OK, numerator degree',len(N)-1)

# Extract series from G = z*P(z)/((1-z)^4*(1-z^4)).
DEN=(1,)
for _ in range(4):DEN=pmul(DEN,one_minus(1))
DEN=pmul(DEN,one_minus(4))
num=pshift(P,1)
counts=[0]*101
for n in range(1,len(counts)):
    counts[n]=(num[n] if n<len(num) else 0)-sum(DEN[j]*counts[n-j] for j in range(1,min(len(DEN)-1,n)+1))
for n in range(2,101):
    c={0:480,1:555,2:456,3:555}[n%4]
    assert counts[n]*96==3*n**4-16*n**3+114*n*n-272*n+c,(n,counts[n])
assert counts[1]==2
print('QUARTIC_QUASIPOLYNOMIAL_IDENTITY_OK, n=2..100')

def direct_profile(word):
    n=len(word)
    return tuple(sum(sum(word[i:i+k])==j for i in range(n-k+1)) for k in range(1,4) for j in range(k+1))

def run_formula(word):
    n=len(word); p=sum(word); Z=n-p
    runs=[]
    for x in word:
        if runs and runs[-1][0]==x:runs[-1]=(x,runs[-1][1]+1)
        else:runs.append((x,1))
    r0=sum(c==0 for c,v in runs);r1=len(runs)-r0
    a0=sum(c==0 and v==1 for c,v in runs)
    a1=sum(c==1 and v==1 for c,v in runs)
    e0=sum(word[j]==0 for j in (0,-1))
    s0=sum(word[j]==0 and runs[t][1]==1 for j,t in ((0,0),(-1,-1)))
    s1=sum(word[j]==1 and runs[t][1]==1 for j,t in ((0,0),(-1,-1)))
    c0=Z-2*r0+a0;c3=p-2*r1+a1
    c1=2*r0-2*a0-e0+s0+a1-s1
    c2=2*r1-2*a1-(2-e0)+s1+a0-s0
    return (Z,p,Z-r0,(n-1)-(Z-r0)-(p-r1),p-r1,c0,c1,c2,c3)

for n in range(3,15):
    obs={direct_profile(w) for w in product((0,1),repeat=n)}
    assert len(obs)==counts[n],(n,len(obs),counts[n])
    for word in product((0,1),repeat=n):
        assert run_formula(word)==direct_profile(word),word
print('DIRECT_EXHAUSTION_AND_RUN_IDENTITIES_OK, n=3..14')

# Independent dynamic programming: append a bit while recording the six
# independent observed counts; deduplication is exact at every step.
D={((b0+b1)<<2)|(int(b0==0 and b1==0)<<10)|(int(b0==1 and b1==1)<<18)|((b0<<1)|b1) for b0,b1 in product(range(2),repeat=2)}
inc=[[0]*2 for _ in range(4)]
for s,b in product(range(4),range(2)):
    x=(s<<1)|b
    inc[s][b]=(b<<2)+(int((s&1)==0 and b==0)<<10)+(int((s&1)==1 and b==1)<<18)+(int(x==0)<<26)+(int(x==7)<<34)+(int(x.bit_count()==1)<<42)
for n in range(3,36):
    T=set()
    for u in D:
        s=u&3; bas=u&~3
        T.add((bas+inc[s][0])|((s<<1)&3))
        T.add((bas+inc[s][1])|(((s<<1)|1)&3))
    D=T
    observed=len({x>>2 for x in D})
    assert observed==counts[n],(n,observed,counts[n])
print('INDEPENDENT_STATE_DP_OK, n=3..35')
print('PROFILE_COUNTS_N1_TO_N16',counts[1:17])
print('VERIFY_OK')
