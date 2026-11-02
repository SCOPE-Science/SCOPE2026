"""Independent rule-level checks for a cup-stacking classification on short/two-edge spiders.
Usage: python3 verify_cup_spiders.py
"""
from collections import deque
from functools import lru_cache

def tree(a,b):
    n=1+a+2*b
    adj=[[] for _ in range(n)]
    def add(u,v):adj[u].append(v);adj[v].append(u)
    for i in range(1,a+1):add(0,i)
    for j in range(b):add(0,a+1+2*j);add(a+1+2*j,a+2+2*j)
    D=[]
    for src in range(n):
        ds=[-1]*n;ds[src]=0;q=deque([src])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if ds[v]<0:ds[v]=ds[u]+1;q.append(v)
        D.append(ds)
    return adj,D

def explicit_one_short(b,target):
    assert b>=2
    c,s=0,1
    x=lambda j:2*j
    y=lambda j:2*j+1
    M=[]
    def move(u,v):M.append((u,v))
    if target==c:
        move(s,c)
        for j in range(1,b+1):move(x(j),y(j));move(y(j),c)
    elif target==s:
        move(c,s)
        for j in range(1,b+1):move(y(j),x(j));move(x(j),s)
    elif target==x(1):
        move(y(1),x(1));move(c,s);move(s,x(1))
        for j in range(2,b+1):move(y(j),x(j));move(x(j),x(1))
    elif target==y(1):
        move(x(1),y(1))
        if b==2:
            move(x(2),y(2));move(s,c);move(c,y(2));move(y(2),y(1))
        elif b%2==0:
            move(c,s);move(s,x(2))
            pending=x(2)
            for j in range(3,b,2):
                move(pending,y(j));move(y(j),y(1))
                move(y(j+1),x(j+1));move(x(j+1),x(j))
                pending=x(j)
            move(pending,y(2));move(y(2),y(1))
        else:
            move(c,x(2));move(y(2),x(2));move(x(2),y(1))
            move(y(3),x(3));move(x(3),s)
            pending=s
            for j in range(4,b,2):
                move(pending,y(j));move(y(j),y(1))
                move(y(j+1),x(j+1));move(x(j+1),x(j))
                pending=x(j)
            move(pending,y(1))
    else:raise ValueError(target)
    return M

def replay(a,b,target,steps):
    _,D=tree(a,b);n=len(D);loads=[1]*n
    assert len(steps)==n-1,(a,b,target,'wrong moves',len(steps),n-1)
    for index,(u,v) in enumerate(steps):
        k=loads[u]
        assert u!=v and k>0 and loads[v]>0 and k==D[u][v],(a,b,target,index,(u,v),loads,D[u][v])
        loads[v]+=k;loads[u]=0
    assert loads[target]==n and sum(loads)==n,(a,b,target,loads)

def exhaustive_unreachable(a,b,target):
    _,D=tree(a,b);n=len(D)
    @lru_cache(None)
    def possible(tup):
        if tup[target]==n:return True
        for u,k in enumerate(tup):
            if not k or u==target:continue
            for v,p in enumerate(tup):
                if u==v or p==0 or D[u][v]!=k:continue
                t=list(tup);t[v]+=k;t[u]=0
                if possible(tuple(t)):return True
        return False
    ans=possible((1,)*n)
    return ans,possible.cache_info().currsize

def main():
    cases=0
    for b in range(2,121):
        for t in (0,1,2,3):
            seq=explicit_one_short(b,t)
            replay(1,b,t,seq);cases+=1
    print('ALL_TARGET_EXPLICIT_CONSTRUCTIONS_OK',cases,'cases, b=2..120')
    checked=0
    for a,b in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)]:
        ans,count=exhaustive_unreachable(a,b,a+1)
        assert ans is False,(a,b,count)
        checked+=1
        print('UNREACHABLE_INNER',a,b,'states',count)
    print('VERIFY_OK',cases,'constructive cases,',checked,'exhaustive obstruction cases')
if __name__=='__main__':main()
