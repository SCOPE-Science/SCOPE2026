"""Exact-rational checks for state-dependent confirmation-bias averaging."""
from fractions import Fraction as Q
from itertools import product


def step(I, x):
    n = len(x)
    assert len(I) == n and all(len(row) == n for row in I)
    assert all(I[i][i] == 1 for i in range(n))
    d = [sum(I[j][i] > 0 for j in range(n)) for i in range(n)]
    out = []
    for i in range(n):
        correction = sum(I[j][i] * (1 - abs(x[j] - x[i])) * (x[j] - x[i])
                         for j in range(n)) / d[i]
        out.append(x[i] + correction)
    assert all(0 <= y <= 1 for y in out)
    return out


def check_exact(I, c, label):
    n = len(I)
    d = [sum(I[j][i] > 0 for j in range(n)) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            assert c[i]*I[j][i]/d[i] == c[j]*I[i][j]/d[j]
    counts = 0
    for v in product(range(5), repeat=n):
        x = [Q(k, 4) for k in v]
        y = step(I, x)
        assert sum(c[i]*x[i] for i in range(n)) == sum(c[i]*y[i] for i in range(n))
        counts += 1
    print(f'{label}: {counts} grid configurations exactly conserve weighted mass')
    return counts


def check_mixed_difference(I, c):
    n = len(I)
    assert n == 3
    d = [sum(I[j][i] > 0 for j in range(n)) for i in range(n)]
    x = [Q(1, 8), Q(3, 8), Q(5, 8)]
    h = Q(1, 32)
    def drift(y):
        f = step(I, y)
        return sum(c[k]*(f[k]-y[k]) for k in range(n))
    for i in range(n):
        for j in range(i + 1, n):
            u = x.copy(); u[i] += h
            v = x.copy(); v[j] += h
            uv = x.copy(); uv[i] += h; uv[j] += h
            divided = (drift(uv) - drift(u) - drift(v) + drift(x))/(h*h)
            a = c[i]*I[j][i]/d[i] - c[j]*I[i][j]/d[j]
            assert divided == 2*a, (i, j, divided, a)
    print('mixed second differences verify all three independent edge-current coefficients')


def main():
    half=Q(1,2)
    # Reciprocal but nonregular path, degrees include positive self-influence.
    I1=[[Q(1),Q(1),Q(0)], [Q(1),Q(1),Q(1)], [Q(0),Q(1),Q(1)]]
    check_exact(I1, [Q(2),Q(3),Q(2)], 'irregular reciprocal three-path')
    y=[Q(0),Q(0),half]
    assert sum(Q(a)*y[i] for i,a in enumerate([2,3,2]))/7 == Q(1,7)
    assert sum(y)/3 == Q(1,6)
    print('three-path conserved consensus = 1/7; initial unweighted mean = 1/6')
    # Reversible but nonreciprocal directed weights constructed from shared fluxes.
    h=[Q(1),Q(2),Q(3),Q(4)]
    edges=[(0,1),(1,2),(2,3)]
    I2=[[Q(int(i==j)) for j in range(4)] for i in range(4)]
    for i,j in edges:
        flux=Q(1,4)
        I2[j][i]=flux/h[i]
        I2[i][j]=flux/h[j]
    d2=[sum(I2[j][i]>0 for j in range(4)) for i in range(4)]
    check_exact(I2,[h[i]*d2[i] for i in range(4)],'asymmetric reversible four-path')
    # Balanced regular directed influence cycle with a nonvanishing current.
    I3=[[Q(1),Q(1),half],[half,Q(1),Q(1)],[Q(1),half,Q(1)]]
    assert all(sum(I3[j][i] for j in range(3))==Q(5,2) for i in range(3))
    assert all(sum(I3[i][j] for j in range(3))==Q(5,2) for i in range(3))
    check_mixed_difference(I3,[Q(1)]*3)
    x=[Q(0),Q(1,3),Q(2,3)]
    y=step(I3,x)
    assert sum(y)-sum(x) == -Q(1,27)
    assert sum(y)/3-sum(x)/3 == -Q(1,81)
    assert I3[0][1]*I3[1][2]*I3[2][0] == 1
    assert I3[1][0]*I3[2][1]*I3[0][2] == Q(1,8)
    print('balanced nonreversible directed triangle: sum change -1/27, mean change -1/81')
    print('all exact arithmetic checks passed')

if __name__=='__main__':
    main()
