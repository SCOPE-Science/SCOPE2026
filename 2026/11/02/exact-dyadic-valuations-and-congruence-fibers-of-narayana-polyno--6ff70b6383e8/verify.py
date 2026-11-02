"""Independent finite checks of the Narayana polynomial valuation theorem.
Run: python verify.py. Uses only Python's standard library.
"""
from math import comb

def catalan(j):
    return comb(2*j,j)//(j+1)

def direct(n,x):
    return sum((comb(n,k)*comb(n,k-1)//n)*x**k for k in range(1,n+1))

def gamma(n,x):
    return x*sum(comb(n-1,2*j)*catalan(j)*x**j*(x+1)**(n-1-2*j) for j in range((n-1)//2+1))

def v2(z):
    if z==0: return None
    return (abs(z)&-abs(z)).bit_length()-1

def s2(z):
    return z.bit_count()

def predicted(n,x):
    if x%2==0: return v2(x)
    if n%2: return s2((n+1)//2)-1
    b=s2(n//2)-1
    return None if x==-1 else b+v2(x+1)

def density(n,k,r):
    assert 1<=r<=k
    if n%2:
        h=s2((n+1)//2)-1
        return 2**(k-r)+(2**(k-1) if r<=h else 0)
    h=s2(n//2)-1
    return 2**(k-r)+2**(k-max(1,r-h))

compare=0
for n in range(1,37):
    for x in range(-26,27):
        d=direct(n,x)
        assert d==gamma(n,x),(n,x,'gamma')
        assert v2(d)==predicted(n,x),(n,x,'valuation')
        compare+=1
residue=0
for n in range(1,25):
    for k in range(1,9):
        for r in range(1,k+1):
            modulus=1<<k
            actual=sum(direct(n,x)%(1<<r)==0 for x in range(modulus))
            expected=density(n,k,r)
            assert actual==expected,(n,k,r,actual,expected)
            residue+=1
print(f'VERIFY_OK direct_vs_gamma_and_valuations={compare} full_residue_count_tests={residue}')
