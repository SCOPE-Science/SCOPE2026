#!/usr/bin/env python3
"""Exact finite-state computation of ECA first-versus-second spatial images."""
from collections import Counter, deque
from functools import lru_cache
import csv
from pathlib import Path

def local(rule, bits):
    return (rule >> bits) & 1

def label(rule, window, steps):
    if steps == 1:
        assert 0 <= window < 8
        return local(rule, window)
    assert steps == 2 and 0 <= window < 32
    row = 0
    for offset in (2, 1, 0):
        row = (row << 1) | local(rule, (window >> offset) & 7)
    return local(rule, row)

def make_graph(rule, steps):
    degree = 2 * steps
    size = 1 << degree
    M = size - 1
    graph = [[0, 0] for _ in range(size)]
    for state in range(size):
        for bit in (0, 1):
            word = 2 * state + bit
            target = word & M
            lab = label(rule, word, steps)
            graph[state][lab] |= (1 << target)
    return graph

def reach(graph, state, bit):
    ans = 0
    while state:
        low = state & -state
        state ^= low
        ans |= graph[low.bit_length() - 1][bit]
    return ans

def class_rule(rule):
    one, two = make_graph(rule, 1), make_graph(rule, 2)
    @lru_cache(maxsize=None)
    def t1(mask, label): return reach(one, mask, label)
    @lru_cache(maxsize=None)
    def t2(mask, label): return reach(two, mask, label)
    start = (15, 65535)
    parent = {start:None}
    queue = deque([start]); count=0
    while queue:
        key=queue.popleft();count+=1
        a,b=key
        for c in (0,1):
            u,v=t1(a,c),t2(b,c)
            if u == 0:
                continue
            if v == 0:
                word=str(c)
                k=key
                while parent[k] is not None:
                    k,letter=parent[k]
                    word=str(letter)+word
                return (False,len(word),word,len(parent))
            nk=(u,v)
            if nk not in parent:
                parent[nk]=(key,c)
                queue.append(nk)
    return (True,0,'',len(parent))

def direct_check(rule, word, steps):
    # Enumerate all length len(word)+2*steps input blocks and test output equality.
    n=len(word)
    target=int(word,2)
    for input_word in range(1 << (n+2*steps)):
        out=0
        for pos in range(n):
            window=(input_word >> (n-pos-1)) & ((1<<(2*steps+1))-1)
            out=(out << 1)|label(rule,window,steps)
        if out==target:
            return True
    return False

def run():
    catalog=[]
    for rule in range(256):
        s,n,w,states=class_rule(rule)
        catalog.append((rule,int(s),n,w,states))
    assert sum(c[1] for c in catalog)==72
    assert Counter(c[2] for c in catalog if not c[1])=={1:4,2:2,3:16,4:28,5:40,6:46,7:24,8:4,9:8,10:8,11:2,12:2}
    assert [(rule,w) for rule,stable,n,w,states in catalog if n==12]==[(126,'011101101110'),(129,'100010010001')]
    assert max(c[4] for c in catalog)==252
    for rule,stable,n,w,states in catalog:
        if not stable:
            assert direct_check(rule,w,1), (rule,'1')
            assert not direct_check(rule,w,2), (rule,'2')
    for rule,word in [(126,'011101101110'),(129,'100010010001')]:
        assert direct_check(rule,word,1)
        assert not direct_check(rule,word,2)
    # Full independent finite-word agreement through n=5 for all rules.
    for r in range(256):
        G1,G2=make_graph(r,1),make_graph(r,2)
        for n in range(1,6):
            for j in range(1<<n):
                w=format(j,'0%db'%n)
                a,b=15,65535
                for c in w:
                    a=reach(G1,a,int(c));b=reach(G2,b,int(c))
                assert (a!=0)==direct_check(r,w,1)
                assert (b!=0)==direct_check(r,w,2)
    with (Path(__file__).resolve().parent / 'classification.csv').open('w',newline='',encoding='utf8') as f:
        writer=csv.writer(f);writer.writerow(['rule','equal_first_second','shortest_difference_length','witness','reachable_pair_states']);writer.writerows(catalog)
    print('VERIFY_OK: 256 exact pair-subset graph closures; 72 first-image-stable, 184 strictly shrinking;')
    print('shortest discrepancy distribution',dict(sorted(Counter(c[2] for c in catalog if not c[1]).items())))
    print('sharp cutoff 12 at rules 126,129 with witnesses; max pair state count 252;')
    print('independent full-word checks lengths 1..5 all rules; extremal witnesses checked by full preimage enumeration')
if __name__=='__main__':run()
