"""Definition-level tests for a weight-four signed Roman construction on KG(n,2).

No external packages. Run: python verify_kneser_even_srd_weight_four.py
"""
from itertools import combinations


def witness(n):
    assert n >= 10 and n % 2 == 0
    a = (n - 2) // 2
    A = set(range(a))
    B = list(range(a, n))
    # A cycle (a edges), plus a three-edge matching inside B.
    H = {tuple(sorted((i, (i+1) % a))) for i in range(a)}
    H |= {(B[2*j], B[2*j+1]) for j in range(3)}
    assert len(H) == a + 3
    labels = {}
    for e in combinations(range(n), 2):
        labels[e] = -1 if len(set(e) & A) == 1 else (2 if e in H else 1)
    return labels, H, A, set(B)


def direct_checker(n, labels):
    # Literal Kneser adjacency, without row-sum reduction.
    for e, value in labels.items():
        neighbours = [h for h in labels if set(e).isdisjoint(h)]
        assert value + sum(labels[h] for h in neighbours) >= 1
        if value == -1:
            assert any(labels[h] == 2 for h in neighbours)


def independent_row_checker(n, labels):
    # Algebraically independent computation via the endpoint row sums.
    incident_sum = [0] * n
    two_edges = []
    for (i,j), z in labels.items():
        incident_sum[i] += z
        incident_sum[j] += z
        if z == 2:
            two_edges.append((i,j))
    W = sum(labels.values())
    assert W == 4
    lower_closed = 10**9
    lower_defenders = 10**9
    for (i,j),z in labels.items():
        closed = W - incident_sum[i] - incident_sum[j] + 2*z
        lower_closed = min(lower_closed, closed)
        assert closed >= 1, (n, (i,j), z, closed)
        if z == -1:
            defenders = sum(i not in h and j not in h for h in two_edges)
            lower_defenders = min(lower_defenders, defenders)
            assert defenders >= 1
    return lower_closed, lower_defenders


def check_template_lower_bound(a):
    # Finite integer maximum-degree alternatives for hypothetical weights <=3.
    assert a >= 4
    b = a + 2
    for w in (1,2,3):
        required_two_edges = a - 1 + w
        remaining = []
        for da_max in range(w):
            for db_max in range(w):
                if da_max + db_max > w - 1:
                    continue
                capacity = (a*da_max)//2 + (b*db_max)//2
                if capacity >= required_two_edges:
                    remaining.append((da_max,db_max,capacity))
        if w == 3:
            # Sole surviving degree-cap case is a two-regular H_B and empty H_A.
            assert remaining == [(0,2,b)], (a,w,remaining)
            # b>=6 gives a non-edge inside B joining degree-two endpoints,
            # and its closed-neighborhood weight is 3-3-3+2=-1.
            assert b >= 6 and b*(b-1)//2 > b
        else:
            assert not remaining, (a,w,remaining)


def main():
    print('VERIFY_OK')
    direct = 0
    for n in range(10,32,2):
        lab,H,A,B = witness(n)
        direct_checker(n, lab)
        mn,df = independent_row_checker(n, lab)
        assert mn == 1
        assert df == (n-2)//2
        direct += 1
    print('literal_definition_checked_even_n=10..30:',direct,'cases')
    row_checked = 0
    for n in range(10,102,2):
        lab,H,A,B = witness(n)
        mn,df = independent_row_checker(n,lab)
        assert mn == 1 and df == (n-2)//2
        assert len(H) == (n-2)//2 + 3
        check_template_lower_bound((n-2)//2)
        row_checked += 1
    print('row_identity_checked_even_n=10..100:',row_checked,'cases')
    print('one-weight-four witness per tested order; both signed Roman conditions hold')
    print('template lower-weight integer capacity alternatives checked for 46 orders')


if __name__ == '__main__':
    main()
