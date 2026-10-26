"""Finite checks for complete extensions of chain-structured argumentation.

Run: python checker.py . Requires only the Python standard library.
"""
from itertools import combinations_with_replacement
from math import comb
from random import Random

CHECKS=0

def fail_if(test, detail):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(detail)

def direct_semantics(rows, n, E):
    """Definitions with direct attacks and full subargument closures."""
    cfree=True
    for a in range(n):
        if not E>>a & 1: continue
        for b in range(n):
            if not E>>b & 1: continue
            if any(rows[x] & ((1<<(b+1))-1) for x in range(a+1)):
                cfree=False
    defended=0
    for a in range(n):
        okay=True
        for x in range(a+1):
            for b in range(n):
                if not (rows[b]>>x & 1): continue
                if not any((E>>c & 1) and (rows[c]&((1<<(b+1))-1)) for c in range(n)):
                    okay=False
        if okay: defended |= 1<<a
    closed = all(not(E>>a & 1) or ((E & ((1<<(a+1))-1)) == ((1<<(a+1))-1)) for a in range(n))
    adm=cfree and closed and (E & ~defended)==0
    complete=adm and defended==E
    stable=adm and all((E>>a & 1) or any((E>>c & 1) and (rows[c]&((1<<(a+1))-1)) for c in range(n)) for a in range(n))
    return complete,stable,defended,cfree

def predicted_semantics(rows, n):
    t=[next((j+1 for j in range(n) if rows[i]>>j&1),n+1) for i in range(n)]
    h=[n]
    for t_i in t:h.append(min(h[-1],t_i-1))
    complete=[k for k in range(n+1) if h[h[k]]==k and h[k]>=k]
    stable=[k for k in range(n+1) if h[k]==k]
    return h,complete,stable

def run_rows(rows):
    n=len(rows)
    h,co,st=predicted_semantics(rows,n)
    C=[];S=[]
    for E in range(1<<n):
        a,b,F,cf=direct_semantics(rows,n,E)
        if a:C.append(E)
        if b:S.append(E)
        if E & (E+1)==0: # all prefixes E=(1<<k)-1
            k=E.bit_count()
            fail_if(F == ((1<<h[h[k]])-1),(n,rows,E,'F'))
            fail_if(cf==(h[k]>=k),(n,rows,E,'CF'))
    fail_if(C==[(1<<k)-1 for k in co],(n,rows,'complete',C,co))
    fail_if(S==[(1<<k)-1 for k in st],(n,rows,'stable',S,st))
    fail_if(len(co)<=n//2+1,(n,rows,'maximum count'))
    fail_if(len(st)<=1,(n,rows,'unique stable'))
    fail_if(not st or max(co)==st[0],(n,rows,'preferred stable'))


def main():
    rng=Random(0x260112038)
    tested=0
    for n in range(1,5):
        max_rows = (1 << (n*n))
        for mask in range(max_rows):
            rows=tuple((mask>>(i*n))&((1<<n)-1) for i in range(n))
            run_rows(rows)
            tested+=1
    for n in range(5,9):
        for _ in range(150):
            rows=tuple(rng.getrandbits(n) for _ in range(n))
            run_rows(rows)
            tested+=1
    for n in range(1,9):
        hs=[];fixed=[]
        for vals in combinations_with_replacement(range(n+1),n):
            h=(n,)+tuple(reversed(vals))
            hs.append(h)
            spots=[k for k in range(1,n+1) if h[k]==k]
            fixed+=spots
            fail_if(len(spots)<=1,(n,h,'double stable'))
        fail_if(len(hs)==comb(2*n,n),(n,'profile census',len(hs)))
        for k in range(1,n+1):
            fail_if(fixed.count(k)==comb(n-1,k-1)*comb(n,k),(n,k,'stable at k'))
        fail_if(len(fixed)*2==len(hs),(n,'half stable'))
        rows=tuple(1<<(n-i-1) for i in range(n))
        h,complete,stable=predicted_semantics(rows,n)
        fail_if(complete==list(range(n//2+1)),(n,'sharpness',complete))
    print('ALL_CHECKS_OK',CHECKS,'direct_attack_structures',tested,'profile_n_le_8',sum(comb(2*n,n) for n in range(1,9)))

if __name__=='__main__': main()
