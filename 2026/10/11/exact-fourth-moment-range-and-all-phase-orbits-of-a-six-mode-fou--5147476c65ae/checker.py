"""Reproducibility checks for the 2-by-3 rectangular Fourier fourth moment.

Python 3 standard library only. Finite tests supplement the supplied algebraic proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from cmath import exp, pi

SUPPORT = tuple((i, j) for j in range(2) for i in range(3))

def fourth_via_correlations(coeff):
    corr = {}
    for (i, j), a in coeff.items():
        for (k, l), b in coeff.items():
            h = (i-k, j-l)
            corr[h] = corr.get(h, 0) + a*b.conjugate()
    return sum(v.real*v.real+v.imag*v.imag for v in corr.values())

def normalize(coeff):
    lam = coeff[(0, 0)]
    alpha = coeff[(1, 0)] / lam
    beta = coeff[(0, 1)] / lam
    return {(i,j): round_complex(coeff[(i,j)]/(lam*alpha**i*beta**j))
            for (i,j) in SUPPORT}

def round_complex(z):
    return complex(round(z.real), round(z.imag))

def dict_of_rows(a,b):
    return {(i,0): a[i] for i in range(3)} | {(i,1): b[i] for i in range(3)}

MIN_REPS = [dict_of_rows((1,1,1),(1,-1,1)),
            dict_of_rows((1,1,-1),(1,1j,1)),
            dict_of_rows((1,1,-1),(1,-1j,1))]
MIN_NORMALS = [{k:round_complex(v) for k,v in d.items()} for d in MIN_REPS]

# Exact formal-polynomial identity at rational points, an extra check rather
# than a substitute for the symbolic expansion in the proof.
for u,v,w in product(range(-3,4),repeat=3):
    x,y,z = Fraction(u,3),Fraction(v,3),Fraction(w,3)
    lhs = x*x+y*y+4*x*y*z+2*z*z
    rhs = 2*(z+x*y)**2 + x*x*(1-y*y)+y*y*(1-x*x)
    assert lhs == rhs

for q, roots, expected_min_count, expected_max_count in (
        (2,(1,-1),8,8),
        (4,(1,1j,-1,-1j),192,64)):
    hist=Counter()
    for values in product(roots,repeat=6):
        c=dict(zip(SUPPORT,values))
        E=fourth_via_correlations(c)
        assert E == round(E)  # gaussian-integer exactness at these small sizes
        E=int(round(E))
        hist[E]+=1
        if E==50:
            assert normalize(c) in MIN_NORMALS
        if E==114:
            assert all(abs(c[(i,j)]-c[(0,0)]*(c[(1,0)]/c[(0,0)])**i*
                           (c[(0,1)]/c[(0,0)])**j)<1e-12 for i,j in SUPPORT)
    assert min(hist)==50 and max(hist)==114
    assert hist[50]==expected_min_count and hist[114]==expected_max_count
    print(f'PHASE_{q}_PASS minima={hist[50]} maxima={hist[114]} energies={sorted(hist.items())}')

# Aperiodic-to-cyclic Fourier equality for alias-free finite tori.
example = dict_of_rows((1,exp(0.17j),exp(-0.81j)),
                       (exp(0.4j),exp(-1.3j),exp(1.2j)))
aperiodic=fourth_via_correlations(example)
for m,n in [(5,3),(7,5),(11,7)]:
    direct=sum(abs(sum(c*exp(2j*pi*(i*k/m+j*l/n))
                       for (i,j),c in example.items()))**4
               for k in range(m) for l in range(n))/(m*n)
    assert abs(aperiodic-direct)<1e-9

for c in MIN_REPS:
    assert fourth_via_correlations(c)==50
assert fourth_via_correlations(dict_of_rows((1,1,1),(1,1,1)))==114
print('CORRELATION_AND_FINITE_FOURIER_PASS')
print('CHECK_PASS')
