#!/usr/bin/env python3
"""Self-contained finite certificates for two-step tortoise fibers of Thue--Morse factors."""
from collections import defaultdict

def mu(w):
    return ''.join('01' if b == '0' else '10' for b in w)

def tortoise(w):
    j = w.find('1')
    return w if j < 0 else w[:j] + w[j+1:] + '1'

def image2(w):
    return tortoise(tortoise(w))

def complete_factors(n):
    m = (n-1).bit_length()
    out = set()
    for ab in ('00','01','10','11'):
        w = ab
        for _ in range(m):
            w = mu(w)
        out.update(w[i:i+n] for i in range(len(w)-n+1))
    return out

def direct_prefix_factors(n, length=16384):
    w='0'
    while len(w)<length: w=mu(w)
    return {w[i:i+n] for i in range(len(w)-n+1)}

expected=(1,2,3,6,6,6,5,3,3,2)
for n in range(1,11):
    fs=complete_factors(n)
    assert fs==direct_prefix_factors(n), ('incomplete set',n)
    groups=defaultdict(list)
    for w in fs:groups[image2(w)].append(w)
    maxi=max(map(len,groups.values()))
    assert maxi==expected[n-1], (n,maxi)
    print('n',n,'factors',len(fs),'images',len(groups),'max_fiber',maxi)

fs10=complete_factors(10)
assert min(w.count('1') for w in fs10)==4
assert all(w.count('1')>=3 for w in fs10)
for w in fs10:
    a,b,c=[-1,-1,-1]
    ones=[i for i,ch in enumerate(w) if ch=='1']
    a=ones[0]
    b=ones[1]-ones[0]-1
    c=ones[2]-ones[1]-1
    v=w[ones[2]+1:]
    assert image2(w)=='0'*(a+b+c)+'1'+v+'11'
print('length_10_minimum_ones',min(w.count('1') for w in fs10))
for n in (11,12,16,32,64,128):
    groups=defaultdict(list)
    for w in complete_factors(n): groups[image2(w)].append(w)
    assert max(map(len,groups.values()))==2
print('supplemental_long_checks', (11,12,16,32,64,128))
print('VERIFY_OK')
