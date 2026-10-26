#!/usr/bin/env python3
"""Independent direct-utility and exact-potential verifier for one-vacancy diversity jumps.
Uses only Python standard library. Enumerations are finite consistency tests, not universal proofs.
"""
from fractions import Fraction
from collections import Counter
from itertools import product,combinations
from math import comb

def run(parts, types):
    n=sum(parts)
    which=tuple(i for i,s in enumerate(parts) for _ in range(s))
    H=tuple(n-s-1 for s in parts)
    assert min(H)>0
    summary=Counter(); count_direct=Counter()
    for vacancy in range(n):
        for remaining in product(range(types),repeat=n-1):
            state=remaining[:vacancy]+(-1,)+remaining[vacancy:]
            agents=Counter(i for i in state if i>=0)
            counts=[[sum(state[v]==t for v in range(n) if which[v]==i) for t in range(types)] for i in range(len(parts))]
            phi=sum(Fraction(x*(x+1)-2*agents[t]*x,2*H[i]) for i,row in enumerate(counts) for t,x in enumerate(row))
            improving=False
            for v,t in enumerate(state):
                if t<0:continue
                old_nei=[state[u] for u in range(n) if which[u]!=which[v] and state[u]>=0]
                old=Fraction(sum(s!=t for s in old_nei),len(old_nei))
                new_state=list(state);new_state[v],new_state[vacancy]=new_state[vacancy],new_state[v]
                new_nei=[new_state[u] for u in range(n) if which[u]!=which[vacancy] and new_state[u]>=0]
                new=Fraction(sum(s!=t for s in new_nei),len(new_nei))
                new_counts=[[sum(new_state[u]==c for u in range(n) if which[u]==i) for c in range(types)] for i in range(len(parts))]
                new_phi=sum(Fraction(x*(x+1)-2*agents[c]*x,2*H[i]) for i,row in enumerate(new_counts) for c,x in enumerate(row))
                assert new-old == new_phi-phi, (parts,state,v,new,old,new_phi,phi)
                summary['moves']+=1
                if new>old: improving=True
            if types==2:
                j=which[vacancy]; redvac=counts[j][1];bluevac=counts[j][0]
                redfull=sum(parts[i] for i in range(len(parts)) if i!=j and counts[i][1]==parts[i])
                bluefull=sum(parts[i] for i in range(len(parts)) if i!=j and counts[i][0]==parts[i])
                pure=all(counts[i][0]*counts[i][1]==0 for i in range(len(parts)) if i!=j)
                predicted=pure and all((bluefull*(parts[j]-parts[i])<=bluevac*H[j] if counts[i][1] else redfull*(parts[j]-parts[i])<=redvac*H[j]) for i in range(len(parts)) if i!=j)
                assert (not improving)==predicted,(parts,state,'predicted',predicted,'improving',improving)
                if not improving:count_direct[sum(t==1 for t in state)]+=1
            summary['states']+=1
    if types==2:
        predicted_count=Counter()
        for j in range(len(parts)):
            other=[i for i in range(len(parts)) if i!=j]
            for choices in product(range(2),repeat=len(other)):
                cr={i:t for i,t in zip(other,choices)}
                reds=sum(parts[i] for i in other if cr[i]==1)
                blues=sum(parts[i] for i in other if cr[i]==0)
                for red_v in range(parts[j]):
                    blue_v=parts[j]-1-red_v
                    valid=all((blues*(parts[j]-parts[i])<=blue_v*H[j] if cr[i]==1 else reds*(parts[j]-parts[i])<=red_v*H[j]) for i in other)
                    if valid:predicted_count[reds+red_v]+=parts[j]*comb(parts[j]-1,red_v)
        assert count_direct==predicted_count,(parts,count_direct,predicted_count)
        summary['equilibria']=sum(count_direct.values())
        summary['by_red']=dict(sorted(count_direct.items()))
    return summary

if __name__=='__main__':
    groups2=[(1,1,1),(1,1,2),(1,2,3),(2,2,2),(2,2,3),(2,2,4),(2,2,5),(2,3,3),(2,3,4),(2,2,2,2),(3,3,3)]
    groups3=[(1,1,1),(1,2,2),(2,2,2),(2,2,3),(2,3,3)]
    tot=Counter()
    for groups,ntype in [(groups2,2),(groups3,3)]:
        for parts in groups:
            r=run(parts,ntype)
            tot['states']+=r['states'];tot['moves']+=r['moves'];tot['cases']+=1
            print('PASS',parts,ntype,r)
    print('TOTAL',dict(tot))
