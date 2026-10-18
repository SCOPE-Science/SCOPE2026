#!/usr/bin/env python3
"""Exact lattice-moment verification for two-point-cluster Lipschitz balls.

Requires Python 3, a C++17 compiler named g++, and standard C++ headers.
All cases are exact integer enumerations and rational postprocessing.
"""
import subprocess
import tempfile
from pathlib import Path
from fractions import Fraction
from math import factorial

HERE = Path(__file__).resolve().parent
CASES = [(2, 1, 2), (2, 1, 1), (2, 2, 3), (3, 1, 2), (3, 1, 1)]

def top_coeff(values, degree):
    v = list(values[:degree + 1])
    assert len(v) == degree + 1
    for _ in range(degree):
        v = [b - a for a, b in zip(v, v[1:])]
    return Fraction(v[0], factorial(degree))

def exact_formula(m, t):
    smaller = t*t*(4*m - 3*m*t + t) / (12*m*(2-t))
    larger = (m*(t*t - 2*t + 2) + (t-2)**2) / (12*m)
    return smaller, larger


def main():
    with tempfile.TemporaryDirectory() as temp:
        exe = str(Path(temp) / 'enumerate')
        subprocess.run(['g++','-O3','-std=c++17',str(HERE / 'enumerate_lattice.cpp'),'-o',exe],check=True)
        for m,a,b in CASES:
            proc = subprocess.run([exe,str(m),str(a),str(b)],capture_output=True,text=True,check=True,timeout=120)
            table = [[int(x) for x in line.split()] for line in proc.stdout.splitlines()]
            d=2*m-1
            assert len(table)==d+3 and [row[0] for row in table]==list(range(d+3))
            volume=top_coeff([x[1] for x in table],d)
            assert volume>0
            within=top_coeff([x[2] for x in table],d+2)/volume/Fraction(2*b*b)
            between=top_coeff([x[3] for x in table],d+2)/volume/Fraction(4*b*b)
            expected=exact_formula(m,Fraction(a,b))
            assert (within,between)==expected,(m,a,b,within,between,expected)
            if a<b:
                assert between>within
            else:
                assert between==within
            print(f'm={m}, t={a}/{b}: lambda_within={within}, lambda_between={between}; PASS')
    print(f'PASS: {len(CASES)} exact lattice-moment spectra, including equilateral boundary')

if __name__=='__main__':
    main()
