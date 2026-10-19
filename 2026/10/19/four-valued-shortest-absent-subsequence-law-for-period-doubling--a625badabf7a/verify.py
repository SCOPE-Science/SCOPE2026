"""Finite verification of the period-doubling shortest-absent-subsequence theorem.
Python 3 standard library. Finite checks do not replace the written proof.
"""
from itertools import product

def v2(n):
    assert n > 0
    return (n & -n).bit_length()-1

def pd(n):
    return ''.join(str(v2(j)%2) for j in range(1,n+1))

def formula(n):
    r=sum(v2(j)%2 for j in range(1,n+1))
    if n==2: return r,{0,1,2}
    if n%2 or (n%4==0 and v2(n)%2==0):return r,{r+1}
    ell=(1 if n%4==0 else 2 if v2(n-2)%2 else 0)
    return r,{r+1}|{r-j for j in range(ell+1)}

def observed(n,w):
    r=w.count('1')
    z=[0]*(n+1)
    for i in range(n-1,-1,-1):z[i]=z[i+1]+(w[i]=='0')
    pos=[i for i,x in enumerate(w) if x=='1']
    missing={r+1}
    for a in range(r+1):
        if z[pos[a-1]+1 if a else 0] < r+1-a:missing.add(a)
    return r,missing

def is_subseq(s,w):
    i=0
    for x in w:
        if i<len(s) and s[i]==x:i+=1
    return i==len(s)

def brute(n,w):
    r,missing=formula(n)
    for k in range(1,r+1):
        for bits in product('01',repeat=k):
            assert is_subseq(''.join(bits),w),(n,k,bits)
    for bits in product('01',repeat=r+1):
        s=''.join(bits)
        expected=s in {'1'*a+'0'*(r+1-a) for a in missing}
        assert (not is_subseq(s,w))==expected,(n,s)

def main():
    w='0'
    for depth in range(13):
        assert pd(len(w))==w
        for n in (range(1,len(w)+1) if len(w)<=128 else range(1,len(w)+1,71)):
            assert observed(n,w[:n])==formula(n),(depth,n)
            if n<=18:brute(n,w[:n])
        w=''.join('01' if x=='0' else '00' for x in w)
    print('PASS: independent morphic construction, valuation formula,')
    print('      full small-subsequence enumeration and suffix criterion.')

if __name__=='__main__':main()
