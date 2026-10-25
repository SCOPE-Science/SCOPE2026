"""Verify the 01-pair enumerator for near-shortest universal binary words.
Standard-library Python 3, no external data.
"""
from itertools import combinations, product
from math import comb

def c01(w):
    z=0;c=0
    for x in w:
        if x=='0':z+=1
        else:c+=z
    return c

def greedy_index(w):
    seen=set();k=0
    for c in w:
        seen.add(c)
        if len(seen)==2:
            k+=1;seen=set()
    return k

def has_subseq(w,p):
    j=0
    for c in w:
        if c==p[j]:
            j+=1
            if j==len(p):return True
    return False

def expected(k):
    baseline=comb(k,2)
    coeff=[0]*(2*k+1)
    for i in range(k):
        for j in range(k+2):
            coeff[i+j]+=comb(k-1,i)
    return {baseline+j:c for j,c in enumerate(coeff)}

def main():
    for k in range(1,10):
        n=2*k+1; counts={}
        for ones in combinations(range(n),k):
            w=['0']*n
            for j in ones:w[j]='1'
            w=''.join(w)
            good=greedy_index(w)>=k
            if k<=5:
                direct=all(has_subseq(w,p) for p in map(''.join,product('01',repeat=k)))
                assert direct==good,(k,w)
            if good:
                d=c01(w);counts[d]=counts.get(d,0)+1
        assert counts==expected(k),(k,counts,expected(k))
        assert sum(counts.values())==(k+2)*2**(k-1)
    print('VERIFY_OK: k=1..9 full fixed-composition enumeration; k<=5 direct all-pattern tests; q-polynomials and totals')
if __name__=='__main__':main()
