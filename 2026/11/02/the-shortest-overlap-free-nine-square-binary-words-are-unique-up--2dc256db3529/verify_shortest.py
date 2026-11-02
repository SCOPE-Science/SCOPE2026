#!/usr/bin/env python3
"""Independent complete prefix-tree checks for shortest overlap-free nine-square words.
Only the binary word combinatorics and reproducibility, no external dependencies.
"""
from functools import lru_cache

MAXLEN=48

def suffix_overlap_binary(word):
    n=len(word)
    for period in range(1,(n-1)//2+1):
        # length 2*period+1 and period period => a x a x a
        tail=word[-(2*period+1):]
        if tail[:period+1]==tail[period:]:
            return True
    return False

def square_factor(word, a, b):
    width=b-a
    return width>0 and width%2==0 and word[a:a+width//2]==word[a+width//2:b]

def best_count_for_word(word):
    best=[0]+[-999]*len(word)
    for end in range(1,len(word)+1):
        for start in range(0,end-1):
            if square_factor(word,start,end):
                best[end]=max(best[end],best[start]+1)
    return best[-1]

def all_nine_factorizations(word):
    @lru_cache(None)
    def visit(start,remaining):
        if remaining==0:
            return ((),) if start==len(word) else ()
        out=[]
        for end in range(start+2,len(word)+1,2):
            if square_factor(word,start,end):
                for rest in visit(end,remaining-1):
                    out.append(((start,end),)+rest)
        return tuple(out)
    return visit(0,9)

def exhaustive():
    # All overlap-free strings of length n are exactly the surviving
    # one-letter extensions of all overlap-free strings of length n-1.
    layer={'':0}
    counts=[]; optimizer_words=[]
    for n in range(1,MAXLEN+1):
        nxt={}
        for word in layer:
            for symbol in ('0','1'):
                candidate=word+symbol
                if not suffix_overlap_binary(candidate):
                    nxt[candidate]=best_count_for_word(candidate)
        if n<48:assert all(v<9 for v in nxt.values()),f'shorter extremizer {n}'
        if n==48:optimizer_words=sorted(w for w,v in nxt.items() if v>=9)
        counts.append((n,len(nxt),max(nxt.values(),default=0),sum(v>=9 for v in nxt.values())))
        layer=nxt
    a='001001101001011010011001011001101001011010011011'
    b=''.join('1' if x=='0' else '0' for x in a)
    assert optimizer_words==sorted([a,b]), optimizer_words
    fac=[all_nine_factorizations(s) for s in optimizer_words]
    assert [len(x) for x in fac]==[1,1]
    for w,cuts in zip(optimizer_words,fac):
        assert len(w)==48 and not any(suffix_overlap_binary(w[:j]) for j in range(1,49))
        assert len(cuts[0])==9
        assert [b-a for a,b in cuts[0]]==[6,4,4,4,12,4,4,4,6]
    assert counts[23][1]==164 and counts[41][2]==8
    assert counts[47]==(48,416,9,2),counts[47]
    return counts,optimizer_words

if __name__=='__main__':
    counts,words=exhaustive()
    for n,count,max_num,nine in counts:
        print(f'{n:2d} overlapfree={count:3d} max_squares={max_num:2d} nine={nine}')
    print('optimizer words:',*words,sep='\n')
    print('NINE_SQUARES_MIN_LENGTH_AND_UNIQUENESS_OK')
