from itertools import product
from math import comb
from collections import Counter

def direct(m,n):
    v=m*n; adj=[]
    for i in range(v):
        adj.append(sum(1<<j for j in range(v) if j!=i and (j//n==i//n or j%n==i%n)))
    p=Counter();cp=Counter(); rounds=Counter()
    for s in range(1,1<<v):
        k=s.bit_count()
        obs=s
        for i in range(v):
            if s>>i&1: obs|=adj[i]
        rounds_t=0
        while obs!=(1<<v)-1:
            new=obs
            for i in range(v):
                if obs>>i&1:
                    unseen=adj[i]&~obs
                    if unseen and unseen&(unseen-1)==0: new|=unseen
            if new==obs:break
            obs=new;rounds_t+=1
        if obs==(1<<v)-1:
            p[k]+=1; rounds[rounds_t]+=1
            reached=(s&-s);front=reached
            while front:
                new=0
                b=front
                while b:
                    vbit=b&-b; b-=vbit
                    idx=vbit.bit_length()-1
                    new|=adj[idx]&s&~reached
                front=new;reached|=front
            if reached==s:cp[k]+=1
    return p,cp,rounds

def full_occupied(r,c,zpolymax):
    # polynomial via choose occupied row and col subset
    coeff=[0]*(zpolymax+1)
    for i in range(r+1):
        for j in range(c+1):
            sgn=(-1)**(i+j)*comb(r,i)*comb(c,j)
            q=(r-i)*(c-j)
            for k in range(q+1):coeff[k]+=sgn*comb(q,k)
    return coeff

def closed(m,n):
    out=[comb(m*n,k) for k in range(m*n+1)]
    for r in range(m-1):
        for c in range(n-1):
            k0=full_occupied(r,c,m*n)
            for k in range(m*n+1):out[k]-=comb(m,r)*comb(n,c)*k0[k]
    return Counter({k:v for k,v in enumerate(out) if v})

for m,n in [(2,2),(2,3),(2,4),(2,6),(3,3),(3,4),(3,5),(4,4)]:
    p,c,r=direct(m,n)
    model=closed(m,n)
    assert p==model,(m,n,p,model)
    d=min(m,n)-1
    expected=(m*n**(m-1) if m<n else (2*m*m**(m-1)-m*m*__import__('math').factorial(m-1)))
    assert p[d]==expected,(m,n,expected,p[d])
    cexp=m*n if m<n else (4 if m==2 else 2*m*m)
    assert c[d]==cexp,(m,n,cexp,c[d])
    print('OK',m,n,'P',dict(p),'C',dict(c),'rounds',dict(r))
print('VERIFY_OK')

def cpoly(m,n):
    # connected spanning subgraphs of K_{r,c} weighted by selected edges
    # recurrence via component of the first left vertex
    B={}
    for r in range(1,m+1):
        for c in range(n+1):
            d=r*c; out=[comb(d,k) for k in range(d+1)]
            for i in range(1,r+1):
                for j in range(c+1):
                    if (i,j)==(r,c): continue
                    if (i,j) not in B:continue
                    w=comb(r-1,i-1)*comb(c,j)
                    for a,u in enumerate(B[i,j]):
                        if not u:continue
                        for b in range((r-i)*(c-j)+1):
                            out[a+b]-=w*u*comb((r-i)*(c-j),b)
            B[r,c]=out
    ret=Counter()
    for r in range(max(1,m-1),m+1):
        for c in range(1,n+1):
            w=comb(m,r)*comb(n,c)
            for k,v in enumerate(B[r,c]):
                if v:ret[k]+=w*v
    for r in range(1,m-1):
        for c in range(max(1,n-1),n+1):
            w=comb(m,r)*comb(n,c)
            for k,v in enumerate(B[r,c]):
                if v:ret[k]+=w*v
    return +ret

for m,n in [(2,2),(2,3),(3,3),(3,4),(3,5),(4,4)]:
    _,real,_=direct(m,n)
    predicted=cpoly(m,n)
    assert real==predicted,(m,n,real,predicted)
    print('CONNECTED_OK',m,n)
