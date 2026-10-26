"""Reproduce exact finite monomial stabilizers and orbit counts.

For prime fields only, the tested nonasymptotic identities use no external packages.
The general theorem uses a separate all-prime-power proof.
"""
from collections import Counter
from itertools import permutations, product
from math import factorial, ceil
from fractions import Fraction


def invertible(A, q, n):
    B = [list(A[i*n:(i+1)*n]) for i in range(n)]
    rank=0
    for c in range(n):
        pivot=next((i for i in range(rank,n) if B[i][c]%q),None)
        if pivot is None: continue
        B[rank],B[pivot]=B[pivot],B[rank]
        scale=pow(B[rank][c],-1,q)
        B[rank]=[(v*scale)%q for v in B[rank]]
        for i in range(rank+1,n):
            x=B[i][c]
            B[i]=[(a-x*b)%q for a,b in zip(B[i],B[rank])]
        rank+=1
    return rank==n


def actual_preservation(A,q,n,sigma,t):
    # Column convention: e_i^2 = sum_j A[j,i] e_j.
    # Check each output coefficient in phi(e_i^2) = phi(e_i)^2.
    for i in range(n):
        for j in range(n):
            lhs=A[j*n+i]*t[j]
            rhs=t[i]**2*A[sigma[j]*n+sigma[i]]
            if (lhs-rhs)%q:
                return False
    return True


def paper_fixed_equation(A,q,n,sigma,t):
    # Fixed points for the action of Wei--Zou (equation (3.1)).
    for i in range(n):
        for j in range(n):
            if (t[i]*A[i*n+j]-t[j]**2*A[sigma[i]*n+sigma[j]])%q:
                return False
    return True


def test(q,n):
    assert q in [2,3,5,7]
    group=list(product(permutations(range(n)),product(range(1,q),repeat=n)))
    assert len(group)==factorial(n)*(q-1)**n
    hist=Counter(); fixed_tot=0; gl=0; trivial=0
    for A in product(range(q),repeat=n*n):
        if not invertible(A,q,n): continue
        gl+=1
        s1=sum(actual_preservation(A,q,n,sigma,t) for sigma,t in group)
        s2=sum(paper_fixed_equation(A,q,n,sigma,t) for sigma,t in group)
        assert s1==s2,(q,n,A,s1,s2)
        hist[s1]+=1; fixed_tot+=s1
        trivial+=(s1==1)
    expected_gl=1
    for i in range(n):expected_gl*=q**n-q**i
    assert gl==expected_gl
    assert fixed_tot%len(group)==0
    # A finite-n fixed-point union bound using the true GL denominator
    # and the integrality of the permutation-orbit codimension.
    epsilon=Fraction(((q-1)**n-1)*q**(n*n-n),gl)
    for sigma in permutations(range(n)):
        k=sum(sigma[i]!=i for i in range(n))
        if k:
            assert k>=2
            codim=ceil(k*(2*n-k)/2)
            epsilon+=Fraction((q-1)**n * q**(n*n-codim),gl)
    assert Fraction(fixed_tot-gl,gl)<=epsilon
    assert Fraction(gl-trivial,gl)<=epsilon
    # The count of orbits via Burnside is an integer and equals the
    # average stabilizer size times |GL|/|G| exactly.
    orbits=fixed_tot//len(group)
    if (q,n)==(2,2): assert orbits==4
    if (q,n)==(3,2): assert orbits==7
    if (q,n)==(2,4): assert orbits==908
    print('FINITE',q,n,'GL',gl,'monomial',len(group), 'orbits',orbits,
          'trivial',trivial,'stabilizers',sorted(hist.items()))


def main():
    for q,n in ((2,2),(2,3),(3,2),(3,3),(5,2),(2,4)):
        test(q,n)
    print('VERIFY_OK')

if __name__=='__main__': main()
