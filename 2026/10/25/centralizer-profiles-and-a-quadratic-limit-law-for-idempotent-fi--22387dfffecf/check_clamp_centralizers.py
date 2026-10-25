#!/usr/bin/env python3
"""Finite checks of the centralizer census for chain contractions."""
from itertools import product
from math import comb, log2

def all_contractions(n):
    """Independent adjacent-value enumeration of nondecreasing 1-Lipschitz maps."""
    for increments in product((0,1), repeat=n-1):
        total=sum(increments)
        for start in range(1,n-total+1):
            values=[start]
            for increment in increments:
                values.append(values[-1]+increment)
            yield tuple(values)

def clamp(n,a,b):
    return tuple(max(a,min(x,b)) for x in range(1,n+1))

def commute(f,g):
    return all(f[g[i]-1]==g[f[i]-1] for i in range(len(f)))

def prediction(n,a,b):
    k=b-a; left=a-1; right=n-b
    if k==0:
        return 2**(n-1)
    return (k+2)*2**(k-1)+(2**left+2**right-2)*2**k+(2**left-1)*(2**right-1)

def main():
    cases=0; maps_count=0; tested_pairs=0
    for n in range(1,11):
        maps=list(all_contractions(n))
        maps_count+=len(maps)
        assert len(maps)==(n+1)*2**(n-2) if n>=2 else len(maps)==1
        assert len(set(maps))==len(maps)
        actual_idemp={f for f in maps if all(f[f[i]-1]==f[i] for i in range(n))}
        expected_idemp={clamp(n,a,b) for a in range(1,n+1) for b in range(a,n+1)}
        assert actual_idemp==expected_idemp, (n,len(actual_idemp))
        for a in range(1,n+1):
            for b in range(a,n+1):
                e=clamp(n,a,b)
                count=sum(commute(f,e) for f in maps)
                tested_pairs+=len(maps)
                want=prediction(n,a,b)
                assert count==want, (n,a,b,count,want)
                cases+=1
        print(f'n={n}: |OCT|={len(maps)}; idempotents={len(expected_idemp)}; all centralizers passed')
    for n in range(2,101):
        idempotents=[(a,b) for a in range(1,n+1) for b in range(a,n+1)]
        largest=0.0
        for a,b in idempotents:
            k=b-a; left=a-1; right=n-b
            exponent=n-1-min(k,left,right)
            actual=log2(prediction(n,a,b))
            assert -2.000001 <= actual-exponent <= log2(4*(n+1))
            largest=max(largest,abs(actual-exponent))
        for t in range((n-1)//3+1):
            count=sum(min(a-1,b-a,n-b)>=t for a,b in idempotents)
            expected=comb(n+1-3*t,2)
            assert count==expected,(n,t,count,expected)
    print(f'ALL_CLAMP_CENTRALIZER_TESTS_PASSED cases={cases} maps={maps_count} commuting_pairs={tested_pairs}')
if __name__=='__main__': main()
