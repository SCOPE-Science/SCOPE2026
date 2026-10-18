"""Independent weighted-distance quotient checker, not a proof of infinite cases."""
from collections import Counter

def rounds(n,k):
    h=n//2
    c=tuple(1 if a==0 else 0 for a in range(h+1))
    ans=[c]
    for step in range(h+3):
        labels=[]
        for a in range(h+1):
            neighbors=Counter()
            for s in range(1,k+1):
                neighbors[c[min((a+s)%n,n-(a+s)%n)]]+=1
                neighbors[c[min((a-s)%n,n-(a-s)%n)]]+=1
            labels.append((c[a],tuple(sorted(neighbors.items()))))
        types={sig:i for i,sig in enumerate(sorted(set(labels)))}
        nc=tuple(types[s] for s in labels)
        if all((c[a]==c[b]) == (nc[a]==nc[b]) for a in range(h+1) for b in range(a+1,h+1)):
            break
        ans.append(nc)
        c=nc
    return ans

pairs=0;level_count=0
for k in range(2,39):
    for n in range(4*k,7*k+16):
        actual=rounds(n,k)
        D=n//2
        R=3 if n==4*k else max(2,(D+k-2)//k)
        assert len(actual)-1==R,(n,k,len(actual)-1,R)
        for r,c in enumerate(actual):
            for a in range(D+1):
                for b in range(a+1,D+1):
                    # The precise predicted equivalence on distance shells.
                    if r==0: same=(a>0 and b>0)
                    elif r==1: same=(1<=a<=k and 1<=b<=k) or (a>k and b>k)
                    elif n==4*k and r==2:same=(a==2*k-1 and b==2*k)
                    elif n==4*k:same=False
                    else:same=(a>r*k and b>r*k)
                    assert (c[a]==c[b])==same,(n,k,r,a,b)
            level_count+=1
        pairs+=1
print('QUOTIENT_SIGNATURES_OK parameter_pairs=%d checked_rounds=%d'%(pairs,level_count))

for k in range(2,60):
    n=4*k
    def neighbor_count(a,b):
        return sum(min((a-v)%n,(v-a)%n)<=k for v in ({b,n-b} if b>0 and b<n//2 else {b}))
    assert neighbor_count(2*k-1,k-1)==1
    assert neighbor_count(2*k,k-1)==0
print('SEAM_DISTINGUISHER_OK k=2..59')
