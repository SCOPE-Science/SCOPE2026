#!/usr/bin/env python3
"""Independent finite checks for Cantor-word threshold-density factor theorem."""
from math import log

def encode(index, base):
    out=0; power=1
    while index:
        if index&1: out+=(base-1)*power
        index>>=1;power*=base
    return out

def digit_word(base, length):
    output=bytearray(length)
    for i in range(length):
        v=i;good=1
        while v:
            if v%base not in (0,base-1):good=0;break
            v//=base
        output[i]=good
    return bytes(output)

def expected(base,k):
    j=k-1;h=j.bit_length();L=encode(j,base)+1
    patterns=set()
    for a in range(1<<h):
        if a&j:continue
        offsets=tuple(encode(a+r,base)-encode(a,base) for r in range(k))
        assert offsets[0]==0 and offsets[-1]==L-1
        assert all(0<=v<L for v in offsets)
        patterns.add(offsets)
    expected_n=1<<(h-j.bit_count())
    assert len(patterns)==expected_n,('formula collision',base,k)
    return L,patterns,expected_n

def scan(base,k,L,word):
    # direct exhaustive factor scan, no Cantor-index use
    n=len(word)
    found={}
    window_count=sum(word[:L]);max_count=window_count
    for i in range(n-L+1):
        if i:
            window_count+=word[i+L-1]-word[i-1]
        if window_count>max_count:max_count=window_count
        if window_count==k:
            factor=word[i:i+L]
            offsets=tuple(j for j,c in enumerate(factor) if c)
            found.setdefault(offsets,set()).add(i)
    return max_count,found

def main():
    cases=0;factor_cases=0;offset_checks=0
    for base,power,max_k in ((3,8,32),(4,7,24),(5,6,20),(6,5,14),(7,5,12)):
        word=digit_word(base,base**power)
        for k in range(1,max_k+1):
            L,patterns,N=expected(base,k)
            if L>len(word)//3:break
            max_count,found=scan(base,k,L,word)
            assert max_count==k,(base,k,L,max_count)
            assert set(found)==patterns,(base,k,L,len(found),len(patterns),set(found)^patterns)
            for pat,starts in found.items():
                for start in starts:
                    assert word[start]==1 and tuple(i for i,x in enumerate(word[start:start+L]) if x)==pat
                    offset_rank=None
                    # independently rank source one by prefix sum; small sample checks
                    if start<200: offset_rank=sum(word[:start])
                    if offset_rank is not None:
                        assert start==encode(offset_rank,base)
                        assert (offset_rank&(k-1))==0
                        offset_checks+=1
            # complete minimal-length check
            if L>1:
                mx0,_=scan(base,k,L-1,word)
                assert mx0==k-1,(base,k,L,mx0)
            cases+=1;factor_cases+=len(found)
        print('base',base,'cases_done',cases,'scan_length',len(word))
    print('VERIFY_OK cases',cases,'distinct_pattern_cases',factor_cases,'start_checks',offset_checks)
if __name__=='__main__':main()
