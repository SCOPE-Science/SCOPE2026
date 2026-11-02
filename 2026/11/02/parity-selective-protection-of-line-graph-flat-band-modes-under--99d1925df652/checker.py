"""Exact finite examples for cycle-flower line-graph flat-band theorem.
Run: python checker.py  (requires SymPy >=1.10).
All tests use integer/rational exact row reduction, no tolerance.
"""
from sympy import Matrix, zeros, eye, diag, Rational
from itertools import product


def graph(lengths):
    # Cycles share only vertex 0; all non-hub vertices differ.
    edges=[]; cycles=[]; next_v=1
    for length in lengths:
        vs=[0]+list(range(next_v,next_v+length-1));next_v+=length-1
        ids=[]
        for t in range(length):
            a,b=vs[t],vs[(t+1)%length]
            ids.append(len(edges));edges.append((a,b))
        cycles.append(ids)
    B=zeros(next_v,len(edges))
    for j,(a,b) in enumerate(edges): B[a,j]=1;B[b,j]=1
    A=B.T*B-2*eye(len(edges))
    # Cross-check the spectral incidence expression against direct edge adjacency.
    A_direct=zeros(len(edges),len(edges))
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            if i != j and ({a,b}&{c,d}): A_direct[i,j]=1
    assert A==A_direct
    return B,A,cycles


def expected_modes(lengths,cycles,d,z):
    even=odd=0
    for ell,cycle in zip(lengths,cycles):
        if all(d[e]==z for e in cycle):
            if ell%2:odd+=1
            else: even+=1
    return even+max(0,odd-1)


def mode_dimension(B,A,d,z):
    M=A+diag(*d)-(z-2)*eye(len(d))
    return M.cols - B.col_join(M).rank()


def dark_dimension(B,cycles,loss):
    touched=[j for j,v in enumerate(loss) if v]
    constraints=B.col_join(Matrix([[int(i==j) for i in range(B.cols)] for j in touched])) if touched else B
    return B.cols-constraints.rank()


def verify_one(lengths, d):
    B,A,cycles=graph(lengths)
    assert (B.T*B-2*eye(len(d)))==A
    dim = B.cols-B.rank()
    pred=sum(1 for x in lengths if x%2==0)+max(0,sum(1 for x in lengths if x%2)-1)
    assert dim==pred, ('flat-band',lengths,dim,pred)
    odd_sites=[j for length,cyc in zip(lengths,cycles) if length%2 for j in cyc]
    even_uniform=all(len({d[j] for j in cyc})==1 for length,cyc in zip(lengths,cycles) if length%2==0)
    odd_cycles=sum(1 for length in lengths if length%2)
    predicted_invariant=even_uniform and (odd_cycles<2 or len({d[j] for j in odd_sites})==1)
    D=diag(*d)
    actual_invariant=all(B*D*v==zeros(B.rows,1) for v in B.nullspace())
    assert actual_invariant==predicted_invariant, ('invariance',lengths,d)
    for z in sorted(set(d)):
        p=expected_modes(lengths,cycles,d,z)
        actual=mode_dimension(B,A,d,z)
        assert actual==p, ('energy',lengths,d,z,actual,p)
    for touched_cycles in [[],[0],[len(cycles)-1], list(range(len(cycles)//2)), list(range(len(cycles)))]:
        loss=[0]*B.cols
        for i in touched_cycles: loss[cycles[i][0]]=i+1
        oddleft=sum(1 for i,x in enumerate(lengths) if x%2 and i not in touched_cycles)
        evenleft=sum(1 for i,x in enumerate(lengths) if x%2==0 and i not in touched_cycles)
        p=evenleft+max(0,oddleft-1)
        actual=dark_dimension(B,cycles,loss)
        assert actual==p,('loss',lengths,touched_cycles,p,actual)
    return len(set(d)),dim


def main():
    families=[[3],[4],[3,3],[3,4],[4,4],[3,3,3],[4,3,4],[3,4,5],[3,3,4,5],[3,3,3,3],[4,4,4,4]]
    cnt=0
    for lengths in families:
        B,A,cycles=graph(lengths); n=B.cols
        patterns=[]
        patterns.append([0]*n)
        patterns.append([i%3 for i in range(n)])
        patterns.append([i%4 for i in range(n)])
        patterns.append([j//2 for j,cyc in enumerate(cycles) for _ in cyc])
        patterns.append([j for j,cyc in enumerate(cycles) for _ in cyc])
        patterns.append([int(j%2==0) for j,cyc in enumerate(cycles) for _ in cyc])
        patterns.append([0 if e in sum(cycles[:2],[]) else 2 for e in range(n)])
        for d in patterns:
            verify_one(lengths,d);cnt+=1
        print('checked',lengths,'n_edges',n,'n_vertices',B.rows,'baseline_flat_dim',n-B.rank())
    # Independent exhaustive Bernoulli probability count for small bouquets.
    for lengths in ([3,3],[3,3,3],[3,3,3,3],[4,4]):
        B,A,cycles=graph(lengths);N=B.cols
        total=0
        for pot in product((0,1),repeat=N):
            for z in (0,1): total+=expected_modes(lengths,cycles,pot,z)
        observed=Rational(total,2**N)
        even=sum(Rational(2,2**L) for L in lengths if not L%2)
        odds=[L for L in lengths if L%2]
        if odds:
            prob_none=1
            for L in odds: prob_none*=1-Rational(1,2**L)
            odd_exp=sum(Rational(2,2**L) for L in odds)-2*(1-prob_none)
        else: odd_exp=0
        predicted=even+odd_exp
        assert observed==predicted,(lengths,observed,predicted)
        print('binary expectation',lengths,str(observed))
    print('PASS',cnt,'exact disorder patterns, five loss patterns per pattern, and full Bernoulli enumeration')

if __name__=='__main__':main()
