"""Self-contained arithmetic verification of the odd-color three-square covering theorem.
Run: python3 verify.py (in the directory containing COVER.tsv and SHARPNESS.tsv).
Only Python's standard library is used.
"""
from pathlib import Path
import csv
from math import comb

ROOT=Path(__file__).resolve().parent
BOUND=103
DEPTH=15


def v2(x):
    assert x>0
    return (x & -x).bit_length()-1


def coefficients_by_product(m, nmax, modulus):
    # Directly multiply the truncated factors (1-x^(2^j))^(-m).
    poly=[1]+[0]*nmax
    part=1
    while part<=nmax:
        coeff=[comb(m+k-1,k)%modulus for k in range(nmax//part+1)]
        nxt=[0]*(nmax+1)
        for i,x in enumerate(poly):
            if not x: continue
            for k in range((nmax-i)//part+1):
                nxt[i+part*k]=(nxt[i+part*k]+x*coeff[k])%modulus
        poly=nxt
        part*=2
    return poly


def coefficients_by_derivative(m,nmax):
    # x B_m'(x)/B_m(x) = m*sum_{k>=1}(2^(v2(k)+1)-1)x^k.
    b=[1]
    for n in range(1,nmax+1):
        t=m*sum((2*(k & -k)-1)*b[n-k] for k in range(1,n+1))
        assert t%n==0
        b.append(t//n)
    return b

with (ROOT/'COVER.tsv').open(encoding='utf-8',newline='') as f:
    rows=[tuple(map(int,(r['residue'],r['modulus_bits'],r['index'],r['valuation'])))
          for r in csv.DictReader(f,delimiter='\t')]
assert len(rows)==156
assert len(set(rows))==156
covered=bytearray(1<<DEPTH)
maxindex=max(n for _,_,n,_ in rows)
assert maxindex==BOUND
for a,L,n,v in rows:
    assert 1<=L<=DEPTH and 1<=a<(1<<L) and a%2==1
    assert 1<=n<=BOUND and v%2==0
    assert L>=v+3+(n.bit_length()-1)
    mod=1<<(v+3)
    b=coefficients_by_product(a,n,mod)
    assert b[n] == 7*(1<<v) % mod, (a,L,n,v,b[n])
    for m in range(a,1<<DEPTH,1<<L):
        assert m%2==1 and covered[m]==0,(m,a,L)
        covered[m]=1
assert all(covered[m]==1 for m in range(1,1<<DEPTH,2))
assert all(covered[m]==0 for m in range(0,1<<DEPTH,2))
assert sum(1<<(DEPTH-L) for _,L,_,_ in rows)==1<<(DEPTH-1)

b=coefficients_by_derivative(613,BOUND)
precision=1+max(v2(x) for x in b)+3
bp=coefficients_by_product(613,BOUND,1<<precision)
assert all(b[i]%(1<<precision)==bp[i] for i in range(BOUND+1))
with (ROOT/'SHARPNESS.tsv').open(encoding='utf-8',newline='') as f:
    witness=[tuple(map(int,(r['index'],r['valuation'],r['odd_part_mod8'])))
             for r in csv.DictReader(f,delimiter='\t')]
assert len(witness)==BOUND+1
for n,v,odd in witness:
    assert (v,odd)==(v2(b[n]),(b[n]>>v2(b[n]))%8)
    if n<BOUND: assert v%2==1 or odd!=7
assert witness[-1]==(103,6,7)
print('VERIFY_OK leaves=156 covered_odd_classes=16384 maximum_index=103 maximum_depth=15 sharp_color=613 sharp_index=103 crosscheck=product_vs_derivative')
