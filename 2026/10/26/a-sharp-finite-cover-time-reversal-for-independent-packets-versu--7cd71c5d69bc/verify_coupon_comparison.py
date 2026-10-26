"""Exact rational checks of coupon-coverage identities and finite mean comparisons.

Run with standard-library Python 3.  Tests are finite checks, not the proof
of the theorems for arbitrary population size or adaptive policies.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial


def harmonic(m):
    return sum((Fraction(1, j) for j in range(1, m + 1)), Fraction(0))


def independent_packet_mean(n, r):
    """Expected number of additional independent uniform r-packets to cover n-r initially unseen labels."""
    m = n - r
    values = [Fraction(0)] * (m + 1)
    for k in range(1, m + 1):
        probs = [Fraction(comb(k, j) * comb(n-k, r-j), comb(n, r))
                 if 0 <= j <= k and 0 <= r-j <= n-k else Fraction(0)
                 for j in range(0, min(k,r)+1)]
        assert sum(probs) == 1
        values[k] = (1 + sum(probs[j] * values[k-j] for j in range(1, len(probs)))) / (1 - probs[0])
    return values[m]


def independent_packet_mean_inclusion(n, r):
    # Inclusion-exclusion for the full cover time including the first packet.
    den = comb(n,r)
    return sum((Fraction((-1)**(j+1) * comb(n,j),1-Fraction(comb(n-j,r),den) if n-j>=r else 1)
                for j in range(1,n+1)),Fraction(0))


def policy_test():
    # Enumerate all possible replacement choices for several history-responsive deterministic policies.
    policies = [
        lambda H,C,t: min(H),
        lambda H,C,t: max(H),
        lambda H,C,t: H[(len(C)+t)%len(H)],
        lambda H,C,t: H[(sum(C)+t*t)%len(H)],
    ]
    tests=0
    for n in range(3,7):
        for r in range(1,n):
            initial=tuple(range(r))
            outside=tuple(range(r,n))
            m=n-r
            for policy in policies:
                states={(initial,initial):Fraction(1)}
                ref={initial:Fraction(1)}
                for t in range(7):
                    observed=defaultdict(Fraction)
                    for (H,C),p in states.items(): observed[C]+=p
                    assert dict(observed)==ref, (n,r,t)
                    tests+=1
                    for j in range(m+1):
                        lhs=sum((factorial(n-len(C))//factorial(n-len(C)-j) if n-len(C)>=j else 0)*p for C,p in observed.items())
                        rhs=Fraction(factorial(m),factorial(m-j))*Fraction(m-j,m)**t
                        assert lhs==rhs
                        tests+=1
                    newstates=defaultdict(Fraction)
                    for (H,C),p in states.items():
                        sH=set(H)
                        old=policy(H,C,t)
                        assert old in sH
                        for x in range(n):
                            if x not in sH:
                                newH=tuple(sorted(sH-{old}|{x}))
                                newC=tuple(sorted(set(C)|{x}))
                                newstates[(newH,newC)]+=p/m
                    states=newstates
                    newref=defaultdict(Fraction)
                    for C,p in ref.items():
                        for x in outside:
                            newref[tuple(sorted(set(C)|{x}))]+=p/m
                    ref=dict(newref)
    return tests


def comparison_test():
    tests=0
    for n in range(2,17):
        for r in range(1,n):
            m=n-r
            iid=1+independent_packet_mean(n,r)
            incl=independent_packet_mean_inclusion(n,r)
            assert iid==incl,(n,r,'inclusion',iid,incl)
            tests+=1
            mark=1+m*harmonic(m)
            if r==1 or m==1:
                assert iid>mark,(n,r,'reverse',iid,mark)
            else:
                assert iid<mark,(n,r,'forward',iid,mark)
                bound=1+Fraction(n,r)*harmonic(m)
                assert iid<bound,(n,r,'strict potential',iid,bound)
                tests+=1
            tests+=1
            # Verify the drift inequality exactly in every reachable nonabsorbing state.
            for k in range(1,m+1):
                drift=Fraction(0)
                for j in range(1,min(k,r)+1):
                    if 0 <= r-j <= n-k:
                        p=Fraction(comb(k,j)*comb(n-k,r-j),comb(n,r))
                        drift+=p*Fraction(n,r)*(harmonic(k)-harmonic(k-j))
                assert drift >= 1,(n,r,k,drift)
                tests+=1
    return tests


def main():
    a=policy_test()
    b=comparison_test()
    print(f'PASS: {a} exact occupancy/coupling assertions; {b} exact expected-time and drift assertions; total {a+b}.')

if __name__=='__main__': main()
