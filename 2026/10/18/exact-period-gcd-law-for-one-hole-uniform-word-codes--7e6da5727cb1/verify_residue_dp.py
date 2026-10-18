"""Independent exact Hamilton-path verifier for the weighted residue theorem.

For every subset of candidate periods at k=2,...,10, compares a directed
Held--Karp minimum path from residue 0 with the claimed gcd-filtration cost.
The tested subsets need not be realizable as a word's proper periods; this
checks a stronger combinatorial construction for arbitrary edge inventories.
"""
from math import gcd

def predicted(k, periods):
    g=k; ans=0
    for p in periods:
        h=gcd(g,p)
        ans+=(g-h)*p
        g=h
    return ans+(g-1)*(k+1)

def shortest_directed_hamilton_path(k, periods):
    adj=[[] for _ in range(k)]
    for x in range(k):
        to_cost={}
        for p in (*periods, k+1):
            y=(x+p)%k
            if y!=x:
                to_cost[y]=min(to_cost.get(y,10**9),p)
        adj[x]=tuple(to_cost.items())
    dp={(1,0):0}
    for mask in range(1,1<<k,2):
        for end in range(k):
            prev=dp.get((mask,end))
            if prev is None: continue
            for to,cost in adj[end]:
                bit=1<<to
                if not (mask&bit):
                    key=(mask|bit,to)
                    new=prev+cost
                    if new<dp.get(key,10**9): dp[key]=new
    return min(dp.get(((1<<k)-1,end),10**9) for end in range(k))

def main():
    count=0
    for k in range(2,11):
        for mask in range(1<<(k-1)):
            periods=tuple(p for p in range(1,k) if mask&(1<<(p-1)))
            assert predicted(k,periods)==shortest_directed_hamilton_path(k,periods),(k,periods)
            count+=1
    print(f'PASS: exact directed Hamilton DP equals gcd/MST cost on {count} period inventories at k=2..10')

if __name__=='__main__':main()
