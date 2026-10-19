#!/usr/bin/env python3
"""Exact checks for the binary weight-one/two universal-cycle enumeration.
Standard library only. Usage: python VERIFY.py
"""
from collections import defaultdict
from itertools import product


def graph(k):
    s=k-1
    mask=(1<<s)-1
    words=[w for w in range(1<<k) if w.bit_count() in (1,2)]
    out=defaultdict(list)
    for w in words:
        v=w>>1
        nxt=w&mask
        out[v].append((w&1,nxt,w))
    assert len(words)==k*(k+1)//2
    assert sorted(out)==sorted([0]+[1<<j for j in range(s)]+[x for x in range(1<<s) if x.bit_count()==2])
    return sorted(out),out,words


def bareiss_det(a):
    a=[row[:] for row in a]
    n=len(a)
    denom=1
    sign=1
    for p in range(n-1):
        if a[p][p]==0:
            r=next((r for r in range(p+1,n) if a[r][p]),None)
            if r is None: return 0
            a[p],a[r]=a[r],a[p]
            sign=-sign
        pivot=a[p][p]
        for i in range(p+1,n):
            for j in range(p+1,n):
                numer=a[i][j]*pivot-a[i][p]*a[p][j]
                assert numer%denom==0
                a[i][j]=numer//denom
            a[i][p]=0
        denom=pivot
    return sign*a[n-1][n-1] if n else 1


def matrix_tree(k):
    vs,out,_=graph(k)
    vs=[v for v in vs if v!=0]
    idx={v:i for i,v in enumerate(vs)}
    matrix=[[0]*len(vs) for _ in vs]
    for v in vs:
        i=idx[v]
        for bit,nxt,_ in out[v]:
            matrix[i][i]+=1
            if nxt: matrix[i][idx[nxt]]-=1
    return bareiss_det(matrix)


def functional_tree_count(k):
    vs,out,_=graph(k)
    s=k-1
    branching=[1<<j for j in range(s)]
    count=0
    for switches in product((0,1),repeat=s):
        nxt={v:out[v][0][1] for v in vs if v not in branching and v!=0}
        for j,v in enumerate(branching):
            opts=sorted(out[v])
            nxt[v]=opts[switches[j]][1]
        good=True
        for v in vs:
            x=v
            seen=set()
            while x and x not in seen:
                seen.add(x)
                x=nxt[x]
            if x:good=False;break
        predicted=not any(switches[j] for j in range(s//2,s))
        assert good==predicted, (k,switches,good,predicted)
        count+=good
    return count


def direct_euler(k):
    # Enumerate each possible outgoing-edge order at every two-way vertex.
    # Following each edge immediately until returning to the root must use
    # all edges to represent an Euler circuit. This test does not use BEST.
    vs,out,words=graph(k)
    s=k-1
    good=set()
    for switches in product((0,1),repeat=s):
        orders={}
        for v in vs:
            choices=sorted(out[v])
            if v and v.bit_count()==1 and switches[v.bit_length()-1]:
                choices=choices[::-1]
            orders[v]=choices
        pos={v:0 for v in vs}
        v=0
        bits=[]
        while pos[v]<len(orders[v]):
            bit,nxt,w=orders[v][pos[v]]
            pos[v]+=1
            bits.append(str(bit))
            v=nxt
        if v==0 and len(bits)==len(words) and all(pos[v]==len(orders[v]) for v in vs):
            word=''.join(bits)
            windows={int(''.join(word[(i+j)%len(word)] for j in range(k)),2) for i in range(len(word))}
            assert windows==set(words)
            # Marked edge 0...01 is unique, no rotational overcount.
            good.add(word)
    return good


def main():
    for k in range(3,11):
        expected=1<<((k-1)//2)
        t=matrix_tree(k)
        f=functional_tree_count(k)
        assert (t,f)==(expected,expected),(k,t,f,expected)
        if k<=8:
            cycles=direct_euler(k)
            assert len(cycles)==expected,(k,len(cycles),expected)
            if k==5: print('EXAMPLE_K5',min(cycles))
        print('PASS',k,expected,t,f)
    print('VERIFY_OK matrix_tree_k=3..10 functional_tree_k=3..10 direct_euler_k=3..8')

if __name__=='__main__':main()
