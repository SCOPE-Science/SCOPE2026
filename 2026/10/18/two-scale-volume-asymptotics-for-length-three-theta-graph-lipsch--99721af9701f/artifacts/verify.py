"""Independent exact lattice/Ehrhart and moment checks for theta-graph dual volumes.
Run with Python 3 standard library; no external packages are required.
"""
from fractions import Fraction
from math import comb, factorial

def exact_formula(m):
    # Integrate 2 (3-h^2)^m over [0,1] and the two outer quadratic pieces.
    main = 2 * sum((Fraction(comb(m,j) * (-1)**j * 3**(m-j), 2*j+1)
                    for j in range(m+1)), Fraction(0))
    return main + Fraction(2**(m+2), 2*m+1)

def slice_points(q,h):
    # Directly enumerate both internal positions (x,y) on a length-three arm.
    # The hub values are zero and h. Graph edges require differences <=q.
    total = 0
    for x in range(-q,q+1):
        for y in range(x-q,x+q+1):
            total += abs(h-y)<=q
    return total

def lattice_count(m,q):
    return sum(slice_points(q,h)**m for h in range(-3*q,3*q+1))

def ehrhart_volume(m):
    # Polytope has integral vertices since edge-incidence inequalities
    # form a totally unimodular system with integral right sides.
    dim=2*m+1
    return Fraction(sum((-1)**(dim-q)*comb(dim,q)*lattice_count(m,q)
                        for q in range(dim+1)),factorial(dim))

def assert_ratio_logconvex():
    # Exact rational checks are corroboration only: the proof uses Cauchy-Schwarz.
    seq=[exact_formula(m) for m in range(1,22)]
    assert all(seq[j]**2 < seq[j-1]*seq[j+1] for j in range(1,len(seq)-1))
    assert all(seq[j+1] < 3*seq[j] for j in range(len(seq)-1))

if __name__=='__main__':
    assert exact_formula(1)==8
    for m in range(1,8):
        a=ehrhart_volume(m)
        b=exact_formula(m)
        assert a==b, (m,a,b)
        print(f'm={m}, dimension={2*m+1}, verified volume={a}')
    assert_ratio_logconvex()
    print('PASS: 7 Ehrhart volumes; 19 exact strict log-convexity checks; 20 upper-ratio checks')
