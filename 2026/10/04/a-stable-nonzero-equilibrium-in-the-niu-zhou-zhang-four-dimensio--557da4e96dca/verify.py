#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations
from math import gcd, pi

# Source parameters, kept exact.
a,b,c,d,e,f = F(34),F(28),F(13,5),F(4),F(9,5),F(12,5)

# Exact nonzero equilibrium obtained from y=-fx, z=a(f+1)x, z=b+cf.
x=(b+c*f)/(a*(f+1))
y=-f*x
z=b+c*f
w=(f*x*x+d*z)/e
E=(x,y,z,w)
expected=(F(428,1445),F(-5136,7225),F(856,25),F(1432077728,18792225))
assert E==expected

# Verify the vector field vanishes exactly.
Fvec=(a*(y-x)+z, b*x-c*y-x*z, x*y-d*z+e*w, f*x+y)
assert Fvec==(F(0),F(0),F(0),F(0))

# Polynomial utilities, coefficients in ascending powers.
def padd(p,q):
    n=max(len(p),len(q)); r=[F(0)]*n
    for i,v in enumerate(p): r[i]+=v
    for i,v in enumerate(q): r[i]+=v
    while len(r)>1 and r[-1]==0: r.pop()
    return r

def pmul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a0 in enumerate(p):
        for j,b0 in enumerate(q): r[i+j]+=a0*b0
    while len(r)>1 and r[-1]==0: r.pop()
    return r

def pscale(p,s): return [s*v for v in p]

def perm_sign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

J=[
    [-a,a,F(1),F(0)],
    [b-z,-c,-x,F(0)],
    [y,x,-d,e],
    [f,F(1),F(0),F(0)],
]
# det(lambda I-J)
M=[]
for i in range(4):
    row=[]
    for j in range(4):
        row.append([-J[i][j], F(1)] if i==j else [-J[i][j]])
    M.append(row)
P=[F(0)]
for p in permutations(range(4)):
    term=[F(1)]
    for i,j in enumerate(p): term=pmul(term,M[i][j])
    P=padd(P,pscale(term,F(perm_sign(p))))
assert len(P)==5 and P[4]==1

# Scale to the primitive integer polynomial printed in the report.
def lcm(a,b): return a//gcd(a,b)*b
L=1
for q in P: L=lcm(L,q.denominator)
ints=[int(q*L) for q in P]
g=0
for v in ints: g=gcd(g,abs(v))
ints=[v//g for v in ints]
# ascending -> descending expected
expected_desc=[10440125,423869075,4674655710,12506994792,643445784]
assert list(reversed(ints))==expected_desc
A4,A3,A2,A1,A0=expected_desc

# Exact quartic Routh-Hurwitz conditions for all roots in Re(lambda)<0.
assert all(v>0 for v in expected_desc)
D2=A3*A2-A4*A1
D3=A3*A2*A1-A4*A1*A1-A3*A3*A0
assert D2==1850867402738339250 and D2>0
assert D3==23033184284619159659128251000 and D3>0

# Optional Durand-Kerner approximation for readable roots; exact Hurwitz signs above are the proof.
coeff=[float(v)/A4 for v in expected_desc]  # monic, descending

def peval(z):
    v=0j
    for c0 in coeff: v=v*z+c0
    return v
roots=[1+0j, 1j, -1+0j, -1j]
for _ in range(200):
    new=[]
    for i,r in enumerate(roots):
        den=1+0j
        for j,s in enumerate(roots):
            if i!=j: den*=r-s
        if abs(den)<1e-20: den+=1e-20
        new.append(r-peval(r)/den)
    if max(abs(new[i]-roots[i]) for i in range(4))<1e-13:
        roots=new; break
    roots=new
roots=sorted(roots,key=lambda z:z.real)
assert max(abs(peval(r)) for r in roots)<1e-6
assert all(r.real<0 for r in roots)
print('E_exact=', ', '.join(str(v) for v in E))
print('P_desc=', expected_desc)
print('Delta2=', D2)
print('Delta3=', D3)
print('roots_approx=', ', '.join(f'{r.real:.12f}{r.imag:+.12f}j' for r in roots))
print('VERIFY_OK')
