#!/usr/bin/env python3
"""Exact arithmetic checks for the integer arithmetic partial derivative multiplicity law."""
from fractions import Fraction
from math import comb, gcd, lcm, log

def vp(n,p):
    e=0
    while n%p==0:
        n//=p; e+=1
    return e

def A(v,p):
    return [(a,a//(p**vp(a,p))) for a in range(1,v+2) if a-1+vp(a,p)==v]

def multiplicity(y,p):
    v=vp(y,p); u=y//p**v
    return sum(u%b==0 for a,b in A(v,p))

def conditional_poly(v,p):
    # generating polynomial E[z^{i_p(y)} | v_p(y)=v]
    b=[b for a,b in A(v,p)]
    arr=[Fraction(0)]*(len(b)+1)
    for mask in range(1<<len(b)):
        ss=[b[i] for i in range(len(b)) if mask&(1<<i)]
        prob=Fraction(1,lcm(*ss) if ss else 1)
        d=len(ss)
        for j in range(d+1):
            arr[j]+=prob * (-1)**(d-j)*comb(d,j)
    assert all(x>=0 for x in arr)
    assert sum(arr)==1
    return arr

def law(p,V):
    coeff=[Fraction(0)]*(V+2)
    for v in range(V+1):
        w=Fraction(p-1,p**(v+1))
        c=conditional_poly(v,p)
        for k,x in enumerate(c): coeff[k]+=w*x
    assert sum(coeff)==1-Fraction(1,p**(V+1))
    return coeff

def direct_test(p, Y):
    counts=[0]*(Y+1)
    for x in range(1,p*Y+1):
        e=vp(x,p)
        if e:
            y=(x//p)*e
            if 1<=y<=Y:counts[y]+=1
    for y in range(1,Y+1):
        assert counts[y]==multiplicity(y,p),(p,y,counts[y],multiplicity(y,p))
    return max(counts)

def test_pgf_mod(v,p):
    b=[b for a,b in A(v,p)]
    L=lcm(*b) if b else 1
    if L>200000:return None
    counts=[0]*(len(b)+1)
    for u in range(1,L+1): counts[sum(u%d==0 for d in b)]+=1
    actual=[Fraction(q,L) for q in counts]
    assert actual==conditional_poly(v,p),(v,p,actual,conditional_poly(v,p))
    return L

if __name__=='__main__':
    for p in (2,3,5,7):
        Y=10000
        mx=direct_test(p,Y)
        for v in range(0,16):test_pgf_mod(v,p)
        V=45 if p==2 else 22
        probs=law(p,V)
        print('p=',p, 'brute_count_range=',Y,'brute_max=',mx,'V=',V,'tail<=',float(Fraction(1,p**(V+1))))
        print('  masses_0_to_4=',[round(float(q),12) for q in probs[:5]],'mean_limit=',(p-1)*log(p/(p-1)))
        truncated_moment=sum(k*float(q) for k,q in enumerate(probs))
        print('  mean_truncated=',truncated_moment)
    print('ALL_TESTS_PASSED')
