"""Exact checks for the square two-block sparse-sign sketch theorem.

Run: python verify.py (Python 3 standard library only).
Finite tests supplement the general combinatorial proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial


def poly_mul_linear(a, constant):
    out = [Fraction(0)] * (len(a) + 1)
    for i, x in enumerate(a):
        out[i] += x*constant
        out[i+1] += x/4
    return out


def law(p,q):
    """Coefficients of E[1_{rank=n} u^C], exact positive finite sum."""
    n=p+q
    out=[Fraction(0) for _ in range(min(p,q)+1)]
    coeff=[Fraction(0) for _ in range(min(p,q)+1)]
    rising=[Fraction(1)]
    pref=Fraction(factorial(n)*factorial(p)*factorial(q),(p*q)**n)
    for k in range(min(p,q)+1):
        if k:
            rising=poly_mul_linear(rising,k-1)
        primary=Fraction(q**(p-k)*p**(q-k),factorial(p-k)*factorial(q-k))
        for i,v in enumerate(rising):
            coeff[i]+=pref*primary*v/factorial(k)
        if k:
            prior=[Fraction(1)]
            for j in range(k-1):
                prior=poly_mul_linear(prior,j)
            previous=Fraction(q**(p-k)*p**(q-k),factorial(p-k)*factorial(q-k))
            for i,v in enumerate(prior):
                coeff[i]-=pref*previous*v/factorial(k-1)
    assert coeff[0]==0
    return coeff


def component_count(p,q, hashes):
    n=p+q
    parent=list(range(n)); vertices=[1]*n; edges=[0]*n
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for h in hashes:
        left,right=divmod(h,q)
        a=root(left);b=root(p+right)
        if a!=b:
            parent[b]=a;vertices[a]+=vertices[b];edges[a]+=edges[b]
        edges[a]+=1
    roots=set(root(i) for i in range(n))
    if any(edges[i]!=vertices[i] for i in roots): return None
    return len(roots)


def hash_enumeration(p,q):
    n=p+q; ans=[Fraction(0) for _ in range(min(p,q)+1)]
    for hashes in product(range(p*q),repeat=n):
        c=component_count(p,q,hashes)
        if c is not None: ans[c]+=Fraction(1,2**c)
    return [a/(p*q)**n for a in ans]


def integer_det(M):
    n=len(M);a=[[Fraction(z) for z in row] for row in M]
    det=Fraction(1)
    for j in range(n):
        idx=next((i for i in range(j,n) if a[i][j]),None)
        if idx is None:return 0
        if idx!=j:
            a[j],a[idx]=a[idx],a[j];det=-det
        pivot=a[j][j];det*=pivot
        for i in range(j+1,n):
            factor=a[i][j]/pivot
            for k in range(j+1,n):a[i][k]-=factor*a[j][k]
            a[i][j]=0
    assert det.denominator==1
    return int(det)


def signed_enumeration(p,q):
    n=p+q;ans=[0 for _ in range(min(p,q)+1)]
    for hashes in product(range(p*q),repeat=n):
        for signs in product((-1,1),repeat=n):
            M=[[0]*n for _ in range(n)]
            for j,(h,sgn) in enumerate(zip(hashes,signs)):
                left,right=divmod(h,q)
                M[left][j]=1;M[p+right][j]=sgn
            det=integer_det(M)
            if det:
                c=component_count(p,q,hashes)
                assert c is not None
                assert det*det==4**c,(p,q,hashes,signs,det,c)
                ans[c]+=1
    return [Fraction(a,(p*q)**n*2**n) for a in ans]


def main():
    hash_pairs=[(1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(1,4),(4,1),(2,3),(3,2),(3,3)]
    for p,q in hash_pairs:
        assert law(p,q)==hash_enumeration(p,q),(p,q,law(p,q),hash_enumeration(p,q))
    for p,q in [(1,1),(1,2),(2,1),(1,3),(2,2)]:
        assert law(p,q)==signed_enumeration(p,q)
    for b,expected in enumerate([Fraction(1,2),Fraction(87,256),Fraction(2675,13122),
                                 Fraction(126557865,1073741824)],1):
        assert sum(law(b,b))==expected
    for p in range(1,11):
        for q in range(1,11):
            coeff=law(p,q)
            assert all(x>=0 for x in coeff)
            # Exact Cauchy-Binet determinant second-moment identity.
            second_moment=sum(x*4**c for c,x in enumerate(coeff))/2**(p+q)
            assert second_moment==Fraction(factorial(p+q),
                                             2**(p+q)*p**p*q**q)
    for q in range(1,15):
        assert sum(law(1,q))==Fraction(factorial(q+1),4*q**q)
    print('VERIFIED: all hash assignments for 11 block-size pairs, up to (3,3).')
    print('VERIFIED: all hash and sign assignments, integer determinants for 5 pairs.')
    print('VERIFIED: exact probability values, one-versus-q closed form,')
    print('nonnegative PGF coefficients and determinant second moments for 100 pairs.')
    for b in range(1,6):print('balanced',b,'=',sum(law(b,b)))

if __name__=='__main__':main()
