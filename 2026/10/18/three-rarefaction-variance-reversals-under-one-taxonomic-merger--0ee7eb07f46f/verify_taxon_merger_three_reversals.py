"""Reproduce the sharp three-reversal census for taxonomic coarsening.
Python >=3.9, standard library only.
Run: python verify_taxon_merger_three_reversals.py [optional-output-csv]
"""
import csv
import sys
from collections import Counter,defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb

@lru_cache(None)
def partitions(n, lower=1):
    if n==0:return ((),)
    return tuple((a,)+tail for a in range(lower,n+1)
                 for tail in partitions(n-a,a))

def absent(N,a,m):
    return Fraction(comb(N-a,m),comb(N,m)) if 0<=m<=N-a else Fraction(0)

@lru_cache(None)
def moments_pairwise(a):
    N=sum(a)
    out=[]
    for m in range(N+1):
        q=[absent(N,v,m) for v in a]
        E=sum((1-z for z in q),Fraction(0))
        V=sum((z*(1-z) for z in q),Fraction(0))
        for i,j in combinations(range(len(a)),2):
            V+=2*(absent(N,a[i]+a[j],m)-q[i]*q[j])
        out.append((E,V))
    return tuple(out)

@lru_cache(None)
def moments_distribution(a):
    """Independent integer coefficient extraction for joint (sample size, richness)."""
    dist={(0,0):1}
    for count in a:
        nxt=defaultdict(int)
        for (m,k),ways in dist.items():
            for j in range(count+1):
                nxt[(m+j,k+(j>0))]+=ways*comb(count,j)
        dist=nxt
    N=sum(a)
    out=[]
    for m in range(N+1):
        den=comb(N,m)
        assert sum(z for (mm,k),z in dist.items() if mm==m)==den
        E=sum((Fraction(z*k,den) for (mm,k),z in dist.items() if mm==m),Fraction(0))
        E2=sum((Fraction(z*k*k,den) for (mm,k),z in dist.items() if mm==m),Fraction(0))
        out.append((E,E2-E*E))
    return tuple(out)

def merge(a,x,y):
    rest=list(a)
    rest.remove(x)
    rest.remove(y)
    return tuple(sorted((x+y,*rest)))

def delta(a,b):
    aa=moments_pairwise(a);bb=moments_pairwise(b)
    return tuple(bb[m][1]-aa[m][1] for m in range(2,sum(a)))

def signs(d):return ''.join('+' if q>0 else '-' if q<0 else '0' for q in d)

def strict_flips(d):
    return sum(u*v<0 for u,v in zip(d,d[1:]))

def census():
    rows=[]
    counts=[]
    hits=[]
    checked=set()
    for N in range(1,17):
        no=0
        for a in partitions(N):
            if a not in checked:
                assert moments_pairwise(a)==moments_distribution(a),a
                checked.add(a)
            pairs=sorted({tuple(sorted((a[i],a[j]))) for i,j in combinations(range(len(a)),2)})
            for x,y in pairs:
                b=merge(a,x,y)
                if b not in checked:
                    assert moments_pairwise(b)==moments_distribution(b),b
                    checked.add(b)
                d=delta(a,b)
                num=strict_flips(d)
                rows.append((N,','.join(map(str,a)),x,y,','.join(map(str,b)),signs(d),num))
                if num>=3:
                    no+=1;hits.append((N,a,(x,y),b,d))
        counts.append((N,len(partitions(N)),sum(r[0]==N for r in rows),no))
    assert hits and len(hits)==1,hits
    N,a,pair,b,d=hits[0]
    assert (N,a,pair,b)==(16,(1,1,1,1,1,1,1,1,2,6),(1,2),(1,1,1,1,1,1,1,3,6))
    assert signs(d)== '+++---+++++++-',signs(d)
    assert strict_flips(d)==3
    return rows,counts,hits

if __name__=='__main__':
    rows,counts,hits=census()
    if len(sys.argv)>1:
        with open(sys.argv[1],'w',encoding='utf8',newline='') as f:
            w=csv.writer(f,lineterminator='\n')
            w.writerow(['N','original_abundances','merged_abundance_x','merged_abundance_y','coarsened_abundances','signs_for_m_2_to_N_minus_1','strict_adjacent_sign_flips'])
            w.writerows(rows)
    print('N, partition count, merger types, count with >=3 strict adjacent reversals')
    for r in counts:print(*r,sep=',')
    N,a,pair,b,d=hits[0]
    print('witness',N,a,pair,b)
    print('m,variance difference')
    for m,v in enumerate(d,2):print(m,v,sep=',')
    print('All variance identities independently checked by integer generating-function coefficients.')
    print('PASS')
