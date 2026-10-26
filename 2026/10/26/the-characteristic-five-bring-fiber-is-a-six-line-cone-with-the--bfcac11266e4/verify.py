"""Exact checks for the characteristic-five power-sum complete intersection.
No external packages are required. The mathematical proof is independent of this script.
"""
from itertools import product, permutations
from collections import Counter
from math import comb

P=5

def q2(v):
    a,b,c=v
    return (a*a+b*b+c*c+(a+b+c)**2)%P

def q3(v):
    a,b,c=v
    return (a**3+b**3+c**3-(a+b+c)**3)%P

def proj3(v):
    for z in v:
        if z%P:
            inv=pow(int(z)%P,-1,P)
            return tuple(int(x)*inv%P for x in v)
    raise ValueError('zero')

base=set()
for v in product(range(P),repeat=3):
    if not any(v):continue
    if q2(v)==q3(v)==0:
        base.add(proj3(v))
assert base == {(1,2,3),(1,2,4),(1,3,2),(1,3,4),(1,4,2),(1,4,3)},base
for a,b,c in base:
    # Critical transversality of the conic and cubic.
    dq2=((2*a+2*(a+b+c))%5,(2*b+2*(a+b+c))%5,(2*c+2*(a+b+c))%5)
    dq3=((3*a*a-3*(a+b+c)**2)%5,(3*b*b-3*(a+b+c)**2)%5,(3*c*c-3*(a+b+c)**2)%5)
    assert any((dq2[i]*dq3[j]-dq2[j]*dq3[i])%5 for i in range(3) for j in range(i+1,3))
    v=(a,b,c,0,-a-b-c)
    assert set(x%5 for x in v)==set(range(5))

# Test both equations before/after lifting any quotient point with any vertex coordinate.
for a,b,c,t in product(range(5),repeat=4):
    x=[(a+t)%5,(b+t)%5,(c+t)%5,t%5,(-a-b-c+t)%5]
    assert sum(x)%5==0
    assert (sum(z*z for z in x)%5)==q2((a,b,c))
    assert (sum(z**3 for z in x)%5)==(q3((a,b,c))+3*t*q2((a,b,c)))%5
assert len(base)==6

# On the six directions, full S5 acts sharply 3-transitively.
base_order=sorted(base)
permactions=set()
for pi in permutations(range(5)):
    images=[]
    for a,b,c in base_order:
        old=[a,b,c,0,(-a-b-c)%5]
        v=[old[i] for i in pi]
        direction=proj3(tuple((v[i]-v[3])%5 for i in range(3)))
        assert direction in base
        images.append(base_order.index(direction))
    permactions.add(tuple(images))
assert len(permactions)==120
assert len({(g[0],g[1],g[2]) for g in permactions})==120

# F_25 = F_5[t]/(t^2+2), since -2=3 is a nonsquare in F_5.
def plus(x,y):return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def prod(x,y):return ((x[0]*y[0]+3*x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
def power(x,n):
    r=(1,0)
    while n:
        if n&1:r=prod(r,x)
        x=prod(x,x);n>>=1
    return r

def count_p3(field):
    one=(1,0);zero=(0,0)
    n=0
    # Unique normalized representatives in P^3: first nonzero entry is 1.
    for start in range(4):
        for suffix in product(field,repeat=3-start):
            a,b,c,t=((zero,)*start+(one,)+suffix)
            s=plus(plus(a,b),c)
            square=plus(plus(plus(power(a,2),power(b,2)),power(c,2)),power(s,2))
            cube=plus(plus(plus(power(a,3),power(b,3)),power(c,3)),tuple((-x)%5 for x in power(s,3)))
            if square==zero and cube==zero:n+=1
    return n
for fld_size,field in [(5,[(i,0) for i in range(5)]),(25,list(product(range(5),repeat=2)))]:
    answer=count_p3(field)
    assert answer==6*fld_size+1,(fld_size,answer)
    print(f'F_{fld_size}: points={answer} (expected {6*fld_size+1})')

# For type (2,3) complete intersections in P^3, Hilbert series (1-z²)(1-z³)/(1-z)^4.
# The Hilbert function stabilizes at 6n-3; this gives arithmetic genus 4.
for n in range(4,10):
    h=comb(n+3,3)-comb(n+1,3)-comb(n,3)+comb(n-2,3) if n>=5 else None
    if n>=5:assert h==6*n-3,(n,h)
print('directions',sorted(base),'PGL2-action',len(permactions),'delta',4+6-1)
print('VERIFY_OK')
