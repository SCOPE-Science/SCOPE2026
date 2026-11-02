#!/usr/bin/env python3
"""Independent exhaustive checks for a cyclic Rule-18 fiber theorem.
This program uses only Python's standard library.
"""
from collections import Counter

def fibs(limit):
    f=[0,1]
    for i in range(2,limit+1):f.append(f[-1]+f[-2])
    return f

def formula(word):
    n=len(word)
    F=fibs(n+3)
    p=[i for i,b in enumerate(word) if b]
    if not p:return F[n-1]+F[n+1]+1 if n>=1 else None
    if len(p)%2:return 0
    r=len(p)//2
    score=0
    for parity in (0,1):
        ext=p+[p[0]+n,p[1]+n] if r>1 else p+[p[0]+n,p[1]+n]
        # Start at p[parity]; gather forward adjacent disjoint pairs.
        pairs=[(ext[parity+2*j],ext[parity+2*j+1]) for j in range(r)]
        product=1
        for j,(start,end) in enumerate(pairs):
            next_start=pairs[(j+1)%r][0]+(n if j==r-1 else 0)
            t=next_start-end-1
            if t<1:
                product=0;break
            product*=F[t]
        score+=product
    return score

def update(bits,n):
    # Standard Wolfram Rule18: next bit =1 iff old triple is 001 or 100.
    mask=(1<<n)-1
    left=((bits<<1)|(bits>>(n-1))) &mask
    right=(bits>>1)|((bits&1)<<(n-1))
    return ((~bits)&(left^right))&mask

def trace_count(word):
    mats=[[[0]*4 for _ in range(4)] for _ in range(2)]
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                i=(a<<1)|b;j=(b<<1)|c
                q=1 if (b==0 and a!=c) else 0
                mats[q][i][j]=1
    m=[[int(i==j) for j in range(4)] for i in range(4)]
    for bit in word:
        t=mats[bit];m=[[sum(m[i][k]*t[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    return sum(m[i][i] for i in range(4))

def main():
    tested=0
    for n in range(1,17):
        counts=Counter(update(x,n) for x in range(1<<n))
        F=fibs(n+3)
        assert counts[0]==F[n-1]+F[n+1]+1, (n,counts[0])
        positive_max=0; argmax=[]
        for w in range(1<<n):
            word=tuple((w>>i)&1 for i in range(n))
            direct=counts[w]
            formula_count=formula(word)
            assert direct==formula_count,(n,w,direct,formula_count)
            if n<=11:
                matrix_count=trace_count(word)
                assert matrix_count==direct,(n,w,matrix_count,direct)
            if w:
                if direct>positive_max:positive_max=direct;argmax=[w]
                elif direct==positive_max:argmax.append(w)
            tested+=1
        if n>=7:
            assert positive_max==F[n-2],(n,positive_max,F[n-2])
            assert len(argmax)==n,(n,len(argmax))
            for y in argmax:
                assert y.bit_count()==2
                assert any((y & (1<<i)) and (y & (1<<((i+1)%n))) for i in range(n))
        print('n=',n,'zero=',counts[0],'positive_max=',positive_max,'maximizers=',len(argmax))
    print('VERIFY_OK',tested,'outputs checked; direct enumeration + formula; transfer traces for n<=11')
if __name__=='__main__':main()
