from itertools import combinations
from collections import defaultdict
from math import comb

def connected(vertices, adj, removed=0):
    live=vertices&~removed
    if not live: return False
    start=live&-live
    seen=start
    fringe=start
    while fringe:
        u=fringe&-fringe; fringe-=u
        idx=u.bit_length()-1
        added=adj[idx]&live&~seen
        seen|=added; fringe|=added
    return seen==live

def kappa(mask,adj):
    nodes=[v for v in range(len(adj)) if mask&(1<<v)]
    if len(nodes)<2 or not connected(mask,adj): return 0
    for r in range(1,len(nodes)):
        for rem in combinations(nodes,r):
            removed=0
            for v in rem: removed |= 1<<v
            if not connected(mask,adj,removed):return r
    return len(nodes)-1

def theorem(n,A,B):
    a=A.bit_count();b=B.bit_count();t=(A&B).bit_count()
    if min(a,b)<2:return 0
    if a==b==2 and t==2:return 0
    return min(a,b)-(1 if t else 0)

def direct_dom(n,A,B):
    for i in range(n):
        if not ((A>>i)&1):
            if not (B&~(1<<i)):return False
        if not ((B>>i)&1):
            if not (A&~(1<<i)):return False
    return True

def polynomial(n,k):
    z=defaultdict(int)
    if k==1:
        for a in range(2,n+1):
            for b in range(2,n+1):z[a,b]+=comb(n,a)*comb(n,b)
        z[2,2]-=comb(n,2)
        return {p:v for p,v in z.items() if v}
    for a in range(k+1,n+1):
        for b in range(k+1,n+1):z[a,b]+=comb(n,a)*comb(n,b)
    for b in range(k,n-k+1):z[k,b]+=comb(n,k)*comb(n-k,b)
    for a in range(k,n-k+1):z[a,k]+=comb(n,k)*comb(n-k,a)
    if n>=2*k:z[k,k]-=comb(n,k)*comb(n-k,k)
    return {p:v for p,v in z.items() if v}

def run():
    tested=0; byn={}; byk={}
    for n in range(3,7):
        adj=[0]*(2*n)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    adj[i]|=1<<(j+n); adj[j+n]|=1<<i
        coeffs=[defaultdict(int) for _ in range(n)]
        for A in range(1<<n):
            for B in range(1<<n):
                mask=A|(B<<n)
                dom=direct_dom(n,A,B)
                predicted=theorem(n,A,B)
                actual=kappa(mask,adj) if dom else 0
                assert actual==predicted,('kappa',n,A,B,dom,predicted,actual)
                for k in range(1,n):
                    if dom and actual>=k:coeffs[k][A.bit_count(),B.bit_count()]+=1
                tested+=1
        for k in range(1,n):
            expected=polynomial(n,k)
            assert expected==dict(coeffs[k]),('poly',n,k,expected,dict(coeffs[k]))
            byk[n,k]=sum(expected.values())
        byn[n]=4**n
    print('VERIFICATION_OK', 'direct_subsets='+str(tested),'profiles='+str(len(byk)))
    for n in range(3,7):
        print('n',n,'k_counts',[(k,byk[n,k]) for k in range(1,n)])
if __name__=='__main__':run()
