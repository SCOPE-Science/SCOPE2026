"""Independent direct finite-field multiplication-matrix verification.
Run: python verify.py
"""
from collections import Counter
from itertools import product


def mul(a,b,q):
    if q==4:
        # GF(4) = GF(2)[h]/(h^2+h+1), binary basis 1,h
        x=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:
                    d=i+j
                    x ^= 1<<d if d<2 else 3
        return x
    return (a*b)%q


def inv(a,q):
    return next(b for b in range(1,q) if mul(a,b,q)==1)


def add(a,b,q):
    return a^b if q==4 else (a+b)%q


def neg(a,q):
    return a if q==4 else (-a)%q


def rank(rows,q):
    rows=[r[:] for r in rows]
    nr=len(rows); nc=len(rows[0]) if rows else 0; k=0
    for j in range(nc):
        pivot=next((i for i in range(k,nr) if rows[i][j]),None)
        if pivot is None: continue
        rows[k],rows[pivot]=rows[pivot],rows[k]
        u=inv(rows[k][j],q)
        rows[k]=[mul(u,v,q) for v in rows[k]]
        for i in range(nr):
            if i!=k and rows[i][j]:
                s=rows[i][j]
                rows[i]=[add(a,neg(mul(s,b,q),q),q) for a,b in zip(rows[i],rows[k])]
        k+=1
        if k==nr: break
    return k


def graph_nullity(n,edges,S,p):
    outside=set(range(n))-S
    z=sum(all(i not in S for i in nbrs) for v,nbrs in enumerate([[j for i,j in edges if i==v]+[i for i,j in edges if j==v] for v in range(n)]) if v in outside)
    seen=set(); c=0
    for v in S:
        if v in seen:continue
        seen.add(v); stack=[v]; col={v:0}; bip=True
        while stack:
            x=stack.pop()
            for a,b in edges:
                if x==a:y=b
                elif x==b:y=a
                else: continue
                if y not in S:continue
                if y not in col:
                    col[y]=col[x]^1;seen.add(y);stack.append(y)
                elif col[y]==col[x]:bip=False
        if p==2 or bip:c+=1
    return z+c


def predicted(n,edges,q):
    m=len(edges); d=1+n+m
    P=Counter({0:1,1:q**m-1,d:(q-1)*q**(n+m)})
    p=2 if q==4 else q
    for mask in range(1,1<<n):
        S={i for i in range(n) if mask>>i&1}
        r=1+n-graph_nullity(n,edges,S,p)
        P[r]+=(q**m)*(q-1)**len(S)
    return +P


def actual(n,edges,q):
    m=len(edges); d=1+n+m
    cnt=Counter()
    for values in product(range(q),repeat=d):
        a=values[0];v=values[1:n+1];w=values[n+1:]
        # M_values columns = product with unit, n linear basis, and m quadratic basis.
        cols=[list(values)]
        for j in range(n):
            col=[0]*d
            col[1+j]=a
            for k,(i,h) in enumerate(edges):
                if j==i:col[1+n+k]=v[h]
                if j==h:col[1+n+k]=v[i]
            cols.append(col)
        for k in range(m):
            col=[0]*d;col[n+1+k]=a;cols.append(col)
        rows=[list(c) for c in zip(*cols)]
        cnt[rank(rows,q)]+=1
    return +cnt


def transfer_trace(n,t,z):
    M=[[z,1,0,0],[0,0,t*z,t*z],[1,1,0,0],[0,0,t,t]]
    P=[[int(i==j) for j in range(4)] for i in range(4)]
    for _ in range(n):
        P=[[sum(P[i][k]*M[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    return sum(P[i][i] for i in range(4))


def cycle_by_subset(n,t,z,p):
    E=[(i,(i+1)%n) for i in range(n)]
    tot=0
    for mask in range(1<<n):
        S={i for i in range(n) if mask>>i&1}
        tot+=t**len(S)*z**graph_nullity(n,E,S,p)
    return tot


def main():
    cases=[
        (2,[(0,1)],2), (3,[(0,1),(1,2)],3),
        (3,[(0,1),(1,2),(2,0)],2),
        (3,[(0,1),(1,2),(2,0)],3),
        (3,[(0,1),(1,2),(2,0)],4),
        (4,[(0,1),(1,2),(2,3),(3,0)],2),
        (4,[(0,1),(1,2),(2,3),(3,0)],3),
        (4,[(0,1),(1,2),(2,3),(3,0),(0,2),(1,3)],2),
        (5,[(0,1),(1,2),(2,0),(3,4)],2),
        (3,[],4),
    ]
    for n,E,q in cases:
        a=actual(n,E,q);b=predicted(n,E,q)
        assert a==b,(n,E,q,a,b)
        assert sum(a.values())==q**(1+n+len(E))
        print('CASE_OK',n,E,q,sorted(a.items()))
    for n in range(3,9):
        for p in [2,3]:
            for t,z in [(2,3),(4,2),(1,5)]:
                b=1 if (p==2 or n%2==0) else 0
                expected=transfer_trace(n,t,z)+t**n*(z**b-1)
                actualval=cycle_by_subset(n,t,z,p)
                assert expected==actualval,(n,p,t,z,expected,actualval)
        print('TRANSFER_OK',n)
    print('VERIFY_OK')

if __name__=='__main__':main()
