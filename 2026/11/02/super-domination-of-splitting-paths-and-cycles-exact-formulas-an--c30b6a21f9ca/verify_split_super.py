"""Standalone exact verifier for super domination in splitting paths and cycles.

The finite inequality and cycle certificates supply the upper bounds for all
orders. Concrete base words and an eight-step insertion give the lower bounds.
Graph-level exhaustive tests independently check the local reduction.
"""
from itertools import product

X = 3  # a boundary position with no vertices
A = (0, 1, 2)  # omitted none / original / duplicate


def local(v):
    """Test one center in a length-five window (outside positions use X)."""
    a, b, c, d, e = v
    if c == 0 or c == X:
        return True
    if c not in (1, 2):
        return False

    def outer_empty(z):
        return z in (0, X)

    def has_witness(j, other):
        if j == X:
            return False
        original_witness = j != 1 and outer_empty(other)
        if c == 2:
            return original_witness
        duplicate_witness = j != 2 and other != 1
        return original_witness or duplicate_witness

    return has_witness(b, a) or has_witness(d, e)


def path_valid(word):
    a = (X, X) + tuple(word) + (X, X)
    return all(local(a[i:i+5]) for i in range(len(word)))


def cycle_valid(word):
    n = len(word)
    return n >= 4 and all(local(tuple(word[(i+j) % n] for j in range(-2, 3))) for i in range(n))


def graph_neighbors(n, cycle):
    assert n >= (4 if cycle else 2)
    adj = [0] * (2*n)
    for i in range(n):
        for j in range(i+1, n):
            if j == i+1 or (cycle and i == 0 and j == n-1):
                for u, v in ((i, j), (i, n+j), (j, n+i)):
                    adj[u] |= 1 << v
                    adj[v] |= 1 << u
    return adj


def graph_super_complement(adj, w):
    all_mask = (1 << len(adj)) - 1
    ss = all_mask ^ w
    supported = 0
    while ss:
        bit = ss & -ss
        s = bit.bit_length()-1
        ss -= bit
        hit = adj[s] & w
        if hit and not hit & (hit-1):
            supported |= hit
    return supported == w


def word_mask(word):
    n = len(word)
    return sum((1 << i if v == 1 else 1 << (n+i) if v == 2 else 0)
               for i, v in enumerate(word))


def target_path(n):
    return (3*n+2)//4 - (1 if n == 6 else 0)


def target_cycle(n):
    return 3*n//4 - (1 if n % 8 == 4 else 0)


states = list(product(A, repeat=4))
index = {s: i for i, s in enumerate(states)}
trans = [(i, index[s[1:] + (v,)], int(v != 0))
         for i, s in enumerate(states) for v in A if local(s + (v,))]
assert len(states) == 81 and len(trans) == 178

# A longest-path potential with edge prices 4*weight - 3.  Its stability
# proves every directed cycle has nonpositive adjusted weight.
h = [0]*81
for iteration in range(81):
    new = h[:]
    for i, j, w in trans:
        new[j] = max(new[j], h[i] + 4*w-3)
    if new == h:
        break
    h = new
assert iteration == 12, 'potential did not stabilize at the expected step'
assert all(4*w-3 <= h[j]-h[i] for i, j, w in trans)
assert min(h) == 0 and max(h) == 6

left = [i for i, s in enumerate(states)
        if local((X, X)+s[:3]) and local((X,)+s)]
right = [i for i, s in enumerate(states)
         if local(s+(X,)) and local(s[1:]+(X, X))]
assert len(left) == len(right) == 46
alpha = max(4*sum(v != 0 for v in states[i])-12-h[i] for i in left)
beta = max(h[i] for i in right)
assert (alpha, beta) == (-2, 4)
# Thus every valid path of length n>=4 has 4*omitted <= 3*n+2.

# Tight arcs are precisely the zero-slack arcs of the potential.
tight = [[] for _ in range(81)]
for i, j, w in trans:
    if 4*w-3 == h[j]-h[i]:
        tight[i].append(j)
assert sum(map(len, tight)) == 90

# Enumerate EVERY simple directed tight cycle once, using the least vertex
# index as canonical starting vertex. No external graph package is needed.
cycles = []
for start in range(81):
    def explore(at, used, path):
        for j in tight[at]:
            if j == start:
                cycles.append(tuple(path))
            elif j > start and j not in used:
                explore(j, used | {j}, path + [j])
    explore(start, {start}, [start])
