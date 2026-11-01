"""Reproduce the exact majority first-entry census on clique-plus-leaf graphs."""
from math import comb

def transition(r, state):
    k, hub, leaf = state
    total = k + hub
    old_one = int(2 * (total - 1) >= r)
    old_zero = int(2 * total > r)
    k_next = k * old_one + (r-k) * old_zero
    score = 2 * (k+leaf) - (r+1)
    hub_next = 1 if score > 0 else (0 if score < 0 else hub)
    return (k_next,hub_next,hub)

def actual(r, s):
    encountered={}
    state=s
    for t in range(10):
        if state in encountered:
            first=encountered[state]
            return first,t-first
        encountered[state]=t
        state=transition(r,state)
    raise AssertionError((r,s))

def expected(r,k,h,l):
    if h:
        return expected(r,r-k,0,1-l)
    if r%2==0:
        j=r//2
        if k==0 and l==0: return (0,1)
        if k<j or (k==j and l==0): return (1,1)
        if k==j and l==1: return (3,1)
        return (2,1)
    j=(r-1)//2
    if k==0 and l==0: return (0,1)
    if k<=j: return (1,1)
    if k==j+1 and l==1: return (0,2)
    return (2,1)

def predicted_census(r):
    mid=comb(r,r//2)
    if r%2==0:
        return {(0,1):2,(1,1):2**(r+1)-2,(2,1):2**(r+1)-2*mid,(3,1):2*mid}
    return {(0,1):2,(0,2):2*mid,(1,1):2**(r+1)-2,(2,1):2**(r+1)-2*mid}

cases=0
for r in range(2,257):
    obs={}
    for k in range(r+1):
        for h in range(2):
            for l in range(2):
                s=(k,h,l)
                e=expected(r,k,h,l)
                a=actual(r,s)
                assert a==e,(r,s,a,e)
                obs[a]=obs.get(a,0)+comb(r,k)
                cases+=1
    assert obs==predicted_census(r),(r,obs,predicted_census(r))
    assert sum(obs.values())==2**(r+2)
print(f"REDUCED_OK r_range=2..256 tested_triples={cases} symbolic_class_and_binomial_census_agree")
for r in range(2,9):
    print(f"r={r}: {predicted_census(r)}")
