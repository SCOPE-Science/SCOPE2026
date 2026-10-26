#!/usr/bin/env python3
"""Standalone exact enumerator for cyclic order-five de Bruijn LZ78 phrase profiles."""
from collections import Counter
from pathlib import Path
import sys

ORDER=5
LENGTH=1<<ORDER


def binary_cycles_switch():
    """Enumerate the local binary entrance/exit switches at 16 four-bit nodes."""
    mask=(1<<(ORDER-1))-1
    for f in range(1<<(LENGTH//2)):
        state=0
        bits=[]
        visited=0
        for _ in range(LENGTH):
            if visited & (1<<state):
                break
            visited |= (1<<state)
            first=state>>(ORDER-1)
            bits.append(str(first))
            suffix=state&mask
            state=(suffix<<1)|(first^((f>>suffix)&1))
        if state==0 and visited==(1<<LENGTH)-1:
            yield ''.join(bits)


def binary_cycles_euler():
    """Independent backtracking over de Bruijn graph edges."""
    edges=[0]
    used=1
    def walk(v,used):
        if len(edges)==LENGTH:
            if v==0:
                yield ''.join(str(e>>(ORDER-1)) for e in edges)
            return
        for bit in (0,1):
            edge=(v<<1)|bit
            if not (used>>edge)&1:
                edges.append(edge)
                yield from walk(edge&15,used|(1<<edge))
                edges.pop()
    yield from walk(0,used)


def parse_set(word):
    """Shortest new phrase rule, with one final dictionary-residual phrase."""
    dictionary=set()
    i=0
    phrases=[]
    while i<len(word):
        stop=i+1
        while stop<=len(word) and word[i:stop] in dictionary:
            stop+=1
        phrase=word[i:min(stop,len(word))]
        if not phrase:
            raise AssertionError('empty phrase')
        phrases.append(phrase)
        dictionary.add(phrase)
        i+=len(phrase)
    assert ''.join(phrases)==word
    return tuple(phrases)


def parse_trie(word):
    """Independent explicit prefix tree, treating exhausted input as one final phrase."""
    root={}
    pos=0
    pieces=[]
    while pos<len(word):
        node=root
        j=pos
        while j<len(word) and word[j] in node:
            node=node[word[j]]
            j+=1
        if j<len(word):
            phrase=word[pos:j+1]
            node[word[j]]={}
            pos=j+1
        else:
            phrase=word[pos:j]
            pos=j
        assert phrase
        pieces.append(phrase)
    assert ''.join(pieces)==word
    return tuple(pieces)


def proper_windows(word):
    assert len(word)==LENGTH
    assert word.startswith('00000')
    circ=word+word[:ORDER-1]
    return {circ[i:i+ORDER] for i in range(LENGTH)}


def rows():
    a=set(binary_cycles_switch())
    b=set(binary_cycles_euler())
    assert a==b,(len(a),len(b),len(a-b),len(b-a))
    assert len(a)==2048
    result=[]
    for s in sorted(a):
        assert len(proper_windows(s))==LENGTH
        values=[]
        for offset in range(LENGTH):
            w=s[offset:]+s[:offset]
            p=parse_set(w)
            q=parse_trie(w)
            assert p==q,(w,p,q)
            values.append(len(p))
        result.append((s,min(values),max(values),values[0]))
    return result


def main():
    entries=rows()
    hist=Counter((low,high) for _,low,high,_ in entries)
    anchored=Counter(anchor for _,_,_,anchor in entries)
    assert hist=={(11,13):6,(11,14):44,(12,13):746,(12,14):1172,(13,13):30,(13,14):50},hist
    assert anchored=={11:18,12:480,13:1508,14:42},anchored
    if len(sys.argv)>1:
        cert=Path(sys.argv[1]); expected='canonical_0_to_5\tcyclic_min\tcyclic_max\tanchored\n' + ''.join(f'{s}\t{a}\t{b}\t{c}\n' for s,a,b,c in entries)
        assert cert.read_text(encoding='ascii')==expected,'certificate mismatch'
    print('VERIFY_OK cycles=2048 cases=65536 rotations=65536')
    print('JOINT',dict(sorted(hist.items())))
    print('ANCHORED',dict(sorted(anchored.items())))

if __name__=='__main__': main()
