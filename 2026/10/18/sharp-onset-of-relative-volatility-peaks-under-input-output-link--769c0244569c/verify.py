"""Exact checks for a three-sector input-output risk reversal."""
from fractions import Fraction as F


def risk(t):
    t = F(t)
    w = (F(1), (1 + t) / 10, (1 + t + t*t) / 10000)
    return sum(x*x for x in w) / sum(w)**2


def determinant3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def solve3(M,b):
    d = determinant3(M)
    assert d != 0
    return [determinant3([[b[r] if c==j else M[r][c]
                           for c in range(3)] for r in range(3)])/d
            for j in range(3)]


def run():
    times = [0, 10, 100, 1000, 10000]
    vals = [risk(t) for t in times]
    assert vals[0] > vals[1] < vals[2] > vals[3] < vals[4]
    for t in times:
        I_minus_tN = [[F(int(r==c) - (t if c == r+1 else 0)) for c in range(3)]
                      for r in range(3)]
        # For each individual unit shock, use the full Leontief inverse, not the closed form.
        w = [sum(solve3(I_minus_tN, [F(int(i==j)) for i in range(3)]))
             for j in range(3)]
        scales = [F(1), F(1, 10), F(1, 10000)]
        w = [a*b for a, b in zip(w, scales)]
        direct = sum(x*x for x in w)/sum(w)**2
        assert direct == risk(t)
    # Two-sector affine inverse numerators are affine, even with simultaneous changes.
    # Example A(t) = [[t/10, t/20], [t/30, t/5]] on 0<=t<=1.
    def risk2(t):
        t=F(t)
        A=[[t/10,t/20],[t/30,t/5]]
        M=[[F(int(i==j))-A[i][j] for j in range(2)] for i in range(2)]
        det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
        assert det>0
        columns=[(M[1][1]-M[1][0])/det, (M[0][0]-M[0][1])/det]
        direct=sum(x*x for x in columns)/sum(columns)**2
        # Cofactors cancel the determinant from the ratio.
        numer=[M[1][1]-M[1][0],M[0][0]-M[0][1]]
        assert direct == sum(x*x for x in numer)/sum(numer)**2
        return direct
    for t in [F(0),F(1,7),F(1,4),F(1,2),F(3,4),F(1)]:
        risk2(t)
    print('EXACT_CHECKS_PASS')
    for t,v in zip(times, vals):
        print('t=%s CV_squared=%s approximate=%.12f' % (t, v, float(v)))


if __name__ == '__main__':
    run()
