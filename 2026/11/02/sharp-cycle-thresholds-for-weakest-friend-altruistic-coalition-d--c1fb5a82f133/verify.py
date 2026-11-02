"""Exact complete tests of the weak-link (min-EQ) global-altruism model.
Python 3 standard library only. No random data or external packages.
"""
from itertools import combinations
from collections import Counter


def part(n):
    if n == 0:
        return [()]
    arr=[0]*n
    out=[]
    def dfs(i,k):
        if i == n:
            out.append(tuple(arr)); return
        for j in range(k+2):
            arr[i]=j; dfs(i+1,max(k,j))
    dfs(1,0)
    return out

def canonical(p):
    d={}
    return tuple(d.setdefault(a,len(d)) for a in p)

def edges_from_bits(n,bits):
    es=list(combinations(range(n),2))
    return {e for k,e in enumerate(es) if bits>>k&1}

def val_min_eq(p,n,edges):
    # Compute all elementary personal valuations, then take the weakest
    # of self and all friendship neighbors, including those outside one's coalition.
    personal=[0]*n
    for i in range(n):
        for j in range(n):
            if i != j and p[i] == p[j]:
                personal[i] += n if tuple(sorted((i,j))) in edges else -1
    return tuple(min(personal[j] for j in range(n) if j==i or tuple(sorted((i,j))) in edges) for i in range(n))

def successors(p):
    for i in range(len(p)):
        for b in list(set(p))+[max(p)+1]:
            if b==p[i]: continue
            q=list(p);q[i]=b
            x=canonical(q)
            if x != p: yield i,x

def has_cycle(adj):
    state=[0]*len(adj)
    def visit(x):
        state[x]=1
        for y in adj[x]:
            if state[y]==1:return True
            if state[y]==0 and visit(y):return True
        state[x]=2
        return False
    return any(state[k]==0 and visit(k) for k in range(len(adj)))

def test_small():
    summary=[]
    for n in range(1,5):
        ps=part(n); where={p:i for i,p in enumerate(ps)}
        count=0; transitions=0; types=Counter()
        for bits in range(1<<(n*(n-1)//2)):
            edges=edges_from_bits(n,bits)
            U=[val_min_eq(p,n,edges) for p in ps]
            adj=[[] for p in ps]
            for k,p in enumerate(ps):
                for i,q in successors(p):
                    if U[where[q]][i]>U[k][i]:
                        adj[k].append(where[q]);transitions+=1
            if has_cycle(adj):
                count+=1
                degrees=tuple(sorted(sum(i in e for e in edges) for i in range(n)))
                types[degrees]+=1
        assert count == (16 if n==4 else 0), (n,count)
        if n==4:
            assert types=={(0,1,1,2):12,(0,2,2,2):4},types
            print('four-vertex cyclic-graph degree signatures',dict(types))
        summary.append((n,1<<(n*(n-1)//2),len(ps),transitions,count))
    return summary

def witness(n):
    assert n>=5
    e={(0,4),(1,3),(2,3),(3,4)} | {(2,k) for k in range(5,n)}
    P=[(0,1,0,0,2),(0,0,1,1,2),(0,0,1,0,2),(0,1,0,1,2)]
    P=[tuple(p)+tuple(range(3,3+n-5)) for p in P]
    # Because n>5, canonicalize labels (new singleton labels are 3,4,...).
    P=[canonical(x) for x in P]
    seq=P+[P[0]]
    steps=[]
    for a,b in zip(seq,seq[1:]):
        movers=[]
        for i,q in successors(a):
            if q==b:movers.append(i)
        assert len(movers)==1,(n,a,b,movers)
        i=movers[0]
        ua=val_min_eq(a,n,e)[i];ub=val_min_eq(b,n,e)[i]
        assert ub>ua,(n,ua,ub)
        steps.append((i,ua,ub))
    return steps

def verify_sum_potential():
    for n in range(1,5):
        ps=part(n)
        for bits in range(1<<(n*(n-1)//2)):
            edges=edges_from_bits(n,bits)
            F=[{j for j in range(n) if j!=i and tuple(sorted((i,j))) in edges} for i in range(n)]
            def personal(p):
                return [n*sum(j in F[i] for j in range(n) if j!=i and p[j]==p[i])-
                        sum(j not in F[i] for j in range(n) if j!=i and p[j]==p[i]) for i in range(n)]
            M=n**3
            weights=[(n*(M+1),M),(2*n,1),(n*(M+1),1)]
            def potentials(p):
                return [sum((u if (i,j) in edges else -v) for i in range(n) for j in range(i+1,n)
                            if p[i]==p[j]) for u,v in weights]
            for p in ps:
                a=personal(p); phi=potentials(p)
                for i,q in successors(p):
                    b=personal(q); psi=potentials(q)
                    for k,fn in enumerate([
                        lambda v,i: M*v[i]+sum(v[j] for j in F[i]),
                        lambda v,i: v[i]+sum(v[j] for j in F[i]),
                        lambda v,i: v[i]+M*sum(v[j] for j in F[i])]):
                        assert fn(b,i)-fn(a,i)==psi[k]-phi[k],(n,bits,p,i,q,k)
    return 'sum-potential-identities verified for all graphs and moves at n<=4'

if __name__=='__main__':
    print('n graphs partitions transitions cyclic_graphs')
    for r in test_small():print(*r)
    for n in [5,6,7,10,20,50]:print('witness',n,witness(n))
    print(verify_sum_potential())
    print('VERIFIED_MIN_EQ_BOUNDARY_AND_SUM_POTENTIALS')
