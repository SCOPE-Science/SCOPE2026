#!/usr/bin/env python3
"""Independent color-refinement check for rooted square Cartesian cycle products."""
from collections import Counter

def stable_refinement(n):
    adj=[]
    for i in range(n):
        for j in range(n):
            adj.append((((i-1)%n)*n+j,((i+1)%n)*n+j,i*n+(j-1)%n,i*n+(j+1)%n))
    colors=[0]*(n*n)
    colors[0]=1
    history=[]
    for step in range(n*n):
        pairs=[(colors[v],tuple(sorted(colors[w] for w in adj[v]))) for v in range(n*n)]
        ids={s:k for k,s in enumerate(sorted(set(pairs)))}
        new=[ids[s] for s in pairs]
        history.append(len(ids))
        if len(set(new))==len(set(colors)):
            return new,history
        colors=new
    raise AssertionError('no stabilization')

def orbit_key(n,v):
    x,y=divmod(v,n)
    a,b=sorted((min(x,n-x),min(y,n-y)))
    return a,b

def main():
    tested=0
    for n in range(5,71):
        colors,history=stable_refinement(n)
        keys=[orbit_key(n,v) for v in range(n*n)]
        classes={}
        for key,c in zip(keys,colors):
            classes.setdefault(key,set()).add(c)
        assert all(len(s)==1 for s in classes.values()),(n,classes)
        assert len(set(colors))==len(classes)==((n//2+1)*(n//2+2))//2,(n,history)
        tested+=n*n
    print('PASS direct rooted counting refinement: 66 orders n=5..70; %d vertex instances' % tested)
    print('PASS predicted orbit keys and class count for every order')
if __name__=='__main__':main()
