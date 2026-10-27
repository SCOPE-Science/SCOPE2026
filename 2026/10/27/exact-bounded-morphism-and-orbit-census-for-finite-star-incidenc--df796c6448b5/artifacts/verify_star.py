#!/usr/bin/env python3
"""Independent exhaustive checks for bounded morphisms of finite star frames.
Only small finite instances are tested; the all-parameter theorem has a separate proof.
"""
from itertools import product
from math import comb
from collections import defaultdict


def frame(n):
    size=2*n+1
    edge=lambda i: n+1+i
    R=[[a==b for b in range(size)] for a in range(size)]
    for i in range(n):
        R[0][edge(i)]=True
        R[i+1][edge(i)]=True
    upper=[tuple(j for j in range(size) if R[i][j]) for i in range(size)]
    return R,upper


def direct_count(r,s):
    R,U=frame(r);T,V=frame(s)
    count=0
    for f in product(range(2*s+1),repeat=2*r+1):
        if len(set(f))!=2*s+1: continue
        if any(not T[f[i]][f[j]] for i in range(2*r+1) for j in U[i]):continue
        if any(not all(any(f[j]==y for j in U[i]) for y in V[f[i]]) for i in range(2*r+1)):continue
        count+=1
    return count


def closed_count(r,s):
    return sum((-1)**k*comb(s,k)*(2*s-k)**r for k in range(s+1))


def finite_pattern_counts(r,s):
    valid=0;orbits=set()
    for w in product(range(2*s),repeat=r):
        l=[0]*s;m=[0]*s
        for v in w:
            if v<s:l[v]+=1
            else:m[v-s]+=1
        if min(l)==0:continue
        valid+=1
        orbits.add(tuple(sorted(zip(l,m))))
    return valid,len(orbits)


def predicted_orbits(r,s):
    # coefficient [u^s z^r] product_{n>=1}(1-u*z^n)^(-n)
    dp={(0,0):1}
    for n in range(1,r+1):
        nxt=defaultdict(int)
        for (k,a),v in dp.items():
            for b in range(0,min(s-k,(r-a)//n)+1):
                nxt[k+b,a+b*n]+=v*comb(n+b-1,b)
        dp=dict(nxt)
    return dp.get((s,r),0)


def main():
    dc=0
    for r in range(2,4):
        for s in range(2,r+1):
            expected=closed_count(r,s)
            found=direct_count(r,s)
            assert found==expected,(r,s,found,expected)
            print(f'DIRECT r={r} s={s} exact={found}')
            dc+=1
    pattern_checks=0
    for r in range(2,7):
        for s in range(2,min(4,r)+1):
            got_n,got_o=finite_pattern_counts(r,s)
            pred_n=closed_count(r,s);pred_o=predicted_orbits(r,s)
            assert got_n==pred_n and got_o==pred_o,(r,s,got_n,pred_n,got_o,pred_o)
            print(f'PATTERN r={r} s={s} maps={got_n} orbits={got_o}')
            pattern_checks+=1
    for r in range(2,16):
        for s in range(2,min(9,r)+1):
            assert (closed_count(r,s)>0)==(r>=s)
            assert predicted_orbits(r,s)>=1
    print(f'VERIFY_OK direct_instances={dc} pattern_instances={pattern_checks} boundary_instances=14')
if __name__=='__main__': main()
