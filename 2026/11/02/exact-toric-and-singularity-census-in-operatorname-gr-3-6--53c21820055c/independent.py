"""Independent F2 row-space enumeration for toric rank-three positroid varieties."""
from itertools import combinations,product
from collections import Counter

def exact_binary_grassmannian(n,k):
    for piv in combinations(range(n),k):
        non=[j for j in range(n) if j not in piv]
        free=[(i,j) for i in range(k) for j in non if j>piv[i]]
        for signs in product((0,1),repeat=len(free)):
            rows=[1<<j for j in piv]
            for (i,j),bit in zip(free,signs):
                rows[i] |= bit<<j
            yield tuple(rows)

def rank3(rows,C):
    a,b,c=(sum(((row>>j)&1)<<q for q,j in enumerate(C)) for row in rows)
    # 3x3 determinant in F2 via permutation formula
    return bool(((a&1)*((b>>1&1)*(c>>2&1)^(b>>2&1)*(c>>1&1))) ^
                ((a>>1&1)*((b&1)*(c>>2&1)^(b>>2&1)*(c&1))) ^
                ((a>>2&1)*((b&1)*(c>>1&1)^(b>>1&1)*(c&1))))

def rank3_alt(rows,C):
    a=[sum(((row>>j)&1)<<q for q,j in enumerate(C)) for row in rows]
    s=0
    for i in range(3):
        if not a[i]:continue
        b=a[i]
        for j in range(i+1,3):
            if (a[j]&(-b)):
                a[j]^=b
    # use xor rank by basis dictionary
    r=0; basis={}
    for x in a:
        while x:
            h=x.bit_length()-1
            if h in basis:x^=basis[h]
            else:basis[h]=x;r+=1;break
    return r==3

def support(rows,n,k):
    if k!=3:raise ValueError
    return frozenset(C for C in combinations(range(n),k) if rank3_alt(rows,C))

def is_positroid(B,n,k):
    ns=[]
    for a in range(n):
        I=min(B,key=lambda b:tuple(sorted((j-a)%n for j in b)))
        ns.append(I)
    for C in combinations(range(n),k):
        possible=True
        for a,I in enumerate(ns):
            aa=sorted((j-a)%n for j in C)
            bb=sorted((j-a)%n for j in I)
            if any(x<y for x,y in zip(aa,bb)):
                possible=False;break
        if possible!=(C in B):return False
    return True

def dim_and_smooth(B,n):
    par=list(range(n))
    def root(x):
        while par[x]!=x:x=par[x]
        return x
    def uni(x,y):par[root(x)]=root(y)
    neigh=[]
    for C in B:
        count=0
        for x in C:
            for y in range(n):
                if y not in C and tuple(sorted((set(C)-{x})|{y})) in B:
                    count+=1;uni(x,y)
        neigh.append(count)
    d=n-len({root(x) for x in range(n)})
    return d,all(t==d for t in neigh)

if __name__=='__main__':
    n,k=6,3
    ans=Counter();allsubspaces=0;allpositroids=set()
    for R in exact_binary_grassmannian(n,k):
        allsubspaces+=1
        B=support(R,n,k)
        if is_positroid(B,n,k):
            assert B not in allpositroids
            allpositroids.add(B)
            ans[dim_and_smooth(B,n)]+=1
    assert allsubspaces==1395,allsubspaces
    assert sum(ans.values())==703
    expect={(0,True):20,(1,True):90,(2,True):180,(3,False):120,(3,True):95,(4,False):144,(4,True):6,(5,False):48}
    assert dict(ans)==expect, (ans,expect)
    print('F2_RREF_OK',allsubspaces,'binary_positroids',len(allpositroids),'dimension_smooth_distribution',dict(sorted(ans.items())))
