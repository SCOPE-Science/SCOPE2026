from itertools import permutations
from math import factorial
from fractions import Fraction
checks=0
for n in range(3,9):
    nperm=factorial(n)
    cyc_sum=0
    mixed_up=[0]*(n-2); mixed_down=[0]*(n-2)
    for p in permutations(range(n)):
        seen=set();c=0
        for x in range(n):
            if x not in seen:
                c+=1;y=x
                while y not in seen:
                    seen.add(y);y=p[y]
        cyc_sum+=c
        for i in range(n-2):
            if p[i]<p[i+1]<p[i+2]: mixed_up[i]+=c
            if p[i]>p[i+1]>p[i+2]: mixed_down[i]+=c
    for i in range(n-2):
        a=Fraction(mixed_up[i],nperm)-Fraction(cyc_sum,6*nperm)
        b=Fraction(mixed_down[i],nperm)-Fraction(cyc_sum,6*nperm)
        assert a==Fraction(3*n-2,6*n*(n-1)*(n-2)),(n,i,'up',a)
        assert b==Fraction(10-3*n,6*n*(n-1)*(n-2)),(n,i,'down',b)
        checks+=2
    print(n,'OK',2*(n-2),'position/covariance identities')
print('VERIFY_OK',checks,'exact enumerative assertions')
