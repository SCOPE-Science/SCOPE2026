"""Independent exhaustive checker for disconnected-subset and cut enumeration.
Finite checks do not replace the proof for arbitrary rectangular dimensions.
Usage: python verify.py
"""
from collections import Counter
from math import comb


def closed_form(m, n):
    answer = Counter()
    for k in range(2, n + 1):
        answer[k] += m * comb(n, k)
    for k in range(2, m + 1):
        answer[k] += n * comb(m, k)
    for a in range(1, n):
        for b in range(1, m):
            answer[1 + a + b] += m * n * comb(n - 1, a) * comb(m - 1, b)
    answer[4] += comb(m, 2) * comb(n, 2)
    return answer


def checks(m, n):
    count = m * n
    allmask = (1 << count) - 1
    neigh = []
    for i in range(m):
        for j in range(n):
            mask = 0
            for a in range(m):
                for b in range(n):
                    if i != a and j != b:
                        mask |= 1 << (a * n + b)
            neigh.append(mask)

    # DFS of actual adjacency, with no use of the proposed characterization.
    def disconnected(S):
        if S.bit_count() < 2:
            return False
        start = S & -S
        frontier = start
        visited = start
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            k = bit.bit_length() - 1
            new = neigh[k] & S & ~visited
            frontier |= new
            visited |= new
        return visited != S

    expected_cut_complements = set()
    for i in range(m):
        for j in range(n):
            R = 0
            for a in range(m):
                for b in range(n):
                    if a == i or b == j:
                        R |= 1 << (a * n + b)
            expected_cut_complements.add(R)
    for i in range(m):
        for k in range(i + 1, m):
            for j in range(n):
                for l in range(j + 1, n):
                    R = ((1 << (i * n + j)) | (1 << (i * n + l))
                         | (1 << (k * n + j)) | (1 << (k * n + l)))
                    expected_cut_complements.add(R)

    actual_disconnected = Counter()
    maximal_disconnected = set()
    for S in range(1 << count):
        if not disconnected(S):
            continue
        actual_disconnected[S.bit_count()] += 1
        if all(not disconnected(S | (1 << k))
               for k in range(count) if not (S >> k) & 1):
            maximal_disconnected.add(S)

    theoretical = closed_form(m, n)
    assert actual_disconnected == theoretical, (m, n, actual_disconnected, theoretical)
    assert maximal_disconnected == expected_cut_complements, (m, n,
       maximal_disconnected ^ expected_cut_complements)
    assert min(allmask.bit_count() - S.bit_count()
               for S in maximal_disconnected) == (m - 1) * (n - 1)
    print(f"PASS m={m} n={n} subsets={1<<count} disconnected={sum(actual_disconnected.values())} "
          f"cuts={len(maximal_disconnected)} distribution={dict(sorted(actual_disconnected.items()))}")
    return 1 << count


def main():
    total = 0
    for m,n in [(3,3),(3,4),(3,5),(4,4),(4,5)]:
        total += checks(m,n)
    print(f"ALL PASS; {total} subsets checked")

if __name__ == '__main__':
    main()
