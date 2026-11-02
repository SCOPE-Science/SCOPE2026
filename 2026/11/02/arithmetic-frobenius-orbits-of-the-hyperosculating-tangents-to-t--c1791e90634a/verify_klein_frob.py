#!/usr/bin/env python3
"""Exact finite-field verification of the hyperflex Frobenius orbits on a plane quartic.

This is a supplementary finite-field check, not a substitute for the uniform proof.
Only the Python standard library is required.
"""
from collections import Counter
from itertools import product

P = 3
MOD = [2, 1, 0, 0, 0, 0, 1]  # v^6 + v + 2 over F_3

def poly_mod(a, b):
    a = list(a)
    while len(a) >= len(b):
        c = a[-1] * pow(b[-1], -1, P) % P
        if c:
            for k in range(len(b)):
                a[len(a)-len(b)+k] = (a[len(a)-len(b)+k] - c*b[k]) % P
        a.pop()
    return a

# No polynomial of degree 1, 2, or 3 divides the degree-6 modulus.
for n in (1, 2, 3):
    for c in product(range(P), repeat=n):
        assert any(poly_mod(MOD, list(c) + [1])), (n,c)

def vec(a):
    return [(a//(P**i))%P for i in range(6)]

def enc(a):
    return sum(int(c % P)*(P**i) for i,c in enumerate(a))

def add(a,b):
    return enc([(x+y)%P for x,y in zip(vec(a),vec(b))])

def neg(a):
    return enc([(-x)%P for x in vec(a)])

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    if a == 0 or b == 0: return 0
    x,y = vec(a),vec(b)
    c = [0]*11
    for i in range(6):
        for j in range(6):
            c[i+j] = (c[i+j] + x[i]*y[j])%P
    for i in range(10,5,-1):
        k=c[i]
        c[i]=0
        c[i-6] = (c[i-6]+k)%P     # v^6 = -v-2 = 2v+1 in F3!
        c[i-5] = (c[i-5]+2*k)%P
    return enc(c[:6])

def power(a,n):
    ans=1
    while n:
        if n&1:ans=mul(ans,a)
        a=mul(a,a)
        n//=2
    return ans

assert power(3,729)==3
for x in range(1,729):
    assert power(x,728)==1

roots=[]
for u in range(1,729):
    y=power(u,10)
    # Direct substitution F(1,y,u)=y+y³u+u³.
    curve=add(add(y,mul(power(y,3),u)),power(u,3))
    # On tangent L=u³X+Y+y³Z, the cubic coefficient equals 1-u*y^9.
    hyperflex=sub(1,mul(u,power(y,9)))
    if curve==0 and hyperflex==0:
        roots.append(u)
        assert power(u,91)==1
        t=power(u,7)
        assert add(add(power(t,4),t),1)==0
assert len(roots)==28
assert all(power(u,91)==1 and add(add(power(power(u,7),4),power(u,7)),1)==0 for u in roots)
# Verify exact identity of all roots of the parametrization.
roots2=[u for u in range(1,729) if power(u,91)==1 and add(add(power(u,28),power(u,7)),1)==0]
assert roots==roots2

# Distinct tangent lines: all normalized by coefficient of Y=1.
tangents={(power(u,3),1,power(u,30)) for u in roots}
assert len(tangents)==28

# Frobenius acts on normalized parameter by cube.
unused=set(roots)
lengths=[]
while unused:
    a=next(iter(unused)); orbit=[];v=a
    while v not in orbit:
        assert v in unused
        orbit.append(v)
        v=power(v,3)
    assert v==a
    unused.difference_update(orbit)
    lengths.append(len(orbit))
assert sorted(lengths)==[1,3,6,6,6,6], sorted(lengths)
assert Counter(lengths)==Counter({1:1,3:1,6:4})
for n in range(1,13):
    actual=sum(power(u,3**n)==u for u in roots)
    predicted=1+(3 if n%3==0 else 0)+(24 if n%6==0 else 0)
    assert actual==predicted, (n,actual,predicted)
# Classify primitive root orders; order-7, -13, -91 components.
orders=Counter()
for u in roots:
    order=next(d for d in (1,7,13,91) if power(u,d)==1)
    orders[order]+=1
assert orders==Counter({1:1,7:6,13:3,91:18}), orders
print('KLEIN_CHAR3_HYPERFLEX_28_ORBITS_1_3_6_6_6_6_F729_PASS')
print('root_orders', sorted(orders.items()))
print('frobenius_orbit_lengths', sorted(lengths))
print('rational hyperflexes over F3, F9, F27, F729:', [sum(power(u,3**n)==u for u in roots) for n in (1,2,3,6)])
