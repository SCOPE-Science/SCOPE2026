#!/usr/bin/env python3
"""Direct finite-field checks for nilpotent commuting tuples in W_1(1) at p=5."""
import itertools
P=5
E=range(P)
X=list(itertools.product(E, repeat=5))
def mul(a,b):
    z=[0]*5
    for i in range(5):
        for j in range(5-i): z[i+j]=(z[i+j]+a[i]*b[j])%P
    return tuple(z)
def deriv(a):return (a[1],2*a[2]%P,3*a[3]%P,4*a[4]%P,0)
def bracket(a,b):
    f=mul(a,deriv(b));g=mul(b,deriv(a));return tuple((x-y)%P for x,y in zip(f,g))
def act(a,b):return mul(a,deriv(b))
def isnil(a):
    for b in [(1,0,0,0,0),(0,1,0,0,0),(0,0,1,0,0),(0,0,0,1,0),(0,0,0,0,1)]:
        c=b
        for _ in range(5):c=act(a,c)
        if any(c):return False
    return True
N=[a for a in X if isnil(a)]
assert len(N)==5**4,len(N)
def ty(a):
    if not any(a):return 'zero'
    for i,x in enumerate(a):
        if x:
            return ('open' if i==0 else f'order{i}')
assert set(ty(x) for x in N)=={'zero','open','order2','order3','order4'}
csizes={'zero':625,'open':5,'order2':25,'order3':25,'order4':125}
from collections import Counter
counts=Counter(ty(x) for x in N)
assert counts=={'zero':1,'open':500,'order2':100,'order3':20,'order4':4},counts
comm={x:[y for y in N if not any(bracket(x,y))] for x in N}
assert all(len(comm[x])==csizes[ty(x)] for x in N)
c2=sum(len(v) for v in comm.values())
formula=lambda m:(P+1)*P**(2*m)+(P**3-P)*P**m-P**3
assert c2==formula(2),(c2,formula(2))
# Compute commuting ordered pairs in each centralizer, independent of global formula.
# For each type, test one representative with direct nested bracket checks.
reps={t:next(x for x in N if ty(x)==t) for t in csizes}
H=lambda r:P**r*((P+1)*P**r-P)
for t,x in reps.items():
    if t=='zero':continue
    ys=comm[x]; brute=sum(not any(bracket(y,z)) for y in ys for z in ys)
    want=H(2) if t=='order4' else len(ys)**2
    assert brute==want,(t,brute,want)
c3=c2 + counts['open']*P**2 + (counts['order2']+counts['order3'])*P**4 + counts['order4']*H(2)
assert c3==formula(3),(c3,formula(3))
# Nilpotents of t-adic order >=2 form Heisenberg subalgebra.
A=[x for x in N if x[0]==x[1]==0]
assert len(A)==P**3
assert len([x for x in A if x[2]==x[3]==0])==P
print('WITT5_NILPOTENT_ALL_ARITY_OK', len(X),len(N),c2,c3,'centralizer types',dict(counts))
