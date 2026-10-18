"""Direct integer checks for sharp Galileo-prefix envelopes.
This program does not replace the infinite proof.
"""
from fractions import Fraction

def digit_map(n, k):
    total = 0
    factor = 1
    while n:
        total += (n & 1)*factor
        factor *= k
        n //= 2
    return total

def upper(n, k):
    assert n >= 1
    r = (n - 1).bit_length()
    return k**r - digit_map(2**r-n,k)

def make_extremal(k, N, kind):
    assert 2 <= k and 2 <= N
    a=[0]*(N+1)
    a[1]=1
    a[2]=k-1
    for m in range(2, (N+1)//2+1):
        if 2*m-1 <= N:
            a[2*m-1]=1 if kind=='lower' else k*a[m]-1
        if 2*m <= N:
            a[2*m]=k*a[m]-1 if kind=='lower' else 1
    S=[0]
    for i in range(1,N+1):
        assert a[i]>=1, (k,kind,i,a[i])
        S.append(S[-1]+a[i])
    for n in range(1,N//2+1):
        assert S[2*n]==k*S[n],(k,kind,n)
    return S

def deterministic_checks():
    tests=0
    for k in range(2,18):
        N=2000
        lo=make_extremal(k,N,'lower')
        hi=make_extremal(k,N,'upper')
        for n in range(1,N+1):
            assert lo[n]==digit_map(n,k)
            assert hi[n]==upper(n,k)
            assert lo[n]<=hi[n]
            # Exact integer-power test for k=2,4,8,16 when alpha integral.
            if k&(k-1)==0:
                degree=k.bit_length()-1
                assert (k-1)*lo[n]>=n**degree
                assert (k-1)*hi[n]<= (k*(k-1)-1)*n**degree
            tests+=1
    return tests

def exhaustive_positive_splits():
    # Enumerate all positive integer splits of internal tree labels for small horizons.
    # Compares every resulting prefix with the theoretical extrema.
    checks=0
    for k,N in [(2,12),(3,9),(4,7)]:
        a=[0]*(N+1);a[1]=1;a[2]=k-1
        def go(m):
            nonlocal checks
            if 2*m-1>N:
                s=0
                for i in range(1,N+1):
                    s+=a[i]
                    assert digit_map(i,k)<=s<=upper(i,k),(k,N,i,s)
                    checks+=1
                return
            # Set children of m.  When only the odd child fits, its still-unseen even
            # sibling is determined but not present in this prefix.
            for left in range(1,k*a[m]):
                a[2*m-1]=left
                if 2*m<=N: a[2*m]=k*a[m]-left
                go(m+1)
        go(2)
    return checks

if __name__=='__main__':
    print('deterministic envelope tests:',deterministic_checks())
    print('all-positive-split prefix tests:',exhaustive_positive_splits())
    print('verification: PASS')
