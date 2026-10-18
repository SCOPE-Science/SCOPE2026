#!/usr/bin/env python3
"""Verify maximal dissociation sets in rectangular rook graphs by two independent methods."""
from collections import Counter
from math import factorial

def species(m, n):
    f=factorial
    p=Counter()
    # star-only, at least one board side completely used
    for b in range(min(m,n//2)+1):
        for c in range(min((m-b)//2,n-2*b)+1):
            mr=m-b-2*c
            nc=n-2*b-c
            if mr<0 or nc<0 or (mr and nc): continue
            k=2*(b+c)
            if not k: continue
            cnt=f(m)*f(n)//(f(b)*f(c)*f(mr)*f(nc)*2**(b+c))
            p[k]+=cnt
    # isolates present, no unused vertices on either side
    for a in range(1,min(m,n)+1):
        for b in range(min(m-a,(n-a)//2)+1):
            for c in range(min((m-a-b)//2,n-a-2*b)+1):
                if a+b+2*c!=m or a+2*b+c!=n:continue
                cnt=f(m)*f(n)//(f(a)*f(b)*f(c)*2**(b+c))
                p[a+2*b+2*c]+=cnt
    return +p

def graph_direct(m,n):
    sz=m*n
    neighbors=[sum(1<<(r*n+c) for r in range(m) for c in range(n)
              if (r==i//n or c==i%n) and r*n+c !=i)
               for i in range(sz)]
    def valid(mask):
        bits=mask
        while bits:
            bit=bits & -bits; i=bit.bit_length()-1
            if (neighbors[i]&mask).bit_count()>1:return False
            bits-=bit
        return True
    poly=Counter()
    for mask in range(1<<sz):
        if not valid(mask):continue
        if any(valid(mask|(1<<j)) for j in range(sz) if not(mask>>j&1)):
            continue
        poly[mask.bit_count()]+=1
    return +poly

def run():
    total=0;tests=0
    for m in range(1,6):
        for n in range(m,9):
            if m*n>20:continue
            p=species(m,n); q=graph_direct(m,n)
            assert p==q, (m,n,p,q)
            total+=1<<(m*n);tests+=1
    print('MAXIMAL_EXHAUSTIVE_OK boards=%d inspected_subsets=%d' %(tests,total))
    grid=0
    for m in range(1,26):
        for n in range(m,26):
            p=species(m,n)
            assert p and all(k>=1 for k in p)
            if m==1:
                assert p==({1:1} if n==1 else {2:n*(n-1)//2})
            grid+=1
    print('SPECIES_BOUNDARY_OK parameter_pairs=%d' %grid)
    for m,n in [(1,1),(1,3),(2,2),(2,3),(3,3),(3,4),(4,4),(4,5),(5,5)]:
        p=species(m,n)
        print('POLY m=%d n=%d : %s' %(m,n,' '.join('%d:%d'%(k,p[k]) for k in sorted(p))))
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':run()
