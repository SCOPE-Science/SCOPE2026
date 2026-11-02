#!/usr/bin/env python3
"""Exact-rational validation of a high-tolerance delegation-game equilibrium theorem.

The exhaustive finite tests supplement, but cannot replace, the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def orbit(profile, agent):
    path=[]
    cur=agent
    while cur not in path:
        path.append(cur)
        cur=profile[cur]
    return path


def payoff(profile, i, positions, q, tau):
    p=1-q
    return p*sum(q**h*(tau-abs(positions[i]-positions[v]))
                 for h,v in enumerate(orbit(profile,i)))


def is_nash(profile, positions, q, tau):
    n=len(profile)
    has_profitable_change=False
    for i in range(n):
        old=payoff(profile,i,positions,q,tau)
        for j in range(n):
            if j!=profile[i]:
                cand=profile[:i]+(j,)+profile[i+1:]
                if payoff(cand,i,positions,q,tau)>old:
                    has_profitable_change=True
    return not has_profitable_change


def is_hamiltonian(profile):
    return len(orbit(profile,0))==len(profile) and profile[orbit(profile,0)[-1]]==0


def bound(n,q,diam):
    return diam*q*(1-q**(n-1))/((1-q)*q**(n-1))


def main():
    total_profiles=total_inequalities=total_hamiltonian=0
    for n in (2,3,4,5):
        profiles=list(product(range(n),repeat=n))
        for q in (F(1,4),F(1,2),F(3,4)):
            positions=tuple(F(i,n-1) for i in range(n))
            tau=bound(n,q,F(1))+F(1,10)
            eq=[d for d in profiles if is_nash(d,positions,q,tau)]
            hams=[d for d in profiles if is_hamiltonian(d)]
            assert set(eq)==set(hams), (n,q,len(eq),len(hams))
            assert len(eq)==factorial(n-1)
            total_profiles+=len(profiles)
            total_inequalities+=len(profiles)*n*(n-1)
            total_hamiltonian+=len(eq)
    # Sharp three-voter transition: positions (0,1,2), tau>2.
    transitions=0
    profiles=list(product(range(3),repeat=3))
    near={(1,0,1),(1,2,1)}
    far={(1,2,0),(2,0,1)}
    for q in (F(1,9),F(1,3),F(1,2),F(3,4),F(9,10)):
        cutoff=1+1/q
        for tau,required in ((F(2,1)+(cutoff-2)/2,near),
                             (cutoff,near|far),
                             (cutoff+F(1,1),far)):
            eq={d for d in profiles if is_nash(d,(F(0),F(1),F(2)),q,tau)}
            assert eq==required,(q,tau,eq,required)
            transitions+=1
    print('VERIFY_OK exact_homogeneous_profiles=%d exact_deviation_comparisons=%d cycle_equilibria=%d three_voter_phases=%d'%(total_profiles,total_inequalities,total_hamiltonian,transitions))
if __name__=='__main__': main()