assert len(cycles) == 3 and all(len(c) == 8 for c in cycles)
# Each closed tight walk is a union of simple length-eight cycles.
# Consequently equality 4*omitted=3*n is impossible at n=4 mod 8.

cycle_by_state = {}
for cyc in cycles:
    for j, state in enumerate(cyc):
        # Eight successive new letters form an insertion returning to state.
        letters = tuple(states[cyc[(j+t+1) % 8]][-1] for t in range(8))
        assert len(letters) == 8 and sum(v != 0 for v in letters) == 6
        cycle_by_state[state] = letters
assert len(cycle_by_state) == 22

PATH_BASE = {
     2: '11', 3: '011', 4: '2201', 5: '22011',
     6: '220120', 7: '2201110', 8: '22011120',
     9: '220111120', 10: '2201111022', 11: '22011120022',
    12: '220111200211', 13: '2201112002211',
    14: '22011112002211', 15: '220111200211220',
}
CYCLE_BASE = {
     4: '0021', 5: '00111', 6: '001111', 7: '0011112',
     8: '00211112', 9: '000211112', 10: '0021111022',
    11: '00221101122',
}


def insert_eight(word, cyclic):
    a = tuple(int(v) for v in word)
    n = len(a)
    for pos in range(n if cyclic else n-3):
        if cyclic:
            b = tuple(a[(pos+i) % n] for i in range(n))
        else:
            b = a
            if pos > n-4:
                continue
        state = index.get(b[:4] if cyclic else b[pos:pos+4])
        if state in cycle_by_state:
            ins = cycle_by_state[state]
            out = (b[:4]+ins+b[4:] if cyclic else
                   b[:pos+4]+ins+b[pos+4:])
            check = cycle_valid(out) if cyclic else path_valid(out)
            if check and sum(v != 0 for v in out) == sum(v != 0 for v in a)+6:
                return out
    raise AssertionError('no valid critical insertion')

for n, w in PATH_BASE.items():
    a = tuple(map(int, w))
    assert len(a) == n and path_valid(a)
    assert sum(v != 0 for v in a) == target_path(n)
    if n >= 8:
        inserted = insert_eight(w, False)
        assert len(inserted) == n+8 and sum(v != 0 for v in inserted) == target_path(n+8)

for n, w in CYCLE_BASE.items():
    a = tuple(map(int, w))
    assert len(a) == n and cycle_valid(a)
    assert sum(v != 0 for v in a) == target_cycle(n)
    inserted = insert_eight(w, True)
    assert len(inserted) == n+8 and sum(v != 0 for v in inserted) == target_cycle(n+8)

# Independent native-graph exhaustive checks, including the absence of any
# valid omission containing both vertices at one original/duplicate index.
cases = 0
masks_checked = 0
for cyclic in (False, True):
    for n in range(4 if cyclic else 2, 9):
        adj = graph_neighbors(n, cyclic)
        largest = -1
        for w in range(1 << (2*n)):
            valid = graph_super_complement(adj, w)
            if valid:
                largest = max(largest, w.bit_count())
                assert all(not (w & (1 << i) and w & (1 << (n+i))) for i in range(n))
        assert largest == (target_cycle(n) if cyclic else target_path(n))
        # Independent equivalence check with the local five-column rule.
        if n <= 6:
            for word in product(A, repeat=n):
                assert graph_super_complement(adj, word_mask(word)) == (
                    cycle_valid(word) if cyclic else path_valid(word))
        masks_checked += 1 << (2*n)
        cases += 1

# Large sample checks are corroboration only; unbounded conclusions above
# follow from the verified inequality and insertion certificates.
for n in range(8, 65):
    p = tuple(map(int, PATH_BASE[8+(n-8)%8]))
    for _ in range((n-len(p))//8):
        p = insert_eight(p, False)
    assert len(p) == n and path_valid(p) and sum(v != 0 for v in p) == target_path(n)
for n in range(4, 65):
    c = tuple(map(int, CYCLE_BASE[4+(n-4)%8]))
    for _ in range((n-len(c))//8):
        c = insert_eight(c, True)
    assert len(c) == n and cycle_valid(c) and sum(v != 0 for v in c) == target_cycle(n)

print('VERIFY_OK: 81 states, 178 arcs, potential stable in 12 passes, 90 tight arcs')
print('VERIFY_OK: exactly 3 tight simple cycles, all of length 8')
print('VERIFY_OK: path endpoints (-2,+4), all base words and eight-step insertions')
print('VERIFY_OK: %d independent graph instances, %d exhaustively checked subsets' % (cases,masks_checked))
