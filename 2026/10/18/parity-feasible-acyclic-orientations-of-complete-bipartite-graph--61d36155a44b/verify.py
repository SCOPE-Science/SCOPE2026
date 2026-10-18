"""Direct edge-orientation verification for bipartite indegree parity."""
from itertools import product
from collections import defaultdict

def brute(a,b):
    assert a>0 and b>0
    out=defaultdict(int)
    for digits in product((0,1), repeat=a*b):
        row=[tuple(digits[i*b:(i+1)*b]) for i in range(a)]
        parity=tuple((b-sum(row[i]))&1 for i in range(a))+tuple(sum(row[i][j] for i in range(a))&1 for j in range(b))
        # Literal directed graph and Kahn topological sort, with no use of
        # the proof's four-cycle/column characterization.
        adj=[[] for _ in range(a+b)]
        indeg=[0]*(a+b)
        for i in range(a):
            for j in range(b):
                u,v=(i,a+j) if row[i][j] else (a+j,i)
                adj[u].append(v)
                indeg[v]+=1
        pending=[v for v in range(a+b) if indeg[v]==0]
        removed=0
        while pending:
            u=pending.pop()
            removed+=1
            for v in adj[u]:
                indeg[v]-=1
                if indeg[v]==0:pending.append(v)
        if removed==a+b:
            out[parity]+=1
    feasible={p for p in product((0,1),repeat=a+b) if sum(p)%2==(a*b)%2}
    assert all((out.get(p,0)>0)==(any(x==0 for x in p)) for p in feasible), (a,b,'classification fail')
    if a==2:
        for p in feasible:
            t=sum(p[2:]); n=b
            if t==0: expected=2**(b-1)
            elif t<b: expected=2**(b-t)
            elif b%2==0: expected=2 if p[:2]==(0,0) else 0
            else: expected=1
            assert out.get(p,0)==expected, (a,b,p,out.get(p,0),expected)
    return len(feasible),sum(out.values())
if __name__=='__main__':
    count=0;cases=0
    for a in range(1,5):
        for b in range(a,9):
            if a*b>20:continue
            sig,orient=brute(a,b)
            print(f'K_{a},{b}: {sig} feasible signatures, {orient} acyclic orientations')
            count+=sig;cases+=1
    print(f'VERIFY_OK {cases} graph orders, {count} feasible signature checks')
