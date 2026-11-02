"""Reproduce numerical and algebraic checks for the unweighted bridge-barbell metric theorem.

Uses only the Python standard library. Numerical tests supplement, but do not
replace, the proof for all integer clique sizes.
"""
from decimal import Decimal, localcontext
from math import sqrt


def parameters(m, n):
    assert m >= 2 and n >= 2
    with localcontext() as ctx:
        ctx.prec = 58
        one = Decimal(1)
        alpha = Decimal(m - 1) / (2 * m)
        beta = Decimal(n - 1) / (2 * n)

        def F(C):
            return ((C * C - alpha).sqrt() + C +
                    (C * C - beta).sqrt()) ** 2 + alpha + beta

        low, high = one, Decimal(2)
        assert F(low) < 9 < F(high)
        for _ in range(200):
            mid = (low + high) / 2
            if F(mid) < 9:
                low = mid
            else:
                high = mid
        C = (low + high) / 2
        return C, alpha, beta, F(C)


def verify_eight_orbits(m, n, C, a, b, tol=Decimal('3e-46')):
    with localcontext() as ctx:
        ctx.prec = 58
        s, t = (C*C-a).sqrt(), (C*C-b).sqrt()
        distances_sq = {
            'left_internal': (Decimal(1), Decimal(1)),
            'right_internal': (Decimal(1), Decimal(1)),
            'left_hub': (C*C, Decimal(1)),
            'right_hub': (C*C, Decimal(1)),
            'bridge': (C*C, Decimal(1)),
            'left_to_right_hub': ((s+C)**2+a, Decimal(4)),
            'right_to_left_hub': ((t+C)**2+b, Decimal(4)),
            'between_leaves': ((s+C+t)**2+a+b, Decimal(9)),
        }
        for key, (val, original) in distances_sq.items():
            assert val + tol >= original, (m, n, key, val-original)
            assert val <= original*C*C + tol, (m, n, key)
        assert abs(distances_sq['between_leaves'][0]-9) < Decimal('1e-45')
        return len(distances_sq)


def squared_euclidean(p, q):
    return sum((x-y)**2 for x, y in zip(p, q))


def coordinates(m, n, C, alpha, beta):
    c, a, b = float(C), float(alpha), float(beta)
    s, t = sqrt(c*c-a), sqrt(c*c-b)
    d = 1+m+n
    def base(axis):
        out = [0.0]*d
        out[0] = axis
        return out
    points = [base(0.0), base(c)]
    for i in range(m):
        p = base(-s)
        for j in range(m):
            p[1+j] = ((1.0 if i == j else 0.0)-1.0/m)/sqrt(2)
        points.append(p)
    for i in range(n):
        p = base(c+t)
        for j in range(n):
            p[1+m+j] = ((1.0 if i == j else 0.0)-1.0/n)/sqrt(2)
        points.append(p)
    return points


def original_distance(i,j,m,n):
    if i == j: return 0
    if {i,j} == {0,1}: return 1
    def side(i):
        return 'left' if 2<=i<2+m else 'right' if 2+m<=i<2+m+n else 'hubL' if i==0 else 'hubR'
    a,b=side(i),side(j)
    if a==b: return 1
    if {a,b} == {'left','hubL'} or {a,b} == {'right','hubR'}: return 1
    if {a,b} == {'left','hubR'} or {a,b} == {'right','hubL'}: return 2
    if {a,b} == {'left','right'}: return 3
    raise ValueError((a,b))


def main():
    orbit_cases=0
    for m in range(2,39):
        for n in range(2,39):
            C,a,b,fc=parameters(m,n)
            assert abs(fc-9)<Decimal('1e-45')
            orbit_cases += verify_eight_orbits(m,n,C,a,b)
            if m==n:
                with localcontext() as ctx:
                    ctx.prec=58
                    closed=(2*(Decimal(9)+a).sqrt()-(Decimal(9)-2*a).sqrt())/3
                    assert abs(C-closed)<Decimal('1e-45')
    pairs=0
    for m in range(2,15):
        for n in range(2,15):
            C,a,b,_=parameters(m,n)
            points=coordinates(m,n,C,a,b)
            for i in range(len(points)):
                for j in range(i+1,len(points)):
                    D=original_distance(i,j,m,n)
                    val=squared_euclidean(points[i],points[j])
                    assert D*D-1e-9<=val<=float(C*C)*D*D+1e-9, (m,n,i,j,val,D)
                    pairs+=1
    print('CHECK_OK', 'parameter_pairs=',37*37, 'exact_orbit_bounds=',orbit_cases,
          'full_coordinate_pairs=',pairs)

if __name__ == '__main__':
    main()
