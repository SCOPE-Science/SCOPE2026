"""Checks optimal independent dominating sets in cyclic tensor products.
Run: python checker.py
No external data or libraries required.
"""
from collections import Counter
from itertools import combinations

def graph_masks(m,q):
    N=m*q
    a=[0]*N
    for i in range(m):
        for c in range(q):
            p=i*q+c
            for j in ((i-1)%m,(i+1)%m):
                for d in range(q):
                    if c!=d: a[p] |= 1<<(j*q+d)
    return a

def exhaustive(m,q):
    masks=graph_masks(m,q)
    bound=(2*m+2)//3
    assert m*q<=30
    all_bits=(1<<(m*q))-1
    opt=[]
    for size in range(bound+1):
        for comb in combinations(range(m*q), size):
            chosen=0
            ok=True
            for p in comb:
                if masks[p]&chosen:
                    ok=False
                    break
                chosen |= 1<<p
            if not ok:
                continue
            covered=chosen
            for p in comb:
                covered |= masks[p]
            if covered==all_bits:
                assert size==bound,('smaller successful set',m,q,size,comb)
                opt.append(frozenset(comb))
    return opt

def legal_word(word,q):
    n=len(word)
    for i,c in enumerate(word):
        a,b=word[(i-1)%n],word[(i+1)%n]
        if c==-1: # full layer; neighboring layers empty
            if a!=0 or b!=0:return False
        elif c>0:
            if a not in (0,c) or b not in (0,c):return False
            if a!=c and b!=c:return False
        else:
            if a==-1 or b==-1:continue
            if not (a>0 and b>0 and a!=b):return False
    return True

def enumerated_words(m,q):
    # enumerate only candidates with weight <= theoretical minimum, prune early
    minimum=(2*m+2)//3 if m>=6 else m
    seq=[];counts=Counter();opt=[]
    def rec(t,w):
        if w>minimum:return
        if t==m:
            if w==minimum and legal_word(seq,q):
                opt.append(tuple(seq))
            return
        for c in (-1,0,*range(1,q+1)):
            # all-color 'F' weight q; other color weight 1
            if seq:
                prev=seq[-1]
                if c==-1 and prev!=0:continue
                if prev==-1 and c!=0:continue
                if c>0 and prev>0 and c!=prev:continue
                if c==0 and prev==0 and len(seq)>=2 and seq[-2]!=-1: continue
            seq.append(c)
            rec(t+1,w+(q if c==-1 else int(c>0)))
            seq.pop()
    rec(0,0)
    return opt

def formula(k,q):
    return 3*((q-1)**k+(-1)**k*(q-1))

def verify():
    for k,q in ((2,3),(2,4),(2,5),(3,3),(3,4),(4,3),(5,3)):
        m=3*k
        opt=enumerated_words(m,q)
        target=formula(k,q)
        assert len(opt)==target,(m,q,len(opt),target)
        # frozen under one-vertex replacements: words with same size have symmetric difference >=4
        # each singleton layer is one vertex; F would correspond to q vertices
        assert all(-1 not in w for w in opt)
        sets=[]
        for w in opt:
            v=frozenset((i,w[i]-1) for i in range(m) if w[i]>0)
            assert len(v)==2*k
            sets.append(v)
        if len(sets)<=3000:
            for ii in range(len(sets)):
                for jj in range(ii+1,len(sets)):
                    assert len(sets[ii]-sets[jj])!=1
        print('words',m,q,'found',len(opt),'formula',target,'isolated',True)
    for m,q in ((6,3),(6,4),(9,3)):
        ex=exhaustive(m,q)
        assert len(ex)==formula(m//3,q)
        wr=enumerated_words(m,q)
        ss={frozenset((i*q+w[i]-1) for i in range(m) if w[i]>0) for w in wr}
        assert set(ex)==ss
        print('EXHAUSTIVE original independence and domination:',m,q,
              'minimum',2*m//3,'count',len(ex))

if __name__=='__main__': verify()
