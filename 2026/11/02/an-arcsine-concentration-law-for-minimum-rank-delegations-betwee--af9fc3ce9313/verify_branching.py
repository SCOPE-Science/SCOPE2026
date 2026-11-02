"""Independent finite-state verification for two-guru ranked delegations on a path.

Run: python3 verify_branching.py
Only Python standard library is required.
"""
from itertools import product
from math import comb, isclose
from fractions import Fraction


def counts_exact(n):
    # Independent ballot count enumerates all preference sequences and all cuts.
    histogram = [0] * (n+1)
    total_min_cost=0
    total_BFD_cost=0
    for pref in product((-1,1), repeat=n):
        # -1 denotes first choice left; +1 first choice right.
        costs=[]
        for cut in range(n+1):
            # All players i<=cut send left; all i>cut send right.
            cost=sum(pref[i-1]==1 for i in range(1,cut+1)) + sum(pref[i-1]==-1 for i in range(cut+1,n+1))
            costs.append(cost)
        m=min(costs)
        t=costs.index(m)
        histogram[t]+=1
        total_min_cost+=m
        # Breadth-first delegation picks the shorter path to a guru; at the
        # unique middle voter (odd n), equal lengths are broken by rank.
        middle=n//2+1
        bfd_cut=n//2 if n%2==0 else (n//2 + (pref[middle-1]==-1))
        total_BFD_cost+=costs[bfd_cut]
        # A separate stepwise walk implementation of the minimizer.
        s=0; minimum=0; argmin=0
        for i,v in enumerate(pref,1):
            s+=v
            if s<minimum:
                minimum=s;argmin=i
        assert argmin==t
        assert m==sum(v==-1 for v in pref)+minimum
    return histogram, Fraction(total_min_cost,2**n), Fraction(total_BFD_cost,2**n)


def strict_count(k):
    return 1 if k==0 else comb(k-1,(k-1)//2)


def weak_count(k):
    return comb(k,k//2)


def expected_formula(n):
    abs_mean=Fraction(n*comb(n-1,(n-1)//2),2**(n-1))
    p_zero=Fraction(comb(n,n//2),2**n) if n%2==0 else Fraction(0)
    return Fraction(n,2)-abs_mean+Fraction(1,2)*(1-p_zero)


def branched(n,orientation):
    # Each 0/1 denotes left/right delegation for each of n inner vertices.
    # Detect all directed cycles by literal path traversal to endpoints 0,n+1.
    for start in range(1,n+1):
        p=start;seen=set()
        while 1<=p<=n:
            if p in seen: return False
            seen.add(p)
            p+=1 if orientation[p-1] else -1
    return True


def independent_bruteforce(n):
    # Crucially this does not assume the cut structure.
    all_choices=list(product((0,1),repeat=n))
    feasible=[c for c in all_choices if branched(n,c)]
    assert len(feasible)==n+1
    for ranks in all_choices:
        global_min=min(sum(choice!=rank for choice,rank in zip(b,ranks)) for b in feasible)
        first_cut=min(sum(choice==0 for choice in b) for b in feasible
                      if sum(choice!=rank for choice,rank in zip(b,ranks))==global_min)
        steps=[1 if v else -1 for v in ranks]
        walk=0;m=0;arg=0
        for i,s in enumerate(steps,1):
            walk+=s
            if walk<m:
                m=walk;arg=i
        assert first_cut==arg
    return len(feasible)*len(all_choices)

if __name__=='__main__':
    checked_profiles=0
    checked_branchings=0
    for n in range(1,16):
        h,c,b=counts_exact(n)
        predicted=[strict_count(k)*weak_count(n-k) for k in range(n+1)]
        assert h==predicted,(n,h,predicted)
        assert sum(predicted)==2**n
        assert c==expected_formula(n),(n,c,expected_formula(n))
        assert b==Fraction(n-(n%2),2)
        checked_profiles+=2**n
    for n in range(1,9):
        checked_branchings+=independent_bruteforce(n)
    # An asymptotic sanity check is NOT offered as a proof.
    # Exact n=3: fractions are 3/8,1/4,1/8,1/4.
    assert [Fraction(v,8) for v in counts_exact(3)[0]] == [Fraction(3,8),Fraction(1,4),Fraction(1,8),Fraction(1,4)]
    print('PASS: preference profiles checked against exact distribution and expectation:',checked_profiles)
    print('PASS: independently traced acyclic branchings by profile:',checked_branchings)
    print('PASS: exact expectation comparisons and tie-breaking at all tested sizes')
