#!/usr/bin/env python3
"""Construct and verify optimal circular covers of all binary words avoiding 00.
Standard library only; the infinite optimality assertion is proved in RESULT.md.
"""
from collections import Counter

def fibonacci(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def lucas(n):
    a,b=2,1
    for _ in range(n): a,b=b,a+b
    return a

def valid_words(n):
    return [format(w,f'0{n}b') for w in range(1<<n) if '00' not in format(w,f'0{n}b')]

def construct(n):
    assert n>=2
    L=n-1
    all_v=valid_words(L)
    edges=[]
    mandatory=valid_words(n)
    for w in mandatory:
        edges.append((w[:-1],w[1:],w[-1],w))
    extra=0
    negative=[v for v in all_v if v[0]=='1' and v[-1]=='0']
    positive=[v for v in all_v if v[0]=='0' and v[-1]=='1']
    destinations=[]
    for v in negative:
        r=len(v)-len(v.lstrip('1'))
        current=v
        for _ in range(r):
            edge_word=current+'1'
            assert '00' not in edge_word
            next_v=edge_word[1:]
            edges.append((current,next_v,'1',edge_word))
            current=next_v
            extra+=1
        assert current[0]=='0' and current[-1]=='1'
        destinations.append(current)
    assert sorted(destinations)==sorted(positive)
    indeg=Counter();outdeg=Counter()
    for u,v,b,w in edges:
        outdeg[u]+=1;indeg[v]+=1
    assert all(indeg[v]==outdeg[v] for v in all_v)
    adj={v:[] for v in all_v}
    for u,v,b,w in edges:
        adj[u].append((v,b))
    stack=[all_v[0]];labels=[];rev=[]
    while stack:
        u=stack[-1]
        if adj[u]:
            v,b=adj[u].pop();stack.append(v);labels.append(b)
        else:
            stack.pop()
            if labels:rev.append(labels.pop())
    assert all(not arr for arr in adj.values())
    seq=''.join(reversed(rev))
    assert len(seq)==len(edges)
    assert len(seq)==lucas(n+1)-1
    windows=Counter(''.join(seq[(i+j)%len(seq)] for j in range(n)) for i in range(len(seq)))
    assert '00' not in seq+seq[0]
    assert set(mandatory).issubset(windows)
    assert set(windows).issubset(mandatory)
    assert sum(windows.values())==len(seq)
    assert extra==fibonacci(n)-1
    return seq,extra,len(mandatory),len(negative)

def small_exhaustive(n, opt):
    # Exhaustively exclude any shorter circular binary word, without assuming it avoids 00.
    required=set(valid_words(n))
    for length in range(n,opt):
        for bits in range(1<<length):
            s=format(bits,f'0{length}b')
            present={''.join(s[(i+j)%length] for j in range(n)) for i in range(length)}
            assert not required.issubset(present)

if __name__=='__main__':
    for n in range(2,13):
        seq,extra,required,negative=construct(n)
        print(f'n={n} required={required} additional={extra} shortest={len(seq)} negative={negative} prefix={seq[:40]}')
        if n<=5: small_exhaustive(n,len(seq))
    print('VERIFY_OK')
