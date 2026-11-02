#!/usr/bin/env python3
"""Exact finite-field certificate for the characteristic-five Bring complete intersection.
No external dependencies. All arithmetic is in F_5.
"""
from itertools import permutations
from math import comb
P=5

def canonical(v):
    """Direction modulo scaling and translation by the all-one vector."""
    den=(v[0]-v[4])%P
    assert den
    iv=pow(den,-1,P)
    return tuple(((v[i]-v[4])*iv)%P for i in range(5))

vectors=sorted(set(canonical(t) for t in permutations(range(P))))
assert len(vectors)==6, vectors
for v in vectors:
    assert sorted(v)==list(range(P))
    assert all(sum(pow(t,j,P) for t in v)%P==0 for j in (1,2,3))
    a,b,c=v[:3];d=v[3]
    assert (a+b+c+d)%P==0
    Q=(a*a+b*b+c*c+d*d)%P
    C=(a*a*a+b*b*b+c*c*c+d*d*d)%P
    assert (Q,C)==(0,0)
print('DIRECTIONS_F5=',vectors)
print('SIX_DISTINCT_LINES_ON_THE_CI_OK')

def mod_rank(mat):
    a=[list(map(lambda t:t%P,row)) for row in mat]
    m=len(a); n=len(a[0])
    r=0
    for j in range(n):
        piv=next((i for i in range(r,m) if a[i][j]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][j],-1,P)
        a[r]=[(x*inv)%P for x in a[r]]
        for i in range(m):
            if i!=r and a[i][j]:
                t=a[i][j]
                a[i]=[(a[i][h]-t*a[r][h])%P for h in range(n)]
        r+=1
        if r==m: break
    return r

h=[]
for n in range(4):
    mons=[(i,j,n-i-j) for i in range(n+1) for j in range(n-i+1)]
    ev=[[pow(v[0],i,P)*pow(v[1],j,P)*pow(v[2],k,P)%P for i,j,k in mons] for v in vectors]
    h.append(mod_rank(ev))
assert h==[1,3,5,6],h
assert sum(6-t for t in h)==9
print('LOCAL_HILBERT_VALUES=',h,'DELTA=9')

S5=list(permutations(range(5)))
assert len(S5)==120
for sigma in S5:
    transformed={canonical(tuple(v[sigma[i]] for i in range(5))) for v in vectors}
    assert transformed==set(vectors)
first=vectors[0]
stabilizer=[sigma for sigma in S5 if canonical(tuple(first[sigma[i]] for i in range(5)))==first]
assert len(stabilizer)==20
assert len({canonical(tuple(first[sigma[i]] for i in range(5))) for sigma in S5})==6
print('SYMMETRY_TRANSITIVE_S5_ACTION_OK; STABILIZER_ORDER=20')

# The defining equations are a regular (1,2,3) complete intersection:
# in the vertex chart, Q/2=a²+b²+c²+ab+ac+bc has Gram I+J,
# determinant 4 mod 5, and C=-3(a+b)(a+c)(b+c).
# Q is irreducible; C cannot contain Q. Bezout gives total six
# reduced transverse points as witnessed above.
mat=[[2,1,1],[1,2,1],[1,1,2]]
det=(mat[0][0]*(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
     -mat[0][1]*(mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0])
     +mat[0][2]*(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0]))%5
assert det==4
assert 1+6*(2+3-4)//2==4
print('SMOOTH_PROJECTIVE_CONIC_AND_REDUCED_INTERSECTION_OK; PA=4')
print('VERIFY_OK')
