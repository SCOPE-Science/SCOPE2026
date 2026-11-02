#!/usr/bin/env python3
"""Exact finite-algebra checks for two-point timing jitter of a double integrator.

Python 3 standard library only.  The analytical spectral argument is in RESULT.md;
finite enumeration here does not replace its proof for arbitrary time horizons.
"""
from fractions import Fraction as F
from itertools import product

class Poly:
    def __init__(self, coefficients=()):
        self.c = tuple(F(x) for x in coefficients)
        while self.c and self.c[-1] == 0:
            self.c = self.c[:-1]
    @staticmethod
    def coerce(x):
        return x if isinstance(x, Poly) else Poly([x])
    def __add__(self, other):
        other = self.coerce(other)
        return Poly([(self.c[i] if i < len(self.c) else 0) +
                     (other.c[i] if i < len(other.c) else 0)
                     for i in range(max(len(self.c), len(other.c)))])
    __radd__ = __add__
    def __neg__(self):
        return Poly([-x for x in self.c])
    def __sub__(self, other):
        return self + -self.coerce(other)
    def __rsub__(self, other):
        return self.coerce(other) - self
    def __mul__(self, other):
        other = self.coerce(other)
        coefficients = [F(0)] * (len(self.c) + len(other.c) - 1) if self.c and other.c else []
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                coefficients[i + j] += a*b
        return Poly(coefficients)
    __rmul__ = __mul__
    def __truediv__(self, scalar):
        return Poly([a/F(scalar) for a in self.c])
    def __eq__(self, other):
        return self.c == self.coerce(other).c
    def __repr__(self):
        return repr(self.c)
    def at(self, x):
        return sum(c * F(x)**i for i,c in enumerate(self.c))

D = Poly([0, 1]); ONE = Poly([1]); ZERO = Poly([])

def A(h):
    return [[ONE - h*h/2, h - 3*h*h/4], [-h, ONE - 3*h/2]]

def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def trans(A):
    return list(map(list, zip(*A)))

def det2(X):
    return X[0][0]*X[1][1] - X[0][1]*X[1][0]

def det3(X):
    return (X[0][0]*(X[1][1]*X[2][2]-X[1][2]*X[2][1])
            - X[0][1]*(X[1][0]*X[2][2]-X[1][2]*X[2][0])
            + X[0][2]*(X[1][0]*X[2][1]-X[1][1]*X[2][0]))

def m_lift(B):
    a,b=B[0]; c,e=B[1]
    return [[a*a,2*a*b,b*b],[a*c,a*e+b*c,b*e],[c*c,2*c*e,e*e]]

def mean(X,Y):
    return [[(X[i][j]+Y[i][j])/2 for j in range(len(X[0]))] for i in range(len(X))]

def numeric_matrix(B,d):
    return [[t.at(d) for t in row] for row in B]

def cov_step(B,Q):
    return mm(mm(B,Q),trans(B))

def mat_diff(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mat_id(n):
    return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]


def main():
    checks=0
    Bp=A(ONE + D);Bm=A(ONE-D)
    K=mean(m_lift(Bp),m_lift(Bm))
    z=D*D
    K_expected=[[(ONE+z)*(ONE+z)/4,(ONE+3*z*z)/4,(ONE-2*z+9*z*z)/16],
                [(3*z-ONE)/2,(6*z-ONE)/2,(9*z-ONE)/8],
                [ONE+z,ONE+3*z,(ONE+9*z)/4]]
    assert K==K_expected;checks+=9
    polynomial=3*z*z*z -11*z*z +12*z-2
    assert det3(mat_diff(mat_id(3), K)) == -polynomial/2; checks+=1
    C=mat_diff(mm(Bp,Bm),mm(Bm,Bp))
    assert det2(C) == -z*(ONE-z)*(ONE-z);checks+=1
    at_one=numeric_matrix(A(ONE),0)
    assert mm(at_one,at_one)==[[F(0)]*2 for _ in range(2)];checks+=1
    h=Poly([F(7,5)])
    assert (4-3*h).at(0)==F(-1,5);checks+=1
    assert det2(A(h)).at(0)==F(-3,25);checks+=1

    # Exact positive-definite quadratic Lyapunov certificate at delta=2/5:
    P=[[F(69675,10916),F(92725,21832)],
       [F(92725,21832),F(204927,43664)]]
    assert P[0][0]>0 and P[0][0]*P[1][1]-P[0][1]**2==F(1420090775,119159056)>0
    checks+=2
    plus=numeric_matrix(Bp,F(2,5));minus=numeric_matrix(Bm,F(2,5))
    result=mean(mm(mm(trans(plus),P),plus),mm(mm(trans(minus),P),minus))
    assert mat_diff(P,result)==[[F(1),F(0)],[F(0),F(1)]];checks+=4

    # Verify the exact covariance transfer against all path-by-path sums.
    for d in [F(1,10),F(1,4),F(2,5),F(1,2)]:
        A1=numeric_matrix(Bp,d);A0=numeric_matrix(Bm,d)
        M=numeric_matrix(K,d)
        for init in ([F(1),F(0)],[F(2),F(-3)],[F(1,7),F(3,5)]):
            V=[init[0]**2,init[0]*init[1],init[1]**2]
            for n in range(0,7):
                moments=[F(0)]*3
                for choices in product((0,1),repeat=n):
                    x=list(init)
                    for ch in choices:
                        B=A1 if ch else A0
                        x=[sum(B[i][j]*x[j] for j in range(2)) for i in range(2)]
                    y=[x[0]**2,x[0]*x[1],x[1]**2]
                    moments=[moments[i]+y[i] for i in range(3)]
                moments=[v/F(2**n) for v in moments]
                assert V==moments,(d,init,n);checks+=1
                V=[sum(M[i][j]*V[j] for j in range(3)) for i in range(3)]
    Froot=lambda x: F(3)*x*x*x-F(11)*x*x+F(12)*x-F(2)
    l=F(1,5);r=F(21,100)
    assert Froot(l)<0<Froot(r);checks+=1
    for i in range(100):
        m=(l+r)/2
        if Froot(m)<0:l=m
        else:r=m
    assert r-l<F(1,10**25);checks+=1
    print(f'PASS: {checks} exact assertions / finite-path checks')
    print('jitter threshold delta in:',float(l**F(1,2)) if False else (float(l)**0.5,float(r)**0.5))
    print('Note: global spectral classification follows from the separate analytic proof.')

if __name__=='__main__':
    main()
