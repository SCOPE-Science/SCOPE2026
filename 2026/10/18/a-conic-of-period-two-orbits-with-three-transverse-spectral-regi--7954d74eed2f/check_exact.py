#!/usr/bin/env python3
"""Exact-arithmetic spot verification of the quadratic-map two-cycle theorem.

Uses only the Python standard library. This is not a substitute for the proof.
"""
from fractions import Fraction as Q


def certify(m, q, delta):
    # Elements are pairs (constant, radical coefficient) in Q[s]/(s*s=q).
    m, q, delta = Q(m), Q(q), Q(delta)
    def cv(t):
        if isinstance(t, tuple):
            return t
        return (Q(t), Q(0))
    def add(a, b):
        a, b = cv(a), cv(b)
        return (a[0] + b[0], a[1] + b[1])
    def neg(a):
        a = cv(a)
        return (-a[0], -a[1])
    def sub(a, b):
        return add(a, neg(b))
    def mul(a, b):
        a, b = cv(a), cv(b)
        return (a[0]*b[0] + q*a[1]*b[1], a[0]*b[1] + a[1]*b[0])
    zero, one, d = cv(0), cv(1), (Q(0), Q(1))
    p = (sub(cv(m), mul(d,Q(1,2))), d, mul(d,2))
    v = (add(cv(m), mul(d,Q(1,2))), neg(d), neg(mul(d,2)))
    eps, mu = Q(2), Q(-4)
    def fmap(s):
        x,y,z=s
        term=sub(add(add(mul(x,x),mul(x,y)),mul(y,y)),eps)
        term=add(term,mul(mu,y))
        return (add(x,y),add(add(y,z),term),add(z,term))
    assert fmap(p)==v and fmap(v)==p
    def jac(s):
        x,y,_=s
        u=add(mul(2,x),y)
        w=add(add(mu,x),mul(2,y))
        return [[one,one,zero], [u,add(one,w),one], [u,w,one]]
    def matmul(A,B):
        return [[sumz([mul(A[i][k], B[k][j]) for k in range(3)]) for j in range(3)] for i in range(3)]
    def sumz(items):
        ans=zero
        for e in items: ans=add(ans,e)
        return ans
    M=matmul(jac(v),jac(p))
    trace=sumz([M[i][i] for i in range(3)])
    e2=sumz([sub(mul(M[i][i],M[j][j]),mul(M[i][j],M[j][i])) for i,j in ((0,1),(0,2),(1,2))])
    det=sumz([sub(mul(M[0][k],sub(mul(M[1][(k+1)%3],M[2][(k+2)%3]),mul(M[1][(k+2)%3],M[2][(k+1)%3]))),zero) for k in range(3)])
    # The determinant expansion above uses cyclic columns and is valid for 3 x 3.
    assert det==one
    assert trace==cv(3+delta) and e2==trace
    assert delta==4*m*m-6
    assert q==(eps-m*m)/Q(3,4)
    return True


def main():
    # The point coordinates are exact in the quadratic number fields Q(sqrt(q)).
    for m,q,D in [(Q(0),Q(8,3),Q(-6)),
                  (Q(1),Q(4,3),Q(-2)),
                  (Q(5,4),Q(7,12),Q(1,4))]:
        certify(m,q,D)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
