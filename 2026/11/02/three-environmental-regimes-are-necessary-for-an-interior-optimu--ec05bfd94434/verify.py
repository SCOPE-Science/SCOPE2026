"""Exact verification of stationary habitat occupancy under changing regimes.

Uses independently constructed continuous-time chain generators, rational
stationary linear solves, and symbolic identities. Standard Python + sympy.
"""
import random
import sympy as sp


def exact_stationary_occupancy(col, ext, generator):
    """Generator is an n*n environment rate matrix, row sums zero."""
    n = len(col)
    Q = sp.zeros(2*n)
    for i in range(n):
        for x in range(2):
            z = 2*i+x
            j = 2*i+(1-x)
            Q[z,j] = col[i] if x == 0 else ext[i]
            for k in range(n):
                if k != i:
                    Q[z,2*k+x] = generator[i,k]
            Q[z,z] = -sum(Q[z,k] for k in range(2*n) if k != z)
    A = Q.T
    b = sp.zeros(2*n,1)
    for j in range(2*n):
        A[2*n-1,j] = 1
    b[2*n-1] = 1
    z = A.inv()*b
    assert all(t >= 0 for t in z)
    assert sum(z) == 1
    return sp.factor(sum(z[2*i+1] for i in range(n)))


def full_regime_generator(n, q):
    return sp.Matrix([[(-q*(n-1) if i==j else q) for j in range(n)] for i in range(n)])


def formula_uniform(col, ext, q):
    n=len(col)
    s=[col[i]+ext[i] for i in range(n)]
    return sp.factor(sum(col[i]/(s[i]+n*q) for i in range(n)) /
                     sum(s[i]/(s[i]+n*q) for i in range(n)))


def formula_two(col, ext, a, b, q):
    s1,s2=col[0]+ext[0],col[1]+ext[1]
    pi1=b/(a+b); pi2=a/(a+b)
    return sp.factor((pi1*col[0]*s2+pi2*col[1]*s1+q*(a+b)*(pi1*col[0]+pi2*col[1])) /
                     (s1*s2+q*(b*s1+a*s2)))


def verify():
    q=sp.symbols('q', positive=True)
    r=random.Random(39286)
    counts=0
    for n in [2,3,4]:
        for _ in range(75):
            col=[sp.Rational(r.randint(1,12),r.randint(1,4)) for j in range(n)]
            ext=[sp.Rational(r.randint(1,12),r.randint(1,4)) for j in range(n)]
            rate=sp.Rational(r.randint(1,9),r.randint(1,5))
            z=exact_stationary_occupancy(col,ext,full_regime_generator(n,rate))
            assert z == formula_uniform(col,ext,rate)
            counts+=1
    for _ in range(90):
        col=[sp.Rational(r.randint(1,12),r.randint(1,4)) for j in range(2)]
        ext=[sp.Rational(r.randint(1,12),r.randint(1,4)) for j in range(2)]
        a=sp.Rational(r.randint(1,9),r.randint(1,4))
        b=sp.Rational(r.randint(1,9),r.randint(1,4))
        rate=sp.Rational(r.randint(1,9),r.randint(1,5))
        G=sp.Matrix([[-rate*a,rate*a],[rate*b,-rate*b]])
        z=exact_stationary_occupancy(col,ext,G)
        assert z == formula_two(col,ext,a,b,rate)
        counts+=1
    c=[sp.Integer(1),sp.Integer(7),sp.Integer(7)]
    e=[sp.Integer(1),sp.Integer(1),sp.Integer(7)]
    P=formula_uniform(c,e,q)
    D=9*q*q+39*q+28
    assert sp.simplify(P - (45*q*q+204*q+140)/(8*D))==0
    assert sp.simplify(P-sp.Rational(5,8)-9*q/(8*D))==0
    assert sp.simplify(sp.diff(P,q)+9*(9*q*q-28)/(8*D**2))==0
    root=2*sp.sqrt(7)/3
    assert sp.simplify(P.subs(q,root)-(27-sp.sqrt(7))/38)==0
    assert sp.limit(P,q,0)==sp.Rational(5,8)
    assert sp.limit(P,q,sp.oo)==sp.Rational(5,8)
    for rate in [sp.Rational(1,10),sp.Rational(1),sp.Rational(4),sp.Rational(13,5)]:
        z=exact_stationary_occupancy(c,e,full_regime_generator(3,rate))
        assert z == P.subs(q,rate)
        assert z > sp.Rational(5,8)
        counts+=1
    print('PASS: exact stationary solves',counts,'; symbolic identities and unique maximum')


if __name__ == '__main__':
    verify()
