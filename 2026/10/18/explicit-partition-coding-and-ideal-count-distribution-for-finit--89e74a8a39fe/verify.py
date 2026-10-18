"""Standalone exact checker for a partition coding of finite linear L-algebras.

Runs with Python standard library only. All tables use top element index 0:
 x_0 > x_1 > ... > x_{n-1}. The value M[i][j] is the index of x_i dot x_j.
"""
from itertools import product, combinations
from math import comb


def partition_tuples(labels):
    labels = tuple(labels)
    if not labels:
        yield ()
        return
    head = labels[0]
    for blocks in partition_tuples(labels[1:]):
        yield (frozenset((head,)),) + blocks
        for j in range(len(blocks)):
            yield blocks[:j] + (blocks[j] | frozenset((head,)),) + blocks[j+1:]


def canonical(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda x: x))


def decode(blocks, n):
    """Inverse constructive bijection, using the finite-chain extension lemma."""
    blocks = tuple(frozenset(b) for b in blocks)
    assert {a for block in blocks for a in block} == set(range(1,n))
    assert sum(len(block) for block in blocks) == n-1
    if n == 1:
        assert blocks == ()
        return ((0,),)
    B, = [b for b in blocks if n-1 in b]
    C = sorted(set(range(1,n)) - B)
    m = len(C)+1
    relabel = {v:i for i,v in enumerate(C, start=1)}
    old_partition = tuple(frozenset(relabel[v] for v in b) for b in blocks if b is not B)
    old = [list(row) for row in decode(old_partition,m)]
    # Append the new smallest invariant element x_m.
    k = m
    for i in range(k): old[i].append(k)
    old.append([0]*(k+1))
    # The remaining choices of x_m dot x_j occur in strict decreasing
    # order as j increases, hence strictly increasing output indices.
    for c in sorted(B - {n-1}):
        k = len(old)
        assert 1 <= c < k
        for i in range(k):
            val = k if i < m else old[old[m][i]][c]
            old[i].append(val)
        old.append([0]*(k+1))
    assert len(old) == n
    return tuple(tuple(row) for row in old)


def encode(M):
    """Map a linear L-algebra on n elements to a partition of [1,n-1]."""
    n = len(M)
    if n == 1: return ()
    invs = [j for j in range(1,n) if all(M[i][j] == j for i in range(j))]
    assert invs
    m = max(invs)
    A = {M[m][j] for j in range(m+1,n)}
    assert len(A) == n-m-1 and A <= set(range(1,n-1))
    B = A | {n-1}
    C = sorted(set(range(1,n)) - B)
    assert len(C) == m-1
    renumber = {i:v for i,v in enumerate(C, start=1)}
    smaller = encode(tuple(tuple(M[i][j] for j in range(m)) for i in range(m)))
    result = [frozenset(renumber[x] for x in b) for b in smaller]
    result.append(frozenset(B))
    return canonical(result)


def is_l(M):
    n = len(M)
    if len(M[0]) != n: return False
    if any(len(r)!=n for r in M): return False
    if any(M[0][j]!=j or M[j][0]!=0 or M[j][j]!=0 for j in range(n)):return False
    if any((M[i][j]==0)!=(i>=j) for i in range(n) for j in range(n)):return False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if M[M[i][j]][M[i][k]] != M[M[j][i]][M[j][k]]:
                    return False
    return True


def direct_linear_tables(n):
    # Independent direct search in the L identities, no use of the extension
    # lemma or the partition inverse. Rows on/under diagonal are zero;
    # row 0 equals identity. Unknown positions (i,j) with 1<=i<j<n
    # cannot output 0 and must be >= j in the chain order (index <= j).
    cells = [(i,j) for j in range(2,n) for i in range(1,j)]
    values = [tuple(range(1,j+1)) for (i,j) in cells]
    for assignment in product(*values):
        M = [[0]*n for _ in range(n)]
        for j in range(n): M[0][j]=j
        for (i,j),v in zip(cells,assignment): M[i][j]=v
        M = tuple(tuple(row) for row in M)
        if is_l(M): yield M


def invariant_indices(M):
    """Non-unit invariant elements, as indices in the descending chain."""
    n = len(M)
    return tuple(j for j in range(1, n)
                 if all(M[i][j] == j for i in range(j)))


def direct_proper_ideal_count(M):
    """Independent brute-force check of all four defining ideal axioms."""
    n = len(M)
    count = 0
    for mask in range(1, (1 << n) - 1):
        I = set(i for i in range(n) if mask & (1 << i))
        good = True
        for x in I:
            for y in range(n):
                if ((M[x][y] in I and y not in I)
                    or M[y][x] not in I
                    or M[M[x][y]][y] not in I
                    or M[y][M[x][y]] not in I):
                    good = False
                    break
            if not good:
                break
        if good:
            count += 1
    return count


def stirling2(n, k):
    if n == 0:
        return int(k == 0)
    if k <= 0:
        return 0
    prev = [1] + [0] * k
    for i in range(1, n + 1):
        row = [0] * (k + 1)
        for j in range(1, min(i,k) + 1):
            row[j] = j * prev[j] + prev[j-1]
        prev = row
    return prev[k]


def run():
    bell = [1,1,2,5,15,52,203,877,4140,21147]
    for n in range(1,9):
        images=set(); matrices=set(); profile = [0] * n
        for P in partition_tuples(range(1,n)):
            P0=canonical(P)
            M=decode(P,n)
            assert is_l(M),('BAD TABLE',n,P0,M)
            Q=encode(M)
            assert Q==P0, ('ROUND TRIP',n,P0,Q)
            assert M not in matrices,('INJECTIVITY',n)
            matrices.add(M); images.add(P0)
            k = len(P0)
            assert len(invariant_indices(M)) == k, (n,P0,invariant_indices(M))
            profile[k] += 1
            if n <= 6:
                assert direct_proper_ideal_count(M) == k, (n,P0,M)
        assert len(matrices)==bell[n-1], (n,len(matrices),bell[n-1])
        assert all(profile[k] == stirling2(n-1,k) for k in range(n)), (n,profile)
        print('constructive',n,len(matrices), 'proper-ideal profile', profile)
    for n in range(1,6):
        all_tables=set(direct_linear_tables(n))
        generated={decode(P,n) for P in partition_tuples(range(1,n))}
        assert all_tables==generated,(n,len(all_tables),len(generated))
        print('direct search',n,len(all_tables),'exact match')
    print('VERIFY_OK')

if __name__=='__main__': run()
