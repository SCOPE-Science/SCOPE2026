"""Finite-field checks of the two-stratum punctual Quot coefficient.
The proof is in RESULT.md; these small tests only check its finite formulas.
"""
from itertools import product

def gaussian(n,k,q):
    if k < 0 or k > n: return 0
    a=b=1
    for i in range(k):
        a*=q**(n-i)-1
        b*=q**(i+1)-1
    return a//b

def proj_lines(n,q):
    # canonical representatives of one-dimensional subspaces over prime fields
    for first in range(n):
        for tail in product(range(q),repeat=n-first-1):
            yield (0,)*first+(1,)+tail

def matrix_rank_two(rows,q):
    a,b=rows
    if not any(a): return int(any(b))
    if not any(b): return 1
    i=next(i for i,z in enumerate(a) if z)
    c=b[i]*pow(a[i],-1,q)%q
    return 1 if all((bj-c*aj)%q==0 for aj,bj in zip(a,b)) else 2

def check(q,d):
    # β=(A,B,C) in P((m²/m³)^d)^*, Xβ=(A,B), Yβ=(B,C).
    ranks={0:0,1:0,2:0}
    for row in proj_lines(3*d,q):
        a=row[:d];b=row[d:2*d];c=row[2*d:]
        ranks[matrix_rank_two((a+b,b+c),q)]+=1
    expected_base=gaussian(d,1,q)*gaussian(2,1,q)
    assert ranks[1]==expected_base,(q,d,ranks,expected_base)
    # One affine graph parameter for each of 2d-1 coefficients.
    total=gaussian(2*d,2,q)+ranks[1]*q**(2*d-1)
    expected=gaussian(2*d,2,q)+q**(2*d-1)*gaussian(d,1,q)*gaussian(2,1,q)
    assert total==expected
    s1=gaussian(d,1,q)
    h1=gaussian(2*d,1,q)
    e2=q*gaussian(d,2,q)
    numerator_t2=total-s1*h1+e2
    assert numerator_t2==q**(2*d)*(gaussian(d,2,q)+gaussian(d,1,q))
    return {'q':q,'d':d,'base':ranks[1],'H_d_t2':total,'NH_d_t2':numerator_t2}

if __name__=='__main__':
    for d in (1,2,3):
        for q in (2,3):
            print(check(q,d))
    print('VERIFY_OK')
