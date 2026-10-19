"""Exact rational checks for a two-patch density-dependent dispersal example."""
from fractions import Fraction as Q

ONE = Q(1)
TWO = Q(2)
HALF = Q(1, 2)
DELTA = Q(1, 14)

def f(x):
    return 5 * x / (1 + x)

def h(x):
    return (1 - DELTA) / (1 + x*x)

def p(x):
    return 1 - h(x)

def F(x, y):
    return (HALF * (h(x)*f(x) + p(y)*f(y)),
            HALF * (p(x)*f(x) + h(y)*f(y)))

def w(x):
    return x / (1 + x)

def derivs(x):
    wp = ONE / (1+x)**2
    hp = -TWO * x * (1-DELTA) / (1+x*x)**2
    sp = hp*w(x) + h(x)*wp
    mp = -hp*w(x) + p(x)*wp
    return Q(5,2)*sp, Q(5,2)*mp

def jac(x, y):
    a,b = derivs(x)
    c,d = derivs(y)
    return ((a,d),(b,c))

def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in (0,1))
                       for j in (0,1)) for i in (0,1))

def trace(A):
    return A[0][0]+A[1][1]

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

A=(Q(2),Q(2,3))
B=(A[1],A[0])
E=(Q(3,2),Q(3,2))
assert h(Q(2)) == Q(13,70) and p(Q(2)) == Q(57,70)
assert h(Q(2,3)) == Q(9,14) and p(Q(2,3)) == Q(5,14)
assert F(*A) == B and F(*B) == A and F(*E) == E
J = jac(*E)
assert J == ((Q(-128,455),Q(62,91)),
             (Q(62,91),Q(-128,455)))
assert J[0][0] + J[0][1] == Q(2,5)
assert J[0][0] - J[0][1] == Q(-438,455)
JA, JB = jac(*A),jac(*B)
assert JA == ((Q(-247,1260), Q(333,364)),
              (Q(199,420), Q(-27,1820)))
assert JB == ((Q(-27,1820), Q(199,420)),
              (Q(333,364), Q(-247,1260)))
M = matmul(JB,JA)
assert M == ((Q(20057,88200), Q(-34119,1656200)),
             (Q(-72029,264600), Q(1390929,1656200)))
assert trace(M) == Q(7953997,7452900)
assert det(M) == Q(3837681,20702500)
assert 1-trace(M)+det(M) == Q(423302,3583125) > 0
assert 1+trace(M)+det(M) == Q(209855777,93161250) > 0
assert 1-det(M) == Q(16864819,20702500) > 0
# Independent algebraic reconstruction of the fixed point and cycle values.
for u,v in (A,B,E):
    assert F(u,v) == (HALF*(h(u)*f(u)+p(v)*f(v)),
                      HALF*(p(u)*f(u)+h(v)*f(v)))
for x in (Q(0),Q(1,1000),Q(1,7),Q(1),Q(10),Q(100)):
    assert 0 < h(x) < 1 and 0 < p(x) < 1
    assert h(x) + p(x) == 1
print('PASS: exact orbit, fixed point, Jacobians, multipliers, and Schur inequalities')
