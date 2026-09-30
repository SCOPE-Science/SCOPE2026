from itertools import combinations
from math import comb


def is_rwsat_star(n, ell, mask):
    r=ell-1
    edges=[]
    idx={}
    k=0
    deg=[0]*n
    adj=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            idx[(i,j)]=k
            if (mask>>k)&1:
                deg[i]+=1; deg[j]+=1
                adj[i]|=1<<j; adj[j]|=1<<i
            k+=1
    added=[0]*n
    # monotone closure: scan missing edges until no change
    remaining=[]
    for i in range(n):
        for j in range(i+1,n):
            if not ((adj[i]>>j)&1):
                remaining.append((i,j))
    changed=True
    while changed and remaining:
        changed=False
        new=[]
        for i,j in remaining:
            Ai = deg[i]>=r or added[i]>=r-1
            Aj = deg[j]>=r or added[j]>=r-1
            Bi = deg[i]==r-1 and added[i]<=r-2
            Bj = deg[j]==r-1 and added[j]<=r-2
            if Ai or Aj or (Bi and Bj):
                added[i]+=1; added[j]+=1
                changed=True
            else:
                new.append((i,j))
        remaining=new
    return not remaining


def mask_from_edges(n, E):
    pos={}
    k=0
    for i in range(n):
        for j in range(i+1,n):
            pos[(i,j)]=k;k+=1
    m=0
    for i,j in E:
        if i>j:i,j=j,i
        m|=1<<pos[(i,j)]
    return m


def explicit_graph(n, ell):
    # core 0..ell-1 is K_ell minus edge (0,1); other vertices isolated
    E=[]
    for i in range(ell):
        for j in range(i+1,ell):
            if (i,j)!=(0,1): E.append((i,j))
    return mask_from_edges(n,E)


def brute_min(n, ell, maxk=None):
    N=comb(n,2)
    positions=list(range(N))
    if maxk is None:maxk=N
    for k in range(maxk+1):
        count=0
        for C in combinations(positions,k):
            mask=0
            for p in C: mask|=1<<p
            count+=1
            if is_rwsat_star(n,ell,mask):
                return k,mask,count
        print('checked',n,ell,'k',k,'graphs',count)
    return None

if __name__=='__main__':
    # construction checks at theorem threshold and beyond
    for ell in range(3,13):
        n=max(ell,2*ell-3)
        mask=explicit_graph(n,ell)
        ok=is_rwsat_star(n,ell,mask)
        print('construction',ell,n,'edges',mask.bit_count(),'target',comb(ell,2)-1,'ok',ok)
        assert ok and mask.bit_count()==comb(ell,2)-1
        # one extra isolated vertex
        mask2=explicit_graph(n+1,ell)
        assert is_rwsat_star(n+1,ell,mask2)
    # complete small exact enumerations
    for n,ell in [(3,3),(4,3),(4,4),(5,4),(5,5),(6,5),(7,5)]:
        target=comb(ell,2)-1
        res=brute_min(n,ell,maxk=min(target,comb(n,2)))
        print('minimum',n,ell,res[0] if res else None,'theorem_target',target)
