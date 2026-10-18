"""Reproducible finite enumeration for the single-start, single-final unary-NFA bound.
No non-standard Python modules are required.  Execute: python verify.py.
Finite checks corroborate, but do not replace, the general proof.
"""
from itertools import permutations


def reachable(start, adjacency):
    todo = [start]
    seen = {start}
    for vertex in todo:
        for target in adjacency[vertex]:
            if target not in seen:
                seen.add(target)
                todo.append(target)
    return seen


def finite_ambiguity(edges, n):
    """Graph test for bounded accepting-walk counts in a unary NFA."""
    forward = [[v for v in range(n) if edges & (1 << (u*n+v))]
               for u in range(n)]
    backward = [[u for u in range(n) if v in forward[u]] for v in range(n)]
    useful = reachable(0, forward) & reachable(n-1, backward)
    visibility = {u: reachable(u, forward) & useful for u in useful}
    cyclic = []
    for u in useful:
        component = frozenset(v for v in useful
                              if v in visibility[u] and u in visibility[v])
        if len(component) >= 2 or u in forward[u]:
            if component not in cyclic:
                cyclic.append(component)
    for component in cyclic:
        for u in component:
            if sum(v in component for v in forward[u]) != 1:
                return False
    for left in cyclic:
        for right in cyclic:
            if left is not right and any(v in visibility[u]
                                         for u in left for v in right):
                return False
    return True


def maximum_runs(edges, n, lengths):
    adjacency = [[v for v in range(n) if edges & (1 << (u*n+v))]
                 for u in range(n)]
    counts = [0]*n
    counts[0] = 1
    maximum = 0
    for _ in range(lengths+1):
        maximum = max(maximum, counts[n-1])
        nxt = [0]*n
        for u in range(n):
            for v in adjacency[u]:
                nxt[v] += counts[u]
        counts = nxt
    return maximum


def extremal_masks(n):
    """Complete ordered DAG plus a loop at precisely one endpoint."""
    output = set()
    for permutation in permutations(range(1,n-1)):
        order = (0,) + permutation + (n-1,)
        mask = 0
        for i, u in enumerate(order):
            for v in order[i+1:]:
                mask |= 1 << (u*n+v)
        output.add(mask | (1 << (0*n+0)))
        output.add(mask | (1 << ((n-1)*n+(n-1))))
    return output


def verify_small():
    for n in (2,3,4):
        maximum = -1
        argmax = set()
        finite_count = 0
        for edges in range(1 << (n*n)):
            if not finite_ambiguity(edges,n):
                continue
            finite_count += 1
            value = maximum_runs(edges,n,30)
            if value > maximum:
                maximum = value
                argmax = {edges}
            elif value == maximum:
                argmax.add(edges)
        assert maximum == 1 << (n-2), (n,maximum)
        if n>=3:
            assert argmax == extremal_masks(n), (n,len(argmax),len(extremal_masks(n)))
        print('n=%d finite-ambiguous transition graphs=%d maximum=%d labeled extremizers=%d' %
              (n,finite_count,maximum,len(argmax)))


def verify_large_witnesses():
    for n in range(3,11):
        masks = extremal_masks(n)
        assert len(masks) == 2*__import__('math').factorial(n-2)
        for mask in masks:
            assert finite_ambiguity(mask,n)
            assert maximum_runs(mask,n,2*n+5) == 2**(n-2)
        print('n=%d checked extremizers=%d optimal ambiguity=%d' %
              (n,len(masks),2**(n-2)))


if __name__ == '__main__':
    verify_small()
    verify_large_witnesses()
    print('ALL CHECKS PASS')
