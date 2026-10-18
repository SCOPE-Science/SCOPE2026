"""Direct exhaustive subalgebra and permutability checks for examples."""
from itertools import combinations, product
from math import prod

def rref(rows,q):
    if not rows:return ()
    a=[list(int(y)%q for y in x) for x in rows]
    nc=len(a[0]); i=0
    for j in range(nc):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        inv=pow(a[i][j],-1,q)
        a[i]=[(z*inv)%q for z in a[i]]
        for k in range(len(a)):
            if k!=i and a[k][j]:
                c=a[k][j]
                a[k]=[(u-c*v)%q for u,v in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return tuple(tuple(z for z in row) for row in a[:i])

def subspaces(n,q):
    for k in range(n+1):
        for pivots in combinations(range(n),k):
            free=[(i,j) for i in range(k) for j in range(pivots[i]+1,n) if j not in pivots]
            for values in product(range(q),repeat=len(free)):
                m=[[0]*n for _ in range(k)]
                for i,p in enumerate(pivots):m[i][p]=1
                for (i,j),v in zip(free,values):m[i][j]=v
                yield tuple(tuple(row) for row in m)

def brackets(v,w,A,q):
    t,u=v[0],v[1:]; s,z=w[0],w[1:]
    return (0,)+tuple((t*sum(A[i][j]*z[j] for j in range(len(u)))-s*sum(A[i][j]*u[j] for j in range(len(u))))%q for i in range(len(u)))

def build(dims,q,blocks):
    n=sum(dims); A=[[0]*n for _ in range(n)]; p=0
    for m in blocks:
        for i in range(len(m)):
            for j in range(len(m)): A[p+i][p+j]=m[i][j]
        p+=len(m)
    all_subspaces=[tuple((0,)+row for row in U) for U in subspaces(n,q)]
    outs=[]
    for mask in range(1<<len(dims)):
        inside=[];outside=[]; pos=0
        for i,d in enumerate(dims):
            (inside if (mask>>i)&1 else outside).extend(range(pos,pos+d))
            pos+=d
        for tup in product(range(q),repeat=len(outside)):
            u=[0]*n
            for j,v in zip(outside,tup):u[j]=v
            B=[(0,)+tuple(int(j==k) for j in range(n)) for k in inside]
            outs.append(tuple(B+[(1,)+tuple(u)]))
    return A,all_subspaces,outs

def permutes(B,C,A,q):
    span=rref(B+C,q)
    for b in B:
        for c in C:
            if len(rref(span+(brackets(b,c,A,q),),q))!=len(span):return False
    return True

def gauss(n,k,q):
    if k>n or k<0:return 0
    ans=1
    for i in range(k):ans=ans*(q**(n-i)-1)//(q**(i+1)-1) if False else ans
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def formula(dims,q):
    d=sum(dims);r=len(dims);G=sum(gauss(d,k,q) for k in range(d+1))
    Q=prod(1+q**j for j in dims)
    count=G*G+prod(1+3*q**j for j in dims)
    for mask in range(1<<r):
        a=sum(dims[i] for i in range(r) if (mask>>i)&1)
        cc=0
        for tmask in range(1<<r):
            if mask&tmask:continue
            b=sum(dims[i] for i in range(r) if (tmask>>i)&1)
            cc+=sum(gauss(a,k,q)*q**(b*(a-k)) for k in range(a+1))
        count+=2*q**(d-a)*cc
    return G,Q,G+Q,count

if __name__=='__main__':
    tests=[(2,[2],[[[0,1],[1,1]]]), # x²+x+1 irreducible over F2
           (2,[3],[[[0,0,1],[1,0,1],[0,1,0]]]), # x³+x+1 F2
           (3,[2],[[[0,2],[1,0]]]),
           (3,[2,2],[[[0,2],[1,0]],[[0,1],[1,2]]]),
           (2,[2,3],[[[0,1],[1,1]],[[0,0,1],[1,0,1],[0,1,0]]])]
    for q,dims,blocks in tests:
        A,V,X=build(dims,q,blocks)
        g,Q,N,P=formula(dims,q)
        print('CASE',q,dims,'G=',g,'Q=',Q,'N=',N,'predicted_pairs=',P,'actual_subspaces=',len(V)+len(X),flush=True)
        assert len(V)+len(X)==N
        allsub=V+X
        # Subalgebra check
        for B in allsub:
            assert all(len(rref(B+(brackets(a,b,A,q),),q))==len(B) for a in B for b in B)
        count=sum(int(permutes(B,C,A,q)) for B in allsub for C in allsub)
        print('actual_pairs=',count,'MATCH=',count==P,flush=True)
        assert count==P
    print('VERIFY_OK')
