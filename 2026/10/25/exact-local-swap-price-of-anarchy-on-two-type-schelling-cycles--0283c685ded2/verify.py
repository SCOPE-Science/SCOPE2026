#!/usr/bin/env python3
"""Exact finite checks for local two-type ring swap inefficiency.

This reproducibility script implements the model with direct utilities, plus an
independent run-length constructor. Enumeration is finite evidence only; the
unbounded result is proved separately.
"""
import json
from collections import defaultdict
from math import comb


def predicted(n,a):
    b=n-a
    r=min(a,b,n//3)
    if n==3*r and max(a,b)<2*r:
        r-=1
    return r


def color_array(mask,n):
    return [(mask>>i)&1 for i in range(n)]


def utility(z,i):
    n=len(z)
    return int(z[(i-1)%n]==z[i])+int(z[(i+1)%n]==z[i])


def direct_profitable(z,i):
    n=len(z); j=(i+1)%n
    if z[i]==z[j]: return False
    u_i=utility(z,i);u_j=utility(z,j)
    w=z.copy();w[i],w[j]=w[j],w[i]
    return utility(w,j)>u_i and utility(w,i)>u_j


def alternating_four(z,i):
    n=len(z)
    a,b,c,d=(z[(i+k)%n] for k in range(4))
    return a==c and b==d and a!=b


def stable(z):
    return not any(direct_profitable(z,i) for i in range(len(z)))


def runs_witness(n,a):
    b=n-a; r=predicted(n,a)
    Aextra=a-r; Bextra=b-r
    if Aextra>=r:
        A=[2]*r; A[0]+=Aextra-r
        B=[1]*r; B[0]+=Bextra
    elif Bextra>=r:
        A=[1]*r; A[0]+=Aextra
        B=[2]*r; B[0]+=Bextra-r
    else:
        # At this point, the desired r is feasible with n>=3r+1.
        # A_i are long for i=1,...,Aextra; B_i are long for i=Aextra,...,r.
        assert Aextra>=1 and Bextra>=r-Aextra+1
        A=[2 if i < Aextra else 1 for i in range(r)]
        B=[2 if i >= Aextra-1 else 1 for i in range(r)]
        B[-1]+=Bextra-(r-Aextra+1)
    z=[]
    for x,y in zip(A,B): z.extend([0]*x+[1]*y)
    assert len(z)==n and z.count(0)==a and z.count(1)==b
    return z


def run():
    exhaustive=[]
    for n in range(3,17):
        maxr=defaultdict(int);stable_count=defaultdict(int)
        for mask in range(1,(1<<n)-1):
            z=color_array(mask,n)
            a=n-sum(z)
            is_stable=stable(z)
            no_alt=not any(alternating_four(z,i) for i in range(n))
            assert is_stable==no_alt,(n,mask)
            if is_stable:
                transitions=sum(z[i]!=z[(i+1)%n] for i in range(n))
                assert transitions%2==0
                r=transitions//2
                maxr[a]=max(maxr[a],r)
                stable_count[a]+=1
        for a in range(1,n):
            assert stable_count[a]>0
            assert maxr[a]==predicted(n,a),(n,a,maxr[a],predicted(n,a))
        exhaustive.append({'n':n,'nonmonochromatic_assignments':(1<<n)-2,
                           'stable_assignments':sum(stable_count.values()),
                           'composition_classes':n-1})

    witness_tests=0
    for n in range(3,113):
        for a in range(1,n):
            z=runs_witness(n,a)
            assert stable(z), (n,a)
            assert sum(z[i]!=z[(i+1)%n] for i in range(n))==2*predicted(n,a)
            witness_tests+=1

    sample={}
    for n,a in [(6,3),(9,4),(12,6),(13,6),(15,7),(18,9)]:
        r=predicted(n,a)
        sample[f'{n}:{a}:{n-a}']={'max_run_pairs':r,'optimum_welfare':n-2,
              'worst_local_welfare':n-2*r,'ratio_numerator':n-2,
              'ratio_denominator':n-2*r,
              'witness':''.join(map(str,runs_witness(n,a)))}
    certificate={'schema_version':1,
       'exhaustive_n_range':[3,16],
       'assignments_checked':sum((1<<n)-2 for n in range(3,17)),
       'composition_cases_checked':sum(n-1 for n in range(3,17)),
       'witness_n_range':[3,112],
       'constructive_cases_checked':witness_tests,
       'exhaustive_by_n':exhaustive,
       'selected_values':sample,
       'finite_scope_warning':'Finite enumerations do not establish the all-n theorem; see analytical proof.'}
    print(json.dumps(certificate,sort_keys=True,separators=(',',':')))

if __name__=='__main__':run()
