from itertools import product

def blocks(r,m):
    x=[str(a) for a in range(3)]
    for j in range(m):
        x=[x[a]*r + x[(a+1)%3] for a in range(3)]
    return x

def exhaustive(r,m):
    B=r+1; n=B**m
    U=blocks(r,m)
    W={U[a]+U[b] for a,b in product(range(3), repeat=2)}
    mins=10**20; maxs=-1; lengths=set(); counts=set()
    for w in W:
        prefix=[0]
        for c in w: prefix.append(prefix[-1]+(c=='0'))
        for i in range(n+1):
            v=prefix[i+n]-prefix[i]
            counts.add(v)
    return min(counts),max(counts),len(counts)

def formula(r,m):
    N=[1,0,0]; g=[]
    for j in range(m):
        g.append(max(N)-min(N))
        N=[r*N[i]+N[(i-1)%3] for i in range(3)]
    return 2+r*sum(g),N

for r in range(2,8):
    for m in range(0, 5 if r<=3 else 4):
        mn,mx,c=exhaustive(r,m)
        a,N=formula(r,m)
        print(r,m,mn,mx,c,a, 'PASS' if c==a and mx-mn+1==a else 'FAIL',flush=True)
        assert c==a and mx-mn+1==a
