"""Independent exact tests for nilpotent products of finite-ring elements."""
from itertools import product
from fractions import Fraction

def mulm(A,B,q,n):
    return tuple(sum(A[i*n+t]*B[t*n+j] for t in range(n))%q for i in range(n) for j in range(n))

def zero_matrix(n): return (0,)*(n*n)
def isnil(A,q,n):
    cur=A
    for j in range(1,n+1):
        if cur==zero_matrix(n):return True
        cur=mulm(cur,A,q,n)
    return False

def ring_test(elems,mul,isnilpotent,expected,kvalues,tag):
    from collections import Counter
    z=0
    for k in kvalues:
        count=0
        for xs in product(elems,repeat=k):
            v=xs[0]
            for x in xs[1:]:v=mul(v,x)
            count+=isnilpotent(v)
        actual=Fraction(count,len(elems)**k)
        assert actual==expected(k),(tag,k,actual,expected(k))
        print(tag,k,actual,'OK')

# M2(F2) explicitly as a noncommutative simple factor; |M2|=16.
q,n=2,2
E=list(product(range(q),repeat=n*n))
ring_test(E,lambda A,B:mulm(A,B,q,n),lambda A:isnil(A,q,n),lambda k:Fraction(1,1)-Fraction(3,4)**k,range(1,5),'M2(F2)')
# F3: one-factor probability and two-factor probability; 81² pairs.
q,n=3,2
E=list(product(range(q),repeat=n*n))
ring_test(E,lambda A,B:mulm(A,B,q,n),lambda A:isnil(A,q,n),lambda k:1-Fraction(8,9)**k,range(1,3),'M2(F3)')
# F2[eps]/eps², 4 elements, coordinates (a,b), (a,b)(c,d)=(ac,ad+bc)
E=list(product(range(2),repeat=2))
ring_test(E,lambda x,y:((x[0]*y[0])%2,(x[0]*y[1]+x[1]*y[0])%2),lambda x:x[0]==0,lambda k:1-Fraction(1,2)**k,range(1,6),'F2[eps]/eps²')
# UT2(F2), 8 elements, coordinates (a,b,c) for [[a,b],[0,c]]
E=list(product(range(2),repeat=3))
ring_test(E,lambda x,y:((x[0]*y[0])%2,(x[0]*y[1]+x[1]*y[2])%2,(x[2]*y[2])%2),lambda x:x[0]==0 and x[2]==0,lambda k:(1-Fraction(1,2)**k)**2,range(1,6),'UT2(F2)')
print('VERIFY_OK')
