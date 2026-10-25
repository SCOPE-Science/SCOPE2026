"""Exact test of 3-state P3-convex enumerator on cactus block cycles."""
def add(a,b):
    n=max(len(a),len(b)); return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b): c[i+j]+=x*y
    return tuple(c)
ONE=(1,)
ZERO=(0,)
Z=(0,1)

def combo(pairs):
    """Returns (product a_i, sum_i b_i product_(j!=i)a_j) without division."""
    p,q=ONE,ZERO
    for a,b in pairs:
        p,q=mul(p,a),add(mul(q,a),mul(p,b))
    return p,q

import random

def cactus_dp(n, blocks):
    inc=[[] for _ in range(n+len(blocks))]
    for k,B in enumerate(blocks):
        for v in B:
            inc[v].append(n+k);inc[n+k].append(v)
    parent=[-2]*len(inc);parent[0]=-1;order=[0]
    for x in order:
        for y in inc[x]:
            if parent[y]==-2:parent[y]=x;order.append(y)
            elif y!=parent[x]:raise AssertionError('not tree')
    assert len(order)==len(inc)
    states={}
    for x in reversed(order):
        if x<n:
            child=[y for y in inc[x] if y!=parent[x]]
            black=Z
            for y in child:black=mul(black,states[y][0])
            a,b=combo((states[y][1],states[y][2]) for y in child)
            states[x]=(black,a,b)
        else:
            verts=list(blocks[x-n]);v=parent[x]
            i=verts.index(v);verts=verts[i:]+verts[:i]
            if len(verts)==2:
                child=verts[1];X,Y0,Y1=states[child]
                states[x]=(add(X,Y0),add(Y0,Y1),X)
                continue
            L=len(verts); out=[ZERO,ZERO,ZERO]
            for vc in (0,1):
                for c1 in (0,1):
                    dp={(vc,c1):ONE}
                    for pos in range(2,L):
                        nd={}
                        for (a,b),val in dp.items():
                            for c in (0,1):
                                X,Y0,Y1=states[verts[pos-1]]
                                weight=X if b else ((add(Y0,Y1)) if a+c==0 else (Y0 if a+c==1 else ZERO))
                                key=(b,c)
                                nd[key]=add(nd.get(key,ZERO),mul(val,weight))
                        dp=nd
                    for (a,b),val in dp.items():
                        X,Y0,Y1=states[verts[-1]]
                        weight=X if b else ((add(Y0,Y1)) if a+vc==0 else (Y0 if a+vc==1 else ZERO))
                        k=c1+b
                        if not vc and k>1:continue
                        j=0 if vc else 1+k
                        out[j]=add(out[j],mul(val,weight))
            states[x]=tuple(out)
    X,Y0,Y1=states[0]
    return add(add(X,Y0),Y1)

def brute_cactus(n,blocks):
    from itertools import combinations
    adj=[0]*n
    for B in blocks:
        edges=[tuple(B)] if len(B)==2 else [(B[i],B[(i+1)%len(B)]) for i in range(len(B))]
        for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    out=[0]*(n+1)
    for s in range(1<<n):
        if all((adj[v]&s).bit_count()<=1 for v in range(n) if not(s>>v&1)):
            out[s.bit_count()]+=1
    return tuple(out)

def sample(n,rng):
    v=1;blocks=[]
    while v<n:
        a=rng.randrange(v);k=rng.randint(1,min(n-v,5))
        blocks.append((a,*range(v,v+k)));v+=k
    return v,blocks

def tests():
    rng=random.Random(260318);ct=0
    for n in range(2,14):
        for trial in range(100):
            m,blocks=sample(n,rng)
            assert cactus_dp(m,blocks)==brute_cactus(m,blocks),(m,blocks,cactus_dp(m,blocks),brute_cactus(m,blocks))
            ct+=1
    for n in range(3,14):
        b=[tuple(range(n))]
        assert cactus_dp(n,b)==brute_cactus(n,b)
        ct+=1
    print('VERIFY_OK',ct,'independent complete subset tests (cactus graphs up to n=13)')
    print('CYCLE_7',cactus_dp(7,[tuple(range(7))]))
    print('TRIANGLE_CHAIN_7',cactus_dp(7,[(0,1,2),(2,3,4),(4,5,6)]))
if __name__=='__main__':tests()
