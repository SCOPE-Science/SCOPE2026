"""Exhaustive independent finite check of a local crossing criterion for tree-transposition words.
Every tested word contains each tree edge exactly twice. Python standard library only.
"""
from itertools import permutations
from collections import Counter
import time, random

TREES = [
('K2',2,[(0,1)],1),
('P3',3,[(0,1),(1,2)],4),
('P4',4,[(0,1),(1,2),(2,3)],42),
('K1_3',4,[(0,1),(0,2),(0,3)],30),
('P5',5,[(0,1),(1,2),(2,3),(3,4)],816),
('K1_4',5,[(0,1),(0,2),(0,3),(0,4)],336),
('Chair5',5,[(0,1),(0,2),(0,3),(3,4)],608),
('P6',6,[(0,1),(1,2),(2,3),(3,4),(4,5)],25520),
('K1_5',6,[(0,1),(0,2),(0,3),(0,4),(0,5)],5040),
('Broom6',6,[(0,1),(0,2),(0,3),(0,4),(4,5)],11220),
('DoubleStar6',6,[(0,1),(0,2),(0,3),(3,4),(3,5)],14480),
('Spider311',6,[(0,1),(0,2),(0,3),(3,4),(4,5)],18880),
('Spider221',6,[(0,1),(0,2),(0,3),(2,4),(3,5)],19680),
]

def words(m):
    remaining=[2]*m
    prefix=[0]*(2*m)
    def recur(i):
        if i==2*m:
            yield tuple(prefix)
            return
        for k in range(m):
            if remaining[k]:
                remaining[k]-=1
                prefix[i]=k
                yield from recur(i+1)
                remaining[k]+=1
    yield from recur(0)

def product_is_identity(word,edges,n):
    p=list(range(n))
    # Right multiply permutation by (a b); this swaps the images in slots a,b.
    for t in word:
        a,b=edges[t]
        p[a],p[b]=p[b],p[a]
    return all(p[i]==i for i in range(n))

def noncrossing_local(word,edges):
    m=len(edges)
    first=[-1]*m
    last=[-1]*m
    for pos,t in enumerate(word):
        if first[t]==-1:first[t]=pos
        else:last[t]=pos
    for a in range(m):
        for b in range(a):
            if not (set(edges[a])&set(edges[b])):continue
            a0,a1=first[a],last[a]
            b0,b1=first[b],last[b]
            if (a0<b0<a1<b1) or (b0<a0<b1<a1):return False
    return True


def check_factor_lemma(word, edges, n):
    # On every contiguous factor, fixed vertices must be exactly the vertices
    # not incident to an edge appearing an odd number of times in the factor.
    for a in range(len(word)+1):
        for b in range(a,len(word)+1):
            sub=word[a:b]
            counts=[0]*len(edges)
            for t in sub:counts[t]+=1
            p=list(range(n))
            for t in sub:
                u,v=edges[t]
                p[u],p[v]=p[v],p[u]
            for v in range(n):
                incident_odd=any(counts[t]%2 for t,e in enumerate(edges) if v in e)
                assert (p[v]==v)==(not incident_odd),(edges,word,a,b,v)


def main():
    total=0
    factor_checks=0
    for name,n,edges,expected in TREES:
        m=len(edges)
        count=0; ok=0
        for w in words(m):
            x=product_is_identity(w,edges,n)
            y=noncrossing_local(w,edges)
            count+=1
            if x!=y:
                raise AssertionError((name,w,x,y))
            if x:
                ok+=1
                # Exhaustively inspect factors for smaller trees; sample fixed
                # witness words for all six larger tree shapes.
                if m<=3 or (m>=4 and ok <= 30):
                    check_factor_lemma(w,edges,n)
                    factor_checks+=1
        assert ok==expected,(name,ok,expected)
        total+=count
        print('EXHAUSTIVE',name,'vertices',n,'words',count,'identity',ok,'criterion_OK')
    print('TOTAL_EXHAUSTIVE',total)
    print('FACTOR_LEMMA_WORDS_CHECKED',factor_checks)
    random.seed(20261017)
    for m in [6,7,8]:
        n=m+1
        # A path and a star; no reliance on any finite bound for the theorem.
        for kind in ['path','star']:
            E=[(j,j+1) for j in range(m)] if kind=='path' else [(0,j+1) for j in range(m)]
            trials=5000
            for _ in range(trials):
                w=[j for j in range(m) for _ in range(2)]
                random.shuffle(w)
                assert product_is_identity(w,E,n)==noncrossing_local(w,E),(m,kind,w)
            print('RANDOM',kind,'edges',m,'tests',trials,'criterion_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
