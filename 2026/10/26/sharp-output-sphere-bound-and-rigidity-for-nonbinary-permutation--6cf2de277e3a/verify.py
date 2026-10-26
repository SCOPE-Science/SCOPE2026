"""Independently verify sharp output volumes for one window-permutation burst.
Uses only the Python standard library.
"""
from itertools import product, permutations
from collections import Counter
from math import factorial


def support_count(block):
    m=len(block)
    cnt=Counter(block)
    den=1
    for v in cnt.values(): den*=factorial(v)
    all_anagrams=factorial(m)//den
    first,last=block[0],block[-1]
    first_fixed=all_anagrams*cnt[first]//m
    last_fixed=all_anagrams*cnt[last]//m
    both=all_anagrams*cnt[first]*(cnt[last]-(first==last))//(m*(m-1))
    return all_anagrams-first_fixed-last_fixed+both


def local_volume(x,k):
    return 1+sum(support_count(x[i:i+m]) for m in range(2,k+1) for i in range(len(x)-m+1))


def direct_volume(x,k):
    y={x}
    n=len(x)
    for i in range(n-k+1):
        block=x[i:i+k]
        for z in set(permutations(block)):
            y.add(x[:i]+z+x[i+k:])
    return len(y)


def max_volume(n,k):
    return 1+sum((n-m+1)*(factorial(m)-2*factorial(m-1)+factorial(m-2)) for m in range(2,k+1))


def check():
    cases=words=0
    for q in range(2,6):
        for k in range(2,min(q,5)+1):
            for n in range(k,8):
                if q**n>16000: break
                N=0; max_word_count=0
                target=max_volume(n,k)
                for x in product(range(q),repeat=n):
                    got=direct_volume(x,k)
                    loc=local_volume(x,k)
                    assert got==loc,(q,k,n,x,got,loc)
                    assert got<=target,(q,k,n,x,got,target)
                    expected=all(len(set(x[i:i+k]))==k for i in range(n-k+1))
                    assert (got==target)==expected,(q,k,n,x,got,target)
                    N+=1; max_word_count+=(got==target)
                falling=1
                for t in range(k): falling*=q-t
                expected_count=falling*(q-k+1)**(n-k)
                assert max_word_count==expected_count,(q,k,n,max_word_count,expected_count)
                cases+=1; words+=N
    # Also compare the local formula outside the q >= k extremal regime.
    for q,k,n in ((2,4,5),(3,5,6)):
        for x in product(range(q),repeat=n):
            assert direct_volume(x,k)==local_volume(x,k)
            words+=1
    print('CHECKED_PARAMETER_TRIPLES',cases)
    print('CHECKED_WORDS',words)
    print('DNA_Q4_K4_N8_MAX',max_volume(8,4))
    print('VERIFY_OK')

if __name__=='__main__': check()
