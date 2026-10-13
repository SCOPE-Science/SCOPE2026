"""Exact finite-field rank census for complete tripartite alternating matrix spaces."""
from collections import Counter
from itertools import product
from math import prod


def gaussian(n,k,q):
    if k<0 or k>n: return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))

def matrices_rank(m,n,k,q):
    if k<0 or k>min(m,n):return 0
    return prod((q**m-q**i)*(q**n-q**i) for i in range(k))//prod(q**k-q**i for i in range(k))

def iso(r,h,q):
    if h<0 or h>r:return 0
    return prod(q**(2*(r-i))-1 for i in range(h))//prod(q**(h-i)-1 for i in range(h))

def surj(d,k,q):
    return prod(q**d-q**i for i in range(k)) if k<=d else 0

def pullback(r,d,q):
    """Rank distribution of T^t J_(2r) T, T uniform in Mat_(2r,d)."""
    ans=Counter()
    for k in range(min(2*r,d)+1):
        for j in range(k//2+1):
            h=k-2*j
            if h>r or j>r-h:continue
            nsub=iso(r,h,q)*q**(2*j*(r-h-j))*gaussian(r-h,j,q*q)
            ans[2*j]+=nsub*surj(d,k,q)
    assert sum(ans.values())==q**(2*r*d),(r,d,q,ans)
    return ans

def formula(a,b,c,q):
    ans=Counter()
    for r in range(min(a,b)+1):
        d=a+b-2*r
        for s in range(min(d,c)+1):
            mult=matrices_rank(a,b,r,q)*matrices_rank(d,c,s,q)*q**(2*r*s)
            for t,count in pullback(r,c-s,q).items():
                ans[2*r+2*s+t]+=mult*count
    assert sum(ans.values())==q**(a*b+a*c+b*c),(a,b,c,q,ans)
    return ans

def field(q):
    if q in (2,3,5):
        return lambda x,y:(x+y)%q,lambda x,y:(x*y)%q,lambda x:pow(x,q-2,q)
    if q==4:
        def mul(x,y):
            v=0
            for i in range(2):
                if (y>>i)&1:v^=x<<i
            if v&4:v^=0b111
            return v
        return lambda x,y:x^y, mul, lambda x:next(y for y in range(1,4) if mul(x,y)==1)
    raise ValueError(q)

def rank(M,q):
    add,mul,inv=field(q)
    n=len(M); M=[row[:] for row in M];r=0
    for col in range(n):
        pivot=next((i for i in range(r,n) if M[i][col]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        pivinv=inv(M[r][col]);M[r]=[mul(x,pivinv) for x in M[r]]
        for i in range(r+1,n):
            coeff=M[i][col]
            if coeff:M[i]=[add(x,mul(coeff,y)) if q==4 or q==2 else (x-coeff*y)%q for x,y in zip(M[i],M[r])]
        r+=1
        if r==n:break
    return r

def exhaustive(a,b,c,q):
    parts=[a,b,c];n=sum(parts)
    edges=[];groups=[[i for i in range(sum(parts[:j]),sum(parts[:j+1]))] for j in range(3)]
    for j in range(3):
        for k in range(j+1,3):
            for x in groups[j]:
                for y in groups[k]:edges.append((x,y))
    # Signed entries; in characteristic two subtraction is addition.
    out=Counter()
    for values in product(range(q),repeat=len(edges)):
        A=[[0]*n for _ in range(n)]
        for (i,j),v in zip(edges,values):
            A[i][j]=v;A[j][i]=v if q%2==0 else (-v)%q
        out[rank(A,q)]+=1
    return out

def direct_pullback(r,d,q):
    """Independently enumerate alternating Gram ranks of linear maps."""
    add,mul,_=field(q)
    def negate(x): return x if q%2==0 else (-x)%q
    out=Counter()
    for entries in product(range(q),repeat=2*r*d):
        T=[list(entries[i*d:(i+1)*d]) for i in range(2*r)]
        G=[[0]*d for _ in range(d)]
        for i in range(d):
            for j in range(i+1,d):
                total=0
                for z in range(r):
                    a,b=T[2*z],T[2*z+1]
                    first=mul(a[i],b[j])
                    second=mul(b[i],a[j])
                    total=add(total,add(first,negate(second)))
                G[i][j]=total
                G[j][i]=negate(total)
        out[rank(G,q)]+=1
    return out

def run():
    cases=[(2,1,1,1),(2,1,1,2),(2,1,2,2),(2,2,2,2),(2,2,2,3),
           (3,1,1,1),(3,1,1,2),(3,1,2,2),(3,2,2,2),
           (4,1,1,1),(4,1,1,2),(4,1,2,2)]
    for q,a,b,c in cases:
        f=formula(a,b,c,q);e=exhaustive(a,b,c,q)
        assert f==e,(q,a,b,c,f,e)
        print('PASS q=%s parts=%s,%s,%s edges=%s ranks=%s'%(q,a,b,c,a*b+a*c+b*c,dict(sorted(f.items()))))
    for q in (2,3,4,5,7):
        for r in range(5):
            for d in range(5):pullback(r,d,q)
    pull_cases=[(q,1,d) for q in (2,3,4) for d in (1,2)]+[(2,2,2),(3,2,2)]
    for q,r,d in pull_cases:
        exact=direct_pullback(r,d,q)
        assert exact==pullback(r,d,q),(q,r,d,exact,pullback(r,d,q))
    print('EXHAUSTIVE_CASES',len(cases),'DIRECT_PULLBACK_CASES',len(pull_cases),'PULLBACK_CHECKS',5*25,'VERIFY_OK')
if __name__=='__main__':run()
