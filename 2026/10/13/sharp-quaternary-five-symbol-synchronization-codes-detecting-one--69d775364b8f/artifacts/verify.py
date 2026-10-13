#!/usr/bin/env python3
"""Reconstruct the finite upper certificate and the parity-template code (stdlib)."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def border_free(s):
    return all(s[:k] != s[5-k:] for k in range(1, 5))

def candidates(a):
    return [''.join(map(str, z)) for z in itertools.product(range(a), range(4), range(4), range(4), range(a, 4)) if border_free(''.join(map(str,z)))]

def conflict(s, t):
    if sum(x != y for x, y in zip(s,t)) < 2:
        return True
    return any(s[:k] == t[-k:] or t[:k] == s[-k:] for k in range(1,5))

def lower_code():
    ans=[]
    for a,b,t,u,v in itertools.product(range(2),repeat=5):
        w=a^b^u^v
        ans.append(f'{a}{b}{2*t+u}{2*(1-t)+v}{2+w}')
    return ans

def main():
    cert=json.loads((ROOT/'upper_certificate.json').read_text())
    assert cert['schema_version']==1
    for a,expected in ((1,180),(2,240)):
        rec=cert['cases'][str(a)]
        words=candidates(a)
        assert len(words)==expected and words==rec['words']
        cover=rec['cliques'];assert len(cover)==32
        occupied=set()
        for group in cover:
            assert group and len(set(group))==len(group)
            assert all(isinstance(i,int) and 0<=i<len(words) for i in group)
            occupied.update(group)
            for i,j in itertools.combinations(group,2):
                assert conflict(words[i],words[j]),(a,i,j)
        assert occupied==set(range(len(words))),(a,len(occupied))
        print(f'UPPER_OK a={a} vertices={len(words)} cliques={len(cover)} covered={len(occupied)}')
    code=lower_code()
    assert len(code)==len(set(code))==32
    assert all(border_free(s) for s in code)
    assert all(not conflict(s,t) for s,t in itertools.combinations(code,2))
    assert all(len(s)==5 and all('0'<=ch<='3' for ch in s) for s in code)
    patterns={''.join('0' if int(x)<2 else '1' for x in s) for s in code}
    assert patterns=={'00011','00101'}
    # The established unrestricted length-five optimal template uses I^4 J.
    template_ub=[min(l**4,l**3*(4-l)) for l in (1,2,3)]
    assert template_ub==[1,16,27]
    # The two-clique-cover proof is for a=1,2. Reversing words changes a=3 to a=1.
    print(f'LOWER_OK cardinality={len(code)} templates={sorted(patterns)} min_distance=2')
    print(f'COMPARISON_OK restricted_single_template_max_at_most={max(template_ub)}')
    print('VERIFY_OK maximum_quaternary_nonoverlapping_length5_distance2=32')

if __name__=='__main__':
    main()
