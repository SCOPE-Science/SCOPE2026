#!/usr/bin/env python3
"""Independent codeword-expansion and pair-coalescence enumeration."""
import json
from math import gcd
from collections import deque

def all_codes_at_nine():
    current={('0','1')}
    for n in range(2,10):
        yield n,current
        if n==9:break
        next_codes=set()
        for code in current:
            for removed in code:
                next_codes.add(tuple(sorted((set(code)-{removed})|{removed+'0',removed+'1'})))
        current=next_codes

def transitions(code):
    proper={''}
    for word in code:
        for i in range(1,len(word)):proper.add(word[:i])
    states=sorted(proper,key=lambda w:(len(w),w))
    idx={s:i for i,s in enumerate(states)}
    rows=tuple(tuple(idx['' if s+b in code else s+b] for s in states) for b in '01')
    return states,rows

def has_reset_by_pairs(code):
    states,rows=transitions(set(code))
    n=len(states)
    pairs=[(a,b) for a in range(n) for b in range(a+1,n)]
    mergers={(a,b) for (a,b) in pairs if any(row[a]==row[b] for row in rows)}
    while True:
        enlarged=set(mergers)
        for a,b in pairs:
            if (a,b) in enlarged:continue
            for row in rows:
                i,j=sorted((row[a],row[b]))
                if i==j or (i,j) in mergers:
                    enlarged.add((a,b));break
        if len(enlarged)==len(mergers):break
        mergers=enlarged
    if len(mergers)==len(pairs):return True,None
    bad=min(set(pairs)-mergers)
    reach={bad};todo=[bad]
    for pair in todo:
        for row in rows:
            i,j=sorted((row[pair[0]],row[pair[1]]))
            assert i!=j
            if (i,j) not in reach:
                reach.add((i,j));todo.append((i,j))
    certificate={'start':[states[z] for z in bad], 'closed_pairs':sorted([[states[a],states[b]] for a,b in reach])}
    return False,certificate

def main():
    counts=[];exceptions=[];certificates={}
    for n,codes in all_codes_at_nine():
        bad=0;bad_coprime=0
        for code in codes:
            good,cert=has_reset_by_pairs(code)
            if not good:
                bad+=1
                g=0
                for word in code:g=gcd(g,len(word))
                if g==1:
                    bad_coprime+=1
                    exceptions.append(list(code))
                    certificates[' '.join(code)]=cert
        counts.append({'size':n,'total':len(codes),'nonsynchronizing':bad,'nonsynchronizing_coprime':bad_coprime})
    print(json.dumps({'counts':counts,'nine_word_exceptions':sorted(exceptions),'certificates':certificates},indent=2))
if __name__=='__main__':main()
