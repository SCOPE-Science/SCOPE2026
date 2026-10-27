"""Independent finite tests for enumeration of repeated subsequences in alternating binary hosts."""
from itertools import product
from collections import defaultdict


def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def closed_count(q,k):
    m,r=divmod(k,q)
    return fib(2*m+3)-2 if r==0 else 2*fib(2*m+2)-2


def is_subsequence(candidate,host):
    pos=0
    for symbol in candidate:
        while pos<len(host) and host[pos]!=symbol:
            pos+=1
        if pos==len(host):
            return False
        pos+=1
    return True


def direct_count(q,k):
    host='01'*k
    maximum=len(host)//q
    roots=[]
    for length in range(1,maximum+1):
        for tup in product('01',repeat=length):
            u=''.join(tup)
            if is_subsequence(u*q,host):
                roots.append(u)
    return len(roots)


def recurrence_coeffs(q,max_k):
    # (1-z)(1-3z^q+z^(2q)) F = 3z^q+z^(q+1)-2z^(2q)
    vals=[0]*(max_k+1)
    rhs={q:3,q+1:1,2*q:-2}
    # numerator colliding powers for q=1 not in scope
    for k in range(max_k+1):
        total=rhs.get(k,0)
        # polynomial denominator: 1-z-3z^q+3z^(q+1)+z^(2q)-z^(2q+1)
        for d,c in ((1,-1),(q,-3),(q+1,3),(2*q,1),(2*q+1,-1)):
            if k>=d:total-=c*vals[k-d]
        vals[k]=total
    return vals


def test():
    tests=0
    for q in range(2,9):
        max_k=18
        coefficients=recurrence_coeffs(q,max_k)
        for k in range(max_k+1):
            expected=closed_count(q,k)
            assert coefficients[k]==expected,(q,k,coefficients[k],expected)
            obtained=direct_count(q,k)
            assert obtained==expected,(q,k,obtained,expected)
            tests+=1
    for q in range(2,9):
        for m in range(1,8):
            a=closed_count(q,q*m)-closed_count(q,q*m-1)
            b=closed_count(q,q*m+1)-closed_count(q,q*m)
            assert a==fib(2*m-1)+fib(2*m+1)
            assert b==fib(2*m)
            for r in range(2,q):
                assert closed_count(q,q*m+r)==closed_count(q,q*m+1)
    # Check the full root-length bivariate generating function independently.
    for q in range(2,7):
        root_polys={1:{q:2},2:{q:1,q+1:1,2*q:2}}
        for ell in range(3,10):
            out=defaultdict(int)
            for exp,c in root_polys[ell-1].items():out[exp+q]+=2*c
            for exp,c in root_polys[ell-2].items():
                out[exp+q]+=c
                out[exp+2*q]-=c
            root_polys[ell]=dict(out)
        for k in range(0,13):
            host='01'*k
            for ell in range(1,min(9,(2*k)//q)+1):
                observed=sum(is_subsequence(''.join(bits)*q,host)
                             for bits in product('01',repeat=ell))
                predicted=sum(coef for exp,coef in root_polys[ell].items() if exp<=k)
                assert observed==predicted,('bivariate',q,k,ell,observed,predicted)
    print('VERIFY_OK',tests,'direct parameter pairs; bivariate root-length, rational recurrence and jump tests passed')


if __name__=='__main__':
    test()
