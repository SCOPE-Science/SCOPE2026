"""Finite subspace enumeration and large-rank diagnostics for two-step free Lie algebras.
This script checks finite examples; the unrestricted result relies on a separate proof."""
from itertools import combinations, product
from math import comb

def qbin(n,k,q):
    if not 0<=k<=n: return 0
    num=1;den=1
    for j in range(k):
        num*=q**(n-j)-1
        den*=q**(k-j)-1
    assert num%den==0
    return num//den

def predicted(d,q):
    N=comb(d,2)
    by_dimension=[0]*(d+N+1)
    by_projection=[0]*(d+1)
    for a in range(d+1):
        M=comb(d-a,2)
        for b in range(M+1):
            v=qbin(d,a,q)*qbin(M,b,q)*q**(a*(M-b))
            by_dimension[a+N-M+b]+=v
            by_projection[a]+=v
    return by_dimension,by_projection

def rows_rref(n,r,q):
    for pivots in combinations(range(n),r):
        piv=set(pivots)
        free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in piv]
        for values in product(range(q),repeat=len(free)):
            basis=[[0]*n for _ in range(r)]
            for i,p in enumerate(pivots): basis[i][p]=1
            for (i,j),value in zip(free,values): basis[i][j]=value
            yield pivots,basis

def contains(pivots,basis,x,q):
    x=x[:]
    for i,p in enumerate(pivots):
        v=x[p]
        if v:
            for j in range(p,len(x)):
                x[j]=(x[j]-v*basis[i][j])%q
    return not any(x)

def observed(d,q):
    n=d+comb(d,2)
    wedge={p:i for i,p in enumerate(combinations(range(d),2))}
    by_dimension=[0]*(n+1)
    by_projection=[0]*(d+1)
    total_checked=0
    for r in range(n+1):
        for piv,basis in rows_rref(n,r,q):
            total_checked+=1
            isideal=True
            for row in basis:
                for j in range(d):
                    v=[0]*n
                    for i in range(d):
                        if i==j:continue
                        k,l=sorted((i,j))
                        v[d+wedge[(k,l)]]=(v[d+wedge[(k,l)]]+row[i]*(1 if i<j else -1))%q
                    if not contains(piv,basis,v,q):
                        isideal=False;break
                if not isideal:break
            if isideal:
                by_dimension[r]+=1
                proj=[row[:d] for row in basis]
                pv=[]
                for row in proj:
                    v=row[:]
                    for b in pv:
                        p=next(i for i,x in enumerate(b) if x)
                        if v[p]:
                            factor=v[p]
                            v=[(x-factor*y)%q for x,y in zip(v,b)]
                    if any(v):
                        p=next(i for i,x in enumerate(v) if x)
                        inv=pow(v[p],-1,q)
                        pv.append([(x*inv)%q for x in v])
                        pv.sort(key=lambda x:next(i for i,v in enumerate(x) if v))
                by_projection[len(pv)]+=1
    return by_dimension,by_projection,total_checked

def diagnostic(q,ds=(4,5,6,7,8,9,10,11,12)):
    from math import log
    theta0=sum(q**(-j*j) for j in range(-12,13))
    thetah=sum(q**(-(j+.5)**2) for j in range(-12,13))
    for d in ds:
        n=comb(d,2); m=comb(d-1,2)
        _,p=predicted(d,q)
        ratio=sum(p[1:])/sum(p)
        e=-d**3/4+d*d-d/2
        theta=lambda k:theta0 if k%2==0 else thetah
        asym=q**e *theta(m+1)/((1-q**-1)*theta(n))
        print('ASYM',q,d,'P_noncentral',f'{ratio:.9g}','asym',f'{asym:.9g}', 'ratio',f'{ratio/asym:.9g}', 'cond_a1',f'{p[1]/sum(p[1:]):.9g}')

if __name__=='__main__':
    for d,q in [(2,2),(2,3),(3,2),(3,3)]:
        expected=predicted(d,q)
        empirical=observed(d,q)
        assert empirical[:2]==expected,(d,q,empirical,expected)
        print('EXHAUSTIVE_OK',d,q,'subspaces',empirical[2], 'ideals',sum(expected[0]), 'dims',expected[0], 'proj',expected[1])
    diagnostic(2)
    diagnostic(3,range(4,11))
    print('VERIFY_OK')
