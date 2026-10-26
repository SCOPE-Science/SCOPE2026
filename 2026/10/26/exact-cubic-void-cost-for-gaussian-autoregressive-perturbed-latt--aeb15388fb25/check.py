"""Independent finite exact checks for the AR(1) Gaussian-lattice void asymptotic.

These computations illustrate finite covariance and excursion identities;
they are not a substitute for the proof of the infinite-volume limit.
"""
from fractions import Fraction as F


def centres(n):
    return {i: (-i - 2 if i <= n // 2 else n-i+2) if 0 <= i <= n else 0
            for i in range(-n, 2*n+1)}


def inverse_check(m, r, variance):
    covariance = [[variance * r**abs(i-j) for j in range(m)] for i in range(m)]
    if m == 1:
        precision = [[1/variance]]
    else:
        den = variance * (1-r*r)
        precision = [[F((1 if i in (0,m-1) else 1+r*r), 1) / den if i==j else
                      -r/den if abs(i-j)==1 else F(0) for j in range(m)] for i in range(m)]
    count = 0
    for i in range(m):
        for j in range(m):
            assert sum(covariance[i][k]*precision[k][j] for k in range(m)) == int(i==j)
            count += 1
    row_limit = variance*(1+r)/(1-r)
    assert all(sum(abs(x) for x in row)<=row_limit for row in covariance)
    return count+1


def geometry_check(n):
    b = centres(n)
    count=0
    for u in [F(1,4), F(3,8), F(1,2)]:
        for e in [F(-1,8),F(0),F(1,8)]:
            for i in range(-n,2*n+1):
                x = i+b[i]+u+e
                assert x<0 or x>n, (n,u,e,i,x)
                count+=1
    return count


def energy_check(n, r):
    b=centres(n)
    e=sum((b[i+1]-r*b[i])**2 for i in range(-n,2*n))
    s=sum(b[i]**2 for i in range(-n,2*n+1))
    jump=sum((b[i+1]-b[i])**2 for i in range(-n,2*n))
    # Exact discrete integration by parts; terminal centres are zero.
    assert e == (1-r)**2*s + r*jump
    mandatory=sum(max(0,min(i,n-i-1))**2 for i in range(n+1))
    assert mandatory <= s
    # Closed-form convergence with explicit uniform O(n^-1) witness;
    # this finite test only corroborates the analytical bound.
    assert abs(F(s,n**3)-F(1,12)) <= F(5,n)
    assert abs(F(e,n**3)-F((1-r)**2,12)) <= F(15,n)
    return 4


def main():
    tests=0
    for m in range(1,15):
        for r in [F(0),F(1,4),F(1,2),F(3,4)]:
            for var in [F(1),F(2)]:
                tests+=inverse_check(m,r,var)
    for n in range(2,23):
        tests+=geometry_check(n)
    for n in [10,20,40,80,160,320,640,1280]:
        for r in [F(0),F(1,4),F(1,2),F(3,4)]:
            tests+=energy_check(n,r)
    print(f'PASS {tests} exact rational covariance, geometry, and energy assertions')
    for r in [F(0),F(1,4),F(1,2),F(3,4)]:
        coefficient=(1-r)/(24*(1+r))
        print(f'rho={r} sigma^2=1 exact cubic coefficient={coefficient} (decimal={float(coefficient):.9f})')

if __name__=='__main__':
    main()
