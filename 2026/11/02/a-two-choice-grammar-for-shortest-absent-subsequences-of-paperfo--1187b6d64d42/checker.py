#!/usr/bin/env python3
"""Standalone exact checks for dyadic paperfolding shortest absent subsequences.
No external libraries, downloads, files, or external verification services required.
"""
from itertools import product

D = {
    ('1','0'):(6,6,6,5,5,4,4,3,3,3,2,2,2,1,1,1,0),
    ('1','1'):(6,6,6,5,5,4,4,3,3,3,2,2,2,1,1,0,0),
    ('0','0'):(6,6,6,5,5,4,4,4,3,3,2,2,2,1,1,1,0),
    ('0','1'):(6,6,6,5,5,4,4,4,3,3,2,2,2,1,1,0,0),
}

def paper_prefix(n):
    def paper(j):
        odd = j // (j & -j)
        return '1' if odd % 4 == 1 else '0'
    return ''.join(paper(j) for j in range(1,n+1))

def word_from_bits(bits):
    return ''.join('1101100' + ('1' if j%2==0 else '0') +
                   '1100100' + bit for j,bit in enumerate(bits))

def suffix_ranks_and_next(w):
    n=len(w)
    nxt=[[n,n] for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        nxt[i]=nxt[i+1].copy();nxt[i][int(w[i])]=i
    rank=[0]*(n+1)
    for i in range(n-1,-1,-1):
        a,b=nxt[i]
        rank[i]=(1+rank[max(a,b)+1]) if max(a,b)<n else 0
    return rank,nxt

def rank_drop_paths(rank,nxt,pos,steps):
    n=len(rank)-1
    paths={('',pos)}
    for _ in range(steps):
        out=set()
        for u,i in paths:
            for b in '01':
                loc=nxt[i][int(b)]
                if loc<n and rank[loc+1]==rank[i]-1:
                    out.add((u+b,loc+1))
        paths=out
    return paths

def expected_words(m):
    choices=['00' + b + '011' if j%2==0 else '001' + b + '11'
             for j in range(m) for b in '01']
    out=['']
    for j in range(m):
        units=['00'+b+'011' if j%2==0 else '001'+b+'11' for b in '01']
        out=[x+y for x in out for y in units]
    return {x+b for x in out for b in '01'}

def missing_words(rank,nxt):
    n=len(rank)-1
    states=rank_drop_paths(rank,nxt,0,rank[0]);out=set()
    for s,i in states:
        for b in '01':
            if nxt[i][int(b)]==n:out.add(s+b)
    return out

def brute_is_subseq(x,w):
    j=0
    for a in w:
        if j<len(x) and x[j]==a:j+=1
    return j==len(x)

def verify():
    words=0
    for m in range(1,9):
        target=expected_words(m)
        for q in product('01',repeat=m-1):
            bits=''.join(q)+'1';w=word_from_bits(bits)
            rank,nxt=suffix_ranks_and_next(w)
            assert rank[0]==6*m,(m,bits,rank[0])
            for j,bit in enumerate(bits):
                e='1' if j%2==0 else '0'
                assert tuple(rank[16*j+s]-rank[16*(j+1)] for s in range(17))==D[(e,bit)]
                for off in (0,1):
                    ps=rank_drop_paths(rank,nxt,16*j+off,6)
                    want={('00'+b+'011' if e=='1' else '001'+b+'11',
                           16*(j+1)+(1 if bit=='0' else 0)) for b in '01'}
                    assert ps==want,(m,bits,j,off,ps,want)
            assert missing_words(rank,nxt)==target,(m,bits)
            words+=1
        print('all internal bit choices, m =',m,'checked')
    for k in range(4,9):
        w=paper_prefix(2**k)
        m=2**(k-4)
        bs=''.join(w[16*j+15] for j in range(m))
        assert bs[-1]=='1'
        assert w==word_from_bits(bs)
        rank,nxt=suffix_ranks_and_next(w)
        assert rank[0]==6*m
        assert missing_words(rank,nxt)==expected_words(m)
        print('paperfolding rank',k,'length',len(w),'SAS length',rank[0]+1,'SAS count',2**(m+1))
    for k in (4,5):
        w=paper_prefix(2**k)
        m=2**(k-4)
        target=expected_words(m)
        found={''.join(t) for t in product('01',repeat=6*m+1)
               if not brute_is_subseq(''.join(t),w)}
        assert found==target
        assert all(brute_is_subseq(''.join(t),w) for t in product('01',repeat=6*m))
        print('independent direct brute check k =',k,'passed')
    print('VERIFY_OK',words,'arbitrary-block words; all six-check stages passed')

if __name__=='__main__':verify()
