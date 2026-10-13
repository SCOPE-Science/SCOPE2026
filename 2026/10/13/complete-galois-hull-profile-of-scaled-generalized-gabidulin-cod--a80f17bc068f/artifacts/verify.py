#!/usr/bin/env python3
from math import gcd

def circ(N,t):
    t%=N
    return min(t,N-t)

cases=0
for N in range(2,42,2):
    for s in range(1,N):
        if gcd(s,N)!=1:
            continue
        inv=pow(s,-1,N)
        for k in range(1,N//2+1):
            A=set(range(k))
            for e in range(N):
                t=(e*inv)%N
                forbidden_R={(i-t)%N for i in A}
                forbidden_L={(i+t)%N for i in A}
                BR=set(range(N))-forbidden_R
                BL=set(range(N))-forbidden_L
                start_R=(k-t)%N
                start_L=(k+t)%N
                assert BR=={(start_R+r)%N for r in range(N-k)}
                assert BL=={(start_L+r)%N for r in range(N-k)}
                for i in range(N):
                    right_partners={j for j in range(N) if ((j-i)*s+e)%N==0}
                    left_partners={j for j in range(N) if ((i-j)*s+e)%N==0}
                    assert right_partners=={(i-t)%N}
                    assert left_partners=={(i+t)%N}
                h=min(k,circ(N,t))
                assert len(A&BR)==h and len(A&BL)==h
                if e==0: assert h==0
                if e==N//2: assert t==N//2 and h==k
                cases+=1

# Direct arithmetic check of the F_9/F_3 example from the source.
# Encode a+b*w by a+3*b, with w^2=-1=2 in F_3.
def add(x,y): return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
def mul(x,y):
    a,b=x%3,x//3; c,d=y%3,y//3
    return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)
def fpow(x,n):
    r=1
    while n:
        if n&1: r=mul(r,x)
        x=mul(x,x); n//=2
    return r
def trace(x): return add(x,fpow(x,3))%3
w=3
alpha=[w,add(1,6)]
lam=add(1,w)
for i,a in enumerate(alpha):
    for j,b in enumerate(alpha):
        assert trace(mul(lam,mul(a,b)))==(1 if i==j else 0)
S=[]
for r in range(2):
    z=0
    for a in alpha: z=add(z,mul(a,fpow(a,3**r)))
    S.append(z)
assert S[0]!=0 and S[1]==0
assert min(1,circ(2,0))==0 and min(1,circ(2,1))==1
print(f"VERIFY_OK cases={cases} F9_scaled_basis=ok right_left=ok")
