from itertools import product
from collections import Counter
from verify import rank, apply, squarezero_count

def prodm(a,b,p):
    n=len(a);m=len(b);d=len(b[0])
    return [[sum(a[i][k]*b[k][j] for k in range(m))%p for j in range(d)] for i in range(n)]

def invmat(m,p):
    n=len(m)
    a=[m[i][:]+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]%p),None)
        if pivot is None:return None
        a[j],a[pivot]=a[pivot],a[j]
        s=pow(a[j][j],-1,p)
        a[j]=[(u*s)%p for u in a[j]]
        for i in range(n):
            if i==j:continue
            t=a[i][j]
            a[i]=[(u-t*v)%p for u,v in zip(a[i],a[j])]
    return [row[n:] for row in a]

def tag(T,u,p):
    n=len(T)
    r=rank(T,p)
    if all(v==0 for v in u):return (r,'zero')
    if rank([row+[u[i]] for i,row in enumerate(T)],p)==r:return (r,'image')
    if not any(apply(T,u,p)):return (r,'kernel')
    return (r,'outside')

def test(n,p):
    GL=[]
    for vals in product(range(p),repeat=n*n):
        G=[list(vals[i*n:(i+1)*n]) for i in range(n)]
        H=invmat(G,p)
        if H is not None:GL.append((G,H))
    pairs={};count=Counter()
    for vals in product(range(p),repeat=n*n):
        T=[list(vals[i*n:(i+1)*n]) for i in range(n)]
        if any(any(row) for row in prodm(T,T,p)):continue
        for u in product(range(p),repeat=n):
            if p!=2 and any(apply(T,u,p)):continue
            t=tag(T,u,p)
            if t not in pairs:pairs[t]=(T,u)
            count[t]+=1
    for t,(T,u) in pairs.items():
        observed=set()
        for G,H in GL:
            A=prodm(prodm(G,T,p),H,p)
            v=apply(G,u,p)
            observed.add((tuple(y for row in A for y in row),v))
        assert len(observed)==count[t],(n,p,t,len(observed),count[t])
        r,kind=t
        N=squarezero_count(n,r,p)
        want={'zero':1,'image':p**r-1,'kernel':p**(n-r)-p**r,'outside':p**n-p**(n-r)}[kind]*N
        assert count[t]==want,(t,count[t],want)
    print('orbit_structure n=',n,'q=',p,'number_of_orbits=',len(pairs),'sizes=',dict(sorted(count.items())))

if __name__=='__main__':
    for n,p in [(2,2),(2,3),(3,2)]:test(n,p)
    print('ORBIT_OK')
