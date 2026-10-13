from math import comb
import sympy as sp

# Universal dimension identity for every admissible radical stratum in a broad replay range.
checks = 0
for n in range(4, 21):
    for k in range(2, n-1):
        for r in range(1, min(k,n-k)+1):
            dim_ogr = r*(n-r) - r*(r+1)//2
            dim_fibre = (k-r)*(n-k-r)
            codim = k*(n-k) - (dim_ogr + dim_fibre)
            assert codim == comb(r+1,2)
            checks += 1

# Symbolic Cauchy--Binet identity F=sum Pluecker^2=det(I+B B^T)
# for k=2,n=4 and k=3,n=6 affine charts.
def all_minors_sum_square(A,k):
    from itertools import combinations
    s=0
    for cols in combinations(range(A.cols),k):
        s += A[:,cols].det()**2
    return sp.expand(s)

for k in (2,3):
    m=k
    xs=sp.symbols('x0:'+str(k*m))
    B=sp.Matrix(k,m,xs)
    A=sp.eye(k).row_join(B)
    lhs=all_minors_sum_square(A,k)
    rhs=sp.expand((sp.eye(k)+B*B.T).det())
    assert sp.expand(lhs-rhs)==0

# Exact singular/smooth witnesses on the chart using i^2=-1.
I=sp.I
for k in range(2,11):
    B2=sp.diag(*([I,I]+[1]*(k-2)))
    M2=sp.eye(k)+B2*B2.T
    assert M2.rank()==k-2
    assert M2.det()==0
    grad2=2*M2.adjugate()*B2
    assert grad2==sp.zeros(k)

    B1=sp.diag(*([I]+[1]*(k-1)))
    M1=sp.eye(k)+B1*B1.T
    assert M1.rank()==k-1
    assert M1.det()==0
    grad1=2*M1.adjugate()*B1
    assert grad1!=sp.zeros(k)

print(f"dimension_identity_checks={checks}")
print("cauchy_binet_symbolic_k2_k3=ok")
print("corank2_singular_witnesses_k2_to_k10=ok")
print("corank1_smooth_witnesses_k2_to_k10=ok")
print("VERIFY_OK")
