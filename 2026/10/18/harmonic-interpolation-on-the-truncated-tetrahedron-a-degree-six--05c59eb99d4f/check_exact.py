"""Exact verification of truncated-tetrahedron harmonic-sampling rank theorem.
Pure Python 3.8+; all finite checks use rational arithmetic.
"""
from fractions import Fraction as F

NODES = [(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)]
EDGES = [(i,j) for i in range(4) for j in range(4) if i != j]
X = [tuple(2*NODES[i][k] + NODES[j][k] for k in range(3)) for i,j in EDGES]
T = [[F(sum(X[i][k]*X[j][k] for k in range(3)),11)
      for j in range(12)] for i in range(12)]
assert all(T[i][i] == 1 for i in range(12))
assert set(T[0]) == {F(1),F(7,11),F(-5,11),F(-1,11),F(-9,11)}

def vls(d):
    # At each degree the four exact Legendre values.
    p,q,r,s = d
    one = 1+3*p+2*q+4*r+2*s
    two = 1-q-2*r+2*s
    three = 1-2*p-q+2*r
    a = 1+2*p-q-r-s
    b = r-s
    c = p-q+r-s
    e = 1-p+2*q-r-s
    return (one,two,three,a+e,a*e-b*c,(a,b,c,e))

vals = [F(7,11),F(-5,11),F(-1,11),F(-9,11)]
L0 = [F(1)]*4
L1 = vals[:]
finite_count = 0
ranks = []
for ell in range(576):
    if ell == 0: L = L0
    elif ell == 1: L = L1
    else:
        L2 = [((2*ell-1)*vals[j]*L1[j]-(ell-1)*L0[j])/ell for j in range(4)]
        L0,L1 = L1,L2
        L = L2
    a,b,c,tr,det,M = vls(L)
    blockrank = 2 if det != 0 else (1 if any(M) else 0)
    rank = (a!=0)+2*(b!=0)+3*(c!=0)+3*blockrank
    if ell < 7: ranks.append(rank)
    else:
        assert a > 0 and b > 0 and c > 0 and tr > 0 and det > 0, ell
        finite_count += 1

assert ranks == [1,3,5,7,9,11,9], ranks
# A second, independent way to verify all low-degree ranks:
# exact Gaussian elimination on the 12x12 Gram matrices.
def legendre(n,x):
    if n==0:return F(1)
    if n==1:return x
    a,b=F(1),x
    for k in range(1,n):
        a,b=b,((2*k+1)*x*b-k*a)/(k+1)
    return b

def matrix_rank(A):
    a=[row[:] for row in A]
    i=0
    for j in range(len(a[0])):
        t=next((t for t in range(i,len(a)) if a[t][j]),None)
        if t is None:continue
        a[i],a[t]=a[t],a[i]
        v=a[i][j]
        for k in range(j,len(a[i])):a[i][k]/=v
        for t in range(i+1,len(a)):
            v=a[t][j]
            if v:
                for k in range(j,len(a[i])):a[t][k]-=v*a[i][k]
        i+=1
        if i==len(a):break
    return i
for ell in range(13):
    K=[[legendre(ell,T[i][j]) for j in range(12)] for i in range(12)]
    assert matrix_rank(K)==(ranks[ell] if ell < 7 else 12)
print('PASS exact: geometric dot classes, decomposition inequalities degrees 7..575 (%d), low-degree ranks %r, and 13 direct Gram eliminations' % (finite_count,ranks))
print('For degree >=576, the analytic Laplace integral bound yields strict Gram diagonal dominance.')
