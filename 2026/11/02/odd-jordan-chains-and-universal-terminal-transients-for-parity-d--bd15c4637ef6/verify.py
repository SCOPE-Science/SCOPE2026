"""Finite checks for characteristic-two edge-neighbor dynamics on trees.
Exact arithmetic and Python standard library only. Finite checks support but do
not replace the separately supplied proof for arbitrary trees.
"""
from itertools import product
from random import Random

def prufer_edges(seq):
    n=len(seq)+2
    deg=[1]*n
    for v in seq: deg[v]+=1
    edges=[]
    for v in seq:
        u=next(i for i in range(n) if deg[i]==1)
        edges.append((u,v));deg[u]-=1;deg[v]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    edges.append((u,v));return edges

def adjacency_line(n,edges):
    m=n-1; rows=[0]*m
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            if i!=j and (a==c or a==d or b==c or b==d): rows[i]|=1<<j
    return rows

def rank(rows):
    b={}
    for v in rows:
        while v:
            k=v.bit_length()-1
            if k not in b:b[k]=v;break
            v^=b[k]
    return len(b)

def matmul(a,b):
    out=[]
    for row in a:
        s=0
        while row:
            h=row & -row;s^=b[h.bit_length()-1];row^=h
        out.append(s)
    return out

def characteristic_polynomial_mod2(a):
    # Determinant of zI+A over F2[z], sign-free in characteristic two.
    m=len(a);dp={0:1}
    for i in range(m):
        nxt={}
        for mask,p in dp.items():
            for j in range(m):
                if (mask>>j)&1:continue
                # Each entry is polynomial z*[i=j] + a[i,j].
                v=(2 if i==j else 0) ^ ((a[i]>>j)&1)
                if not v:continue
                prod=0
                if v&1:prod^=p
                if v&2:prod^=p<<1
                k=mask|(1<<j)
                nxt[k]=nxt.get(k,0)^prod
        dp=nxt
    return dp.get((1<<m)-1,0)

def forest_polynomial(n,edges):
    # Matrix-forest coefficient formula, reduced mod two.
    m=len(edges);p=0
    for mask in range(1<<m):
        root=list(range(n));size=[1]*n
        def find(x):
            while root[x]!=x:x=root[x]
            return x
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                a,b=find(u),find(v)
                root[b]=a;size[a]+=size[b]
        sizes=[size[i] for i in range(n) if root[i]==i]
        if all(k%2 for k in sizes): p^=1<<(len(sizes)-1)
    return p

def apply(a,x):
    return sum((((row&x).bit_count()&1)<<i) for i,row in enumerate(a))

def verify_tree(n,edges,check_forest=True,check_orbits=True):
    m=n-1;a=adjacency_line(n,edges)
    assert rank(a)==(m if n%2 else m-1),(n,edges,'nullity')
    p=characteristic_polynomial_mod2(a) if check_forest else None
    if check_forest:assert p==forest_polynomial(n,edges),(n,edges,p)
    if n%2:
        if check_forest:assert p&1
        t=0
    else:
        assert p is not None
        t=(p & -p).bit_length()-1
        assert t%2==1
    cur=[1<<i for i in range(m)]
    for k in range(t+2 if t else 3):
        pred=m-min(k,t)
        assert rank(cur)==pred,(n,edges,k,rank(cur),pred)
        cur=matmul(cur,a)
    if check_orbits and m<=7:
        counts=[0]*(t+1)
        for x in range(1<<m):
            seen={};y=x;step=0
            while y not in seen:
                seen[y]=step;step+=1;y=apply(a,y)
            tau=seen[y]
            assert tau<=t
            counts[tau]+=1
        target=([1<<m] if t==0 else [1<<(m-t)]+[1<<(m-t+j-1) for j in range(1,t+1)])
        assert counts==target,(n,edges,counts,target)
    return t

def main():
    tested=0; dist={}
    for n in range(2,7):
        for seq in product(range(n),repeat=n-2):
            t=verify_tree(n,prufer_edges(seq))
            dist[(n,t)]=dist.get((n,t),0)+1;tested+=1
    rng=Random(1979)
    for n in (7,8,9,10,12,14):
        for _ in range(35):
            seq=[rng.randrange(n) for _ in range(n-2)]
            t=verify_tree(n,prufer_edges(seq),check_forest=True,check_orbits=n<=8)
            dist[(n,t)]=dist.get((n,t),0)+1;tested+=1
    for n in (4,8,16,32,64):
        path=[(i,i+1) for i in range(n-1)]
        star=[(0,i) for i in range(1,n)]
        # Large cases: char polynomial via path recurrence in the proof,
        # here only ranks and powers are independently computed.
        for edges,t in ((path,n-1),(star,1)):
            a=adjacency_line(n,edges);cur=[1<<i for i in range(n-1)]
            for k in range(t+2):
                assert rank(cur)==(n-1)-min(k,t),(n,k)
                cur=matmul(cur,a)
            tested+=1
    print('trees checked:',tested)
    print('small n nilpotent-size frequency:',sorted((k,v) for k,v in dist.items() if k[0]<=6))
    print('LINE_TREE_EDGE_XOR_VERIFY_OK')
if __name__=='__main__':main()
