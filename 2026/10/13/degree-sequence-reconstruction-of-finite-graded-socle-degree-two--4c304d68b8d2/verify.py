"""Finite-field checks for the zero-divisor-graph reconstruction formula.

The algebra multiplication is (v,c)(w,e)=B(v,w)z on the maximal ideal.
Only small prime fields are enumerated; the general claim uses a proof.
"""
from itertools import product
from collections import Counter


def mat_bilin(v, w, mat, p):
    return sum(v[i]*mat[i][j]*w[j] for i in range(len(v)) for j in range(len(v))) % p


def stats(p, matrix):
    d=len(matrix)
    vectors=list(product(range(p), repeat=d))
    zeros=sum(mat_bilin(v,v,matrix,p)==0 for v in vectors)
    expected_zero = p**(d-1)
    is_alternating = p == 2 and all(matrix[i][i]%2==0 for i in range(d))
    if p==2 and is_alternating:
        expected_zero=p**d
    if p%2 and d%2==0:
        determinant = det_mod(matrix,p)
        discriminant = ((-1)**(d//2)*determinant)%p
        chi = 1 if pow(discriminant,(p-1)//2,p)==1 else -1
        expected_zero += chi*(p-1)*p**((d-2)//2)
    assert zeros == expected_zero,(p,matrix,zeros,expected_zero)
    verts=[(v,c) for v in vectors for c in range(p) if any(v) or c]
    degrees=Counter()
    for v,c in verts:
        deg=sum(mat_bilin(v,w,matrix,p)==0 and ((v,c)!=(w,e)) for w,e in verts)
        degrees[deg]+=1
    expected=Counter()
    expected[p**(d+1)-2]=p-1
    expected[p**d-2]+=p*(zeros-1)
    expected[p**d-1]+=p*(p**d-zeros)
    expected=Counter({degree:count for degree,count in expected.items() if count})
    assert degrees==expected,(p,matrix,degrees,expected)
    assert len(verts)==p**(d+1)-1
    return zeros,dict(sorted(degrees.items()))


def det_mod(m,p):
    a=[[x%p for x in row] for row in m]
    d=len(m); res=1
    for i in range(d):
        piv=next((j for j in range(i,d) if a[j][i]),None)
        assert piv is not None
        if piv!=i:
            a[piv],a[i]=a[i],a[piv];res=-res
        z=a[i][i]
        res=res*z%p
        iz=pow(z,-1,p)
        for j in range(i+1,d):
            f=a[j][i]*iz%p
            for k in range(i,d):a[j][k]=(a[j][k]-f*a[i][k])%p
    return res%p


def diagonal(*d):return [[v if i==j else 0 for j in range(len(d))] for i,v in enumerate(d)]


if __name__=='__main__':
    tests=[(2,diagonal(1,1)),(2,[[0,1],[1,0]]),
        (2,diagonal(1,1,1)),(2,diagonal(1,1,1,1)),
        (2,[[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]),
        (3,diagonal(1,1)),(3,diagonal(1,2)),(3,diagonal(1,1,1)),
        (3,diagonal(1,1,1,1)),(3,diagonal(1,1,1,2)),
        (5,diagonal(1,1)),(5,diagonal(1,2)),(5,diagonal(1,1,1))]
    for p,mat in tests:
        z,degrees=stats(p,mat)
        print('q=',p,'dim=',len(mat),'diagonal=',[mat[i][i] for i in range(len(mat))],
          'isotropic=',z,'degrees=',degrees)
    print('VERIFY_OK')
