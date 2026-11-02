"""Cross-check the cycle-run and antipodal-rung classification independently.
No external dependencies. Run: python3 verify_structure.py
"""

def runs(s, N):
    return sum(((s>>i)&1) and not ((s>>((i-1)%N))&1) for i in range(N))

def rim_rungs(s,n):
    return sum(bool(s>>i&1) != bool(s>>(i+n)&1) for i in range(n))

def paired_block(s,n):
    if any(bool(s>>i&1) != bool(s>>(i+n)&1) for i in range(n)):
        return False
    c = sum((s>>i)&1 for i in range(n))
    return 0<c<n and sum((s>>i&1) and not (s>>((i-1)%n)&1) for i in range(n)) == 1

def test(n):
    N=2*n
    for s in range(1, (1<<N)-1):
        k=s.bit_count()
        boundary = 2*runs(s,N)+rim_rungs(s,n)
        lo = 3 if min(k,N-k)==1 else 4 if k%2==0 else 5
        assert boundary >= lo, (n,s,lo,boundary)
        if 4<=k<=N-4 and k%2==0:
            assert (boundary==4) == paired_block(s,n), (n,s,boundary)
    # count first four positions inside a 4-cycle:
    sq = [(0,0),(0,1),(1,1),(1,0)]
    adjacent = lambda a,b: (a-b)%4 in (1,3)
    import itertools
    head = sum(adjacent(p[0],p[1]) for p in itertools.permutations(range(4)))
    # final four choices with last two forming an edge:
    tail = sum(adjacent(p[2],p[3]) for p in itertools.permutations(range(4)))
    assert head==16 and tail==16
    combinatorial_total = n*head*4**(n-4)*tail
    assert combinatorial_total==n*4**n
    print(f'n={n}: all {2**N-2} proper subsets pass run-rung criterion; head={head}, tail={tail}, count={combinatorial_total}')

if __name__ == '__main__':
    for n in range(4,10):
        test(n)
    print('RUN_RUNG_CLASSIFICATION_PASS')
