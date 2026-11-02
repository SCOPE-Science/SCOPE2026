"""Independent exact checks for a two-habitat correlated-catastrophe model.

Requires sympy. Execute: python verify.py
"""
from itertools import product
from sympy import Matrix, Rational, symbols, diff, factor, simplify

c, d, e, k, rho = symbols('c d e k rho', positive=True)
Delta = (c + e + k)**2 + c*d
D = 2*Delta - rho*k*(c - d + e + k)
J = 2*c*(c + d)/D
M = 2*c*(2*(c + d + e + k) - rho*k)/D
assert simplify(diff(J, rho) - 2*c*k*(c+d)*(c-d+e+k)/D**2) == 0
assert simplify(diff(M, rho) + 4*c*d*k*(c+d)/D**2) == 0

# Each row is the departure state of the full four-state model
# (empty-empty, occupied-empty, empty-occupied, occupied-occupied).
def generator(C, R, E, K, Z):
    L = E + (1-Z)*K
    return Matrix([
        [-2*C, C, C, 0],
        [E+K, -(E+K+C+R), 0, C+R],
        [E+K, 0, -(E+K+C+R), C+R],
        [Z*K, L, L, -(2*L+Z*K)],
    ])

def steady(Q):
    A = Q.T.copy()
    A[0,:] = Matrix([[1,1,1,1]])
    p = A.inv()*Matrix([1,0,0,0])
    assert Q.T*p == Matrix([0,0,0,0])
    assert sum(p) == 1
    return p

n = 0
for C,R,E,K,Z in product([Rational(1,2),1,3], [Rational(1,3),1,4],
                            [Rational(1,4),2], [Rational(1,2),2],
                            [0,Rational(1,4),Rational(3,5),1]):
    Q = generator(C,R,E,K,Z)
    assert all(sum(Q.row(i)) == 0 for i in range(4))
    p = steady(Q)
    assert all(v>0 for v in p)
    vals = {c:C,d:R,e:E,k:K,rho:Z}
    assert p[3] == J.subs(vals)
    assert p[1]+p[2]+2*p[3] == M.subs(vals)
    n += 1
assert n==144

for R, J0, J1, M0, M1 in [
    (1, Rational(1,5), Rational(2,9), Rational(4,5), Rational(7,9)),
    (3, Rational(1,3), Rational(1,3), 1, Rational(11,12)),
    (4, Rational(5,13), Rational(10,27), Rational(14,13), Rational(26,27)),
]:
    assert J.subs({c:1,d:R,e:1,k:1,rho:0}) == J0
    assert J.subs({c:1,d:R,e:1,k:1,rho:1}) == J1
    assert M.subs({c:1,d:R,e:1,k:1,rho:0}) == M0
    assert M.subs({c:1,d:R,e:1,k:1,rho:1}) == M1

print(f'PASS: {n} independent exact four-state stationary solves, two derivative identities, and three exact boundary cases')
