from itertools import product, combinations
from math import comb


def crown_edges(n):
    # vertices 0..n-1 are A, n..2n-1 are B
    return {(i, n+j) for i in range(n) for j in range(n) if i != j}


def adj_from_edges(n, edges):
    adj=[set() for _ in range(2*n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    return adj


def is_trdf(labels, adj):
    pos=[v for v,x in enumerate(labels) if x>0]
    twos={v for v,x in enumerate(labels) if x==2}
    for v,x in enumerate(labels):
        if x==0 and not (adj[v] & twos):
            return False
    for v in pos:
        if not any(labels[w]>0 for w in adj[v]):
            return False
    return True


def classified_optima(n):
    out=set()
    # different-index defenders a_i=2,b_j=2; forced ones a_j,b_i
    for i in range(n):
        for j in range(n):
            if i==j: continue
            lab=[0]*(2*n)
            lab[i]=2; lab[n+j]=2; lab[j]=1; lab[n+i]=1
            out.add(tuple(lab))
    # same-index defenders; choose one 1 on each shore away from index
    for i in range(n):
        for p in range(n):
            if p==i: continue
            for q in range(n):
                if q==i: continue
                lab=[0]*(2*n)
                lab[i]=2; lab[n+i]=2; lab[p]=1; lab[n+q]=1
                out.add(tuple(lab))
    return out


def brute_optima(n):
    edges=crown_edges(n); adj=adj_from_edges(n,edges)
    best=10**9; opts=set(); checked=0
    for lab in product((0,1,2), repeat=2*n):
        w=sum(lab)
        if w>6: continue
        checked+=1
        if w>best: continue
        if is_trdf(lab,adj):
            if w<best: best=w; opts={lab}
            elif w==best: opts.add(lab)
    return best,opts,checked


def survives(lab, n, deleted):
    adj=adj_from_edges(n,crown_edges(n)-set(deleted))
    return is_trdf(lab,adj)


def witness_deleted(n):
    arcs=[(0,1)]
    cyc=list(range(2,n))
    if len(cyc)==2:
        arcs += [(cyc[0],cyc[1]),(cyc[1],cyc[0])]
    else:
        arcs += [(cyc[k],cyc[(k+1)%len(cyc)]) for k in range(len(cyc))]
    return {(i,n+j) for i,j in arcs}


def main():
    exhaustive_assignments=0
    deletion_sets=0
    for n in (4,5):
        best,opts,checked=brute_optima(n)
        exhaustive_assignments += checked
        predicted=classified_optima(n)
        assert best==6, (n,best)
        assert opts==predicted, (n,len(opts),len(predicted),len(opts^predicted))
        assert len(opts)==n*n*(n-1)
        edges=sorted(crown_edges(n))
        # Every smaller deletion leaves at least one weight-six optimum.
        for k in range(n-1):
            for F in combinations(edges,k):
                deletion_sets += 1
                assert any(survives(lab,n,F) for lab in predicted), (n,k,F)
        # Explicit n-1 deletion witness kills every optimum and stays isolate-free.
        F=witness_deleted(n)
        assert len(F)==n-1
        adj=adj_from_edges(n,crown_edges(n)-F)
        assert min(map(len,adj))>=1
        assert not any(is_trdf(lab,adj) for lab in predicted)
    # Algebraic lower-bound inequality behind the directed-deletion proof.
    algebra_cases=0
    for n in range(4,61):
        for a in range(1,n):
            for b in range(1,n-a+1):
                k=n-a-b
                if k<0: continue
                algebra_cases += 1
                assert a*b+k >= n-1
    # Witness degree pattern for a larger range.
    witness_cases=0
    for n in range(4,101):
        F=witness_deleted(n)
        assert len(F)==n-1
        adj=adj_from_edges(n,crown_edges(n)-F)
        assert min(map(len,adj))==n-2
        witness_cases += 1
    print('ALL CHECKS PASSED')
    print(f'exhaustive_orders=4,5; assignments_weight_le_6={exhaustive_assignments}')
    print(f'deletion_sets_below_threshold={deletion_sets}; algebra_cases={algebra_cases}')
    print(f'optimizer_counts_n4_n5={4*4*3},{5*5*4}; witness_orders=4..100')

if __name__=='__main__':
    main()
