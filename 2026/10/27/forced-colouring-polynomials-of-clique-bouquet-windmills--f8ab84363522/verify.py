"""Direct finite verification of a formula for forced colouring on clique bouquets.
All color labels are 0,...,m-1; -1 means initially uncoloured.
"""
from itertools import permutations, product
from collections import Counter
from math import factorial, comb


def bouquet(m,k):
    n=1+k*(m-1)
    adj=[set() for _ in range(n)]
    for b in range(k):
        blade=[0]+list(range(1+b*(m-1),1+(b+1)*(m-1)))
        for i in blade:
            for j in blade:
                if i!=j: adj[i].add(j)
    return [tuple(sorted(x)) for x in adj]


def force(initial,adj,m):
    f=list(initial)
    while True:
        forced=[]
        for v,c in enumerate(f):
            if c!=-1:continue
            seen={f[u] for u in adj[v] if f[u]!=-1}
            if len(seen)==m-1:
                (missing,)=set(range(m))-seen
                forced.append((v,missing))
        if not forced:break
        for v,c in forced:f[v]=c
    return all(c!=-1 for c in f) and all(f[v]!=f[u] for v,nei in enumerate(adj) for u in nei)


def full_colorings(m,k):
    for hub in range(m):
        for blades in product(permutations([c for c in range(m) if c!=hub]),repeat=k):
            yield (hub,)+tuple(c for b in blades for c in b)


def proposed_good(bits,coloring,m,k):
    if bits&1:
        # A chosen bit denotes uncoloured, so the hub is blank.
        if any(sum((bits>>(1+b*(m-1)+j))&1 for j in range(m-1))>1 for b in range(k)):
            return False
        visible={coloring[v] for v in range(1,len(coloring)) if not (bits>>v)&1}
        return len(visible)==m-1
    return all(sum((bits>>(1+b*(m-1)+j))&1 for j in range(m-1))<=1 for b in range(k))


def coefficients(m,k):
    n=1+k*(m-1)
    counts=Counter()
    adj=bouquet(m,k)
    for colors in full_colorings(m,k):
        for bits in range(1<<n):
            initial=[-1 if bits>>v&1 else c for v,c in enumerate(colors)]
            actual=force(initial,adj,m)
            pred=proposed_good(bits,colors,m,k)
            assert actual==pred,(m,k,colors,bits,actual,pred)
            if actual:counts[bits.bit_count()]+=1
    full_count=m*factorial(m-1)**k
    expected={0:full_count}
    for j in range(1,k+2):
        c=(comb(k,j)*(m-1)**j if j<=k else 0)
        c+=(comb(k,j-1)*(m-1)**(j-1) if 0<=j-1<=k else 0)
        if j==k+1:c-=(m-1)
        expected[j]=c*full_count
    assert counts==Counter({j:v for j,v in expected.items() if v}),(m,k,counts,expected)
    return n,sum(counts.values()),sum(counts.values())//full_count,tuple(counts[j]//full_count for j in range(k+2))


def direct_partial_check(m,k):
    adj=bouquet(m,k);n=len(adj)
    by_uncolored=Counter()
    for colors in product([-1]+list(range(m)),repeat=n):
        if force(colors,adj,m):by_uncolored[colors.count(-1)]+=1
    expected=coefficients(m,k)[-1]
    full=m*factorial(m-1)**k
    assert tuple(by_uncolored[j] for j in range(k+2))==tuple(full*x for x in expected)
    return sum(by_uncolored.values())


def main():
    for m,k in [(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(5,1)]:
        n,num,ratio,c=coefficients(m,k)
        print('m=%d k=%d N=%d successful=%d ratios=%s'% (m,k,n,num,c))
    for m,k in [(3,1),(3,2),(3,3),(4,1),(4,2)]:
        print('partial_check',m,k,direct_partial_check(m,k))
    print('VERIFY_OK')
if __name__=='__main__':main()
