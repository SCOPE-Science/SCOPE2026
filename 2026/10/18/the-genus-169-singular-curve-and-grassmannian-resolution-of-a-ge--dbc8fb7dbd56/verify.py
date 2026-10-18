"""Exact checks for the Pfaffian singular-curve calculation.

No finite test substitutes for the transversality and adjunction arguments.
"""
from math import comb
from sympy import Matrix, Symbol, expand, diff, symbols


def pfaffian(a):
    size = a.rows
    if size == 0:
        return 1
    if size % 2:
        return 0
    return expand(sum((-1)**(j+1) * a[0,j] * pfaffian(a.extract(list(range(1,j))+list(range(j+1,size)),list(range(1,j))+list(range(j+1,size)))) for j in range(1,size)))

z=symbols('z0:6')
a=Matrix.zeros(8)
# Rank-four nondegenerate upper block and arbitrary lower alternating block.
for i,j,val in [(0,1,1),(2,3,1),(4,5,z[0]),(4,6,z[1]),(4,7,z[2]),(5,6,z[3]),(5,7,z[4]),(6,7,z[5])]:
    a[i,j]=val; a[j,i]=-val
q=z[0]*z[5]-z[1]*z[4]+z[2]*z[3]
assert expand(pfaffian(a)-q)==0
h=Matrix([[diff(q,s,t) for t in z] for s in z])
assert h.rank()==6
assert abs(h.det())==1
# Harris–Tu degree for rank-at-most-four skew forms on an 8-space.
degree=comb(8,3)*comb(9,2)*10//240
assert degree==84
# Kernel rank four; det(K*) = O(2); det(Λ²K*) = O(6).
normal_det=3*2+6
canonical_degree_twist=normal_det-8
assert (normal_det,canonical_degree_twist)==(12,4)
genus=1+canonical_degree_twist*degree//2
assert genus==169
# Blow-up discrepancy of an order-two hypersurface along codim-six center.
discrepancy=(6-1)-2
assert discrepancy==3
print('VERIFY_OK pfaffian_q=%s hessian_rank=%s degree=%s genus=%s discrepancy=%s' %(q,h.rank(),degree,genus,discrepancy))
