from itertools import combinations


def crown_graph(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def d2(u,v,adj):
    if u == v:
        return 0
    return 1 if v in adj[u] else 2


def is_adjacency_resolving(S,adj):
    S=tuple(S)
    order=len(adj)
    reps=[]
    for u in range(order):
        reps.append(tuple(d2(u,s,adj) for s in S))
    return len(set(reps)) == order


def predicted_basis(n,S):
    S=set(S)
    if len(S) != n-1:
        return False
    occup=[]
    chosen_a=chosen_b=0
    for i in range(n):
        a=i in S
        b=n+i in S
        occup.append(int(a)+int(b))
        chosen_a += int(a)
        chosen_b += int(b)
    if occup.count(0) != 1 or occup.count(1) != n-1 or occup.count(2) != 0:
        return False
    if n == 3:
        return chosen_a == 2 or chosen_b == 2
    return True


def predicted_count(n):
    return 6 if n == 3 else n * 2**(n-1)


def main():
    total_subset_checks=0
    total_basis_checks=0
    total_bases=0
    for n in range(3,10):
        adj=crown_graph(n)
        optimum=n-1
        for size in range(optimum):
            for S in combinations(range(2*n),size):
                total_subset_checks += 1
                assert not is_adjacency_resolving(S,adj), (n,size,S)
        bases=0
        for S in combinations(range(2*n),optimum):
            total_subset_checks += 1
            actual=is_adjacency_resolving(S,adj)
            predicted=predicted_basis(n,S)
            total_basis_checks += 1
            assert actual == predicted, (n,S,actual,predicted)
            bases += int(actual)
        assert bases == predicted_count(n), (n,bases,predicted_count(n))
        total_bases += bases
    print('VERIFY_OK n_range=3..9 subset_checks=%d basis_checks=%d bases=%d max_order=18' % (
        total_subset_checks,total_basis_checks,total_bases))


if __name__=='__main__':
    main()
