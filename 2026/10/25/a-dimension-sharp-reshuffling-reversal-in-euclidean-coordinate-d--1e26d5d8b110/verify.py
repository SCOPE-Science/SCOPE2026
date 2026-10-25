#!/usr/bin/env python3
"""Exact finite-path verification of the coordinate-reshuffling comparison.
Requires sympy. No network or external data are required.
"""
import itertools
from sympy import Matrix, eye, symbols, factor, Rational, zeros


def epoch_products(matrix, sampling):
    """List the exact epoch error maps, with the earliest update on the right."""
    n = matrix.rows
    maps = [eye(n) - eye(n)[:, i] * matrix[i, :] / matrix[i, i]
            for i in range(n)]
    if sampling == 'permutation':
        paths = list(itertools.permutations(range(n)))
    elif sampling == 'independent':
        paths = list(itertools.product(range(n), repeat=n))
    else:
        raise ValueError(sampling)
    out = []
    for path in paths:
        e = eye(n)
        for i in path:
            e = maps[i] * e
        out.append((path, e))
    return out


def gram_mean(products, weight):
    n = weight.rows
    total = zeros(n, n)
    for _, product in products:
        total += product.T * weight * product
    return total / len(products)


def check_two_variables():
    a, b, c = symbols('a b c', positive=True)
    H = Matrix([[a, c], [c, b]])
    rr = gram_mean(epoch_products(H, 'permutation'), eye(2))
    iid = gram_mean(epoch_products(H, 'independent'), eye(2))
    target = (c**4/(a**2*b**2)-1)*eye(2)/4
    assert (rr - iid - target).applyfunc(factor) == zeros(2, 2)
    assert (rr[0, 0] - (c**4/(a*a*b*b)+c*c/(b*b))/2).factor() == 0
    assert (rr[1, 1] - (c**4/(a*a*b*b)+c*c/(a*a))/2).factor() == 0
    return 'symbolic two-coordinate identity verified for arbitrary nonzero diagonal entries'


def check_three_variables():
    q = Rational(3,4)
    A = Matrix([[1,q,Rational(1,4)], [q,1,q], [Rational(1,4),q,1]])
    x = Matrix([0,1,0])
    assert A[0,0] == 1
    assert A[:2,:2].det() == Rational(7,16)
    assert A.det() == Rational(3,32)
    rr = epoch_products(A,'permutation')
    iid = epoch_products(A,'independent')
    assert len(rr)==6 and len(iid)==27
    grp = {}
    for label, paths in [('RR',rr),('IID',iid)]:
        for first in range(3):
            chosen=[M for path,M in paths if path[0]==first]
            norm_sum=sum(((M*x).T*(M*x))[0] for M in chosen)
            energy_sum=sum(((M*x).T*A*(M*x))[0] for M in chosen)
            grp[label,first]=(norm_sum,energy_sum)
    assert grp['RR',0] == (Rational(5697,2048),Rational(639,2048))
    assert grp['RR',1] == (0,0)
    assert grp['RR',2] == grp['RR',0]
    assert grp['IID',0] == (Rational(12331,1024),Rational(1765,1024))
    assert grp['IID',1] == (0,0)
    assert grp['IID',2] == grp['IID',0]
    rr_norm = (x.T*gram_mean(rr,eye(3))*x)[0]
    iid_norm = (x.T*gram_mean(iid,eye(3))*x)[0]
    rr_energy = (x.T*gram_mean(rr,A)*x)[0]
    iid_energy = (x.T*gram_mean(iid,A)*x)[0]
    assert rr_norm == Rational(1899,2048)
    assert iid_norm == Rational(12331,13824)
    assert rr_norm-iid_norm == Rational(1949,55296) > 0
    assert rr_energy == Rational(213,2048)
    assert iid_energy == Rational(1765,13824)
    assert rr_energy-iid_energy == -Rational(1309,55296) < 0
    return ('3x3 exact 6+27 path enumeration and SPD certificate verified; '
            'Euclidean RR-IID=1949/55296, energy RR-IID=-1309/55296')


if __name__ == '__main__':
    print(check_two_variables())
    print(check_three_variables())
    print('PASS')
