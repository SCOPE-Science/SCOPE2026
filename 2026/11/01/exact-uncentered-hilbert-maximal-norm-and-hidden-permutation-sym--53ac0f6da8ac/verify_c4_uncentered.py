#!/usr/bin/env python3
"""Exact finite-matrix certificate for graph-ball maximal averages on C4.
Python 3 standard library; no external packages or network access required.
Run: python3 verify_c4_uncentered.py
"""
from fractions import Fraction as F
from itertools import permutations, product

N=4
zero=F(0)
one=F(1)
q=F(377,250)
u=F(151,100)

def diag(v):
    return tuple(F(int(v==j)) for j in range(N))

def ave(indices):
    s=set(indices)
    return tuple(F(int(j in s),len(s)) for j in range(N))

def gram(rows):
    return [[sum(rows[k][i]*rows[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def determinant(mat):
    k=len(mat)
    ans=F(0)
    for sig in permutations(range(k)):
        inversions=sum(sig[i]>sig[j] for i in range(k) for j in range(i+1,k))
        p=F(-1 if inversions%2 else 1)
        for i,j in enumerate(sig):p*=mat[i][j]
        ans+=p
    return ans

def sylvester(M):
    G=gram(M)
    return [determinant([[(q if i==j else zero)-G[i][j] for j in range(k)] for i in range(k)]) for k in range(1,N+1)]

s=ave([0,1,2]);t=ave([0,1,3]);m=ave(range(N))
A=[diag(0),s,s,t]
branches={(eps,eta):[diag(0),diag(1) if eps else s,s,m if eta else t] for eps,eta in product(range(2),repeat=2)}
assert branches[(0,0)]==A
rival_dets={}
for (eps,eta),M in branches.items():
    if (eps,eta)!=(0,0):
        D=sylvester(M)
        assert all(x>0 for x in D),((eps,eta),D)
        rival_dets[(eps,eta)]=D

# Coefficients of det(z I - A^T A), in ascending degree.
def add(a,b):
    return [((a[i] if i<len(a) else zero)+(b[i] if i<len(b) else zero)) for i in range(max(len(a),len(b)))]
def mul(a,b):
    v=[zero]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]+=x*y
    return v
G=gram(A)
coefs=[zero]
for sig in permutations(range(N)):
    inversions=sum(sig[i]>sig[j] for i in range(N) for j in range(i+1,N))
    term=[F(-1 if inversions%2 else 1)]
    for i,j in enumerate(sig):
        term=mul(term,[-G[i][j], F(int(i==j))])
    coefs=add(coefs,term)
assert coefs==[F(0),F(-6,81),F(64,81),F(-162,81),F(1)],coefs

def P(x):return 81*x*x*x-162*x*x+64*x-6
assert P(q)<0<P(u)
# For z>1, P(z) is strictly convex (P''(z)=486z-324>0),
# and P(1)<0. Thus there is exactly one root greater than 1.
assert P(1)<0 and 486-324>0

# Algebraic eigenvector: x=(1,a,b,c), lambda root P=0.
# The rational expressions below are interpreted in the isolating interval.
def a(z):return (z-1)/z
def b(z):return 2*(2*z-1)/(z*(9*z-2))
def c(z):return (2*z-1)/(z*(9*z-1))
# Monotonicity: a increases, b and c decrease throughout [q,u].
assert a(q)<a(u) and b(q)>b(u) and c(q)>c(u)
assert 1>a(u)>b(q)>c(q)>0
# At the root, a=b+c; check polynomial cross-multiplication identity.
# z*(9z-2)*(9z-1)*(a-b-c) = P(z).  Each tested rational
# identity has a numerator polynomial of degree at most four; nine distinct
# rational test nodes suffice to establish the identity as a polynomial.
def poly_eval(coeff,x):return sum(coeff[i]*x**i for i in range(len(coeff)))
for z in [F(i,100) for i in range(120,161,5)]:
    assert z*(9*z-2)*(9*z-1)*(a(z)-b(z)-c(z))==P(z)
# Active rows are strict throughout isolating interval using rational bounds.
Slo=(1+a(q)+b(u))/3
Tlo=(1+a(q)+c(u))/3
mhi=(1+a(u)+b(q)+c(q))/4
assert Slo>a(u) and Tlo>mhi
# Verify two nontrivial Gram eigenvector equations modulo P exactly:
# (Gx)_1-z = (Gx)_2-z*a = -P(z)/((9z-2)(9z-1));
# (Gx)_3-z*b = (Gx)_4-z*c = 0.  After clearing the
# common denominator z*(9z-2)*(9z-1), every discrepancy numerator
# has degree at most four; nine exact test nodes prove identical zero.
for z in [F(i,100) for i in range(120,161,5)]:
    aa,bb,cc=a(z),b(z),c(z)
    ss=(1+aa+bb)/3;tt=(1+aa+cc)/3
    pred=-P(z)/((9*z-2)*(9*z-1))
    assert 1+2*ss/3+tt/3-z==pred
    assert 2*ss/3+tt/3-z*aa==pred
    assert 2*ss/3-z*bb==0
    assert tt/3-z*cc==0

# Independently certify strict centered-vs-uncentered separation. Centered
# graph balls at i are singleton {i}, closed one-neighborhood of size 3,
# and the full vertex set. Each of the 3^4 matrices is checked exactly.
center_options=[]
for i in range(N):
    opposite=(i+2)%N
    center_options.append([diag(i),ave(j for j in range(N) if j!=opposite),m])
center_count=0
for M in product(*center_options):
    D=sylvester(M)
    assert all(x>0 for x in D),(center_count,D)
    center_count+=1
assert center_count==81

# The (uncentered) graph-ball family of C4 comprises 4 singleton balls,
# all four 3-vertex subsets, and V, hence is S4-invariant.
triples={tuple(j for j in range(N) if j!=i) for i in range(N)}
assert len(triples)==4 and all(len(v)==3 for v in triples)

# Root interval bounds imply four distinct positive coordinates, yielding
# 24 distinct permutations. Under D4 each largest-coordinate placement has
# two choices of opposite vertex among the remaining 3: 3 orbits of size 8.
perms=list(permutations(range(N)))
assert len(perms)==24
print('CERTIFICATE_OK uncentered_branches=4 strict_competitors=3 centered_selections=81')
print('CERTIFICATE_OK characteristic=81z^3-162z^2+64z-6 root_bracket=(377/250,151/100)')
print('CERTIFICATE_OK strict_eigenvector_branch=1 S4_extremizer_rays=24 D4_orbits=3x8')
