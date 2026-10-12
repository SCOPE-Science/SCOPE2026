#!/usr/bin/env python3
"""Independent, exact finite certificate for the weighted quadratic-norm classification."""
from collections import defaultdict

COLLISIONS = [
 ((1,3),(7,1)), ((4,3),(8,1)), ((3,4),(9,2)),
 ((7,4),(11,2)), ((2,5),(10,3)), ((5,5),(11,3)),
 ((5,5),(13,1)), ((1,6),(11,4)), ((2,6),(14,2)),
 ((9,5),(15,1)), ((10,5),(14,3)), ((8,6),(16,2)),
 ((1,7),(17,1)), ((6,7),(18,1)), ((1,8),(19,2)),
 ((16,5),(20,1)), ((5,12),(17,10))]

def bareiss_det(A):
    # Integer fraction-free elimination; exact division is asserted throughout.
    A = [row[:] for row in A]
    n = len(A)
    sign = 1
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            t = next((t for t in range(k+1,n) if A[t][k]),None)
            assert t is not None
            A[k],A[t]=A[t],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]

rows=[]
for ((a,b),(c,d)) in COLLISIONS:
    assert a*a+6*b*b==c*c+6*d*d
    assert all(1<=j<=20 for j in (a,b,c,d))
    row=[0]*20
    for i,t in ((a,1),(b,6),(c,-1),(d,-6)):
        row[i-1]+=t
    rows.append(row)
assert len(rows)==17
assert all(sum(row)==0 and sum(row[i]*(i+1)**2 for i in range(20))==0 and sum(row[i]*(-1)**(i+1) for i in range(20))==0 for row in rows)
minor=[r[3:] for r in rows]
assert bareiss_det(minor)==432
assert bareiss_det([[1,j*j,(-1)**j] for j in (1,2,3)]) != 0
# The 20-coordinate collision space is exactly span{1,n^2,(-1)^n}.
for n in range(21,5001):
    y=(n-1)%7+1
    a=(5*n-12*y)//7
    b=(2*n+5*y)//7
    assert n%7 == y%7
    assert 0<a<n and 0<b<n and 0<y<n
    assert (5*n-12*y)%7==0 and (2*n+5*y)%7==0
    assert a*a+6*b*b==n*n+6*y*y
    assert a%2==n%2 and b%2==y%2
# Residue classes uniquely decode the parities of all represented pairs.
for a in range(1,101):
    for b in range(1,101):
        t=a*a+6*b*b
        weights={0:7,1:5,2:-5,3:-7}
        assert (-1)**a+6*(-1)**b==weights[t%4]
print('EXACT_CERTIFICATE_OK collisions=17 determinant=432 dimension=3 induction_tested=4980 parity_pairs=10000')
