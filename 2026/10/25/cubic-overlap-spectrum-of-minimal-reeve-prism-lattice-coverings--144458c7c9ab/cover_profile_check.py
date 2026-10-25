"""Independent arithmetic checks for the lattice-cover multiplicity theorem.

No external dependencies; execute with Python 3.9+.
"""
from fractions import Fraction as F
from math import floor

def rational_tail(m, k):
    if k == 1:
        return F(1)
    p = lambda t: max(F(0), F(1) - F(2 * t, m)) ** 3
    return F(m, 6) * (p(k - 2) - p(k - 1))

def analytical_mass(m, k):
    return rational_tail(m, k) - rational_tail(m, k + 1)

def direct_mass(m, k):
    # Closed form derived independently by integrating the affine density
    # against the integer-translation triangular kernel.
    q = m // 2
    if m == 1:
        return F(5,6) if k == 1 else (F(1,6) if k == 2 else F(0))
    if k == 1:
        return F(2,m) - F(4, 3*m*m)
    if 2 <= k <= q:
        return F(4,m) * (1 - F(2*(k-1),m))
    if m % 2 == 0:
        return F(4,3*m*m) if k == q+1 else F(0)
    return F(25,6*m*m) if k == q+1 else (F(1,6*m*m) if k == q+2 else F(0))

def count_vertical(m, x, y, z):
    a = m * max(F(0), x + y - 1)
    b = m * min(x, y) + 1
    return sum(1 for shift in range(-m-2,m+3) if a <= z + shift <= b)

def main():
    exact_instances = 0
    for m in range(1,71):
        levels = list(range(1,m+5))
        masses = [analytical_mass(m,k) for k in levels]
        assert all(v>=0 for v in masses)
        assert sum(masses) == 1
        assert all(analytical_mass(m,k) == direct_mass(m,k) for k in levels)
        mean = sum(k*p for k,p in zip(levels,masses))
        variance = sum(k*k*p for k,p in zip(levels,masses)) - mean*mean
        assert mean == 1 + F(m,6)
        assert variance == F(m*m,72) + F(1,6) - (F(1,24*m*m) if m%2 else F(0))
        exact_instances+=len(levels)
    direct_points=0
    boundary_points=0
    for m in range(1,14):
        for i in range(1,21):
            for j in range(1,21):
                x,y=F(2*i-1,40),F(2*j-1,40)
                a=m*max(F(0),x+y-1)
                b=m*min(x,y)+1
                ell=b-a
                for v in range(1,21):
                    z=F(2*v-1,40)
                    if (z-a).denominator==1 or (z-b).denominator==1:
                        boundary_points+=1
                        continue
                    actual=count_vertical(m,x,y,z)
                    assert actual in (floor(ell), floor(ell)+1)
                    # Rounding-up event is encoded exactly by fractional alignment.
                    expected=(floor(ell)+int(((z-a) % 1) < (ell % 1)))
                    assert actual == expected, (m,x,y,z,ell,actual,expected)
                    direct_points+=1
    print('COVER_PROFILE_CHECK_OK exact_mass_cases=',exact_instances,
          'direct_membership_points=',direct_points,'excluded_boundaries=',boundary_points)
if __name__=='__main__':main()
