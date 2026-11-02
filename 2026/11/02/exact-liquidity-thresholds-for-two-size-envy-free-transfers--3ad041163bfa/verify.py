from fractions import Fraction
from itertools import product

def predicted(n,ones,large,r,budgets):
    W=ones+r*large
    C=[(Fraction(W,n)+Fraction(x)).numerator//(Fraction(W,n)+Fraction(x)).denominator for x in budgets]
    return W<=sum(C) and large<=sum(x//r for x in C)

def possible_loads(n,ones,large,r):
    initial=(0,)*n
    s={initial}
    for unit in [r]*large+[1]*ones:
        new=set()
        for loads in s:
            for i in range(n):
                z=list(loads);z[i]+=unit;new.add(tuple(z))
        s=new
    return s

def constructed(n, ones, large, r, budgets):
    W=ones+r*large
    mean=Fraction(W,n)
    caps=[int((mean+Fraction(b)).numerator//(mean+Fraction(b)).denominator) for b in budgets]
    if not (W<=sum(caps) and large<=sum(c//r for c in caps)):
        return None
    big_left=large
    big=[]
    for c in caps:
        t=min(big_left,c//r)
        big.append(t)
        big_left-=t
    assert big_left==0
    unit_left=ones
    unit=[]
    for c,t in zip(caps,big):
        u=min(unit_left,c-r*t)
        unit.append(u)
        unit_left-=u
    assert unit_left==0
    loads=[unit[i]+r*big[i] for i in range(n)]
    payments=[mean-load for load in loads]
    assert sum(loads)==W and sum(payments)==0
    for i in range(n):
        assert payments[i]>=-Fraction(budgets[i])
        for j in range(n):
            assert loads[i]+payments[i]>=loads[j]+payments[j]
    return loads, payments

cases=0; brute_checks=0; constructed_count=0
for n in range(1,5):
 for r in range(2,6):
  for ones in range(0,6):
   for large in range(0,6):
    if ones+large>7:continue
    W=ones+r*large
    loads=possible_loads(n,ones,large,r)
    caps_by_B=[]
    for B in product([Fraction(0),Fraction(1,3),Fraction(1),Fraction(2)],repeat=n):
     oracle=predicted(n,ones,large,r,B)
     tested=any(all(Fraction(z[i])<=Fraction(W,n)+B[i] for i in range(n)) for z in loads)
     brute_checks+=len(loads)
     if oracle!=tested:raise AssertionError((n,r,ones,large,B,oracle,tested,loads))
     produced=constructed(n,ones,large,r,B)
     if (produced is not None)!=oracle:raise AssertionError((n,r,ones,large,B))
     if produced is not None:constructed_count+=1
     cases+=1
print('VERIFY_OK cases=',cases,'load_vectors_checked=',brute_checks,'constructive_allocations=',constructed_count)
# Sharp obstruction outside the unit-plus-r denomination class:
# n=3, goods (2,2,2,3), capacities (3,3,3), every item positive,
# total=9 and every 3-good fits individually, but packing impossible.
others={ (0,0,0) }
for v in [2,2,2,3]:
 others={tuple(l[j]+(v if j==i else 0) for j in range(3)) for l in others for i in range(3)}
assert not any(all(c<=3 for c in x) for x in others)
print('BOUNDARY_OK 2+2+2+3 / capacities 3,3,3')
