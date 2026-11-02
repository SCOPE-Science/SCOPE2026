from math import comb
from collections import Counter

def te(n): return n*(n-1)*(n-2)//6

def legendre(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def square_roots_count(z,p,h):
    if h==0: return 1
    mod=p**h; z%=mod
    if z==0:return p**(h//2)
    v=0
    while z%p==0: z//=p;v+=1
    if v%2: return 0
    return 2*(p**(v//2)) if legendre(z,p)==1 else 0

def critical_alpha(p,k,base):
    # root of 3*a*a=1 modulo p^k; exact Hensel iteration
    a=base
    for j in range(1,k):
        mod=p**(j+1)
        a=(a+(-((3*a*a-1)//(p**j))*pow(6*a,-1,p)%p)*p**j)%mod
    return a

def predicted_fibers(p,k):
    m=p**k
    if p==2:
        return [3 if y==0 else 1 for y in range(2)] if k==1 else [5 if y%4==0 else 1 for y in range(m)]
    if p==3:return [3]*m
    inv6=pow(6,-1,p)
    base=[((x*(x-1)*(x-2))*inv6)%p for x in range(p)]
    regular=Counter(base[x] for x in range(p) if (3*(x-1)**2-1)%p!=0)
    crit=[x for x in range(p) if (3*(x-1)**2-1)%p==0]
    out=[regular[y%p] for y in range(m)]
    for x in crit:
        a=critical_alpha(p,k,(x-1)%p)
        v=(-a*pow(9,-1,m))%m
        c=(a*pow(2,-1,m))%m
        for y in range(v%p,m,p):
            if k==1:out[y]+=1
            elif (y-v)%(p*p)==0:
                u=((y-v)//(p*p)*pow(c,-1,p**(k-2)))%(p**(k-2)) if k>2 else 0
                out[y]+=p*square_roots_count(u,p,k-2)
    return out

def direct_fibers(p,k):
    m=p**k
    period=m*(p if p in (2,3) else 1)
    cnt=[0]*m
    for n in range(period): cnt[te(n)%m]+=1
    return cnt

def check():
    total=0; levels=0
    for p in [2,3,5,7,11,13,17,19,23,29,31]:
        for k in range(1,13):
            if p**k>35000:break
            got=direct_fibers(p,k);pred=predicted_fibers(p,k)
            assert got==pred, (p,k,[(i,x,y) for i,(x,y) in enumerate(zip(got,pred)) if x!=y][:10])
            m=p**k
            if p>=5:
                chi=legendre(-3,p)
                assert sum(1 for r in got if r>0)==m*((2*p+chi)//3)//p
            else:assert all(got)
            print('LEVEL_OK',p,k,m,'image',sum(c>0 for c in got),'fiber_histogram',sorted(Counter(got).items()))
            total+=m;levels+=1
    for m in [6,12,15,18,20,24,30,35,45,55,63,72,75,88,99,100,126,135,245,264,315,330,420,525,594,625,990]:
        factor=[]; z=m;d=2
        while d*d<=z:
            if z%d==0:
                k=0
                while z%d==0:z//=d;k+=1
                factor.append((d,k))
            d+=1
        if z>1: factor.append((z,1))
        period=1
        pred={}
        for p,k in factor:
            period*=p**k*(p if p in(2,3) else 1)
            pred[(p,k)]=predicted_fibers(p,k)
        got=Counter(te(n)%m for n in range(period))
        for y in range(m):
            ans=1
            for (p,k),v in pred.items(): ans*=v[y%(p**k)]
            assert got[y]==ans,(m,y,got[y],ans)
        print('CRT_OK',m,period,'image',len(got))
    print('VERIFY_OK',total,levels)
if __name__=='__main__':check()
