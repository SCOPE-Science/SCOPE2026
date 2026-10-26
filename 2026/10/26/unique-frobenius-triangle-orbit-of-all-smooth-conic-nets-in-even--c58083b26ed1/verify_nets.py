"""Exact finite-field checks for all-smooth nets of plane conics.
The arithmetic is completely specified in this file.
"""
from itertools import product


def tables(q):
    assert q in (2, 4)
    if q == 2:
        mul = [[a & b for b in range(q)] for a in range(q)]
    else:
        # Field F_2[u]/(u^2+u+1), with bit-coded elements 0,1,u,1+u.
        mul = []
        for a in range(4):
            row = []
            for b in range(4):
                c = 0
                for i in range(2):
                    for j in range(2):
                        if (a >> i & 1) and (b >> j & 1):
                            c ^= 1 << (i+j)
                if c & 4:
                    c ^= 7  # u^2 = u+1
                row.append(c)
            mul.append(row)
    return mul


def projective_points(q):
    return [(1, y, z) for y in range(q) for z in range(q)] + [(0, 1, z) for z in range(q)] + [(0, 0, 1)]


def anisotropic_graph_count(q):
    # Every smooth net projects isomorphically onto the 3D polar-form space.
    # Its 9 square coefficients A_{ij} specify the cubic
    # C(r) = r1*r2*r3 + sum_i,j r_i^2 A_ij r_j.
    mul = tables(q)
    points = projective_points(q)
    tests = []
    for r in points:
        b = mul[mul[r[0]][r[1]]][r[2]]
        weights = [mul[mul[r[i]][r[i]]][r[j]] for i in range(3) for j in range(3)]
        test = [[mul[weights[k]][a] for a in range(q)] for k in range(9)]
        tests.append((b, test))
    accepted = []
    for A in product(range(q), repeat=9):
        for const, terms in tests:
            val = const
            for k in range(9):
                val ^= terms[k][A[k]]
            if val == 0:
                break
        else:
            accepted.append(A)
    return accepted


def smooth_conic_count_F2():
    good = []
    for c in range(64):
        a,b,d,e,f,g = [(c >> i) & 1 for i in range(6)]
        # a*X^2+b*Y^2+d*Z^2+e*XY+f*XZ+g*YZ.
        x,y,z = g,f,e
        val = (a*x + b*y + d*z + e*x*y + f*x*z + g*y*z) & 1
        if (x or y or z) and val:
            good.append(c)
    nets=set()
    for aa in good:
        for bb in good:
            if bb <= aa:continue
            for cc in good:
                if cc <= bb or cc == aa^bb:continue
                span = frozenset((aa,bb,cc,aa^bb,aa^cc,bb^cc,aa^bb^cc))
                if span.issubset(good):nets.add(span)
    return len(good),len(nets)


def expected(q):
    return q**3*(q-1)**2*(q+1)//3


if __name__=='__main__':
    for q in (2,4):
        found=anisotropic_graph_count(q)
        print(f'q={q}: graph nets={len(found)} expected={expected(q)} match={len(found)==expected(q)}')
        if q==2:
            print('q=2: accepted graph matrices as 9-digit words:', [''.join(map(str,x)) for x in found])
    smooth,nets=smooth_conic_count_F2()
    print(f'q=2 independent all-linear-subspace check: smooth conics={smooth}, all-smooth nets={nets}')
    assert nets==len(anisotropic_graph_count(2))==expected(2)
