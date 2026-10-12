"""Exact finite-field checks for the power-sum Bring model.

The proof of the universal statements is in RESULT.md. This script enumerates
representative small prime fields and checks the characteristic-five line model.
"""
from itertools import product, permutations, combinations
from collections import Counter


def normalize(pt, p):
    a = next(x for x in pt if x % p)
    inv = pow(a, -1, p)
    return tuple((x * inv) % p for x in pt)


def points_proj4(p):
    # Each point has one representative with first nonzero coordinate 1.
    for i in range(5):
        for tail in product(range(p), repeat=4-i):
            yield (0,) * i + (1,) + tail


def in_curve(pt, p):
    return all(sum(pow(x, k, p) for x in pt) % p == 0 for k in (1, 2, 3))


def jac_rank(pt, p):
    mat = [[1] * 5, [2*x % p for x in pt], [3*x*x % p for x in pt]]
    r = 0
    for j in range(5):
        z = next((i for i in range(r, 3) if mat[i][j]), None)
        if z is None:
            continue
        mat[r], mat[z] = mat[z], mat[r]
        inv = pow(mat[r][j], -1, p)
        mat[r] = [v * inv % p for v in mat[r]]
        for i in range(3):
            if i != r:
                s = mat[i][j]
                mat[i] = [(v - s * w) % p for v, w in zip(mat[i], mat[r])]
        r += 1
        if r == 3:
            break
    return r


def lines_p5():
    E = (1,) * 5
    out = {}
    for v in permutations(range(5)):
        pts = frozenset(normalize(tuple((s*e+t*w) % 5 for e,w in zip(E,v)),5)
                        for s,t in product(range(5),repeat=2) if s or t)
        out[pts] = v
    return out


def run():
    lines = lines_p5()
    assert len(lines) == 6
    P = normalize((1,)*5, 5)
    assert all(len(line) == 6 and P in line for line in lines)
    assert all(a & b == {P} for a,b in combinations(lines,2))
    for line in lines:
        assert all(in_curve(q,5) for q in line)
    q5 = {pt for pt in points_proj4(5) if in_curve(pt,5)}
    assert len(q5) == 31 == len(set.union(*(set(x) for x in lines)))
    assert q5 == set.union(*(set(x) for x in lines))
    assert {q for q in q5 if jac_rank(q,5) < 3} == {P}
    # Direct conic-cubic factor intersection in three affine direction coordinates.
    # Coordinates t1,t2,t3, t4=-(t1+t2+t3), t5=0.
    base = []
    for a,b,c in product(range(5),repeat=3):
        if a==b==c==0:
            continue
        d = (-a-b-c)%5
        if (a*a+b*b+c*c+d*d)%5==0 and (a*a*a+b*b*b+c*c*c+d*d*d)%5==0:
            base.append(normalize((a,b,c,d,0),5))
    assert len(set(base)) == 6
    # The conic and cubic meet transversely at each of the six points.
    # Their combined projective degree is 2*3=6, so these six distinct
    # simple geometric points exhaust the complete intersection.
    for a,b,c,d,e in set(base):
        A,B,C = (a+b)%5,(a+c)%5,(b+c)%5
        assert sum(z==0 for z in (A,B,C)) == 1
        gq = tuple(2*(2*t + u + v)%5 for t,u,v in
                   ((a,b,c),(b,a,c),(c,a,b)))
        gc = tuple((-3*w)%5 for w in (B*C+A*C, B*C+A*B, A*C+A*B))
        assert any((gq[i]*gc[j]-gq[j]*gc[i])%5 for i,j in combinations(range(3),2))
    for a,b,c in product(range(5), repeat=3):
        d = (-a-b-c) % 5
        q = (a*a+b*b+c*c+d*d) % 5
        h = (a*a*a+b*b*b+c*c*c+d*d*d) % 5
        assert q == 2*(a*a+b*b+c*c+a*b+b*c+c*a) % 5
        assert h == -3*(a+b)*(b+c)*(c+a) % 5
    # Degrees in each variable are <5, so equality on all F5^3
    # verifies these polynomial identities coefficientwise in F5.
    # Characteristic 2 and 3: projective surfaces, not curves.
    for p in (2,3):
        pts = [v for v in points_proj4(p) if in_curve(v,p)]
        assert all(jac_rank(v,p)==2 for v in pts)
        print('special-surface', p, 'rational points', len(pts))
    for p in (7,11,13):
        pts = [v for v in points_proj4(p) if in_curve(v,p)]
        assert all(jac_rank(v,p)==3 for v in pts)
        print('smooth-curve', p, 'rational points',len(pts))
    print('VERIFY_OK: six F5 lines, exactly 31 F5 points, unique singular point; smooth small-prime fibers')


if __name__=='__main__':
    run()
