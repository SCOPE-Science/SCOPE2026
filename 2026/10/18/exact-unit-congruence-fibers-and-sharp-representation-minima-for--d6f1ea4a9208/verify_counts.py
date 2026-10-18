"""Exact independent finite checks for unit quadratic-congruence fiber formulas.

No external libraries. This is a finite consistency check, not a proof of the
unrestricted theorem, whose proof is in RESULT.md.
"""
from math import gcd


def factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            k=0
            while n%p==0:
                n//=p
                k+=1
            out.append((p,k))
        p+=1
    if n>1:out.append((n,1))
    return out


def chi(a,p):
    a%=p
    if a==0:return 0
    t=pow(a,(p-1)//2,p)
    return 1 if t==1 else -1


def local_prime(p,d,m):
    assert p%2==1
    e=chi(-1,p)
    z=chi(m,p)
    if d%p==0:
        return (p-1)*(p-2-e-2*z) if m%p else (p-1)**2*(1+e)
    a=chi(d,p)
    return p*p-3*p+3+e+2*a+z*(a*(p+e)+2) if m%p else (p-1)*(p-2-2*a-e)


def local_two(e,d,m):
    if not e:return 1
    t=min(e,3)
    if (m-(2-d))%(2**t):return 0
    return 2**(3*(e-1)-max(e-3,0))


def theorem(n,d,m):
    total=1
    for p,k in factors(n):
        total*= local_two(k,d,m) if p==2 else p**(2*(k-1))*local_prime(p,d,m)
    return total


def direct_counts(n,d):
    units=[x for x in range(n) if gcd(x,n)==1]
    cnt=[0]*n
    for a in units:
        aa=a*a
        for b in units:
            s=aa+b*b
            for c in units:
                cnt[(s-d*c*c)%n]+=1
    return cnt


def independent_pair_convolution(n,d):
    units=[x for x in range(n) if gcd(x,n)==1]
    sq=[x*x%n for x in units]
    counts2=[0]*n
    for x in sq:
        for y in sq:counts2[(x+y)%n]+=1
    ans=[0]*n
    for m in range(n):
        ans[m]=sum(counts2[(m+d*z)%n] for z in sq)
    return ans


def run():
    pairs=0
    for n in [3,5,7,9,11,13,16,17,19,23,25,27,29,31,32,35,37,41,43,47,49,64,65,77,81,91,125,128]:
        dd=list(range(n)) if n<=49 else [0,1,2,3,5,11,n//2,n-1]
        for d in dd:
            expected=[theorem(n,d,m) for m in range(n)]
            observed=independent_pair_convolution(n,d)
            assert expected==observed,(n,d,[(m,expected[m],observed[m]) for m in range(n) if expected[m]!=observed[m]][:5])
            assert sum(expected)==sum(gcd(x,n)==1 for x in range(n))**3
            if n<=37 and d in (0,1,2,n-1):
                assert direct_counts(n,d)==expected,(n,d,'triple count')
            pairs+=1
    # Validate exact sharp worst-fiber minima and the previously known existence criterion.
    for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
        for d in range(p):
            expected=min(local_prime(p,d,m) for m in range(p))
            if p==3:
                proposed=0
            elif p==5:
                proposed=8 if chi(d,p)==-1 else 0
            elif p%4==3:
                proposed=(p-1)*(p-3) if d%p else 0
            else:
                proposed=(p-1)*(p-3) if chi(d,p)==-1 else (p-1)*(p-5)
            assert expected==proposed,(p,d,expected,proposed)
    print('VERIFY_OK',pairs,'modulus/parameter profiles; direct triples and pair convolution agree; local sharp minima confirmed')

if __name__=='__main__':run()
