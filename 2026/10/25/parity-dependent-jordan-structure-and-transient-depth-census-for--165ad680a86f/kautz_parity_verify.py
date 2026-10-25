"""Independent finite-field checks of parity evolution on Kautz digraphs.

Run with Python 3: python kautz_parity_verify.py
All assertions construct adjacency directly and do not invoke the symbolic proof.
"""
from itertools import product


def words(q, m):
    return [x for x in product(range(q), repeat=m)
            if all(x[i] != x[i+1] for i in range(m-1))]


def neighbours(q, m):
    w = words(q, m)
    ix = {x: i for i, x in enumerate(w)}
    return [[ix[x[1:]+(c,)] for c in range(q) if c != x[-1]] for x in w]


def rows_of_matrix(adj):
    return [sum(1 << j for j in ns) for ns in adj]


def compose(a, b):
    result = []
    for mask in a:
        z = 0
        while mask:
            low = mask & -mask
            z ^= b[low.bit_length()-1]
            mask ^= low
        result.append(z)
    return result


def rank(rows):
    pivots = {}
    for x in rows:
        while x:
            h = x.bit_length()-1
            if h not in pivots:
                pivots[h] = x
                break
            x ^= pivots[h]
    return len(pivots)


def expected_rank(q, m, t):
    if t <= m-1:
        return q * (q-1)**(m-1-t)
    return q if q % 2 == 0 else q-1


def apply(state, adj):
    ans = 0
    for i, ns in enumerate(adj):
        parity = 0
        for j in ns:
            parity ^= (state >> j) & 1
        ans |= parity << i
    return ans


def exhaustive_orbits(q, m, adj):
    n = len(adj)
    if n > 12:
        return 0
    k = 0 if q == 2 else (m-1 if q % 2 == 0 else m)
    rank_last = expected_rank(q, m, k)
    r = [expected_rank(q,m,t) for t in range(k+1)]
    count_depth = [2**(n-r[t]+rank_last) for t in range(k+1)]
    actual_depth = [0]*(k+1)
    periodic = set()
    fixed = set()
    twocycle = set()
    for state in range(1 << n):
        seq=[state]
        for t in range(k+2):
            seq.append(apply(seq[-1], adj))
        delay=next(t for t in range(k+1) if seq[t]==seq[t+2])
        actual_depth[delay]+=1
        if delay==0:
            periodic.add(state)
            if seq[0]==seq[1]:fixed.add(state)
            else:twocycle.add(tuple(sorted((seq[0],seq[1]))))
    assert [sum(actual_depth[:t+1]) for t in range(k+1)]==count_depth, (q,m,'depth')
    assert len(fixed)==2**(q-1),(q,m,'fixed',len(fixed))
    assert len(periodic)==2**rank_last,(q,m,'periodic')
    assert len(twocycle)==(2**(q-2) if q%2==0 else 0),(q,m,'cycles')
    return 1 << n


def main():
    cases=[]
    configurations=0
    verified_powers=0
    for q, mm in ((2,7),(3,5),(4,4),(5,3),(6,3),(7,2),(8,2)):
        for m in range(1,mm+1):
            adj = neighbours(q,m)
            n=len(adj)
            a=rows_of_matrix(adj)
            ident=[1 << i for i in range(n)]
            p=ident
            for t in range(m+3):
                observed=rank(p)
                expected=expected_rank(q,m,t)
                assert observed==expected,(q,m,t,observed,expected)
                verified_powers+=1
                p=compose(p,a)
            configurations+=exhaustive_orbits(q,m,adj)
            cases.append((q,m,n))
    print('KAUTZ_PARITY_VERIFY_OK')
    print('graph_instances',len(cases),'rank_power_checks',verified_powers,
          'exhaustively_simulated_configs',configurations)
    print('tested',cases)

if __name__=='__main__':
    main()
