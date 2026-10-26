#!/usr/bin/env python3
"""Independent finite checks for the four-run gapped-pair-deck theorem.
Uses direct positional enumeration, not the proof's run-count formulas.
"""
from collections import defaultdict, Counter

def deck(w):
    z=w.count('0'); t=w.count('1'); g={p:0 for p in ['00','01','10','11']}
    for i in range(len(w)):
        for j in range(i+2,len(w)):
            g[w[i]+w[j]]+=1
    return (z,t,g['00'],g['01'],g['10'],g['11'])

def runs(w):
    return 0 if not w else 1+sum(w[i-1]!=w[i] for i in range(1,len(w)))

def repr4(w):
    if runs(w)!=4:return None
    chunks=[]
    for x in w:
        if not chunks or x!=chunks[-1][0]:chunks.append([x,1])
        else:chunks[-1][1]+=1
    return chunks

def divcount(t,z,p):
    if p<1:return 0
    return sum(1 for i in range(1,t) for j in range(1,z) if i*j==p)

checks=0
for n in range(1,15):
    classes=defaultdict(list)
    for i in range(1<<n):
        w=format(i,f'0{n}b')
        d=deck(w);classes[d].append(w)
        r=runs(w)
        if n>=3 and r<=3:
            # checked after full class built
            pass
        if r==4:
            z,t,_,q,_,_=d
            v=repr4(w)
            if w[0]=='0':
                a,b,c,dd=(x[1] for x in v)
                assert q==z*t-2-b*c
            else:
                a,b,c,dd=(x[1] for x in v)
                assert q==b*c-1
            assert len([x for x in classes[d] if runs(x)==4])<=divcount(t,z,q+1)+divcount(t,z,z*t-2-q)
            checks+=1
    for d,ws in classes.items():
        if n>=3 and any(runs(x)<=3 for x in ws):
            assert len(ws)==1,(n,d,ws)
        four=[x for x in ws if runs(x)==4]
        if four:
            z,t,_,q,_,_=d
            assert len(ws)==divcount(t,z,q+1)+divcount(t,z,z*t-2-q),(n,d,ws)
            checks+=1
    if n==2:
        assert classes[deck('01')]==['01','10']
    if n==6:
        doubles=sorted(tuple(ws) for ws in classes.values() if len(ws)>1)
        assert doubles==[('001101','010011'),('011001','100110'),('101100','110010')],doubles
        assert len(classes)==61
    if n in (3,4,5,6,8,10,12,14):
        print('n=',n,'profiles=',len(classes),'non-singletons=',sum(len(ws)>1 for ws in classes.values()))
for k in range(1,9):
    p=1<<k;t=z=p+1
    words=[]
    for j in range(k+1):
        b=1<<j;c=1<<(k-j)
        a=t-c;d=z-b
        words.append('1'*a+'0'*b+'1'*c+'0'*d)
    assert len(set(words))==k+1
    assert len({deck(w) for w in words})==1
    checks+=1
print('VERIFY_OK',checks,'assertions of run statistics and full fibers, plus unbounded-family checks')
for t in range(2,12):
    for z in range(2,12):
        words=[]
        for a in range(1,z):
            for b in range(1,t):
                words.append('0'*a+'1'*b+'0'*(z-a)+'1'*(t-b))
        for a in range(1,t):
            for b in range(1,z):
                words.append('1'*a+'0'*b+'1'*(t-a)+'0'*(z-b))
        S={i*j for i in range(1,t) for j in range(1,z)}
        predicted=2*len(S)-sum(t*z-1-p in S for p in S)
        observed=len({deck(w) for w in words})
        assert observed==predicted,(t,z,predicted,observed)
print('OPTIMAL_PROFILE_COUNT_OK',100)
