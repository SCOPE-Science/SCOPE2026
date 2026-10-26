"""Check subdivision open-independent open-locating-dominating/perfect-code correspondence.
Uses independent direct signature enumeration, without theorem-specific pruning.
Python 3 standard library only.
"""
import itertools
import random
from collections import Counter

def signature_old_codes(n, edges):
    size=n+len(edges)
    adjacency=[0]*size
    for i,(a,b) in enumerate(edges):
        w=n+i
        adjacency[w]|=(1<<a)|(1<<b)
        adjacency[a]|=1<<w
        adjacency[b]|=1<<w
    answers=[]
    for mask in range(1<<size):
        sig=[adj&mask for adj in adjacency]
        if 0 in sig or len(set(sig))<size:
            continue
        if any((sig[v]).bit_count()!=1 for v in range(size) if mask>>v&1):
            continue
        answers.append(mask)
    return set(answers)

def predicted_codes(n, edges):
    neighbors=[0]*n
    for a,b in edges:
        neighbors[a]|=1<<b
        neighbors[b]|=1<<a
    codes=[]
    for T in range(1<<n):
        if any(((neighbors[v]|(1<<v))&T).bit_count()!=1 for v in range(n)):
            continue
        if any(neighbors[t].bit_count()<2 for t in range(n) if T>>t&1):
            continue
        mask=((1<<n)-1)^T
        for i,(a,b) in enumerate(edges):
            if ((T>>a)&1) != ((T>>b)&1):
                mask|=1<<(n+i)
        codes.append(mask)
    return set(codes)

def check(n, bits):
    pairs=list(itertools.combinations(range(n),2))
    edges=[e for i,e in enumerate(pairs) if bits>>i&1]
    direct=signature_old_codes(n,edges)
    predicted=predicted_codes(n,edges)
    assert direct==predicted, (n,bits,edges,direct^predicted)
    return len(direct)

if __name__=='__main__':
    total=0; nonzero=0; dist=Counter()
    for n in range(1,5):
        for bits in range(1<<(n*(n-1)//2)):
            k=check(n,bits)
            total+=1; nonzero+=k>0; dist[(n,k)]+=1
    random.seed(832126)
    samples={0,(1<<10)-1,0b0010010101,0b1001010101,0b1011011010}
    while len(samples)<75:
        samples.add(random.randrange(1<<10))
    for bits in sorted(samples):
        k=check(5,bits)
        total+=1;nonzero+=k>0;dist[(5,k)]+=1
    print('PASS: compared independent direct enumeration with perfect-code map')
    print('graphs_checked',total,'graphs_with_codes',nonzero)
    print('distribution',sorted((str(key),n) for key,n in dist.items()))
    for n in (3,6,9):
        cyc=[(i,(i+1)%n) for i in range(n)]
        print('cycle_base',n,'codes',len(predicted_codes(n,cyc)))
