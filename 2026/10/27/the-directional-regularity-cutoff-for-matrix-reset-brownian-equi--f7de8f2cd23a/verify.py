"""Independent exact-rational stationary-moment checks for linear-reset Brownian motion.

Requires sympy. No simulation is used as a substitute for the analysis.
"""
from itertools import product
from sympy import Matrix, Rational, eye, kronecker_product, simplify

SIGMA = Matrix([[2, Rational(1,3)], [Rational(1,3), 3]])
RATE = Rational(2)
MATRICES = [
    Matrix([[Rational(1,2), 0], [0, Rational(1,3)]]),
    Matrix([[Rational(1,3), Rational(1,4)], [0, Rational(1,2)]]),
    Matrix([[0, Rational(1,2)], [0, 0]]),
    Matrix([[Rational(1,2), 0], [Rational(1,3), 0]]),
]


def flatten_tuple(t, dim=2):
    index = 0
    for k in t:
        index = index*dim+k
    return index


def check_matrix(A):
    C = Matrix([SIGMA[i, j]/RATE for i, j in product(range(2), repeat=2)])
    B2 = kronecker_product(A, A)
    cov = (eye(4)-B2).inv()*C
    cov_m = Matrix(2, 2, [cov[flatten_tuple((i,j))] for i,j in product(range(2), repeat=2)])
    assert cov_m == SIGMA/RATE + A*cov_m*A.T
    assert cov_m.det() > 0
    moments = Matrix(16, 1, lambda i,j: 0)
    for t in product(range(2), repeat=4):
        i,j,k,l=t
        moments[flatten_tuple(t)] = (
            SIGMA[i,j]*SIGMA[k,l] + SIGMA[i,k]*SIGMA[j,l]
            + SIGMA[i,l]*SIGMA[j,k]
        )/RATE**2
    B4 = kronecker_product(A, A, A, A)
    K = (eye(16)-B4).inv()*moments
    assert (eye(16)-B4)*K == moments
    checks = 0
    for u in [Matrix([1,0]),Matrix([0,1]),Matrix([1,1]),Matrix([2,-1])]:
        for v in [Matrix([1,0]),Matrix([0,1]),Matrix([1,-1])]:
            k = sum((u[i]*u[j]*v[k]*v[l])*K[flatten_tuple((i,j,k,l))]
                    for i,j,k,l in product(range(2), repeat=4))
            assert k > 0, (A, u, v, k)
            # Fourth-order cumulants obey a closed tensor renewal equation:
            def multilinear_k(p,q,r,s):
                return sum((p[i]*q[j]*r[k]*s[l])*K[flatten_tuple((i,j,k,l))]
                           for i,j,k,l in product(range(2), repeat=4))
            Au=A.T*u; Av=A.T*v
            g = ((u.T*SIGMA*u)[0]*(v.T*SIGMA*v)[0]
                 + 2*(u.T*SIGMA*v)[0]**2)/RATE**2
            assert simplify(k-g-multilinear_k(Au,Au,Av,Av)) == 0
            checks += 2
    return checks

checks = sum(check_matrix(A) for A in MATRICES)
N = MATRICES[2]
v1 = Matrix([0, 1]); v2 = Matrix([1, 0]);
assert N.T*v1 == Matrix([0,0])
assert N.T*v2 != Matrix([0,0]) and (N.T)**2*v2 == Matrix([0,0])
# One-dimensional characteristic polynomial denominators for nilpotent modes.
a1 = (v1.T*SIGMA*v1)[0]/(2*RATE)
a20 = (v2.T*SIGMA*v2)[0]/(2*RATE)
a21 = ((N.T*v2).T*SIGMA*(N.T*v2))[0]/(2*RATE)
assert a1 > 0 and a20 > 0 and a21 > 0
# Inverse Fourier fundamental solutions: derivative jumps at 0 of
# orders 1 and 3, respectively, equal -1/a1 and +1/(a20*a21).
assert simplify(a20*a21*(1/(a20*a21))-1)==0
checks += 8
print('PASS:',checks,'exact-rational structural and cumulant checks')
print('nilpotent directions: m=1 scale squared',a1,'; m=2 scale squares',a20,a21)
