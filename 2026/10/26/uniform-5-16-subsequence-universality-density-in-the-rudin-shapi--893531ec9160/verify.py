#!/usr/bin/env python3
"""Reproducible verification of Rudin--Shapiro arch-transfer identities."""
from collections import Counter
from itertools import product

MORPHISM = {"a":"ab", "b":"ac", "c":"db", "d":"dc"}
BIT = {"a":0, "b":0, "c":1, "d":1}
STATES = (None,0,1)

def symbol_transform(bit):
    out={}
    for s in STATES:
        if s is None: out[s]=(0,bit)
        elif s==bit: out[s]=(0,s)
        else: out[s]=(1,None)
    return out

def compose(left,right):
    out={}
    for s in STATES:
        a,mid=left[s]
        b,end=right[mid]
        out[s]=(a+b,end)
    return out

def closed_formula(m,letter,pending):
    assert m>=4
    q=5*(1<<(m-4))
    even = m%2==0
    base=q-(int(even) if letter in 'ad' else int(not even))
    penalty=(int(pending==1) if letter in 'ab' else int(pending==0))
    end=(int(even) if letter in 'ac' else int(not even))
    return (base+penalty,end)

def get_rs(n):
    return (n & (n>>1)).bit_count()%2

def greedy(word,start=None):
    count=0;state=start
    for b in word:
        if state is None: state=b
        elif state!=b: count+=1;state=None
    return count,state

def direct_index(word):
    # Not using arch property: explicitly test existence of every binary target.
    def embeds(t):
        j=0
        for b in word:
            if b==t[j]:
                j+=1
                if j==len(t):return True
        return False
    for k in range(1,len(word)//2+2):
        if not all(embeds(t) for t in product((0,1),repeat=k)):
            return k-1
    raise AssertionError('Unreachable')

def dyadic_chunks(start,n):
    ans=[];pos=start; end=start+n
    while pos<end:
        j=(pos&-pos).bit_length()-1 if pos else (end-pos).bit_length()-1
        j=min(j,(end-pos).bit_length()-1)
        ans.append((pos,1<<j));pos+=1<<j
    return ans

def run():
    trans={x:symbol_transform(BIT[x]) for x in MORPHISM}
    for m in range(23):
        if m>=4:
            for x in MORPHISM:
                for s in STATES:
                    got=trans[x][s]
                    want=closed_formula(m,x,s)
                    assert got==want,('formula',m,x,s,got,want)
                    assert abs(got[0]-5*(1<<m)/16)<=1,('discrepancy',m,x,s)
        elif m<=3:
            for x in MORPHISM:
                for s in STATES:
                    got=trans[x][s]
                    assert abs(got[0]-5*(1<<m)/16)<=1
        trans={x:compose(trans[MORPHISM[x][0]],trans[MORPHISM[x][1]]) for x in MORPHISM}
    # Morphism agrees with the binary-digit definition, not just its own recurrence.
    w='a'
    for m in range(16):
        bits=tuple(BIT[c] for c in w)
        assert all(bit==get_rs(i) for i,bit in enumerate(bits))
        if m>=4:
            assert greedy(bits)[0]==5*(1<<(m-4))-int(m%2==0)
        w=''.join(MORPHISM[c] for c in w)
    bits=tuple(get_rs(i) for i in range(4096))
    for start in range(0,128,7):
        for n in range(1,15):
            factor=bits[start:start+n]
            assert greedy(factor)[0]==direct_index(factor)
    # Check every short aligned chunk and the claimed at-most-two-per-scale tiling.
    for start in range(0,210):
        for n in range(1,110):
            parts=dyadic_chunks(start,n)
            assert sum(L for _,L in parts)==n
            assert len(parts)<=2*(n.bit_length())
            assert max(Counter(L for _,L in parts).values())<=2
            assert all(i%L==0 for i,L in parts)
            value=greedy(bits[start:start+n])[0]
            assert abs(value-5*n/16)<=2*n.bit_length(),('factor',start,n,value)
    print('RS_UNIFORM_UNIVERSALITY_PASS transfers=23 dyadic=16 brute=19x14 factors=22890')

if __name__=='__main__':
    run()
