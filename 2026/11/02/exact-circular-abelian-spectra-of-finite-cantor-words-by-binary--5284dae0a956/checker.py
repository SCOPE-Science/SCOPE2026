#!/usr/bin/env python3
"""Independent finite-window test for the stated Cantor circular Abelian spectrum.
Uses only Python standard library; no network or external files.
"""
from itertools import accumulate

def cantor_index(s):
    out=0
    place=1
    while s:
        if s & 1:
            out += 2*place
        place *= 3
        s >>= 1
    return out

def predicted_spans(n):
    t=1<<n
    d=[None,1]
    for m in range(2,t+1):
        s=m-2
        if s == 0:
            reduction=0
        else:
            h=s.bit_length()-1
            r=((s+1) & -(s+1)).bit_length()-1
            reduction=3**h-3**r if r <= h else 0
        d.append(2+cantor_index(s)-reduction)
    return d

def word(n):
    w='1'
    for _ in range(n):
        w=w+('0'*len(w))+w
    return w

def brute_one_spans(w):
    positions=[i for i,x in enumerate(w) if x=='1']
    n=len(w); t=len(positions)
    pp=positions+[i+n for i in positions]
    return [None]+[min(pp[i+m-1]-pp[i]+1 for i in range(t)) for m in range(1,t+1)]

def brute_length_spectrum(w):
    n=len(w); t=w.count('1')
    a=[int(z) for z in w]
    sums=[]
    for length in range(1,n+1):
        count=sum(a[:length])
        lo=hi=count
        for i in range(1,n):
            count += a[(i+length-1)%n]-a[i-1]
            lo=min(lo,count)
            hi=max(hi,count)
        sums.append(hi-lo+1)
    return sums

def predicted_length_spectrum(n,d):
    length=3**n
    t=1<<n
    def M(k):
        return sum(v<=k for v in d[1:])
    return [M(l)+M(length-l)-t+1 for l in range(1,length+1)]

def main():
    for n in range(1,8):
        w=word(n)
        spans=predicted_spans(n)
        observed_spans=brute_one_spans(w)
        assert observed_spans==spans, ('spans',n,observed_spans,spans)
        observed=brute_length_spectrum(w)
        predicted=predicted_length_spectrum(n,spans)
        assert observed==predicted, ('spectrum',n,observed,predicted)
        total=3**n+2*(6**n-1)//5
        assert sum(observed)==total, ('total',n,sum(observed),total)
        assert sum(spans[1:]) == ((1<<n)*(3**n+1)//2-(6**n-1)//5)
        print('rank',n,'length',len(w),'ones',w.count('1'),'spectrum_total',sum(observed),'status=PASS')
    print('ALL CHECKS PASSED')
if __name__=='__main__':
    main()
