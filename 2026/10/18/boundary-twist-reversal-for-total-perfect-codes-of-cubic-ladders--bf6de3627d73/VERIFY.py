"""Definition-level verification of total perfect codes on cyclic ladders.

Run: python VERIFY.py. Does not use the periodicity lemma or code classification
when enumerating candidate vertex subsets.
"""
from itertools import product, combinations


def neighbours(n, twisted):
    """Vertices (r,i) are numbered 2*i+r; twisted flips the row at the seam."""
    adj = [set() for _ in range(2*n)]
    def edge(a, b):
        adj[a].add(b)
        adj[b].add(a)
    for i in range(n):
        edge(2*i, 2*i+1)
        if i+1 < n:
            edge(2*i, 2*(i+1))
            edge(2*i+1, 2*(i+1)+1)
        else:
            if twisted:
                edge(2*i, 1)
                edge(2*i+1, 0)
            else:
                edge(2*i, 0)
                edge(2*i+1, 1)
    return [sum(1 << v for v in N) for N in adj]


def required_count(n, twisted):
    if n % 3:
        return 0
    return (3 if n % 6 == 0 else 9) if twisted else (9 if n % 6 == 0 else 3)


def direct_codes(n, twisted):
    adj = neighbours(n, twisted)
    if n % 3:  # still enumerate all subsets for a direct zero check
        target = None
    else:
        target = 2*n//3
    found = []
    for mask in range(1 << (2*n)):
        # Cardinality criterion is a necessary consequence of 3-regularity.
        # It is not used for speed here; all subsets are checked against the definition.
        if all((mask & a).bit_count() == 1 for a in adj):
            found.append(mask)
    return found


def periodic_codes(n, twisted):
    words = []
    for first in product(range(4), repeat=6):
        if any(((first[(i-1) % 6] >> a) & 1)
               + ((first[(i+1) % 6] >> a) & 1)
               + ((first[i] >> (1-a)) & 1) != 1
               for i in range(6) for a in (0, 1)):
            continue
        if not all(first[(i+n) % 6] == ((((first[i] & 1) << 1) | (first[i] >> 1)) if twisted else first[i])
                   for i in range(6)):
            continue
        mask = 0
        for i in range(n):
            mask |= first[i % 6] << (2*i)
        words.append(mask)
    return set(words)


def main():
    tests = 0
    masks = 0
    for n in range(3, 10):
        for twisted in (False, True):
            actual = set(direct_codes(n, twisted))
            formula = periodic_codes(n, twisted)
            assert actual == formula, (n, twisted, len(actual), len(formula), actual ^ formula)
            assert len(actual) == required_count(n, twisted), (n, twisted, len(actual))
            assert all(x.bit_count() == 2*n//3 for x in actual)
            # Count *unordered* decompositions of the labeled vertex set
            # into three total perfect codes. No structural lemma is used.
            partition_count = sum(1 for a, b, c in combinations(actual, 3)
                                  if not (a & b or a & c or b & c)
                                  and (a | b | c) == (1 << (2*n))-1)
            assert partition_count == (0 if len(actual) == 0 else
                                       (1 if len(actual) == 3 else 6)), (n, twisted, partition_count)
            tests += 1
            masks += (1 << (2*n))
    for n in range(3, 151):
        for twisted in (False, True):
            assert len(periodic_codes(n, twisted)) == required_count(n, twisted)
    print(f'VERIFICATION_OK graph_profiles={tests} graph_masks={masks} '
          f'periodic_profiles={2*(151-3)}')

if __name__ == '__main__':
    main()
