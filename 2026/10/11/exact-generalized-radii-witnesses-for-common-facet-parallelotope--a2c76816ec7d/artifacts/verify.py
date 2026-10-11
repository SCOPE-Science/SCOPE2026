from fractions import Fraction as F
from itertools import permutations

def e1(x): return sum(x, F(0))
def e2(x): return x[0]*x[1]+x[0]*x[2]+x[1]*x[2]
def prod(x):
    z=F(1)
    for y in x: z*=y
    return z

def check(s):
    assert prod(s)==1
    a=[x*x for x in s]
    lam=[(x+1/x)/2 for x in s]
    assert prod(a)==1
    A=e1(a); B=e2(a); P=prod(lam); S=e1(lam)
    for i,j,k in permutations(range(3),3):
        if len({i,j,k})<3: continue
        t1,t2=a[i],a[j]
        assert 1/(t1*t2)+t1+t2 == A
        assert 1/t1+1/t2+t1*t2 == B
        assert lam[i]+lam[j]+P/(lam[i]*lam[j]) == S
    # exact weighted Cauchy support check on representative nonnegative weights
    for w in ([F(1),F(2),F(3)],[F(5),F(0),F(7)],[F(2),F(11),F(1)]):
        lhs=sum(s[q]*w[q] for q in range(3))**2
        rhs=sum(a[q]*w[q] for q in range(3))*sum(w)
        assert lhs <= rhs

for s in ([F(2),F(3),F(1,6)],[F(3,2),F(5,3),F(2,5)],[F(7,4),F(8,7),F(1,2)]):
    check(s)
print('VERIFY_OK')
