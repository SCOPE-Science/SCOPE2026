"""Exact elementary finite-field checks for the multi-theta Kirchhoff singular-support theorem.

Run with Python 3 (no external packages). These finite checks corroborate,
but do not establish, the characteristic-zero all-parameter theorem.
"""
from itertools import product, combinations


def f_grad(flat, m, q):
    a = [flat[2*i] for i in range(m)]
    b = [flat[2*i+1] for i in range(m)]
    u = [(a[i]+b[i]) % q for i in range(m)]
    v = [a[i]*b[i] % q for i in range(m)]
    terms = [v[i] * prod(u[j] for j in range(m) if j!=i) for i in range(m)]
    f = sum(terms) % q
    deriv = []
    for i in range(m):
        other = sum(v[j] * prod(u[k] for k in range(m) if k!=i and k!=j)
                    for j in range(m) if j!=i)
        base = prod(u[j] for j in range(m) if j!=i)
        deriv.extend(((b[i]*base+other)%q, (a[i]*base+other)%q))
    return f, deriv


def prod(values):
    v=1
    for x in values:
        v *= x
    return v


def component_test(flat,m,q):
    a=[flat[2*i] for i in range(m)]
    b=[flat[2*i+1] for i in range(m)]
    u=[(a[i]+b[i])%q for i in range(m)]
    v=[a[i]*b[i]%q for i in range(m)]
    for i in range(m):
        if a[i]==b[i]==0:
            rest=sum(v[j]*prod(u[k] for k in range(m) if k!=i and k!=j) for j in range(m) if j!=i)
            if rest%q==0: return True
    return sum(t==0 for t in u)>=3


def projective_vectors(q,length):
    for first in range(length):
        for suffix in product(range(q),repeat=length-first-1):
            yield (0,)*first+(1,)+suffix


def audit(m,q):
    examined=sing=part_counts=0
    for x in projective_vectors(q,2*m):
        examined+=1
        f,grad=f_grad(x,m,q)
        actual=(f==0 and all(y==0 for y in grad))
        predicted=component_test(x,m,q)
        if actual!=predicted:
            raise AssertionError((m,q,x,actual,predicted,f,grad))
        sing+=actual
    return m,q,examined,sing


def verify_symbolic_sample(m):
    # Homogeneous gradient identity: sum x_i dF/dx_i = (m+1) F.
    q=101
    for k in range(60):
        x=tuple(((k+17*i*i+7*i+3) % q) for i in range(2*m))
        f,grad=f_grad(x,m,q)
        assert sum(x[i]*grad[i] for i in range(2*m))%q == (m+1)*f%q


def verify_generic_nodes(m):
    # Quadratic forms at generic component points, represented by their
    # Hessian matrices after units are discarded; rank 3 in char 0.
    from fractions import Fraction
    # For C_i, Q = A*s*t+s*w+t*w where A != 0.
    h_c=[[0,3,1],[3,0,1],[1,1,0]]
    # For L_{ijk}, Q=v_i*y*z+v_j*x*z+v_k*x*y; all v_i nonzero.
    h_l=[[0,7,5],[7,0,3],[5,3,0]]
    def det(t):
        return (t[0][0]*(t[1][1]*t[2][2]-t[1][2]*t[2][1])
                -t[0][1]*(t[1][0]*t[2][2]-t[1][2]*t[2][0])
                +t[0][2]*(t[1][0]*t[2][1]-t[1][1]*t[2][0]))
    assert det(h_c)==6 and det(h_l)==210


if __name__=='__main__':
    for m,q in [(3,5),(4,3),(5,2)]:
        print('m,q,projective_points,singular_points =',audit(m,q))
    for m in range(3,12): verify_symbolic_sample(m)
    verify_generic_nodes(4)
    print('VERIFY_OK')
