"""Independent finite checks for the exact five-run palindromic-defect distribution.

Run with Python 3, no external packages. Exhaustive checks are finite evidence;
the accompanying mathematical argument proves the unrestricted identities.
"""
from collections import Counter
from itertools import product
from math import comb


def word(a,b,c,d,e):
    return '0'*a+'1'*b+'0'*c+'1'*d+'0'*e


def palindromes_by_centers(w):
    pal=set()
    for mid in range(len(w)):
        for left,right in ((mid,mid),(mid,mid+1)):
            while left>=0 and right<len(w) and w[left]==w[right]:
                pal.add(w[left:right+1]);left-=1;right+=1
    return pal


def predicted_defect(a,b,c,d,e):
    return (max(0,min(a,e)-c) if b!=d else 0)


def direct_histogram(n):
    hist=Counter()
    for a in range(1,n-3):
        for b in range(1,n-a-2):
            for c in range(1,n-a-b-1):
                for d in range(1,n-a-b-c):
                    e=n-a-b-c-d
                    hist[predicted_defect(a,b,c,d,e)]+=1
    return hist


def generating_coefficient(n,r):
    """Coefficient of z^n y^r from the proved bivariate rational GF."""
    if r>=1:
        k=n-(2*r+6)
        return sum(2*comb(k-3*j+2,2) for j in range(k//3+1)) if k>=0 else 0
    total=comb(n-1,4) if n>=5 else 0
    return total-sum(generating_coefficient(n,i) for i in range(1,max(0,(n-6)//2)+1))


def predicted_total_defect(n):
    ans=0
    # [z^n] 2 z^8 / ((1-z)^3(1-z^3)(1-z^2)^2)
    for k in range((n-8)//3+1) if n>=8 else []:
        for ell in range((n-8-3*k)//2+1):
            q=n-8-3*k-2*ell
            ans+=2*(ell+1)*comb(q+2,2)
    return ans


def run():
    tested=0
    for a,b,c,d,e in product(range(1,6),repeat=5):
        s=word(a,b,c,d,e)
        actual=len(s)-len(palindromes_by_centers(s))
        expectation=predicted_defect(a,b,c,d,e)
        assert actual==expectation,(a,b,c,d,e,actual,expectation)
        tested+=1
    for n in range(5,27):
        histogram=direct_histogram(n)
        assert sum(histogram.values())==comb(n-1,4)
        for r in range(0,max(0,(n-6)//2)+2):
            assert histogram[r]==generating_coefficient(n,r),(n,r,histogram[r],generating_coefficient(n,r))
        assert sum(r*count for r,count in histogram.items())==predicted_total_defect(n)
        assert max(histogram)==max(0,(n-6)//2),(n,max(histogram))
    # all <= four runs are rich; check 4-run exhaustive boundary
    for a,b,c,d in product(range(1,6),repeat=4):
        w='0'*a+'1'*b+'0'*c+'1'*d
        assert len(palindromes_by_centers(w))==len(w),(a,b,c,d)
    print('VERIFY_OK five_run_palindrome_centers=3125 four_run_boundary=625 histograms_n=5..26 moments_n=5..26')

if __name__=='__main__':
    run()
