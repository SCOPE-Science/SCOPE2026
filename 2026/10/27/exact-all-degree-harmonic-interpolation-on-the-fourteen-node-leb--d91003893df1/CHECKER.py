#!/usr/bin/env python3
"""Exact-rational certificate for pure-degree spherical-harmonic sampling on
six axial and eight body-diagonal points of the unit two-sphere.

No floating-point rank decisions are used.  The infinite tail is discharged
in the accompanying proof using the classical Bernstein bound.
"""
from fractions import Fraction as Q

LIMIT=29

def legendre_at_values(limit):
    # Values at 0 and 1/3 are rational.  The third value is stored as
    # u+v/sqrt(3), making all relevant squares rational.
    z=[Q(1),Q(0)]
    c=[Q(1),Q(1,3)]
    d=[(Q(1),Q(0)),(Q(0),Q(1))]
    for n in range(2, limit):
        z.append(-Q(n-1,n)*z[-2])
        c.append((Q(2*n-1,3)*c[-1]-(n-1)*c[-2])/n)
        u,v=d[-1]; U,V=d[-2]
        d.append(((Q(2*n-1,3)*v-(n-1)*U)/n,
                  ((2*n-1)*u-(n-1)*V)/n))
        assert (d[-1][1]==0) if n%2==0 else (d[-1][0]==0)
    return z,c,d

def expected(n):
    if n==0: return 1
    if n==1: return 3
    if n==2: return 5
    if n==3: return 4
    if n in (4,5,6,8,10,14): return 6
    return 7

def rational_matrix_rank(matrix):
    """Exact Gaussian elimination on a fresh copy of a rational matrix."""
    a=[list(row) for row in matrix]
    rows=len(a); cols=len(a[0]); rank=0
    for col in range(cols):
        pivot=next((k for k in range(rank,rows) if a[k][col]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        t=a[rank][col]
        a[rank]=[v/t for v in a[rank]]
        for j in range(rows):
            if j!=rank and a[j][col]:
                t=a[j][col]
                a[j]=[x-t*y for x,y in zip(a[j],a[rank])]
        rank+=1
        if rank==rows:break
    return rank

def raw_seven_node_rank(n,b,c,d):
    """An independent rational-rank calculation of the seven-node Gram.

    For odd n, congruence scaling of the three axis rows and columns by
    sqrt(3) makes all entries rational, without changing rank.
    """
    squares=[(1,1),(1,-1),(-1,1),(-1,-1)]
    mat=[[Q(0) for _ in range(7)] for _ in range(7)]
    for i in range(7):
        for j in range(7):
            if i==j:
                mat[i][j]=Q(3) if (n%2 and i<3) else Q(1)
            elif i<3 and j<3:
                mat[i][j]=b
            elif i>=3 and j>=3:
                e,f=squares[i-3];E,F=squares[j-3]
                dot=Q(1+e*E+f*F,3)
                mat[i][j]=c if dot>0 else c*((-1)**n)
            else:
                axis=i if i<3 else j
                corner=j-3 if j>=3 else i-3
                e,f=squares[corner]
                sig=[1,e,f][axis]
                mat[i][j]=d*sig if n%2 else d
    return rational_matrix_rank(mat)

def signs(x):
    return '+' if x>0 else '0' if x==0 else '-'


def main():
    z,c,d=legendre_at_values(LIMIT)
    lines=['degree parity rank key_det other_a other_b']
    even_zeros=[]; odd_zeros=[]; special_zeros=[]
    for n in range(LIMIT):
        b=z[n]; h=c[n]
        D=d[n][0]**2 + d[n][1]**2/Q(3)
        assert D>=0
        if n%2==0:
            assert d[n][1]==0
            aa=1+2*b; cc=1+3*h; dd=aa*cc-12*D
            assert aa>=0 and cc>=0 and dd>=0
            assert 1-b>=0 and 1-h>=0
            # rank of 2x2 block, with diagonal entries nonnegative
            two_rank=2 if dd>0 else (1 if aa+cc>0 else 0)
            rank=2*int(1-b>0)+3*int(1-h>0)+two_rank
            if dd==0: even_zeros.append(n)
            lines.append(f'{n:2d} even {rank} {signs(dd)} {signs(1-b)} {signs(1-h)}')
        else:
            assert d[n][0]==0
            det=1+h-4*D
            special=1-3*h
            assert det>=0 and special>=0
            assert 1+h>=0
            rank=3*(2 if det>0 else (1 if 1+h>0 else 0))+int(special>0)
            if det==0: odd_zeros.append(n)
            if special==0: special_zeros.append(n)
            lines.append(f'{n:2d} odd  {rank} {signs(det)} {signs(special)} -')
        # For odd n the cross-block factor d is the rational numerator v,
        # whereas D contains its square divided by 3.
        assert rank==raw_seven_node_rank(n,b,h,d[n][1] if n%2 else d[n][0]),(n,rank)
        assert rank==expected(n),(n,rank,expected(n))
    assert even_zeros==[0,2,4,6,8,10,14]
    assert odd_zeros==[1,3]
    assert special_zeros==[1,5]
    n=14
    aa=1+2*z[n]
    D14=d[n][0]
    assert D14!=0
    cube_over_axis=-aa/(4*D14)
    assert cube_over_axis==Q(-729,1024)
    assert 3*D14+(1+3*c[n])*cube_over_axis==0
    assert Q(72,1) < Q(157,50)*29*Q(4,5)  # strict Gershgorin tail
    print('\n'.join(lines))
    print('even_2x2_determinant_zeros:',even_zeros)
    print('odd_2x2_determinant_zeros:',odd_zeros)
    print('odd_remaining_scalar_zeros:',special_zeros)
    print('degree14_even_orbit_null_relation_cube_over_axis:',cube_over_axis)
    print('Bernstein_Gershgorin_for_all_n_ge_29: strict (pi>157/50,sin>4/5)')
    print('29 finite degrees checked by rational arithmetic; PASSED')

if __name__=='__main__': main()
