#!/usr/bin/env python3
"""Independent exhaustive two-sided EF minimax for the 4-round cycle witness.
This checks game strategies directly, not logical-type hash equality.
"""
from functools import lru_cache

def edges(parts):
    n=sum(parts); d=[[False]*n for _ in range(n)]
    j=0
    for c in parts:
        for i in range(c):
            a=j+i;b=j+(i+1)%c
            d[a][b]=d[b][a]=True
        j+=c
    return d

A=edges((9,9)); B=edges((11,));n=len(A);m=len(B)
visited=[0]
@lru_cache(None)
def win(a,b,remaining):
    visited[0]+=1
    if remaining==0:return True
    for source in (0,1):
        X,Y=(A,B) if source==0 else (B,A)
        x,y=(a,b) if source==0 else (b,a)
        xset=set(x);yset=set(y)
        for u in range(len(X)):
            if u in xset:continue
            possible=False
            for v in range(len(Y)):
                if v in yset:continue
                if all(X[u][xx]==Y[v][yy] for xx,yy in zip(x,y)):
                    aa,bb=(a+(u,),b+(v,)) if source==0 else (a+(v,),b+(u,))
                    if win(aa,bb,remaining-1):
                        possible=True;break
            if not possible:return False
    return True

def verify():
    # Both graphs are vertex transitive, so after round one choose representatives 0,0.
    assert win((0,),(0,),3)
    print('DIRECT_EF_4_ROUND_DUPLICATOR_WINS')
    print('RECURSIVE_GAME_STATES='+str(visited[0]))
    print('DIRECT_EF_OK')
if __name__=='__main__':verify()
