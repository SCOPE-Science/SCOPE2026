"""Independent exhaustive FO^3 quantifier-rank type refinement on two affine planes.

The unassigned marker * is used to compute sentence types exactly, rather
than deriving sentential equivalence from arbitrarily assigned triples.
"""
import itertools


def poset(q):
    assert q in (2,3)
    pts=list(itertools.product(range(q),repeat=2))
    lines=[]
    for m in range(q):
        for b in range(q):
            lines.append(frozenset(i for i,(x,y) in enumerate(pts) if (y-m*x-b)%q==0))
    for a in range(q):
        lines.append(frozenset(i for i,(x,y) in enumerate(pts) if x==a))
    return [frozenset()]+[frozenset({i}) for i in range(q*q)]+lines+[frozenset(range(q*q))]


def initial(q):
    F=poset(q);n=len(F);v=n+1;none=n
    cases=list(itertools.product(range(v),repeat=3))
    order={(a,b):i for i,(a,b) in enumerate(itertools.product(range(v),repeat=2))}
    incl=[[int(F[a]<=F[b]) for b in range(n)] for a in range(n)]
    atomic=[]
    for tup in cases:
        atomic.append(tuple(
          (i,j,int(tup[i]==tup[j]),incl[tup[i]][tup[j]])
          for i in range(3) for j in range(3)
          if tup[i]!=none and tup[j]!=none))
    return n,cases,atomic


def main():
    data=[initial(2),initial(3)]
    signatures=sorted(set(x for _,_,v in data for x in v))
    pools={key:i for i,key in enumerate(signatures)}
    cols=[[pools[x] for x in atoms] for _,_,atoms in data]
    start_ids=[len(tuples)-1 for n,tuples,_ in data]  # (*,*,*) is last
    first=None
    for depth in range(8):
        roots=[cols[i][start_ids[i]] for i in range(2)]
        eq=roots[0]==roots[1]
        print('quantifier_rank=%d agree=%s types=%d' % (depth,eq,len(pools)))
        if not eq and first is None: first=depth
        if depth==7:break
        sig_batches=[]
        for (n,tuples,_),row in zip(data,cols):
            v=n+1
            signs=[]
            # a triple (a,b,c) is encoded (a*v+b)*v+c.
            for a,b,c in tuples:
                w0=tuple(sorted({row[(i*v+b)*v+c] for i in range(n)}))
                w1=tuple(sorted({row[(a*v+i)*v+c] for i in range(n)}))
                w2=tuple(sorted({row[(a*v+b)*v+i] for i in range(n)}))
                signs.append((row[(a*v+b)*v+c],w0,w1,w2))
            sig_batches.append(signs)
        pools={s:i for i,s in enumerate(sorted(set(x for batch in sig_batches for x in batch)))}
        cols=[[pools[x] for x in batch] for batch in sig_batches]
    assert first==4, first
    print('FO3_REFINEMENT_OK earliest_quantifier_rank=4')

if __name__=='__main__':main()
