"""Exact combinatorial checks and independent rational polygon example.

The infinite theorems rely on the written proof, not this finite test.
"""
from fractions import Fraction as F
from math import gcd


def reflected_fan_cover(r, k):
    assert r >= 2 and k >= 1
    n = 2*r
    length = r-1
    directions = (n*k + length - 1)//length
    starts = [(n*j)//directions for j in range(directions)]
    coverage = [sum(((i-s) % n) < length for s in starts) for i in range(n)]
    assert min(coverage) >= k, (r,k,directions,starts,coverage)
    assert (directions - 1)*length < n*k <= directions*length
    return directions, min(coverage)


def optimal_weight_classes(r):
    n = 2*r
    length = r-1
    for j in range(n):
        assert sum(((i-j) % n) < length for i in range(n)) == length
    assert gcd(n, length) == (1 if r%2 == 0 else 2)
    if r % 2 == 0:
        weights = [F(1,length)] * n
    else:
        # One endpoint in the alternating family (zero mass on one parity).
        weights = [F(2,length) if j%2 == 0 else F(0) for j in range(n)]
    for i in range(n):
        assert sum((weights[j] for j in range(n) if ((i-j)%n) < length),F(0)) == 1
    assert sum(weights,F(0)) == F(n,length)


def noncentrosymmetric_nonequiangular_hexagon():
    u = [(F(1),F(0)),(F(3,5),F(4,5)),(F(-5,13),F(12,13))]
    cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
    d=[cross(u[1],u[2]), cross(u[2],u[0]), cross(u[0],u[1])]
    assert d == [F(56,65),F(-12,13),F(4,5)]
    assert all(x > -2 and x < 2 for x in d)
    assert all(sum((d[j]*u[j][i] for j in range(3)), F(0)) == 0 for i in range(2))
    seq=u+[(-v[0],-v[1]) for v in u]
    edge_lengths=[F(1)+x/2 for x in d]+[F(1)-x/2 for x in d]
    edges=[(edge_lengths[j]*seq[j][0],edge_lengths[j]*seq[j][1]) for j in range(6)]
    assert all(cross(edges[j],edges[(j+1)%6])>0 for j in range(6))
    assert all(sum((e[i] for e in edges),F(0)) ==0 for i in range(2))
    assert any(edge_lengths[j]!=edge_lengths[j+3] for j in range(3))
    # The first and second consecutive angular turns differ since the unit
    # direction dot products are 3/5 and 33/65, respectively.
    dot=lambda a,b:a[0]*b[0]+a[1]*b[1]
    assert dot(u[0],u[1]) != dot(u[1],u[2])
    verts=[(F(0),F(0))]
    for dx,dy in edges:
        x,y=verts[-1]; verts.append((x+dx,y+dy))
    assert verts[-1]==verts[0]
    return len(verts)-1


def main():
    cases=0
    for r in range(2,41):
        optimal_weight_classes(r)
        for k in range(1,51):
            reflected_fan_cover(r,k)
            cases+=1
    assert noncentrosymmetric_nonequiangular_hexagon()==6
    print('VERIFY_OK: %d exact cyclic multicover cases; parity of optimal weight cells; rational noncentral, nonequiangular hexagon.'%cases)

if __name__=='__main__':
    main()
