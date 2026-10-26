"""Recompute determinantal witnesses and the sharp leading latent-cap constant."""
import sympy as sp
from random import Random

rng = Random(1987)

def adj2(A):
    return sp.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]])

exact_checks = 0
for _ in range(400):
    p = sp.Matrix([rng.randint(1,9),rng.randint(1,9)])
    q = sp.Matrix([rng.randint(1,9),rng.randint(1,9)])
    u = sp.Matrix([rng.randint(1,9),rng.randint(1,9)])
    v = sp.Matrix([rng.randint(1,9),rng.randint(1,9)])
    A = p*q.T
    N = adj2(A).T
    L = sp.trace(A.T*A)
    gamma = (v.T*adj2(A)*u)[0]
    eta = (v.T*A.T*u)[0]
    assert L>0 and eta>0 and A.det()==0
    assert sp.simplify(sp.trace(N.T*N)-L)==0
    assert (v.T*adj2(A)*u)[0] == ((v.T*sp.Matrix([q[1],-q[0]]))[0]
               *(sp.Matrix([p[1],-p[0]]).T*u)[0])
    for B in (1, 5, 50, 10**6):
        t = -gamma/(B*L+eta)
        Z = (A+t*N).row_join(u).col_join(sp.Matrix([[v[0],v[1],-B]]))
        assert Z.det()==0
        assert sp.simplify((A+t*N).det()-t*L)==0
        assert sp.simplify(sp.trace((t*N).T*(t*N))-t*t*L)==0
        if B==10**6:
            assert all(float(x)>0 for x in A+t*N)
            if gamma:
                E2=t*t*L
                ratio=sp.N(E2*B*B*L/gamma**2)
                assert abs(float(ratio)-1)<0.01
        exact_checks+=1

A=sp.ones(2,2)
u=v=sp.Matrix([1,2])
N=adj2(A).T
L=sp.trace(A.T*A)
gamma=(v.T*adj2(A)*u)[0]
eta=(v.T*A.T*u)[0]
print('symbolic exact determinant and norm checks:',exact_checks)
print('star witness parameters:', {'L':L,'gamma':gamma,'eta':eta})
for B in (10,100,1000,10000):
    t=-gamma/(B*L+eta)
    Z=(A+t*N).row_join(u).col_join(sp.Matrix([[1,2,-B]]))
    assert Z.det()==0 and all(x>0 for x in A+t*N)
    E2=float(t*t*L)
    print('B=%d, error_squared=%.12g, B_squared_times_error=%.12g' % (B,E2,B*B*E2))
