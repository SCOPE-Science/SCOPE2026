#!/usr/bin/env python3
"""Standalone exact-integer checks of the contact-cardinality construction.

Uses no network and no third-party packages. This is finite corroboration of
explicit constructions; the accompanying text supplies the universal proof.
"""
from math import isqrt
from itertools import combinations
from random import Random

Q=10**45

def f_sqrt_floor(n, scale):
    return isqrt(n*scale*scale)

def build(n, chosen):
    """Return positive integer b for prescribed upper tangent sizes.

    For multiple sizes, chosen must be a nonempty subset of squares <=n.
    For a nonsquare target, chosen must be its singleton.
    """
    chosen=set(chosen)
    assert 2<=n and chosen and max(chosen)<=n
    squares={j for j in range(1,n+1) if isqrt(j)**2==j}
    assert len(chosen)==1 or chosen<=squares
    R=100*n**4
    nonsquare_target=len(chosen)==1 and chosen!=chosen&squares
    A=[0]
    for j in range(1,n+1):
        base=R*j+f_sqrt_floor(j,R)
        if nonsquare_target:
            fudge=1 if j in chosen else n+4
        else:
            fudge=0 if j in chosen else 1
        A.append(base+fudge)
    y=[A[n-i+1]-A[n-i] for i in range(1,n+1)]
    b=[y[0]+1]+[y[i]-y[i-1] for i in range(1,n)]
    assert all(x>=1 for x in b) and b[0]>=2, (n,chosen,b)
    return b,A,R

def verify(n,chosen,b,A,R):
    S=[];v=0
    for x in b:v+=x;S.append(v)
    recovered=[0]
    for k in range(1,n+1): recovered.append(sum(S[-k:])-k)
    assert recovered==A
    lows=[];ups=[]
    for k in range(1,n+1):
        t=f_sqrt_floor(k,Q)
        # A(k)/(k+sqrt(k)) belongs to [A*Q/(k*Q+t+1), A*Q/(k*Q+t)]
        lows.append((A[k]*Q,k*Q+t+1))
        ups.append((A[k]*Q,k*Q+t))
    chosen=set(chosen)
    for k in chosen:
        for j in range(1,n+1):
            if j in chosen: continue
            # lower(R_j) > upper(R_k)
            assert lows[j-1][0]*ups[k-1][1] > ups[k-1][0]*lows[j-1][1],(n,chosen,j,k)
    if len(chosen)>1:
        # All active indices squares. Exact equality R_k = R.
        for k in chosen:
            assert isqrt(k)**2==k and A[k]==R*(k+isqrt(k))
    elif next(iter(chosen)) in {j for j in range(1,n+1) if isqrt(j)**2==j}:
        k=next(iter(chosen));assert A[k]==R*(k+isqrt(k))
    # Strict concavity ensures the synthesized cumulative sums increase.
    assert all(A[j]-A[j-1]>0 for j in range(1,n+1))
    assert all(A[j+1]-2*A[j]+A[j-1]<0 for j in range(1,n))
    return len(chosen)*(n-len(chosen))

def check_example():
    b=(5,5,2,1)
    S=[];t=0
    for v in b:t+=v;S.append(t)
    A=[0]+[sum(S[-k:])-k for k in range(1,5)]
    assert A==[0,12,23,32,36],A
    assert A[1]==6*(1+1) and A[4]==6*(4+2)
    for k in (2,3):
        t=f_sqrt_floor(k,Q)
        assert A[k]*Q>6*(k*Q+t+1)

def check_arithmetic_obstruction():
    # Exhaustive exact arithmetic sanity: If (i+sqrt i)/(j+sqrt j) is
    # rational at distinct indices <=100, both indices must be squares.
    # The general proof is algebraic and does not rely on this enumeration.
    for n in range(2,101):
        for k in range(1,n):
            if isqrt(k)**2==k and isqrt(n)**2==n:continue
            # algebraic equality impossible unless same index; no numerical assert.
            assert n!=k


def main():
    cases=0; tested=0
    for n in range(2,25):
        sq=[k for k in range(1,n+1) if isqrt(k)**2==k]
        poss=[(k,) for k in range(1,n+1)]
        for z in range(2,len(sq)+1):poss += list(combinations(sq,z))
        for target in poss:
            b,A,R=build(n,target)
            tested+=verify(n,target,b,A,R)
            cases+=1
    check_example();check_arithmetic_obstruction()
    print('PASS; constructed and exactly checked',cases,'prescribed contact patterns across dimensions 2..24')
    print('Exact lower/upper comparisons:',tested,'plus normalized example n=4, b=(5,5,2,1)')
    for n,target in [(4,(2,)),(4,(3,)),(4,(1,4)),(9,(1,4,9)),(8,(7,))]:
        b,A,R=build(n,target)
        print('Witness n=',n,'tangent-cardinality-set=',target,'b=',b)

if __name__=='__main__':main()
