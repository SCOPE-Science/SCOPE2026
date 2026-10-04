from collections import deque, defaultdict
from math import comb

def trans_dp(n,kind):
    # 0-indexed; independently transcribed from Fig.4 of arXiv:1005.0129v1.
    a=[]; b=[]
    for q in range(n):
        if q <= n-3:
            a.append(q+1); b.append(q+1)
        elif q==n-2:
            a.append(0); b.append(n-1)
        else:
            if kind=='Dp': a.append(1); b.append(0)
            else: a.append(0); b.append(1)
    return (a,b)

def act_mask(S,t):
    out=0; i=0
    while S:
        if S&1: out |= 1<<t[i]
        S >>= 1; i += 1
    return out

def poly_add(A,B):
    n=max(len(A),len(B)); C=[0]*n
    for i,x in enumerate(A): C[i]+=x
    for i,x in enumerate(B): C[i]+=x
    while len(C)>1 and C[-1]==0: C.pop()
    return C

def poly_shift(A,k=1): return [0]*k + A

def bfs_weight(n,kind):
    a,b=trans_dp(n,kind); full=(1<<n)-1
    dist={full:0}; polys={full:[1]}; q=deque([full]); first=None
    while q:
        S=q.popleft(); d=dist[S]
        if first is not None and d>=first: continue
        for letter,t in [('a',a),('b',b)]:
            T=act_mask(S,t); nd=d+1
            if T not in dist:
                dist[T]=nd; polys[T]=[]; q.append(T)
            if dist[T]==nd:
                contrib=poly_shift(polys[S]) if letter=='a' else polys[S]
                polys[T]=poly_add(polys[T],contrib) if polys[T] else contrib[:]
                if T.bit_count()==1 and first is None: first=nd
    total=[]; targets={}
    for S,d in dist.items():
        if d==first and S.bit_count()==1:
            total=poly_add(total,polys[S]) if total else polys[S][:]
            targets[S.bit_length()]=polys[S]
    return first,total,targets,len(dist)

def direct_layer(n,kind,L):
    # Independent frozenset implementation: enumerate all length-d image subsets and a-weight counts.
    a,b=trans_dp(n,kind)
    def step(S,t): return frozenset(t[i] for i in S)
    cur={frozenset(range(n)):{0:1}}
    first=None
    for d in range(1,L+1):
        nxt={}
        for S,h in cur.items():
            for is_a,t in [(1,a),(0,b)]:
                T=step(S,t); hh=nxt.setdefault(T,{})
                for k,c in h.items(): hh[k+is_a]=hh.get(k+is_a,0)+c
        cur=nxt
        if any(len(S)==1 for S in cur):
            first=d; break
    coeff={}
    targets={}
    for S,h in cur.items():
        if len(S)==1:
            target=next(iter(S))+1; targets[target]=h
            for k,c in h.items(): coeff[k]=coeff.get(k,0)+c
    out=[0]*(max(coeff)+1 if coeff else 1)
    for k,c in coeff.items():out[k]=c
    return first,out,targets

def expected(kind):
    # n=9 factorizations expanded with integer arithmetic.
    # Dp: z^8(1+z)^30(2+z)^6; Dpp: z^7(1+z)^30(1+z+z^2)^6.
    if kind=='Dp':
        p=[1]
        for _ in range(30): p=poly_add(p,poly_shift(p))
        q=[1]
        for _ in range(6):
            new=[0]*(len(q)+1)
            for i,c in enumerate(q):new[i]+=2*c;new[i+1]+=c
            q=new
        r=[0]*(len(p)+len(q)-1)
        for i,x in enumerate(p):
            for j,y in enumerate(q):r[i+j]+=x*y
        return [0]*8+r
    p=[1]
    for _ in range(30): p=poly_add(p,poly_shift(p))
    q=[1]
    for _ in range(6):
        new=[0]*(len(q)+2)
        for i,c in enumerate(q):
            new[i]+=c;new[i+1]+=c;new[i+2]+=c
        q=new
    r=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return [0]*7+r

for kind,L,target in [('Dp',58,2),('Dpp',56,1)]:
    d,p,tg,reach=bfs_weight(9,kind)
    d2,p2,tg2=direct_layer(9,kind,L)
    e=expected(kind)
    assert d==L==d2
    assert p==p2==e
    assert set(tg)=={target} and set(tg2)=={target}
    assert sum(p)==(2**30)*(3**6)==782757789696
    print(kind,'distance',d,'reachable_bfs',reach,'target',target,'count',sum(p),'degree_range',(next(i for i,c in enumerate(p) if c),len(p)-1),'coefficients',p)
print('VERIFY_OK')
