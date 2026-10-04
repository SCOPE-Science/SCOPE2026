from itertools import product
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def euler_matrix(Q, k, chi):
    rho = Q.rows
    M = sp.zeros(rho + 2)
    # Order (e, f_1,...,f_rho,p), where e=(1,0,0), p=(0,0,1).
    M[0,0] = -chi
    M[0,rho+1] = 1
    M[rho+1,0] = 1
    for i in range(rho):
        M[i+1,0] = k[i]
        for j in range(rho):
            M[i+1,j+1] = -Q[i,j]
    return M


def reduced_target(Q):
    rho = Q.rows
    T = sp.zeros(rho + 2)
    # Order (e,p,f_1,...,f_rho): H plus -Q.
    T[0,1] = T[1,0] = 1
    for i in range(rho):
        for j in range(rho):
            T[i+2,j+2] = -Q[i,j]
    return T


def explicit_reduce(M, Q, k, chi):
    rho = Q.rows
    # Simultaneously reorder rows and columns from (e,f...,p) to (e,p,f...).
    order = [0, rho+1] + list(range(1,rho+1))
    A = M.extract(order, order)
    # Row f_i <- row f_i - k_i row p.
    for i in range(rho):
        A.row_op(i+2, lambda v,j: v - k[i]*A[1,j])
    # Col e <- col e + chi col p.
    old0 = [A[i,0] for i in range(rho+2)]
    old1 = [A[i,1] for i in range(rho+2)]
    for i in range(rho+2):
        A[i,0] = old0[i] + chi*old1[i]
    return A

examples = [
    (sp.Matrix([[2]]), [0], 2),
    (sp.Matrix([[1,0],[0,-1]]), [3,-1], 1),
    (sp.Matrix([[4,1],[1,-2]]), [5,7], 3),
    (sp.Matrix([[6,1,0],[1,-2,1],[0,1,-4]]), [2,-3,5], 4),
    (sp.Matrix([[8,1,0,0],[1,-2,1,0],[0,1,-4,1],[0,0,1,-6]]), [1,2,3,4], 5),
]

checked = 0
for Q,k,chi in examples:
    assert Q.det() != 0
    M = euler_matrix(Q,k,chi)
    T = reduced_target(Q)
    R = explicit_reduce(M,Q,k,chi)
    assert R == T
    # Determinant identity before invoking the surface-signature sign conclusion.
    rho = Q.rows
    assert M.det() == (-1)**(rho+1) * Q.det()
    sM = smith_normal_form(M, domain=ZZ)
    sT = smith_normal_form(T, domain=ZZ)
    # Smith forms may differ by signs on diagonal; compare absolute invariant factors.
    invM = sorted(abs(int(sM[i,i])) for i in range(sM.rows))
    invT = sorted(abs(int(sT[i,i])) for i in range(sT.rows))
    assert invM == invT
    sQ = smith_normal_form(Q, domain=ZZ)
    invQ = sorted(abs(int(sQ[i,i])) for i in range(sQ.rows))
    assert invM == sorted([1,1] + invQ)
    checked += 1

print(f'matrix_examples_checked={checked}')
print('explicit_integral_reduction=ok')
print('determinant_identity=ok')
print('smith_invariant_factors=ok')
print('VERIFY_OK')
