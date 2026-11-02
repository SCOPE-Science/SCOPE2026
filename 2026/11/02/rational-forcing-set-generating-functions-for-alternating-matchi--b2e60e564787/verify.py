#!/usr/bin/env python3
"""Independent finite checks of alternating-matching temporal forcing formulas."""
from itertools import combinations
from math import ceil


def dynamics(n, T, mask):
    blue = mask
    for t in range(1, T+1):
        old = blue
        for a in range(0 if t & 1 else 1, n-1, 2):
            pair = (1<<a) | (1<<(a+1))
            if old & pair:
                blue |= pair
    return blue == (1<<n)-1


def criterion(n, T, mask):
    B = [j for j in range((n+1)//2) if mask & (3 << (2*j))]
    if not B:
        return False
    p = (T-1)//2
    q = (n-T)//2  # ceil((n-T-1)/2) for integer n,T
    return B[0] <= p and B[-1] >= q and all(b-a <= T for a,b in zip(B,B[1:]))


def predicted_min(n,T):
    if T % 2:
        return (n+2*T-1)//(2*T)
    return (n+2*T)//(2*T)  # ceil((n+1)/(2T))


def polynomial_via_blocks(n,T):
    m=(n+1)//2
    weights=[2]*m
    if n%2: weights[-1]=1
    P=[0]*(n+1)
    for bmask in range(1,1<<m):
        chosen=[j for j in range(m) if bmask>>j & 1]
        if chosen[0]>(T-1)//2 or chosen[-1]<(n-T)//2 or any(b-a>T for a,b in zip(chosen,chosen[1:])):continue
        current=[1]
        for j in chosen:
            nxt=[0]*(len(current)+weights[j])
            for k, v in enumerate(current):
                if weights[j]==1:
                    nxt[k+1]+=v
                else:
                    nxt[k+1]+=2*v
                    nxt[k+2]+=v
            current=nxt
        for k,v in enumerate(current):P[k]+=v
    return P


def multiply(A,B):
    c=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B): c[i+j]+=a*b
    return c


def min_count_formula(n,T):
    m=(n+1)//2; s=predicted_min(n,T)
    p=(T-1)//2
    G=[0]+[1]*T
    V=[1]
    for i in range(s-1):V=multiply(V,G)
    V=multiply([1]*(p+1),V)
    if n%2:
        r=T//2
        W=[1]+[2]*r
        V=multiply(V,W)
        factor=1<<(s-1)
    else:
        V=multiply(V,[1]*(p+1))
        factor=1<<s
    return factor*(V[m-1] if m-1<len(V) else 0)




def addpoly(a,b):
    out=[0]*max(len(a),len(b))
    for j,x in enumerate(a):out[j]+=x
    for j,x in enumerate(b):out[j]+=x
    return out


def mulpoly(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def rational_gf_coefficient(n,T):
    m=n//2; p=(T-1)//2; r=T//2
    w=[0,2,1]; z=[0,1]
    H=[[1]]
    for j in range(1,m+1):
        acc=[0]
        for d in range(1,min(j,T)+1): acc=addpoly(acc,H[j-d])
        H.append(mulpoly(w,acc))
    A=[1]*(p+1)
    if n%2==0:
        # x*w*A(x)^2 / (1-w G_T(x))
        C=multiply(A,A)
        out=[0]
        for a,coeff in enumerate(C):
            j=m-1-a
            if j>=0:out=addpoly(out,mulpoly(w,[x*coeff for x in H[j]]))
    else:
        # A(x)*(z+w*(x+...+x^r))/(1-w G_T(x))
        out=[0]
        for a in range(p+1):
            j=m-a
            if j>=0:out=addpoly(out,mulpoly(z,H[j]))
            for b in range(1,r+1):
                j=m-a-b
                if j>=0:out=addpoly(out,mulpoly(w,H[j]))
    return out+[0]*(n+1-len(out))

def run():
    cases=0; subsets=0
    for n in range(2,15):
        for T in range(1,11):
            P=[0]*(n+1)
            for mask in range(1<<n):
                actual=dynamics(n,T,mask)
                expected=criterion(n,T,mask)
                assert actual==expected,(n,T,mask,actual,expected)
                if actual: P[mask.bit_count()]+=1
                subsets+=1
            Q=polynomial_via_blocks(n,T)
            assert P==Q,(n,T,P,Q)
            R=rational_gf_coefficient(n,T)
            assert P==R,(n,T,P,R)
            minimum=next(i for i,v in enumerate(P) if v)
            assert minimum==predicted_min(n,T),(n,T,minimum,predicted_min(n,T))
            assert P[minimum]==min_count_formula(n,T),(n,T,P[minimum],min_count_formula(n,T))
            cases+=1
    print('DIRECT_SNAPSHOT_VS_INTERVAL_CRITERION_OK',cases,'parameter_cases',subsets,'seed_sets')
    for T in range(1,13):
        n=2*T
        # One source is sufficient iff T odd.
        count=sum(dynamics(n,T,1<<i) for i in range(n))
        assert (count>0)==bool(T%2),(T,count)
    print('HORIZON_PARITY_OBSTRUCTION_OK T=1..12')
    print('VERIFY_OK')

if __name__=='__main__':run()
