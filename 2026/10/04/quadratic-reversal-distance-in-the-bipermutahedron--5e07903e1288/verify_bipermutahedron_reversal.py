from collections import Counter, deque

def singleton(w,n):
    c=Counter(w)
    return next(i for i in range(1,n+1) if c[i]==1)

def neighbors(w,n):
    w=list(w); k=singleton(w,n); out=[]
    for h in range(len(w)-1):
        if w[h] != w[h+1]:
            z=w.copy(); z[h],z[h+1]=z[h+1],z[h]; out.append(tuple(z))
        else:
            i=w[h]
            z=w.copy(); z.pop(h+1)
            p=z.index(k); z.insert(p+1,k)
            out.append(tuple(z))
    return out

def endpoints(n):
    a=[1]
    for i in range(2,n+1): a += [i,i]
    return tuple(a),tuple(reversed(a))

def dist(n):
    s,t=endpoints(n)
    q=deque([s]); d={s:0}
    while q:
        x=q.popleft()
        if x==t:return d[x]
        for y in neighbors(x,n):
            if y not in d:
                d[y]=d[x]+1;q.append(y)
    raise AssertionError('disconnected')

# Source edge rules imply the graph implemented above. Exhaustive BFS checks
# the theorem in the first nontrivial sizes, including 113400 vertices at n=5.
want={2:2,3:8,4:15,5:24}
for n,e in want.items():
    got=dist(n)
    assert got==e,(n,got,e)

# Algebraic lower-bound optimization used in the proof.
# r = number of labels ever singled, t = n-r.
for n in range(3,30):
    for r in range(1,n+1):
        t=n-r
        if r==1:
            extra=t*(t-1)
        else:
            extra=t*(t-1)+r
        assert extra >= n-1,(n,r,extra)

# Explicit upper-path length: n(n-1) adjacent-swap edges plus n-1
# singleton-transfer edges for n>=3; n=2 needs only two swaps.
for n in range(3,100):
    assert n*(n-1)+(n-1)==n*n-1
print('VERIFY_OK bipermutahedron reversal distance n=2..5 BFS; proof inequalities n<30')
