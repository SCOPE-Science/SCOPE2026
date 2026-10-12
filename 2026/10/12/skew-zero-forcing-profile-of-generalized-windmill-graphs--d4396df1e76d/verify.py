from itertools import product
from math import comb

PAIRS=[(2,3),(2,4),(2,5),(3,3),(3,4),(4,3)]

def graph(k,m):
    n=1+k*m
    adj=[set() for _ in range(n)]
    for i in range(k):
        blade=list(range(1+i*m,1+(i+1)*m))
        for v in blade:
            adj[0].add(v); adj[v].add(0)
        for a in range(m):
            for b in range(a+1,m):
                u,v=blade[a],blade[b]
                adj[u].add(v); adj[v].add(u)
    return adj

def closure(adj,mask):
    n=len(adj)
    blue={v for v in range(n) if (mask>>v)&1}
    while True:
        move=None
        for v in range(n):
            white=[u for u in adj[v] if u not in blue]
            if len(white)==1:
                move=white[0]; break
        if move is None: break
        blue.add(move)
    return len(blue)==n

def criterion(k,m,mask):
    center_blue=bool(mask&1)
    ws=[]
    for i in range(k):
        w=sum(1 for j in range(m) if not ((mask>>(1+i*m+j))&1))
        ws.append(w)
    return max(ws)<=2 and (center_blue or any(w!=2 for w in ws))

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def predicted_coeffs(k,m):
    f=[0]*(m+1)
    f[m]=1; f[m-1]=m; f[m-2]=comb(m,2)
    p=[1]
    for _ in range(k): p=conv(p,f)
    q=p+[0]
    for i,a in enumerate(p): q[i+1]+=a
    q[k*(m-2)]-=comb(m,2)**k
    return q

total=0
min_checks=0
for k,m in PAIRS:
    adj=graph(k,m); n=len(adj)
    obs=[0]*(n+1)
    for mask in range(1<<n):
        total+=1
        actual=closure(adj,mask)
        pred=criterion(k,m,mask)
        if actual!=pred:
            raise AssertionError((k,m,mask,actual,pred))
        if actual: obs[mask.bit_count()]+=1
    pc=predicted_coeffs(k,m)
    if obs!=pc: raise AssertionError((k,m,obs,pc))
    z=next(i for i,a in enumerate(obs) if a)
    if z!=k*(m-2)+1: raise AssertionError(('Z',k,m,z))
    expected=comb(m,2)**(k-1)*(comb(m,2)+k*m)
    if obs[z]!=expected: raise AssertionError(('count',k,m,obs[z],expected))
    min_checks+=1
print(f"VERIFY_OK parameter_pairs={len(PAIRS)} subset_checks={total} minimum_checks={min_checks} max_order={max(1+k*m for k,m in PAIRS)}")
