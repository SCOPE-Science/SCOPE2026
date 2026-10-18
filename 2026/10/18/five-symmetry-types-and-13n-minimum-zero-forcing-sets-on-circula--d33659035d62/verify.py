"""Independent exhaustive tests for minimum zero forcing sets of circular ladders.
Run with Python 3, standard library only. Does not establish an infinite theorem."""
from itertools import combinations

def neighbors(n):
    return tuple(tuple({layer*n+(i-1)%n, layer*n+(i+1)%n,
                        (1-layer)*n+i})
                 for layer in range(2) for i in range(n))

def zero_forcing(n, initial):
    adj = neighbors(n)
    blue = set(initial)
    while True:
        newly = set()
        for u in blue:
            uncolored = [v for v in adj[u] if v not in blue]
            if len(uncolored) == 1:
                newly.add(uncolored[0])
        if not newly:
            return len(blue) == 2*n
        blue.update(newly)

def transform(n, initial, rotation, reflection, switch):
    return frozenset((layer ^ switch)*n +
                     ((rotation + (-i if reflection else i)) % n)
                     for v in initial
                     for layer,i in [divmod(v,n)])

def five_orbits(n):
    top = lambda i: i%n
    bot = lambda i: n+i%n
    bases = [
        {top(0),top(1),top(2),top(3)},
        {top(0),top(1),top(2),bot(0)},
        {top(0),top(1),top(3),bot(1)},
        {top(0),top(1),bot(0),bot(1)},
        {top(0),top(1),bot(0),bot(-1)},
    ]
    return [set(transform(n,S,k,refl,switch)
                for k in range(n)
                for refl in (False,True)
                for switch in (0,1)) for S in bases]

def run():
    # Finite independent verification of the exact first/second-force table.
    for n in range(5,26):
        for triple, first_target, allowed in (
            ((0,1,2), n+1, {n-1, 3, n, n+2}),
            ((0,1,n), n-1, {2, n-2, n+1, 2*n-1}),
        ):
            for d in range(2*n):
                if d in triple or d == first_target:
                    continue
                blue = set(triple) | {d, first_target}
                second_possible = any(sum(v not in blue for v in neighbors(n)[u]) == 1
                                      for u in blue)
                assert second_possible == (d in allowed), (n,triple,d)
    checks = 0
    for n in range(5,20):
        orbit = five_orbits(n)
        expected = [2*n,4*n,4*n,n,2*n]
        assert [len(v) for v in orbit] == expected, (n, 'orbit counts')
        assert len(set().union(*orbit)) == 13*n, (n, 'overlapping orbit')
        assert all(zero_forcing(n,S) for family in orbit for S in family)
        checks += sum(len(fam) for fam in orbit)
        if n <= 15:
            actual = {frozenset(S) for S in combinations(range(2*n),4)
                      if zero_forcing(n,S)}
            assert actual == set().union(*orbit), (n,'classification')
            for S in combinations(range(2*n),3):
                assert not zero_forcing(n,S), (n,'three-vertex forcing')
            checks += len(actual)
            print('n=',n,' min=4 count=',len(actual),' orbit_sizes=',expected)
    for n in (20,30,50,100):
        orbit=five_orbits(n)
        assert [len(v) for v in orbit]==[2*n,4*n,4*n,n,2*n]
        assert all(zero_forcing(n,S) for family in orbit for S in family)
        checks+=13*n
        print('construction n=',n, 'sets=',13*n)
    print('VERIFICATION_OK; confirmed_sets_and_rechecks=',checks)
if __name__ == '__main__':
    run()
