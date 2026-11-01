"""Finite reproducibility checks for planar-factor ridge inequalities.
These checks supplement, not replace, the analytic argument.
"""
from itertools import product
from math import comb, sqrt

TRIANGLE = (3*sqrt(3), 6*sqrt(3), 3)  # area, perimeter, vertices; inradius 1
SQUARE = (4.0, 8.0, 4)
INTERVAL = (2.0, 2.0)  # length, endpoints, interval [-1,1]

def multiply(a, b):
    result = [0.0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result

def ridge_of_product(polygons, interval_count):
    coefficients = [1.0]
    for f in polygons:
        coefficients = multiply(coefficients, f)
    for _ in range(interval_count):
        coefficients = multiply(coefficients, INTERVAL)
    return coefficients[2]

def run():
    checked=0
    for m in range(7):
        for ell in range(7):
            n=2*m+ell
            if n<3:
                continue
            for labels in product((0,1),repeat=m):
                factors=[TRIANGLE if flag else SQUARE for flag in labels]
                actual=ridge_of_product(factors,ell)
                cube=(2**n)*comb(n,2)
                penalty=(2**n)*(6*sqrt(3)-9)/4*sum(labels)
                assert actual+1e-9>=cube+penalty, (m,ell,labels,actual,cube,penalty)
                if not any(labels):
                    assert abs(actual-cube)<1e-6, (m,ell,labels)
                checked+=1
    prism_gap=ridge_of_product([TRIANGLE],1)-24
    assert abs(prism_gap-(12*sqrt(3)-18))<1e-12
    assert prism_gap>0
    print(f"PASS: {checked} Cartesian products of regular tangent triangles, squares and unit intervals.")
    print(f"Sharp triangular-prism absolute ridge gap: {prism_gap:.15f}")

if __name__=='__main__':
    run()
