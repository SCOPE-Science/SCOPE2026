"""Independent exact tests for perfect-edge-domination polynomial of matched-deletion bicliques."""
from collections import Counter
from math import comb


def edge_list(m, n, t):
    return [(i, m+j) for i in range(m) for j in range(n) if not (i==j and i<t)]


def enumerated_polynomial(m, n, t):
    ed = edge_list(m, n, t)
    N = len(ed)
    out = Counter()
    for pattern in range(1 << N):
        deg = [0] * (m+n)
        for k, (u, v) in enumerate(ed):
            if (pattern >> k) & 1:
                deg[u] += 1
                deg[v] += 1
        if all(((pattern >> k) & 1) or deg[u] + deg[v] == 1 for k, (u,v) in enumerate(ed)):
            out[pattern.bit_count()] += 1
    return dict(out)


def prediction(m,n,t):
    if (m,n,t)==(3,3,3):
        return {2:3,4:6,6:1}
    q=Counter({m*n-t:1})
    q[m] += n-t
    q[n] += m-t
    return {k:v for k,v in q.items() if v}


def verify():
    num_cases=0
    num_subsets=0
    for m in range(3,6):
        for n in range(m,7):
            for t in range(m+1):
                es=edge_list(m,n,t)
                if len(es)>18: continue
                actual=enumerated_polynomial(m,n,t)
                expected=prediction(m,n,t)
                assert actual==expected,(m,n,t,actual,expected)
                num_cases+=1
                num_subsets+=(1<<len(es))
    # Algebraic certificate using all independent candidate zero sets.
    count_zero_set_checks=0
    for m in range(3,9):
        for n in range(m,11):
            for t in range(m+1):
                es=edge_list(m,n,t)
                counts=Counter()
                # U can only live in one side or be a deleted matched pair.
                for a_bits in range(1<<m):
                    U={i for i in range(m) if (a_bits>>i)&1}
                    F=[(u,v) for (u,v) in es if u not in U]
                    deg=[0]*(m+n)
                    for (u,v) in F: deg[u]+=1;deg[v]+=1
                    if all((u,v) in F or deg[u]+deg[v]==1 for (u,v) in es):
                        counts[len(F)]+=1
                for b_bits in range(1,1<<n):
                    U={m+j for j in range(n) if (b_bits>>j)&1}
                    F=[(u,v) for (u,v) in es if v not in U]
                    deg=[0]*(m+n)
                    for u,v in F:deg[u]+=1;deg[v]+=1
                    if all((u,v) in F or deg[u]+deg[v]==1 for (u,v) in es):
                        counts[len(F)]+=1
                for i in range(t):
                    U={i,m+i}
                    F=[(u,v) for u,v in es if u not in U and v not in U]
                    deg=[0]*(m+n)
                    for u,v in F:deg[u]+=1;deg[v]+=1
                    if all((u,v) in F or deg[u]+deg[v]==1 for u,v in es):
                        counts[len(F)]+=1
                assert {k:v for k,v in counts.items() if v}==prediction(m,n,t),(m,n,t,counts,prediction(m,n,t))
                count_zero_set_checks+=1
    for n in range(4,45):
        assert prediction(n,n,n-1)=={n:2,n*n-(n-1):1}
        assert prediction(n,n,n)=={n*(n-1):1}
    print('PASS brute edge-subset cases',num_cases)
    print('PASS independently considered edge subsets',num_subsets)
    print('PASS independent-zero-set test configurations',count_zero_set_checks)
    print('PASS all cardinality formulas and matching deletion jumps for n=4..44')

if __name__=='__main__':
    verify()
