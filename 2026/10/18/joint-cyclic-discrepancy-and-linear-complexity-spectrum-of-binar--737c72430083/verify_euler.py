"""Independent Euler-graph and Berlekamp-Massey checker for order-five binary universal cycles."""
from collections import Counter

def bm_period(w):
    s=w+w; n=len(s)
    c=[0]*(n+1); b=[0]*(n+1); c[0]=1;b[0]=1
    L=0;shift=1
    for j in range(n):
        discrepancy=s[j]
        for t in range(1,L+1):discrepancy^=c[t]&s[j-t]
        if discrepancy:
            old=c[:]
            for i in range(n+1-shift):c[i+shift]^=b[i]
            if 2*L<=j:
                L=j+1-L;b=old;shift=1
            else:shift+=1
        else:shift+=1
    return L

def disc_cyclic(w):
    largest=0
    for start in range(len(w)):
        d=0
        for j in range(len(w)):
            d+=1 if w[(start+j)%len(w)] else -1
            largest=max(largest,abs(d))
    return largest

def main():
    counts=Counter();tracks=[0]
    # Rooted circuit at the all-zero five-bit edge, following suffix-prefix overlap.
    def dfs(v,used):
        if len(tracks)==32:
            if v!=0:return
            w=[e>>4 for e in tracks]
            assert len(w)==32 and len(set(tracks))==32
            counts[bm_period(w),disc_cyclic(w)]+=1
            return
        for bit in (0,1):
            e=(v<<1)|bit
            if not (used>>e)&1:
                tracks.append(e)
                dfs(e&15,used|(1<<e))
                tracks.pop()
    dfs(0,1)
    print('EULER_BM',sum(counts.values()),sorted(counts.items()))
    assert sum(counts.values())==2048
    print('EULER_BM_OK')
    return counts
if __name__=='__main__':main()
