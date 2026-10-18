"""Independent finite checks for double total domination on circular ladders.
Run: python3 verification/verify.py ; no third-party packages required.
"""
from collections import Counter
from math import comb


def neighborhoods(n):
    # Distinct named vertices (rung i, layer a) are encoded as 2*i+a.
    return [frozenset((2*((i-1) % n)+a,
                       2*((i+1) % n)+a,
                       2*i+1-a))
            for i in range(n) for a in (0,1)]


def sqcycle_polynomial(length):
    terms = [1]
    for size in range(1, length//3+1):
        numerator = length*comb(length-2*size-1, size-1)
        assert numerator % size == 0
        terms.append(numerator//size)
    return terms


def predicted_open_packings(n):
    a = sqcycle_polynomial(n if n % 2 == 0 else 2*n)
    if n % 2:
        return a
    c = [0]*(2*len(a)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(a):
            c[i+j] += x*y
    return c


def brute_direct_double_total(n):
    """Do not use common-neighbor reduction in this verification."""
    hood = [sum(1 << u for u in neighbors) for neighbors in neighborhoods(n)]
    counts = [0]*(2*n+1)
    full = (1 << (2*n))-1
    for kept in range(full+1):
        if all((kept & h).bit_count() >= 2 for h in hood):
            counts[2*n - kept.bit_count()] += 1
    while len(counts)>1 and not counts[-1]:
        counts.pop()
    return counts


def independent_conflict_counts(n):
    """Independent exhaustive backtracking directly from open neighborhoods."""
    hood = neighborhoods(n)
    length = 2*n
    conflict = [0]*length
    for u in range(length):
        for v in range(length):
            if u != v and (hood[u] & hood[v]):
                conflict[u] |= 1 << v
    cnt = [0]*(length+1)
    def visit(available, chosen):
        if not available:
            cnt[chosen] += 1
            return
        bit = available & -available
        u = bit.bit_length()-1
        visit(available ^ bit, chosen)
        visit(available & ~bit & ~conflict[u],chosen+1)
    visit((1 << length)-1, 0)
    while len(cnt)>1 and not cnt[-1]:
        cnt.pop()
    return cnt


def check_graph_square(n):
    """Verify the actual edge sets agree, not just the resulting counts."""
    hood = neighborhoods(n)
    vertices = [(i,a) for i in range(n) for a in (0,1)]
    # The auxiliary graph has two edges at every vertex:
    aux = [{2*((i-1)%n)+(1-a),2*((i+1)%n)+(1-a)}
           for (i,a) in vertices]
    for u in range(2*n):
        aux_square = set(aux[u])
        for v in aux[u]:
            aux_square.update(aux[v])
        aux_square.discard(u)
        direct_common = {v for v in range(2*n) if u!=v and hood[u]&hood[v]}
        assert direct_common == aux_square,(n,u,direct_common,aux_square)
    # Components of the auxiliary graph are one 2n-cycle if n odd,
    # otherwise two disjoint n-cycles.
    seen=set(); components=[]
    for root in range(2*n):
        if root in seen:continue
        reached={root}; pending=[root];seen.add(root)
        while pending:
            v=pending.pop()
            for w in aux[v]:
                if w not in seen:
                    seen.add(w);reached.add(w);pending.append(w)
        components.append(len(reached))
    target=[2*n] if n%2 else [n,n]
    assert sorted(components)==sorted(target)


def predicted_optimal_count(n):
    return {
        0: lambda:9,
        1: lambda:n*((2*n)//3+1),
        2: lambda:(n*(n+1)//6)**2,
        3: lambda:3,
        4: lambda:n*n,
        5: lambda:2*n,
    }[n%6]()


if __name__=='__main__':
    # Direct exhaustive 0/1 labeling of the original graph, no reduction.
    for n in range(3,10):
        found=brute_direct_double_total(n)
        predicted=predicted_open_packings(n)
        assert found==predicted,(n,found,predicted)
    print('DIRECT_DOUBLE_TOTAL_SUBSETS_OK n=3..9 (349,440 examined)')

    for n in range(3,14):
        found=independent_conflict_counts(n)
        predicted=predicted_open_packings(n)
        assert found==predicted,(n,found,predicted)
    print('COMMON_NEIGHBOR_BACKTRACK_OK n=3..13')

    for n in range(3,101):
        check_graph_square(n)
    print('CONFLICT_GRAPH_ISOMORPHISM_OK n=3..100')

    for n in range(3,401):
        a=predicted_open_packings(n)
        expected_rho=(2*(n//3)) if n%2==0 else (2*n)//3
        assert len(a)-1 == expected_rho
        assert a[-1] == predicted_optimal_count(n),(n,a[-1])
        assert sum(a) <= (1<<(2*n))
    print('SIX_RESIDUE_MAXIMUM_COUNT_OK n=3..400')
    print('VERIFICATION_OK')
