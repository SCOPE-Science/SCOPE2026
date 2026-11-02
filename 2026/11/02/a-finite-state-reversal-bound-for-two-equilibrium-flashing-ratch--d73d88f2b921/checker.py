"""Exact rational checker for a two-phase three-site stochastic ratchet.

Requires Python 3.9 or newer, standard library only.
Run: python checker.py
All assertions use exact rational arithmetic.
"""
from fractions import Fraction as F
import random


def inverse(a):
    n = len(a)
    m = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for i in range(n):
        j = next(j for j in range(i, n) if m[j][i])
        m[i], m[j] = m[j], m[i]
        c = m[i][i]
        m[i] = [v / c for v in m[i]]
        for j in range(n):
            if j != i:
                c = m[j][i]
                m[j] = [u - c * v for u, v in zip(m[j], m[i])]
    return [row[n:] for row in m]


def mv(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def qmatrix(w, c):
    q = [[F(0) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        j = (i + 1) % 3
        x, y = F(c[i], w[i]), F(c[i], w[j])
        q[j][i] += x
        q[i][i] -= x
        q[i][j] += y
        q[j][j] -= y
    return q


def reduced(q):
    # Columns e0-e2 and e1-e2 generate the zero-total-mass subspace.
    return [[q[i][j] - q[i][2] for j in range(2)] for i in range(2)]


def build(w, c, rate):
    qs = [qmatrix(w[a], c[a]) for a in range(2)]
    m = [[F(0) for _ in range(6)] for _ in range(6)]
    for a in range(2):
        for i in range(3):
            for j in range(3):
                m[3*a+i][3*a+j] += qs[a][i][j]
            m[3*a+i][3*a+i] -= rate
            m[3*(1-a)+i][3*a+i] += rate
    return m


def direct(w, c, rate):
    q = build(w, c, rate)
    q[5] = [F(1)] * 6
    inv = inverse(q)
    p = [row[5] for row in inv]
    js = [sum((F(c[a][k], w[a][k])*p[3*a+k] -
               F(c[a][k], w[a][(k+1)%3])*p[3*a+(k+1)%3]
               for a in range(2)), F(0)) for k in range(3)]
    assert js[0] == js[1] == js[2]
    assert sum(p[:3]) == sum(p[3:]) == F(1,2)
    return js[0]


def mat2vec(a, x):
    return [a[0][0]*x[0]+a[0][1]*x[1], a[1][0]*x[0]+a[1][1]*x[1]]


def current_coefficients(w, c):
    qs = [reduced(qmatrix(w[a], c[a])) for a in range(2)]
    invs = [inverse(q) for q in qs]
    h = [[-invs[0][i][j]-invs[1][i][j] for j in range(2)] for i in range(2)]
    trace = h[0][0] + h[1][1]
    det = h[0][0]*h[1][1] - h[0][1]*h[1][0]
    assert trace > 0 and det > 0
    pi = [[F(x, sum(w[a])) for x in w[a]] for a in range(2)]
    delta = [pi[1][i]-pi[0][i] for i in range(2)]

    def flux(a, x):
        return F(c[a][0])*(x[0]/w[a][0]-x[1]/w[a][1])

    def functional(z):
        u0 = mat2vec(invs[0], z)
        u1 = mat2vec(invs[1], z)
        return flux(0, u0)-flux(1, u1)

    b = -functional(delta)/2
    adj = [[trace-h[0][0], -h[0][1]], [-h[1][0], trace-h[1][1]]]
    a = -functional(mat2vec(adj, delta))/2
    return a, b, trace, det


def predicted(w,c,r):
    a,b,t,d = current_coefficients(w,c)
    return r*(a*r+b)/(1+t*r+d*r*r)


def main():
    w = [[1,1,1], [1,3,6]]
    c = [[1,1,1], [5,1,2]]
    a,b,t,d = current_coefficients(w,c)
    assert (a,b,t,d) == (F(2,255),-F(3,340),F(853,510),F(169,306)), (a,b,t,d)
    assert -b/a == F(9,8)
    assert b < 0 and a > 0
    count = 0
    for n in range(1, 40):
        r = F(n, 8)
        expected = F(3)*r*(8*r-9)/(2*(845*r*r+2559*r+1530))
        assert predicted(w,c,r) == direct(w,c,r) == expected
        count += 1
    rng = random.Random(618204)
    for _ in range(180):
        w = [[rng.randint(1,9) for _ in range(3)] for _ in range(2)]
        c = [[rng.randint(1,9) for _ in range(3)] for _ in range(2)]
        for r in (F(1,7), F(3,2), F(9,1), F(100,1)):
            assert predicted(w,c,r) == direct(w,c,r)
            count += 1
    print('PASS: exact stationary current vs reduced two-dimensional formula: %d comparisons' % count)
    print('PASS: sharp flat-phase reversal at rate 9/8; strict positive denominators')




def determinant(a):
    n = len(a)
    b = [row[:] for row in a]
    prod = F(1)
    for k in range(n):
        j = next((j for j in range(k,n) if b[j][k]), None)
        if j is None:
            return F(0)
        if j != k:
            b[j],b[k]=b[k],b[j]
            prod = -prod
        x = b[k][k]
        prod *= x
        for j in range(k+1,n):
            z = b[j][k]/x
            for l in range(k+1,n):
                b[j][l] -= z*b[k][l]
    return prod


def generic_generators(weights, conducts):
    n = len(weights[0])
    qs=[]
    for a in range(2):
        q = [[F(0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            j=(i+1)%n
            x=F(conducts[a][i],weights[a][i])
            y=F(conducts[a][i],weights[a][j])
            q[j][i]+=x; q[i][i]-=x
            q[i][j]+=y; q[j][j]-=y
        qs.append(q)
    return qs


def generic_current(weights, conducts, r, reduced=False):
    n=len(weights[0])
    qs=generic_generators(weights,conducts)
    if reduced:
        restr = [[[q[i][j]-q[i][n-1] for j in range(n-1)]
                  for i in range(n-1)] for q in qs]
        ia=[inverse(q) for q in restr]
        h=[[-ia[0][i][j]-ia[1][i][j] for j in range(n-1)] for i in range(n-1)]
        delta=[F(weights[1][i],sum(weights[1]))-F(weights[0][i],sum(weights[0]))
               for i in range(n-1)]
        mat=[[(F(i==j)+r*h[i][j]) for j in range(n-1)] for i in range(n-1)]
        z=mv(inverse(mat), [-r*x for x in delta])
        u0=mv(ia[0],z); u1=[-x for x in mv(ia[1],z)]
        js=F(conducts[0][0])*(u0[0]/weights[0][0]-u0[1]/weights[0][1])/2
        js+=F(conducts[1][0])*(u1[0]/weights[1][0]-u1[1]/weights[1][1])/2
        return js, determinant(mat)
    q=[[F(0) for _ in range(2*n)] for _ in range(2*n)]
    for a in range(2):
        for i in range(n):
            for j in range(n):
                q[a*n+i][a*n+j] += qs[a][i][j]
            q[a*n+i][a*n+i]-=r
            q[(1-a)*n+i][a*n+i]+=r
    q[-1]=[F(1)]*(2*n)
    p=[row[-1] for row in inverse(q)]
    return sum((F(conducts[a][0])*(p[a*n]/weights[a][0]-p[a*n+1]/weights[a][1])
                for a in range(2)),F(0))


def high_dimensional_checks():
    rng=random.Random(811711)
    count=0
    for n, trials in ((4,35),(5,20)):
        for _ in range(trials):
            w=[[rng.randint(1,6) for i in range(n)] for a in range(2)]
            c=[[rng.randint(1,6) for i in range(n)] for a in range(2)]
            for r in (F(1,4),F(1),F(3),F(7)):
                prediction, den=generic_current(w,c,r,True)
                assert den>0
                assert generic_current(w,c,r,False)==prediction
                count+=1
            # The degree at most n-2 statement: its n-th forward difference vanishes.
            vals=[]
            for k in range(1,n+2):
                r=F(k)
                j,den=generic_current(w,c,r,True)
                vals.append(j*den/r)
            for layer in range(n-1):
                vals=[vals[k+1]-vals[k] for k in range(len(vals)-1)]
            assert all(v==0 for v in vals)   # (n-1)-st differences of degree <= n-2
            count+=1
    print('PASS: generic ring sizes 4 and 5, exact reduction, determinant, polynomial-degree: %d comparisons' % count)


if __name__ == '__main__':
    main()
    high_dimensional_checks()
