"""Palindromic trail extension test for the binary order-five de Bruijn graph.
The source is self-contained; exhaustive runs require no external data.
"""
from itertools import product


def can_extend(p, n=5):
    if len(p) < n:
        return False
    N = 1 << n
    edges = [int(p[i:i+n], 2) for i in range(len(p)-n+1)]
    if len(edges) != len(set(edges)) or len(edges) > N:
        return False
    used = set(edges)
    vertices = set()
    neighbors = {a: set() for a in range(N//2)}
    for x in range(N):
        if x not in used:
            a, b = x >> 1, x & ((N//2)-1)
            neighbors[a].add(b)
            neighbors[b].add(a)
            vertices.update((a,b))
    first, last = int(p[:n-1], 2), int(p[-(n-1):], 2)
    if not vertices:
        return first == last
    if first not in vertices or last not in vertices:
        return False
    reached = {first}
    frontier = [first]
    while frontier:
        for b in neighbors[frontier.pop()]:
            if b not in reached:
                reached.add(b)
                frontier.append(b)
    return reached == vertices


def palindromes(length):
    mid = (length+1)//2
    for v in product('01', repeat=mid):
        half = ''.join(v)
        yield half + half[:length//2][::-1]


if __name__ == '__main__':
    expected = {14: 0, 15: 6, 16: 0, 17: 0}
    for length, target in expected.items():
        count = sum(can_extend(w) for w in palindromes(length))
        print(f'EULER L={length} extendible_palindromes={count}')
        assert count == target, (length, count, target)
    # No even palindrome of length >=14 and no odd palindrome of length >=17
    # can appear, since its central length-14 or length-17 subfactor would.
    print('EULER_VERIFY_OK')
