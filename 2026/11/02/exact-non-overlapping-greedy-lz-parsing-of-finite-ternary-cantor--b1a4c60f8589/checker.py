#!/usr/bin/env python3
"""Direct finite validation of the non-overlapping greedy Cantor-word parse."""

def parse(text):
    i=0
    out=[]
    while i<len(text):
        best_len=0
        best_src=None
        for s in range(i):
            t=0
            while s+t<i and i+t<len(text) and text[s+t]==text[i+t]:
                t+=1
            if t>best_len:
                best_len=t
                best_src=s
        length=max(1,best_len)
        if best_src is not None and best_len:
            assert best_src+length<=i
            assert text[best_src:best_src+length]==text[i:i+length]
        out.append((i,length))
        i+=length
    return out

def expected(k):
    if k==0:return [(0,1)]
    if k==1:return [(0,1),(1,1),(2,1)]
    pairs=[(0,1),(1,1),(2,2),(4,1),(5,3)]
    for j in range(1,k-1):
        q=3**(j-1)
        pairs.extend([(8*q,4*q),(12*q,3*q),(15*q,9*q)])
    q=3**(k-2)
    pairs.append((8*q,q))
    return pairs

def main():
    w='1'
    for k in range(8):
        got=parse(w)
        wanted=expected(k)
        assert got==wanted, (k,got,wanted)
        assert len(got)==(1 if k==0 else 3*k)
        if k>=3:
            for j in range(1,k-1):
                q=3**(j-1)
                for target,source,size in [(8*q,2*q,4*q),(12*q,9*q,3*q),(15*q,3*q,9*q)]:
                    assert source+size<=target
                    assert w[source:source+size]==w[target:target+size]
        print('level',k,'length',len(w),'phrases',len(got),'PASS')
        w=w+'0'*len(w)+w
if __name__=='__main__':main()
