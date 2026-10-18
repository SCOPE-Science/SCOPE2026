"""Exact integer certificate for tetrahedra in a rhombic dodecahedron.

Run: python verify.py
The infinite-parameter bound is proved analytically in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


def det3_independent(a,b,c):
    cols=(a,b,c)
    total=0
    for order in permutations(range(3)):
        inversions=sum(order[i]>order[j] for i in range(3) for j in range(i+1,3))
        term=1 if inversions%2==0 else -1
        for row in range(3):
            term*=cols[row][order[row]]
        total+=term
    return total


def tetra_det(v):
    cols=[[v[j][i]-v[0][i] for i in range(3)] for j in range(1,4)]
    p=det3(*cols)
    assert p==det3_independent(*cols)
    return p


def main():
    corners=list(product((-1,1),repeat=3))
    axes=[tuple((2*s if j==i else 0) for j in range(3)) for i in range(3) for s in (-1,1)]
    vertices=axes+corners
    assert len(vertices)==14 and len(set(vertices))==14
    histogram=Counter()
    max_abs=0
    maximal=[]
    for ids in combinations(range(14),4):
        d=abs(tetra_det([vertices[i] for i in ids]))
        k=sum(i<6 for i in ids)
        histogram[(k,d)]+=1
        if d>max_abs:
            max_abs=d
            maximal=[]
        if d==max_abs:
            maximal.append(frozenset(ids))
    expect={
      0:{0:12,8:56,16:2},
      1:{0:48,4:144,8:96,12:48},
      2:{0:72,4:144,8:144,12:48,16:12},
      3:{4:32,8:96,12:24,20:8},
      4:{0:3,16:12}
    }
    assert histogram==Counter({(k,d):freq for k,row in expect.items() for d,freq in row.items()})
    assert sum(histogram.values())==1001
    assert max_abs==20
    assert len(maximal)==8
    expected=[]
    for e in corners:
        tet={e} | {tuple((-2*e[i] if j==i else 0) for j in range(3)) for i in range(3)}
        expected.append(frozenset(vertices.index(x) for x in tet))
    assert set(maximal)==set(expected)
    assert all(len(p&q)<=2 for p,q in combinations(maximal,2))
    assert Fraction(max_abs,6)==Fraction(10,3)
    assert Fraction(max_abs,6*16)==Fraction(5,24)
    # Four-generator witness gives precisely (S+m)/(6S) for rational samples;
    # no finite sample is used as proof of the bound for all real generators.
    tests=0
    for a,b,c in product((Fraction(0),Fraction(1,3),Fraction(1,2),Fraction(1)), repeat=3):
        generators=((1,0,0),(0,1,0),(0,0,1),(a,b,c))
        signs=((-1,-1,-1,-1),(-1,1,1,1),(1,-1,1,1),(1,1,-1,1))
        pts=[tuple(sum(s[i]*generators[i][j] for i in range(4)) for j in range(3)) for s in signs]
        determinant=det3(*[tuple(pts[t][j]-pts[0][j] for j in range(3)) for t in (1,2,3)])
        assert determinant==8*(2+a+b+c)
        minors=[abs(det3(*[generators[i] for i in range(4) if i!=skip])) for skip in range(4)]
        assert minors==[a,b,c,1]
        S=sum(minors)
        assert Fraction(determinant,6*8*S)==(S+1)/(6*S)
        tests+=1
    print('VERIFY_OK vertex_sets=1001 max_determinant=20 maximizing_sets=8 max_intersection=2 parameter_samples='+str(tests))


if __name__=='__main__':
    main()
