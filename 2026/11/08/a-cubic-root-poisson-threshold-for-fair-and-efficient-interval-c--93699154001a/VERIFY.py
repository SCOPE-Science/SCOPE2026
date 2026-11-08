#!/usr/bin/env python3
"""Independent finite checks for the path-approval committee theorem.

For candidates 0,...,m-1, voter i approves candidates i and i+1.
The checks enumerate all committees for m<=10, all EJR voter subsets for
m<=8, and compare a two-bit dynamic program to direct enumeration through m=12.
These finite tests complement, but do not replace, the analytic proof.
"""
from itertools import combinations, product
from math import ceil, comb

def pareto_brute(bits):
    m=len(bits)
    k=sum(bits)
    old=[bits[i]+bits[i+1] for i in range(m-1)]
    for selected in combinations(range(m),k):
        other=[int(i in selected) for i in range(m)]
        welfare=[other[i]+other[i+1] for i in range(m-1)]
        if all(a>=b for a,b in zip(welfare,old)) and any(a>b for a,b in zip(welfare,old)):
            return False
    return True

def jr_brute(bits):
    m=len(bits)
    k=sum(bits)
    if not k: return False
    ballots=[{i,i+1} for i in range(m-1)]
    for candidate in range(m):
        if bits[candidate]: continue
        uncovered=sum(1 for ballot in ballots if candidate in ballot and not any(bits[j] for j in ballot))
        if uncovered*k>=m-1: return False
    return True

def ejr_brute(bits):
    m=len(bits)
    k=sum(bits)
    if not k: return False
    ballots=[{i,i+1} for i in range(m-1)]
    for ell in range(1,k+1):
        for subset in range(1,1<<(m-1)):
            S=[i for i in range(m-1) if subset>>i&1]
            if len(S)*k<ell*(m-1): continue
            shared=set.intersection(*(ballots[i] for i in S))
            if len(shared)<ell: continue
            if not any(sum(bits[j] for j in ballots[i])>=ell for i in S): return False
    return True

def local_conditions(bits):
    m=len(bits)
    k=sum(bits)
    po=not ((bits[0]==1 and bits[1]==0) or (bits[-1]==1 and bits[-2]==0))
    active=(ceil((m-1)/2)<=k<=m-2)
    jr=not any(bits[i:i+3]==(0,0,0) for i in range(m-2)) if active else True
    return po,jr

def dp_count(m,k):
    active=(ceil((m-1)/2)<=k<=m-2)
    states={(0,0,0):1, (0,1,1):1, (1,1,2):1}
    for _ in range(2,m):
        new={}
        for (a,b,ones),count in states.items():
            for c in (0,1):
                if active and a==b==c==0: continue
                key=(b,c,ones+c)
                new[key]=new.get(key,0)+count
        states=new
    return sum(count for (a,b,ones),count in states.items() if ones==k and b<=a)

def main():
    po_cases=jr_cases=ejr_cases=dp_cases=0
    for m in range(3,11):
        for bits in product((0,1),repeat=m):
            if not sum(bits): continue
            po,jr=local_conditions(bits)
            assert po==pareto_brute(bits),(m,bits,"PO")
            assert jr==jr_brute(bits),(m,bits,"JR")
            po_cases+=1
            jr_cases+=1
            if m<=8:
                assert ejr_brute(bits)==jr,(m,bits,"EJR")
                ejr_cases+=1
    for m in range(3,13):
        for k in range(1,m+1):
            actual=sum(1 for bits in product((0,1),repeat=m)
                       if sum(bits)==k and all(local_conditions(bits)))
            assert actual==dp_count(m,k),(m,k,actual,dp_count(m,k))
            dp_cases+=1
    print("PASS Pareto condition, profiles:",po_cases)
    print("PASS JR condition, profiles:",jr_cases)
    print("PASS JR=EJR, profiles:",ejr_cases)
    print("PASS DP exact counts, (m,k) cases:",dp_cases)
    for m,k in [(16,10),(32,22),(64,48),(128,103),(256,216)]:
        print("Exact joint probability",m,k,dp_count(m,k),"/",comb(m,k),
              "=",round(dp_count(m,k)/comb(m,k),8))
if __name__=="__main__":
    main()
