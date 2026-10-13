#!/usr/bin/env python3
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json

MU={'0':'01','1':'21','2':'03','3':'23'}

def morph(w): return ''.join(MU[c] for c in w)
def iterate(k):
    w='0'
    for _ in range(k): w=morph(w)
    return w

def code(w): return ''.join(str(int(c)//2) for c in w)
def factors(w,L): return {w[i:i+L] for i in range(len(w)-L+1)}

def is_rep(w):
    n=len(w)
    return any(all(w[i]==w[i+p] for i in range(n-p)) for p in range(1,n//2+1))

def factorizations(w):
    n=len(w)
    @lru_cache(None)
    def rec(i):
        if i==n: return ((),)
        out=[]
        for j in range(i+1,n+1):
            if is_rep(w[i:j]):
                for tail in rec(j): out.append((j-i,)+tail)
        return tuple(out)
    return rec(0)

# Engine A: exact bounded factor language from the 4-letter uniform morphism.
# A length-L factor of morph(z) is determined by a source factor of length at
# most ceil((L+1)/2), hence at most 23 for L<=45. Equality of all factor sets
# through length 45 at two consecutive levels makes stabilization inductive.
u9,u10=iterate(9),iterate(10)
for L in range(1,46):
    assert factors(u9,L)==factors(u10,L),(L,'not stabilized')
rp=code(u10)
F={L:factors(rp,L) for L in range(1,46)}

records=[]
for L in range(1,46):
    for w in sorted(F[L]):
        fac=factorizations(w)
        if fac:
            records.append({'length':L,'word':w,'factorizations':[list(x) for x in fac]})

profile=Counter(len(x['factorizations']) for x in records)
amb=[x for x in records if len(x['factorizations'])>1]
uniq=[x for x in records if len(x['factorizations'])==1]
assert len(records)==232
assert len(uniq)==112 and len(amb)==120
assert dict(sorted(profile.items()))=={1:112,2:94,3:12,4:2,5:10,6:2}
assert min(x['length'] for x in amb)==9
assert max(x['length'] for x in uniq)==30
assert max(len(x['factorizations']) for x in records)==6
assert len([x for x in records if len(x['factorizations'])==6])==2

# Engine B: independent bit generation from the odd-part characterization.
def odd_part(n):
    while n%2==0: n//=2
    return n

def paper_bit(n):
    # one-based regular paperfolding convention matching the source coding
    return '0' if odd_part(n)%4==1 else '1'

direct=''.join(paper_bit(n) for n in range(1,1+65536))
for L in range(1,46):
    assert factors(direct,L)==F[L],(L,'direct language mismatch')

# Independently recompute every catalogued factorization and compare exact bytes.
cat=json.loads((Path(__file__).resolve().parent/'catalog.json').read_text(encoding='utf-8'))
assert cat['records']==records
assert cat['summary']['factorizable_factors']==232
assert cat['summary']['unique_factorization']==112
assert cat['summary']['nonunique_factorization']==120

cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text(encoding='utf-8'))
assert cert['factorization_count_distribution']=={'1':112,'2':94,'3':12,'4':2,'5':10,'6':2}
assert cert['published_global_length_cutoff']==45

print('VERIFY_OK exact_factor_language_L<=45=1 factorizable=232 unique=112 ambiguous=120 '
      'multiplicities=1:112,2:94,3:12,4:2,5:10,6:2 shortest_ambiguous=9 '
      'longest_unique=30 max_factorizations=6 direct_oddpart_prefix=65536')
