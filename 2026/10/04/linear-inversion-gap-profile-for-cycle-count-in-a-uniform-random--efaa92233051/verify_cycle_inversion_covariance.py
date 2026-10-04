#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from math import factorial

def cycles(p):
    n=len(p)
    seen=[False]*n
    c=0
    for i in range(n):
        if not seen[i]:
            c+=1
            x=i
            while not seen[x]:
                seen[x]=True
                x=p[x]
    return c

def same_cycle(p,i,j):
    x=i
    while True:
        x=p[x]
        if x==j:
            return True
        if x==i:
            return False

def H(n,power=1):
    return sum((Fraction(1,k**power) for k in range(1,n+1)),Fraction(0))

def run():
    local_cov_checks=0
    total_cov_checks=0
    completion_rule_checks=0
    variance_checks=0
    correlation_checks=0
    permutations_checked=0

    for n in range(2,9):
        ps=list(permutations(range(n)))
        N=factorial(n)
        permutations_checked += N
        cs=[cycles(p) for p in ps]
        meanC=Fraction(sum(cs),N)

        invs=[]
        for p in ps:
            invs.append(sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
        meanV=Fraction(sum(invs),N)

        for i in range(n):
            for j in range(i+1,n):
                vals=[int(p[i]>p[j]) for p in ps]
                meanI=Fraction(1,2)
                cov=sum(
                    (Fraction(cs[k])-meanC)*(Fraction(vals[k])-meanI)
                    for k in range(N)
                )/N
                target=Fraction(-(2*(j-i)-1),2*n*(n-1))
                assert cov==target
                local_cov_checks+=1

                # Verify the conditional same-cycle completion rule.
                for a in range(n):
                    for b in range(n):
                        if a==b:
                            continue
                        idx=[k for k,p in enumerate(ps) if p[i]==a and p[j]==b]
                        if not idx:
                            continue
                        pr=Fraction(sum(same_cycle(ps[k],i,j) for k in idx),len(idx))
                        if a==i or b==j:
                            expected=Fraction(0)
                        elif a==j or b==i:
                            expected=Fraction(1)
                        else:
                            expected=Fraction(1,2)
                        assert pr==expected
                        completion_rule_checks+=1

        covCV=sum(
            (Fraction(cs[k])-meanC)*(Fraction(invs[k])-meanV)
            for k in range(N)
        )/N
        assert covCV==Fraction(-(2*n-1),12)
        total_cov_checks+=1

        varC=sum((Fraction(c)-meanC)**2 for c in cs)/N
        targetC=H(n,1)-H(n,2)
        assert varC==targetC
        variance_checks+=1

        varV=sum((Fraction(v)-meanV)**2 for v in invs)/N
        targetV=Fraction(n*(n-1)*(2*n+5),72)
        assert varV==targetV
        variance_checks+=1

        rho2=covCV*covCV/(varC*varV)
        target_rho2=Fraction((2*n-1)**2,2*n*(n-1)*(2*n+5)) / targetC
        assert rho2==target_rho2
        correlation_checks+=1

    print(
        "VERIFY_OK "
        f"permutations_checked={permutations_checked} "
        f"local_cov_checks={local_cov_checks} "
        f"completion_rule_checks={completion_rule_checks} "
        f"total_cov_checks={total_cov_checks} "
        f"variance_checks={variance_checks} "
        f"correlation_checks={correlation_checks}"
    )

if __name__=="__main__":
    run()
