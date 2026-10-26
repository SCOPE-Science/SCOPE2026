#!/usr/bin/env python3
"""Independent exhaustive small Ehrenfeucht--Fraisse comparisons for rook graphs."""
from functools import lru_cache
from itertools import combinations_with_replacement

def graph(a,b):
    vertices=[(i,j) for i in range(a) for j in range(b)]
    n=len(vertices)
    adj=tuple(tuple(int(i!=j and (vertices[i][0]==vertices[j][0] or vertices[i][1]==vertices[j][1])) for j in range(n)) for i in range(n))
    return adj

def ef(A,B,q):
    n=len(A);m=len(B)
    @lru_cache(None)
    def win(X,Y,remaining):
        if remaining==0:
            return True
        for side in (0,1):
            S=A if side==0 else B
            T=B if side==0 else A
            oldS=X if side==0 else Y
            oldT=Y if side==0 else X
            for s in range(len(S)):
                possible=False
                for t in range(len(T)):
                    if all((s==si)==(t==ti) and S[s][si]==T[t][ti] for si,ti in zip(oldS,oldT)):
                        XX=X+(s,) if side==0 else X+(t,)
                        YY=Y+(t,) if side==0 else Y+(s,)
                        if win(XX,YY,remaining-1):
                            possible=True;break
                if not possible:
                    return False
        return True
    result=win((),(),q)
    return result,win.cache_info().currsize

if __name__=='__main__':
    for q,cap in ((1,3),(2,3),(3,4)):
        reps=list(combinations_with_replacement(range(1,cap+1),2))
        checks=0
        maximum=0
        for ix,(a,b) in enumerate(reps):
            for c,d in reps[ix:]:
                outcome,nstates=ef(graph(a,b),graph(c,d),q)
                expected=(sorted((min(a,q),min(b,q)))==sorted((min(c,q),min(d,q))))
                assert outcome==expected,(q,(a,b),(c,d),outcome,expected)
                checks+=1;maximum=max(maximum,nstates)
        print(f'PASS q={q} graph-factor ceiling={cap} pairwise comparisons={checks} largest DP-state count={maximum}')
    for q,(a,b),(c,d) in ((4,(3,5),(4,5)),(4,(4,4),(5,5)),(4,(2,5),(2,4))):
        outcome,nstates=ef(graph(a,b),graph(c,d),q)
        expected=(sorted((min(a,q),min(b,q)))==sorted((min(c,q),min(d,q))))
        assert outcome==expected
        print(f'PASS q={q} {a}x{b} vs {c}x{d}: equivalent={outcome}, DP states={nstates}')
    print('These finite games corroborate; the uniform theorem uses an independent symbolic strategy.')
