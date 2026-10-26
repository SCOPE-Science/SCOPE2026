"""Exhaustive rank-one Rota--Baxter operator checks for finite quiver algebras."""
from itertools import product
from math import comb

def algebra(n,edges):
    d=n+len(edges); mul=[[None]*d for _ in range(d)]
    for i in range(n): mul[i][i]=i
    for j,(s,t) in enumerate(edges,n):
        mul[s][j]=j
        mul[j][t]=j
    return mul

def add(x,y,q):
    return x ^ y if q==4 else (x+y)%q

def mult(x,y,q):
    if q!=4:return x*y%q
    out=0
    for j in range(2):
        if (y>>j)&1:out^=x<<j
    if out&8:out^=0b1110  # reduce x^3=(x+1)x
    if out&4:out^=0b111   # reduce x^2=x+1
    return out

def field_sum(seq,q):
    out=0
    for x in seq:out=add(out,x,q)
    return out

def times(a,b,mul,q):
    d=len(a); out=[0]*d
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            k=mul[i][j]
            if k is not None and y:out[k]=add(out[k],mult(x,y,q),q)
    return tuple(out)

def exact_count(n,edges,q):
    d=n+len(edges); m=algebra(n,edges)
    f_set=[]
    for f in product(range(q),repeat=d):
        if not any(f):continue
        first=next(x for x in f if x)
        if first!=1:continue  # first nonzero f coefficient is 1
        f_set.append(f)
    nonzero=[x for x in product(range(q),repeat=d) if any(x)]
    answer=0
    for a in nonzero:
        asq=times(a,a,m,q)
        left=[];right=[]
        for j in range(d):
            ej=tuple(int(i==j) for i in range(d))
            left.append(times(a,ej,m,q))
            right.append(times(ej,a,m,q))
        for f in f_set:
            p=[field_sum((mult(f[k],left[j][k],q) for k in range(d)),q) for j in range(d)]
            r=[field_sum((mult(f[k],right[i][k],q) for k in range(d)),q) for i in range(d)]
            ok=True
            for i in range(d):
                if not ok:break
                for j in range(d):
                    c=mult(f[i],f[j],q)
                    x=add(mult(f[i],p[j],q),mult(f[j],r[i],q),q)
                    if any(add(mult(c,asq[k],q),(-mult(x,a[k],q) if q!=4 else mult(x,a[k],q))%q,q) for k in range(d)):
                        ok=False;break
            if ok:answer+=1
    return answer

def gf_rank_support(n,edges,S):
    # Rank of the unsigned bipartite incidence matrix: source vertices and target vertices separate.
    parent=list(range(2*n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(x,y):
        a,b=find(x),find(y)
        if a!=b:parent[a]=b;return 1
        return 0
    rank=0
    for j,(s,t) in enumerate(edges):
        if (S>>j)&1:rank+=union(s,n+t)
    return rank

def prediction(n,edges,q):
    d=n+len(edges);m=len(edges)
    numerator=0
    for S in range(1,1<<m):
        k=S.bit_count();r=gf_rank_support(n,edges,S)
        numerator+=(q-1)**k*(q**(d-r)-1)
    assert numerator%(q-1)==0
    nil=numerator//(q-1)
    idem=0
    for B in range(1<<n):
        u=v=0
        for s,t in edges:
            bs=(B>>s)&1;bt=(B>>t)&1
            if bs and not bt:u+=1
            if bt and not bs:v+=1
        idem+=q**(u+v)*(q**u+q**v-2)
    return nil+idem,nil,idem

def f_poly(n,a,b):
    if n==1:return 2
    p,c=2,2+a+b
    for i in range(3,n+1):p,c=c,2*c+(a*b-1)*p
    return c

def path_formula(n,q):
    e=n-1
    nil=(q**n*(2*q-1)**e -q**(n+e)-q**e+1)//(q-1)
    idem=2*(f_poly(n,q*q,q)-f_poly(n,q,q))
    return nil+idem,nil,idem

def main():
    cases=[(2,[(0,1)],2),(2,[(0,1)],3),(2,[(0,1)],4),
           (3,[(0,1),(1,2)],2),(3,[(0,1),(1,2)],3),(3,[(0,1),(0,2)],3),
           (4,[(0,1),(1,2),(2,3)],2),
           (3,[(0,1),(0,2)],2),
           (3,[(0,1),(1,2),(0,2)],2),
           (2,[(0,1),(0,1)],2),
           (2,[(0,0),(0,1)],2),
           (1,[(0,0)],2),
           (2,[(0,0),(0,1),(1,0),(1,1)],2)]
    for n,edges,q in cases:
        p=prediction(n,edges,q)
        actual=exact_count(n,edges,q)
        assert p[0]==actual,(n,edges,q,actual,p)
        if edges==[(i,i+1) for i in range(n-1)]:
            assert p==path_formula(n,q),(n,q,p,path_formula(n,q))
        print('CHECK',n,edges,q,'count',actual,'nil',p[1],'idem',p[2])
    print('RANK_ONE_QUIVER_RB_OK',len(cases))
if __name__=='__main__':main()
