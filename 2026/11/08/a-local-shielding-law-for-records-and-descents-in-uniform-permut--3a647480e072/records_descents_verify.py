"""Exhaustive finite checks of the record-descent covariance support and weights."""
from itertools import permutations
from fractions import Fraction
from math import factorial

checks=0
for n in range(2,10):
    records=[0]*n
    descents=[0]*(n-1)
    joint=[[0]*(n-1) for _ in range(n)]
    total_record=total_descent=total_cross=0
    for p in permutations(range(n)):
        m=-1;R=[0]*n
        for i,x in enumerate(p):
            R[i]=int(x>m)
            if x>m:m=x
        D=[int(p[j]>p[j+1]) for j in range(n-1)]
        for i,x in enumerate(R):
            records[i]+=x
            if x:
                for j,y in enumerate(D):joint[i][j]+=y
        for j,y in enumerate(D):descents[j]+=y
        r=sum(R);d=sum(D)
        total_record+=r;total_descent+=d;total_cross+=r*d
    fac=factorial(n)
    for i in range(n):
        for j in range(n-1):
            got=Fraction(joint[i][j],fac)-Fraction(records[i]*descents[j],fac**2)
            if i==j: expected=Fraction(j,2*(j+1)*(j+2))
            elif i==j+1: expected=-Fraction(1,2*(j+2))
            else:expected=Fraction(0)
            assert got==expected,(n,i+1,j+1,got,expected)
            checks+=1
    got=Fraction(total_cross,fac)-Fraction(total_record*total_descent,fac**2)
    assert got==-Fraction(n-1,2*n),(n,got)
    checks+=1
print('PASS', checks, 'exact comparisons, exhaustive permutations through n=9')

# Test the stronger joint shielding property for all disjoint comparison pairs.
for n in range(2,8):
    ps=list(permutations(range(n)))
    for mask in range(1,1<<(n-1)):
        if mask&(mask<<1):
            continue
        sites=[j for j in range(n-1) if mask>>j&1]
        covered=set(sites)|{j+1 for j in sites}
        outside=tuple(i for i in range(n) if i not in covered)
        tab={}
        for p in ps:
            top=-1;R=[]
            for x in p:
                R.append(int(x>top));top=max(top,x)
            key=tuple(R[i] for i in outside)
            outcomes=tuple(int(p[j]>p[j+1]) for j in sites)
            entry=tab.setdefault(key,{})
            entry[outcomes]=entry.get(outcomes,0)+1
        for entry in tab.values():
            assert len(entry)==2**len(sites)
            assert len(set(entry.values()))==1
            checks+=1
print('PASS', checks, 'total checks including exact matching-site shielding')
