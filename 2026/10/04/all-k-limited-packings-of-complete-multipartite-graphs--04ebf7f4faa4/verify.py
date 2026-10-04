from itertools import combinations
from math import comb

def comps(n,r,prefix=()):
    if r==1:
        yield prefix+(n,); return
    for a in range(1,n-r+2):
        yield from comps(n-a,r-1,prefix+(a,))

def all_profiles(max_order=9):
    for N in range(2,max_order+1):
        for r in range(2,N+1):
            yield from comps(N,r)

def offsets(ns):
    out=[]; s=0
    for i,n in enumerate(ns):
        out += [i]*n; s+=n
    return out

def literal(mask,ns,k):
    part=offsets(ns); N=len(part)
    for v in range(N):
        i=part[v]
        cnt=0
        for u in range(N):
            if u==v or part[u]!=i:
                cnt += (mask>>u)&1
        if cnt>k:
            return False
    return True

def structural(mask,ns,k):
    part=offsets(ns); r=len(ns)
    b=[0]*r
    s=0
    for u,i in enumerate(part):
        if (mask>>u)&1:
            b[i]+=1; s+=1
    if s<=k:
        return True
    t=s-k+1
    return all(x>=t for x in b)

def formula_L(ns,k):
    N=sum(ns); r=len(ns); m=min(ns)
    q=(r*(k-1))//(r-1)
    return min(N,max(k,min(k+m-1,q)))

def prior_bip(ns,k):
    m,n=ns
    if k==1:return 1
    return min(k-1,m)+min(k-1,n)

profiles=subset_checks=criterion_checks=count_checks=bip_checks=0
for ns in all_profiles(9):
    profiles+=1; N=sum(ns)
    for k in range(1,N+2):
        counts=[0]*(N+1)
        best=-1
        for mask in range(1<<N):
            subset_checks+=1
            a=literal(mask,ns,k); b=structural(mask,ns,k)
            criterion_checks+=1
            if a!=b:
                raise AssertionError(('criterion',ns,k,mask,a,b))
            if a:
                s=mask.bit_count(); counts[s]+=1; best=max(best,s)
        # exact coefficient formula
        exp=[]
        for s in range(N+1):
            if s<=min(k,N):
                exp.append(comb(N,s)); continue
            t=s-k+1
            # profile DP
            dp=[0]*(s+1); dp[0]=1
            for n in ns:
                nd=[0]*(s+1)
                for z in range(s+1):
                    if dp[z]:
                        for j in range(t,min(n,s-z)+1):
                            nd[z+j]+=dp[z]*comb(n,j)
                dp=nd
            exp.append(dp[s])
        if counts!=exp:
            raise AssertionError(('counts',ns,k,counts,exp))
        count_checks+=N+1
        f=formula_L(ns,k)
        if best!=f:
            raise AssertionError(('L',ns,k,best,f,counts))
        if len(ns)==2:
            p=min(N,prior_bip(ns,k))
            # prior formula assumes usual k and naturally caps at N when k is huge
            if best!=p:
                raise AssertionError(('bip',ns,k,best,p))
            bip_checks+=1
print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={count_checks} bipartite_checks={bip_checks} max_order=9')
