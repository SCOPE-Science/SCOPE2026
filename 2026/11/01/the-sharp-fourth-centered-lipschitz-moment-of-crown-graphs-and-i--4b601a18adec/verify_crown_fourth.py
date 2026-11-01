#!/usr/bin/env python3
"""Exact finite diagnostics for the sharp fourth centered Lipschitz moment of crown graphs.
All calculations use Python integer and rational arithmetic; no external dependencies.
"""
from fractions import Fraction
from itertools import product


def score(vals):
    N=len(vals)
    s=sum(vals)
    return Fraction(sum((N*x-s)**4 for x in vals),N**5)


def formulas(n):
    exceptional=Fraction(1,16)+Fraction(5,n)
    balanced=Fraction(1,2)
    if n%2:
        balanced-=Fraction(1,4*n*n)+Fraction(3,16*n**4)
    return exceptional,balanced


def count_candidates(n):
    # Permute the n matched A--B index pairs simultaneously. For each
    # A-level class, only the count of B vertices at their upper endpoint matters.
    best=Fraction(-1)
    modes=set()
    tested=0
    N=2*n
    for c0 in range(1,n+1):
        for c1 in range(n-c0+1):
            c2=n-c0-c1
            cs=(c0,c1,c2)
            A=[0]*c0+[1]*c1+[2]*c2
            ranges=[]
            bounds=[]
            for j,c in enumerate(cs):
                if not c:
                    bounds.append((0,0))
                    ranges.append((0,))
                    continue
                rest=A.copy()
                rest.remove(j)
                lo,hi=max(rest)-1,min(rest)+1
                assert lo<=hi
                bounds.append((lo,hi))
                ranges.append(range(c+1) if lo<hi else (0,))
            for upper_counts in product(*ranges):
                hist={-1:0,0:c0,1:c1,2:c2,3:0}
                for c,(lo,hi),k in zip(cs,bounds,upper_counts):
                    hist[lo]+=c-k
                    hist[hi]+=k
                s=sum(v*c for v,c in hist.items())
                val=Fraction(sum(c*(N*v-s)**4 for v,c in hist.items()),N**5)
                tested+=1
                if val>best:
                    best=val
                    modes={(cs,upper_counts)}
                elif val==best:
                    modes.add((cs,upper_counts))
    return best,tested,len(modes)


def labelled(n):
    # Separate direct endpoint enumeration on indexed labelled A sites.
    best=Fraction(-1)
    count=0
    for a in product((0,1,2),repeat=n):
        if min(a)!=0:
            continue
        intervals=[]
        for i in range(n):
            rest=[a[j] for j in range(n) if j!=i]
            lo,hi=max(rest)-1,min(rest)+1
            if lo>hi:
                break
            intervals.append((lo,hi))
        if len(intervals)!=n:
            continue
        for b in product(*[tuple(sorted(set(t))) for t in intervals]):
            # All cross edges are checked from the original graph.
            assert all(abs(a[i]-b[j])<=1 for i in range(n) for j in range(n) if i!=j)
            count+=1
            best=max(best,score(a+b))
    return best,count


def run():
    tested=0
    for n in range(3,37):
        best,k,num=count_candidates(n)
        tested+=k
        assert best==max(formulas(n)),(n,best,formulas(n))
        assert (best==formulas(n)[0])==(n<=11)
        assert num>=1
    print('EXACT_SYMMETRY_REDUCED_ENDPOINT_MAXIMA_OK',34,tested)
    count=0
    for n in range(3,7):
        best,k=labelled(n)
        count+=k
        assert best==max(formulas(n)),(n,best)
    print('DIRECT_LABELLED_ENDPOINT_EXHAUSTION_OK',4,count)
    for n in range(3,70):
        ex,ba=formulas(n)
        witness_ex=[0]+[2]*(n-1)+[3]+[1]*(n-1)
        witness_ba=[2]*(n//2)+[0]*(n-n//2)+[1]*n
        assert score(witness_ex)==ex
        assert score(witness_ba)==ba
        assert ex>ba if n<=11 else ba>ex
    print('EXACT_WITNESSES_AND_INTEGER_THRESHOLD_OK',67)
    for n in range(3,80):
        N=2*n
        # Algebraic sum of fourfold deviations for an arbitrary sign vector
        for plus in range(n+1):
            minus=n-plus
            vals=[1]*plus+[-1]*minus+[0]*n
            d=plus-minus
            F=Fraction(n,N)+Fraction(d*d,N*N)*(-4+Fraction(6*n,N))-Fraction(3*d**4,N**4)
            assert score(vals)==F
    print('EXACT_THREE_LEVEL_FOURTH_MOMENT_IDENTITY_OK',77)
    print('ALL_CROWN_FOURTH_MOMENT_CHECKS_OK')


if __name__=='__main__':
    run()
