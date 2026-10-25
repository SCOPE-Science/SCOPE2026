"""Exact binary comparison shattering for 321-avoiding permutations of length <=8.
All integers are exact; a bit represents one permutation in lexicographic order.
"""
from itertools import permutations, combinations
from functools import lru_cache
import json,math,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent

def avoids321(p):
    n=len(p)
    return not any(p[i]>p[j]>p[k] for i in range(n) for j in range(i+1,n) for k in range(j+1,n))

def universe(n):
    words=[p for p in permutations(range(1,n+1)) if avoids321(p)]
    q=list(combinations(range(n),2))
    rows=[]
    for i,j in q:
        mask=sum(1<<k for k,p in enumerate(words) if p[i]<p[j])
        rows.append(mask)
    full=(1<<len(words))-1
    return words,q,rows,full

def exact_rank(words,rows,full):
    @lru_cache(None)
    def rank(s):
        if s & (s-1) == 0: return 0
        bound=s.bit_count().bit_length()-1
        best=0
        for mask in rows:
            yes=s&mask
            no=s&(~mask)&full
            if not yes or not no:continue
            if min(yes.bit_count(),no.bit_count())<(1<<best): continue
            score=1+min(rank(no),rank(yes))
            if score>best:best=score
            if best==bound:break
        return best
    return rank

def build():
    ranks=[]
    for n in range(1,9):
        words,q,rows,full=universe(n)
        rank=exact_rank(words,rows,full)
        d=rank(full)
        ranks.append([n,len(words),d,rank.cache_info().currsize])
        print('DIM',n,len(words),d,rank.cache_info().currsize,flush=True)
        if n==8:
            assert d==9
            depth=d
            queries=[None]*(2**depth)
            leaf=[None]*(2**depth)
            def grow(s,rem,node):
                if rem==0:
                    idx=(s&-s).bit_length()-1
                    leaf[node-2**depth]=list(words[idx]);return
                for ix,mask in enumerate(rows):
                    a=s&(~mask)&full
                    b=s&mask
                    if a and b and a.bit_count()>=2**(rem-1) and b.bit_count()>=2**(rem-1) and rank(a)>=rem-1 and rank(b)>=rem-1:
                        queries[node]=list(q[ix])
                        grow(a,rem-1,2*node)
                        grow(b,rem-1,2*node+1)
                        return
                raise RuntimeError('certificate cannot grow')
            grow(full,depth,1)
            cert={'schema_version':1,'n':n,'depth':depth,'queries_heap_one_indexed':queries[1:],'leaf_witnesses_left_to_right':leaf}
            with open(HERE/'tree_depth9.json','w',encoding='utf-8') as f:json.dump(cert,f,separators=(',',':'),ensure_ascii=False);f.write('\n')
    with open(HERE/'dimensions.json','w',encoding='utf-8') as f:json.dump(ranks,f,separators=(',',':'));f.write('\n')
    print('CERTIFICATE_WRITTEN',len(cert['queries_heap_one_indexed']),len(leaf),flush=True)
if __name__=='__main__':build()
