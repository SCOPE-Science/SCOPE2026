"""Finite rational tests for commutation of epistemic minima and event probabilities."""
from itertools import combinations, product
from fractions import Fraction
from math import comb

def partitions(seq):
    if not seq:
        yield ()
    else:
        x,*tail=seq
        for part in partitions(tail):
            yield ((x,),)+part
            for i in range(len(part)):
                out=list(part);out[i]=(x,)+out[i]
                yield tuple(out)

def rows(n,q):
    # Nonnegative integral rows summing to q, /q.
    def compositions(k,s):
        if k==1:
            yield (s,)
        else:
            for a in range(s+1):
                for rest in compositions(k-1,s-a):
                    yield (a,)+rest
    return list(compositions(n,q))

def evaluate(part,mat,q):
    n=len(mat)
    cells=[tuple(c) for c in part]
    # scaled quantities (un-divided by q): min and mu
    all_equal=True
    criteria_hold=True
    for C in cells:
        common=[sum(mat[C[0]][j] for j in D) for D in cells]
        homogeneous=all([sum(mat[v][j] for j in D) for D in cells]==common for v in C)
        Dplus=[(D,a) for D,a in zip(cells,common) if len(D)>1 and a>0]
        selector_cover=homogeneous and all(any(all(sum(mat[v][j] for j in D if j!=x)==0 and mat[v][x]==a for D,a,x in zip((dd for dd,aa in Dplus),(aa for dd,aa in Dplus),ss)) for v in C) for ss in product(*(D for D,a in Dplus)))
        for Pbits in range(1<<n):
            P={j for j in range(n) if Pbits>>j&1}
            KP={j for D in cells if set(D)<=P for j in D}
            nested=min(sum(mat[v][j] for j in P) for v in C)
            inner=[sum(mat[w][j] for j in KP) for w in C]
            if any(nested!=iv for iv in inner):
                all_equal=False
            if homogeneous:
                assert nested >= inner[0]
        if not selector_cover:
            criteria_hold=False
        if homogeneous:
            if not Dplus:
                predictor=0
            else:
                predictor=sum(a for D,a in Dplus)-min(max(sum(mat[v][x] for x in ss) for v in C) for ss in product(*(D for D,a in Dplus)))
            # exact max across global P >= prediction; recompute on class
            localmax=max(min(sum(mat[v][j] for j in range(n) if mask>>j&1) for v in C)-sum(mat[C[0]][j] for D in cells if all(mask>>i&1 for i in D) for j in D) for mask in range(1<<n))
            assert localmax==predictor,(part,mat,C,predictor,localmax)
        if not homogeneous or not selector_cover:
            criteria_hold=False
    assert all_equal == criteria_hold, (part,mat)

if __name__=='__main__':
    tot=0
    for n,q in [(1,2),(2,2),(3,2)]:
        ps=list(partitions(list(range(n))))
        rr=rows(n,q)
        for mat in product(rr,repeat=n):
            for p in ps:
                evaluate(p,mat,q)
                tot+=1
        print(f'exhaustive n={n} denominator={q} cases={len(ps)*len(rr)**n}')
    # Complete 4-state symmetric rows whose support lies in information cell: 4 cell partitions, denominator two.
    n=4;rr=rows(n,2)
    for mat in product(rr,repeat=n):
        for p in [((0,1,2,3),),((0,1),(2,3)),((0,1,2),(3,))]:
            evaluate(p,mat,2);tot+=1
    print('ALL_CHECKS_OK cases=',tot)
