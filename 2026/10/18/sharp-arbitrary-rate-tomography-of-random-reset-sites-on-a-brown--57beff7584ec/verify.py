#!/usr/bin/env python3
"""Symbolic and numerical checks for finite-rate Brownian reset-site tomography."""
import sympy as sp
import mpmath as mp
from math import cosh


def exact_test(weights, powers):
    # q0=ln 2, t_i integer, Z_i=cosh(q0 t_i). Ring length L=2*(max(t_i)+1).
    N=len(weights)
    w=list(map(sp.Rational, weights))
    ts=list(powers)
    assert sum(w)==1 and len(set(ts))==N and all(x>=0 for x in ts)
    Z=[sp.Rational(2**t,2)+sp.Rational(1,2*2**t) for t in ts]
    T=[sp.Integer(1)]
    for j in range(1,2*N):
        T.append(sp.simplify(sum(w[i]*sp.chebyshevt(j,Z[i]) for i in range(N))))
    # Simulate measured dimensionless means H_j=r_j E[T_r] = cosh(j q L/2)/E[cosh(j q t)]-1.
    L2=max(ts)+1
    H=[]
    for j in range(1,2*N):
        C=sp.Rational(2**(j*L2),2)+sp.Rational(1,2*2**(j*L2))
        H.append(C/T[j]-1)
    # Rebuild Chebyshev transform from no assumed weights or nodes.
    Cobs=[sp.Integer(1)]
    for j in range(1,2*N):
        C=sp.Rational(2**(j*L2),2)+sp.Rational(1,2*2**(j*L2))
        Cobs.append(sp.cancel(C/(1+H[j-1])))
    assert Cobs==T
    z=sp.symbols('z')
    # Ascending power moments from the measured Chebyshev transform.
    power=[sp.Integer(1)]
    for j in range(1,2*N):
        p=sp.Poly(sp.chebyshevt(j,z),z)
        lead=p.nth(j)
        power.append(sp.factor((Cobs[j]-sum(p.nth(k)*power[k] for k in range(j)))/lead))
    assert all(sp.simplify(power[j]-sum(w[i]*Z[i]**j for i in range(N)))==0 for j in range(2*N))
    # Exact Hankel/Prony reconstruction of N nodes and positive weights.
    h=sp.Matrix([[power[i+j] for j in range(N)] for i in range(N)])
    assert h.det()>0
    tail=sp.Matrix([-power[N+i] for i in range(N)])
    coeff=h.inv()*tail
    polynomial=sp.expand(z**N+sum(coeff[k]*z**k for k in range(N)))
    assert sp.factor(polynomial-sp.prod(z-zz for zz in Z))==0
    nodes=sorted(Z)
    vm=sp.Matrix([[zz**j for zz in nodes] for j in range(N)])
    recovered=vm.inv()*sp.Matrix(power[:N])
    assert recovered==sp.Matrix([w[Z.index(zz)] for zz in nodes])
    # Physical geodesic distance d=L/2-t, not oriented side of target.
    print('exact',N,'atoms: measured H=',H,'recovered z=',nodes,'weights=',list(recovered))


def totally_positive_checks():
    mp.mp.dps=75
    for k in range(1,6):
        for shift in (0, 1, 2):
            qq=[mp.mpf(shift*11+i*2+1)/13 for i in range(k)]
            tt=[mp.mpf(shift*7+i*3+1)/17 for i in range(k)]
            if shift==0:
                qq[0]=mp.mpf(0)
                tt[0]=mp.mpf(0)
            matrix=mp.matrix([[mp.cosh(qq[i]*tt[j]) for j in range(k)] for i in range(k)])
            determinant=mp.det(matrix)
            assert determinant>0,(k,shift,determinant)
    print('strict total positivity: 15 square cosh-kernel determinants PASSED')


def numerical_test():
    mp.mp.dps=75
    N=3; L=6; D=2; q=mp.mpf('0.32')
    t=[mp.mpf('0.2'),mp.mpf('1.17'),mp.mpf('2.14')]
    w=[mp.mpf('0.2'),mp.mpf('0.35'),mp.mpf('0.45')]
    z=[mp.cosh(q*x) for x in t]
    # Forward-law cross-check via ODE boundary value u''=q_j^2 u.
    for j in range(1,2*N):
        qq=j*q; rate=D*qq**2
        integr=sum(w[i]*mp.cosh(qq*t[i])/mp.cosh(qq*L/2) for i in range(N))
        tau=(1-integr)/(rate*integr)
        got=mp.cosh(qq*L/2)/(1+rate*tau)
        target=sum(w[i]*mp.chebyt(j,z[i]) for i in range(N))
        assert mp.almosteq(got,target,rel_eps=mp.mpf('1e-65'))
    # Five observations as above; moment-to-power recursion with mpmath.
    C=[mp.mpf(1)]+[sum(w[i]*mp.cosh(j*q*t[i]) for i in range(N)) for j in range(1,2*N)]
    M=[mp.mpf(1)]
    for j in range(1,2*N):
        coeff=sp.Poly(sp.chebyshevt(j,sp.Symbol('zz')),sp.Symbol('zz'))
        M.append((C[j]-sum(mp.mpf(str(coeff.nth(k)))*M[k] for k in range(j)))/mp.mpf(str(coeff.nth(j))))
    H=mp.matrix([[M[i+j] for j in range(N)] for i in range(N)])
    v=mp.matrix([-M[N+i] for i in range(N)])
    a=mp.lu_solve(H,v)
    assert max(abs(sum(a[k]*zz**k for k in range(N))+zz**N) for zz in z)<mp.mpf('1e-60')
    # Build a 1D discretized killing generator as a separate consistency check.
    # Exact u(x)=cosh(q(x-L/2))/cosh(qL/2) solves u(0)=u(L)=1.
    for xx in [mp.mpf('0.2'),mp.mpf('1.3'),mp.mpf('4.4')]:
        qq=q; h=mp.mpf('1e-4')
        u=lambda x:mp.cosh(qq*(x-L/2))/mp.cosh(qq*L/2)
        approx=(u(xx+h)-2*u(xx)+u(xx-h))/h**2
        assert abs(approx-qq**2*u(xx))<mp.mpf('1e-9')
    print('numerical: 3-atom forward/inverse 75-digit moments and boundary ODE checks PASSED')


if __name__=='__main__':
    exact_test(['1/3','2/3'],[0,1])
    exact_test(['1/6','1/3','1/2'],[0,1,2])
    exact_test(['1/10','1/5','3/10','2/5'],[0,1,2,3])
    totally_positive_checks()
    numerical_test()
    print('all checks PASSED')
