"""Independent finite-Hamiltonian and exact rank-order verification."""
from itertools import product, combinations, permutations
from fractions import Fraction
from math import comb, factorial
import random

def h(s,J):
    return -sum(J[i]*s[i]*s[i+1] for i in range(len(J)))

def predicted_stable(s,J,r):
    n=len(s)
    eligible={j for j in range(1,n) if j>r and n-j>r and all(J[j-1]<J[k-1] for k in range(max(1,j-r),min(n-1,j+r)+1) if k!=j)}
    walls={j for j in range(1,n) if s[j-1]!=s[j]}
    return walls<=eligible

def brute_stable(s,J,r):
    n=len(s)
    old=h(s,J)
    for q in range(1,min(r,n)+1):
        for S in combinations(range(n),q):
            t=list(s)
            for i in S:t[i]*=-1
            if h(t,J)<old: return False
    return True

checks=0
for n in range(3,11):
    for trial in range(3):
        J=list(range(1,n))
        random.Random(n*100+trial).shuffle(J)
        for r in range(1,min(4,n)+1):
            expected=2**(sum(j>r and n-j>r and all(J[j-1]<J[k-1] for k in range(max(1,j-r),min(n-1,j+r)+1) if k!=j) for j in range(1,n))+1)
            total=0
            for s in product((-1,1),repeat=n):
                x=predicted_stable(s,J,r)
                y=brute_stable(s,J,r)
                assert x==y,(n,r,J,s,x,y)
                total+=y
                checks+=1
            assert total==expected,(n,r,J,total,expected)
print('PASS direct full-state and all allowed flip subsets:',checks,'checks')

def both_probability(r,d):
    # Enumerate union windows of two minima; exact for small dimensions.
    L=2*r+d+1
    successes=0
    for a in permutations(range(L)):
        if a[r]!=min(a[:2*r+1]):continue
        if a[r+d]!=min(a[d:d+2*r+1]):continue
        successes+=1
    return Fraction(successes,factorial(L))
for r,d in ((1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(2,5)):
    z=both_probability(r,d)
    m=2*r+1
    target=Fraction(0) if d<=r else (Fraction(2,m*(m+d)) if d<=2*r else Fraction(1,m*m))
    assert z==target,(r,d,z,target)
print('PASS exact rank-order joint probabilities:',8,'checks')
for r in range(1,8):
    m=2*r+1
    sigma=4/m*sum(1/(m+d) for d in range(r+1,2*r+1))-2*r/m**2
    assert sigma>0
    print('r',r,'entropy coefficient',1/m,'variance-density',sigma)
