"""Exact independent checks for complementary-pair zero-sum avoidance.

Finite exhaustive checks are a cross-check, not a proof for arbitrary dimensions.
"""
from itertools import combinations, combinations_with_replacement
from math import comb


def coeff_base(m, n, stride=1):
    """Coefficient of ((1+t)/(1-t))**m at t**(n/stride)."""
    if n % stride:
        return 0
    k = n // stride
    if k == 0:
        return 1
    return sum(comb(m,j)*comb(m+k-j-1,k-j)
               for j in range(min(m,k)+1))


def signed_coeff(m,n):
    return (-1)**(n//2)*comb(m,n//2) if n % 2 == 0 and n//2 <= m else 0


def formula(dim,length):
    N=1<<dim;m=N//2
    zero_total=(comb(N,length) if length <= N else 0)+(N-1)*signed_coeff(m,length)
    assert zero_total % N==0
    t=coeff_base(m,length)-m*coeff_base(m,length,2)
    assert t % N==0, (dim,length,t)
    return zero_total//N +(N-1)*(t//N)


def brute(dim,length):
    N=1<<dim
    count=0
    for seq in combinations_with_replacement(range(N),length):
        total=0
        for v in seq:total ^=v
        ok=True
        for i,j in combinations(range(length),2):
            if (seq[i]^seq[j])==total:
                ok=False;break
        if ok:count+=1
    return count


def independent_dynamic(dim,length):
    """Count directly by XOR-state polynomials, without character algebra.

    For total zero, choose a subset of distinct group elements. For a
    nonzero total, restrict occupancy to one element of each T-pair.
    """
    size=1<<dim
    dp={(0,0):1}
    for x in range(size):
        ndp=dict(dp)
        for (k,t),v in dp.items():
            if k<length:
                key=(k+1,t^x)
                ndp[key]=ndp.get(key,0)+v
        dp=ndp
    count=dp.get((length,0),0)
    for T in range(1,size):
        pairs=[]
        visited=set()
        for x in range(size):
            if x in visited:continue
            pairs.append((x,x^T))
            visited.add(x);visited.add(x^T)
        dp={(0,0):1}
        for x,y in pairs:
            ndp=dict(dp)
            for (k,t),v in dp.items():
                for c in range(1,length-k+1):
                    if c%2:
                        for z in (x,y):
                            key=(k+c,t^z)
                            ndp[key]=ndp.get(key,0)+v
                    else:
                        key=(k+c,t)
                        ndp[key]=ndp.get(key,0)+2*v
            dp=ndp
        count+=dp.get((length,T),0)
    return count


def orbit_case():
    from collections import Counter
    from itertools import product
    d=3;n=8
    types=Counter()
    for seq in combinations_with_replacement(range(8),8):
        T=0
        for x in seq:T^=x
        if any((seq[i]^seq[j])==T for i,j in combinations(range(8),2)):
            continue
        types[tuple(sorted(Counter(seq).values(),reverse=True))]+=1
    assert types=={(1,)*8:1,(5,1,1,1):224,(3,3,1,1):336},types


def main():
    for d,upper in [(2,12),(3,11)]:
        for n in range(2,upper+1):
            a=brute(d,n)
            b=formula(d,n)
            assert a==b,(d,n,a,b)
            print(f'd={d}, n={n}: {a}')
    for d,n in [(3,8),(4,8),(4,12),(4,16)]:
        assert independent_dynamic(d,n)==formula(d,n),(d,n)
    orbit_case()
    assert formula(3,8)==561
    assert formula(4,16)==13032001
    print('VERIFY_OK')

if __name__=='__main__':main()
