"""Exact integer verification of finite paperfolding string-attractor certificates.

Usage: python verify.py. Requires only Python >=3.9 and pf_cert.json.
"""
import json
from pathlib import Path


def paperfolding_prefix(n):
    letters=[]
    for i in range(1,n+1):
        j=i
        while j%2==0:
            j//=2
        letters.append('0' if j%4==1 else '1')
    return ''.join(letters)


def verify_upper(word, positions):
    n=len(word)
    assert positions == sorted(set(positions))
    assert positions and all(1<=p<=n for p in positions)
    # Distinct substrings, from all possible starting coordinates.
    all_factors=set()
    hit_factors=set()
    for start in range(n):
        for end in range(start+1,n+1):
            factor=word[start:end]
            all_factors.add(factor)
            if any(start < p <= end for p in positions):
                hit_factors.add(factor)
    assert all_factors == hit_factors, (n, len(all_factors-hit_factors))
    return len(all_factors)


def verify_lower(word, rows, denominator):
    n=len(word)
    loads=[0]*n
    total=0
    for row in rows:
        start=row['start']-1
        length=row['length']
        units=row['weight_units']
        assert 0<=start<n and 1<=length<=n-start and isinstance(units,int) and units>0
        factor=word[start:start+length]
        covered=0
        at=word.find(factor)
        assert at>=0
        while at!=-1:
            covered |= ((1<<length)-1)<<at
            at=word.find(factor,at+1)
        assert covered
        total+=units
        for j in range(n):
            if (covered>>j)&1:
                loads[j]+=units
    assert max(loads)<=denominator, (n,max(loads),denominator)
    return total,max(loads)


def main():
    cert=json.loads(Path(__file__).with_name('pf_cert.json').read_text('utf-8'))
    assert set(cert)=={'denominator','cases'}
    denom=cert['denominator']
    assert denom==16
    expected={128:(5,80),256:(6,92),512:(6,96),1024:(7,102)}
    assert len(cert['cases'])==4
    for case in cert['cases']:
        n=case['n']
        assert n in expected
        count=len(case['positions_1based'])
        factor_count=verify_upper(paperfolding_prefix(n),case['positions_1based'])
        lb,max_load=verify_lower(paperfolding_prefix(n),case['lower_factors'],denom)
        assert lb==case['lower_bound_numerator']
        assert (count,lb)==expected[n],(n,count,lb)
        assert denom*(count-1) < lb <= denom*count
        print(f'n={n} factors={factor_count} optimum={count} lower={lb}/{denom} maxload={max_load}/{denom}')
    print('PAPERFOLDING_ATTRACTORS_VERIFY_OK')


if __name__=='__main__':main()
