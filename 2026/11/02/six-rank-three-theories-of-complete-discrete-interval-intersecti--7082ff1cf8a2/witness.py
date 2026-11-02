"""Explicit q=3 boundary witness for the all-interval intersection graphs."""

def signatures(n):
    intervals=[(a,b) for a in range(1,n+1) for b in range(a,n+1)]
    def adj(i,j):
        x,y=intervals[i],intervals[j]
        return i!=j and max(x[0],y[0])<=min(x[1],y[1])
    def atomic(i,j,k):
        return (i==j,i==k,j==k,adj(i,j),adj(i,k),adj(j,k))
    pair={(i,j):frozenset(atomic(i,j,k) for k in range(len(intervals)))
          for i in range(len(intervals)) for j in range(len(intervals))}
    prof={intervals[i]:frozenset(pair[i,j] for j in range(len(intervals)))
          for i in range(len(intervals))}
    return prof

if __name__=='__main__':
    first=signatures(5);second=signatures(6)
    S=set(first.values());T=set(second.values())
    extras=T-S
    reps=[interval for interval,profile in second.items() if profile in extras]
    print('q2 singleton profile counts:', len(S),len(T))
    print('new profiles:',len(extras))
    print('new profile representatives in G6:',reps)
    print('all G5 profiles persist:',S.issubset(T))
    assert len(extras)==1 and reps==[(3,4)] and S.issubset(T)
    print('BOUNDARY_WITNESS_OK')
