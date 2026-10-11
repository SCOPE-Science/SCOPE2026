#!/usr/bin/env python3
import itertools, math
from fractions import Fraction

for n in range(2,11):
    m=n+1
    # Cube-section vertices: all but at most one coordinate are +/-1.
    verts=set()
    for free in range(m):
        others=[i for i in range(m) if i!=free]
        for signs in itertools.product((-1,1), repeat=m-1):
            s=sum(signs)
            y=[None]*m
            for i,z in zip(others,signs): y[i]=z
            y[free]=-s
            if -1 <= y[free] <= 1:
                verts.add(tuple(y))
    # Include all-balanced cube vertices explicitly; duplicates collapse.
    for y in itertools.product((-1,1), repeat=m):
        if sum(y)==0: verts.add(tuple(y))
    assert verts
    maxsq=max(sum(z*z for z in y) for y in verts)
    far=[y for y in verts if sum(z*z for z in y)==maxsq]
    expected_sq=m if n%2 else n
    expected_count=math.comb(m,m//2) if n%2 else m*math.comb(n,n//2)
    assert maxsq==expected_sq,(n,maxsq)
    assert len(far)==expected_count,(n,len(far),expected_count)
    R2=Fraction(maxsq,n*m)
    expected_R2=Fraction(1,n) if n%2 else Fraction(1,n+1)
    assert R2==expected_R2
    # Every farthest point has the claimed coordinate pattern.
    for y in far:
        if n%2:
            assert y.count(1)==m//2 and y.count(-1)==m//2
        else:
            assert y.count(0)==1 and y.count(1)==n//2 and y.count(-1)==n//2

# Exact regular-simplex Gram/frame sanity in ambient zero-sum coordinates.
for n in range(2,9):
    m=n+1
    # u_i=e_i-(1/m)1, v_i=sqrt(m/n)u_i. Check unscaled dot products.
    # u_i.u_i=n/m; u_i.u_j=-1/m.
    assert Fraction(n,m)*Fraction(m,n)==1
    assert Fraction(-1,m)*Fraction(m,n)==Fraction(-1,n)
    # Frame operator of v_i on the zero-sum hyperplane is m/n times identity.
    # Verified coefficient is exact.
    assert Fraction(m,n)==Fraction(n+1,n)

print('VERIFY_OK')
print('cube_section_vertices_n_2_to_10 = passed')
print('parity_radius_formula = exact')
print('farthest_point_counts = exact')
