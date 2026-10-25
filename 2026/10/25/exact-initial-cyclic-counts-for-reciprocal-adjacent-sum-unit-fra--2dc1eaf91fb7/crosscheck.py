"""Independent exact-rational checks at the first feasible sizes; no external packages."""
from itertools import permutations
from fractions import Fraction

def count(n, circle):
    iterator=((1,)+u for u in permutations(range(2,n+1))) if circle else permutations(range(1,n+1))
    result=[]
    for a in iterator:
        if a[1 if circle else 0]>=a[-1]:
            continue
        pairs=list(zip(a,a[1:]))
        if circle:pairs.append((a[-1],a[0]))
        s=sum((Fraction(1,x+y) for x,y in pairs),Fraction(0,1))
        if s==1:result.append(a)
    return result

assert count(7,False)==[(4,5,7,2,1,3,6)]
assert count(8,True)==[(1,3,5,4,6,2,7,8),(1,5,2,4,3,7,8,6)]
assert len(count(8,False))==8
assert len(count(9,True))==5
print('CROSSCHECK_OK')
