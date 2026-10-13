"""Exact-rational reconstruction of the two-step Kaczmarz sampling example.

No third-party modules are required.  The input vector depends affinely on t.
Polynomial comparisons below cover the ENTIRE real interval [1/2, 3/2].
"""
from fractions import Fraction as Q
from itertools import combinations, product

ROWS = ((3, -4, 2), (3, -2, -4), (2, 3, -4))
LEFT, RIGHT = Q(1, 2), Q(3, 2)
# Represent affine scalars as (constant coefficient, coefficient of t).
INITIAL = ((Q(-10), Q(0)), (Q(0), Q(1)), (Q(-30), Q(0)))


def dot(a, b):
    return sum((x*y for x,y in zip(a,b)), Q(0))


def residual(row, y):
    return (sum((row[i] * y[i][k] for i in range(3)), Q(0)) for k in range(2))


def eval_affine(affine, t):
    return affine[0] + affine[1] * t


def project(y, i):
    row = ROWS[i]
    r = tuple(residual(row,y))
    return tuple(tuple(y[k][d] - Q(row[k],29)*r[d] for d in range(2)) for k in range(3))


def square_poly(y):
    a = sum((v[0]*v[0] for v in y), Q(0))
    b = sum((2*v[0]*v[1] for v in y), Q(0))
    c = sum((v[1]*v[1] for v in y), Q(0))
    return (a,b,c)


def min_quadratic_on_interval(p):
    a,b,c = p
    probes = [LEFT, RIGHT]
    if c>0:
        vertex = -b/(2*c)
        if LEFT < vertex < RIGHT:
            probes.append(vertex)
    return min(a+b*t+c*t*t for t in probes)


BRANCH_TESTS=0

def pick(subset, y):
    global BRANCH_TESTS
    rs = [tuple(residual(row,y)) for row in ROWS]
    chosen = max(subset, key=lambda i:abs(eval_affine(rs[i],Q(1))))
    ci = rs[chosen]
    for j in subset:
        if j == chosen: continue
        cj = rs[j]
        # Squared absolute-residual margin as a quadratic polynomial in t.
        margin=(ci[0]**2-cj[0]**2,
                2*(ci[0]*ci[1]-cj[0]*cj[1]),
                ci[1]**2-cj[1]**2)
        assert min_quadratic_on_interval(margin)>0,(subset,chosen,j,margin)
        BRANCH_TESTS += 1
    return chosen


def exact_expectation(beta):
    subsets = list(combinations(range(3), beta))
    acc=[Q(0),Q(0),Q(0)]
    paths=[]
    for s1,s2 in product(subsets,repeat=2):
        i=pick(s1,INITIAL)
        y=project(INITIAL,i)
        j=pick(s2,y)
        z=project(y,j)
        val=square_poly(z)
        paths.append((s1,s2,i,j))
        for k in range(3): acc[k]+=val[k]
    return tuple(v/Q(len(paths)) for v in acc), paths


def det3(r):
    a,b,c=r
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def main():
    assert det3(ROWS)==70
    assert all(sum(a*a for a in row)==29 for row in ROWS)
    expected={
        1:(Q(4*30675050,219501),Q(-4*839010,219501),Q(4*26103,219501)),
        2:(Q(2*57312850,219501),Q(-2*2466480,219501),Q(2*43707,219501)),
        3:(Q(4*3628725,24389),Q(-4*170920,24389),Q(4*2836,24389)),
    }
    outcomes={}
    for beta in (1,2,3):
        result, paths=exact_expectation(beta)
        assert result==expected[beta], (beta,result,expected[beta])
        outcomes[beta]=result
        print('sample size',beta,'F(t) coefficients',result)
        print('F(1) =',sum(result), 'paths=',len(paths))
        if beta==3: assert paths==[((0,1,2),(0,1,2),2,0)]
    diff12=tuple(outcomes[1][i]-outcomes[2][i] for i in range(3))
    diff31=tuple(outcomes[3][i]-outcomes[1][i] for i in range(3))
    assert diff12==(Q(2*1345750,73167),Q(2*262820,73167),Q(2*2833,73167))
    assert diff31==(Q(4*1983475,219501),Q(-4*699270,219501),Q(-4*579,219501))
    assert min_quadratic_on_interval(diff12)>0
    assert min_quadratic_on_interval(diff31)>0
    print('all strict branch margins verified on [1/2,3/2]; comparisons=',BRANCH_TESTS)
    print('all mean-square and dominance identities PASS')

if __name__=='__main__': main()
