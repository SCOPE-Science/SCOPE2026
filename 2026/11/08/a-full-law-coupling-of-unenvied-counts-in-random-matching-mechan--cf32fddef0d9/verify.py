#!/usr/bin/env python3
"""Exact finite-market verification of the unenvied-count distribution in house assignment."""
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial


def recurrence(n):
    dist={1:F(1)}
    for j in range(2,n+1):
        m=n-j+1
        nxt={}
        for r,p in dist.items():
            for h in range(r+1):
                # Relative first-arrival order of r exposed singletons and m unexposed types.
                transition = F(m * factorial(r)//factorial(r-h) * factorial(m+r-h-1), factorial(m+r))
                t=r+1-h
                nxt[t]=nxt.get(t,F(0))+p*transition
        dist=nxt
        assert sum(dist.values())==1
    return dist


def singleton_formula(n):
    out={}
    for u in range(1,n+1):
        d=n-u
        a=F(0)
        for t in range(d+1):
            for h in range(d-t+1):
                a+=F(comb(d,t)*(-1)**(d-t)*comb(d-t,h)*factorial(u+h-1),(n-t)**(u+h))
        out[u]=u*comb(n,u)*a
    return out


def brute(n):
    profiles=list(permutations(range(n)))
    counts={}
    for prefs in product(profiles,repeat=n):
        remaining=set(range(n))
        alloc=[]
        for order in prefs:
            selected=next(item for item in order if item in remaining)
            remaining.remove(selected);alloc.append(selected)
        # Count agents whose allocated objects are not preferred by another to their own.
        positions=[{obj:rank for rank,obj in enumerate(pr)} for pr in prefs]
        u=sum(all(positions[j][alloc[j]] < positions[j][alloc[i]] for j in range(n) if j!=i)
              for i in range(n))
        counts[u]=counts.get(u,0)+1
    return {i:F(c,len(profiles)**n) for i,c in counts.items()}




def brute_da(n):
    """Independently enumerate student-proposing deferred acceptance incl. school priorities."""
    profiles=list(permutations(range(n)))
    counts={}
    for prefs in product(profiles,repeat=n):
        positions=[{obj:rank for rank,obj in enumerate(pr)} for pr in prefs]
        for priors in product(profiles,repeat=n):
            priority=[{stu:rank for rank,stu in enumerate(pr)} for pr in priors]
            next_choice=[0]*n
            held=[None]*n
            pending=list(range(n))
            while pending:
                student=pending.pop()
                school=prefs[student][next_choice[student]]
                next_choice[student]+=1
                prior=held[school]
                if prior is None: held[school]=student
                elif priority[school][student] < priority[school][prior]:
                    held[school]=student;pending.append(prior)
                else: pending.append(student)
            alloc=[None]*n
            for school,student in enumerate(held): alloc[student]=school
            assert all(a is not None for a in alloc)
            unenvied=sum(all(positions[j][alloc[j]] < positions[j][alloc[i]] for j in range(n) if j!=i) for i in range(n))
            counts[unenvied]=counts.get(unenvied,0)+1
    return {i:F(c,len(profiles)**(2*n)) for i,c in counts.items()}


def verify_fixed_priorities(n):
    """For each fixed strict priority profile, enumerate all student rankings."""
    profiles=list(permutations(range(n)))
    expected=recurrence(n)
    cases=0
    for priors in product(profiles,repeat=n):
        priority=[{student:rank for rank,student in enumerate(pr)} for pr in priors]
        counts={}
        for prefs in product(profiles,repeat=n):
            positions=[{house:rank for rank,house in enumerate(pr)} for pr in prefs]
            next_choice=[0]*n
            held=[None]*n
            pending=list(range(n))
            while pending:
                student=pending.pop()
                house=prefs[student][next_choice[student]]
                next_choice[student]+=1
                prior=held[house]
                if prior is None: held[house]=student
                elif priority[house][student] < priority[house][prior]:
                    held[house]=student;pending.append(prior)
                else: pending.append(student)
            assigned=[None]*n
            for house,student in enumerate(held): assigned[student]=house
            count=sum(all(positions[j][assigned[j]]<positions[j][assigned[i]]
                          for j in range(n) if j!=i) for i in range(n))
            counts[count]=counts.get(count,0)+1
        exact={u:F(value,len(profiles)**n) for u,value in counts.items()}
        assert exact==expected,(priors,exact,expected)
        cases+=1
    return cases


def mixed_moments(n,r):
    # Verify specified subsets' exact unenvied probability by independent finite-position sampling.
    from itertools import combinations
    cumul=F(0)
    for pos in combinations(range(1,n+1),r):
        p=F(factorial(r))
        for j,i in enumerate(pos,1):
            p/=n-i+j
        cumul+=p
    return cumul*factorial(r)

if __name__=='__main__':
    checks=0
    for n in range(1,10):
        a=recurrence(n);b=singleton_formula(n)
        assert a==b,(n,a,b)
        assert sum(a.values())==1
        assert sum(u*p for u,p in a.items())==sum(F(1,i) for i in range(1,n+1))
        for r in range(1,min(n,5)+1):
            assert sum(p*F(factorial(u),factorial(u-r)) for u,p in a.items() if u>=r)==mixed_moments(n,r)
            checks+=1
        checks+=3
        if n<=4:
            c=brute(n)
            assert c==a,(n,c,a)
            checks+=1
        if n<=3:
            d=brute_da(n)
            assert d==a,(n,d,a)
            checks+=1
        print('n=',n,'P(U=u)=',[str(a.get(u,0)) for u in range(1,n+1)])
    cases=verify_fixed_priorities(3)
    checks+=cases
    print('PASS',checks,'independent distribution, moment and exhaustive comparisons')
