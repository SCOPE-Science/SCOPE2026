"""Finite checks of abelianization sizes for parity kernels; not a proof of the universal theorem."""
from itertools import permutations, product


def kernel(block_sizes):
    blocks = []
    start = 0
    for size in block_sizes:
        blocks.append(list(range(start, start + size)))
        start += size
    result = []
    for choices in product(*(permutations(b) for b in blocks)):
        p = list(range(start))
        for block, image in zip(blocks, choices):
            for x, y in zip(block, image):
                p[x] = y
        inv = sum(p[i] > p[j] for i in range(start) for j in range(i+1, start))
        if inv % 2 == 0:
            result.append(tuple(p))
    return result


def multiply(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def abelianization_order(block_sizes):
    elements = kernel(block_sizes)
    identity = tuple(range(sum(block_sizes)))
    commutators = {
        multiply(multiply(multiply(a,b),inverse(a)),inverse(b))
        for a in elements for b in elements
    }
    subgroup = {identity}
    pending = [identity]
    while pending:
        g = pending.pop()
        for h in commutators:
            gh = multiply(g,h)
            if gh not in subgroup:
                subgroup.add(gh)
                pending.append(gh)
    return len(elements)//len(subgroup)


def expected(block_sizes):
    rs = [m for m in block_sizes if m >= 2]
    if len(rs) == 0:
        return 1
    if len(rs) == 1:
        return 3 if rs[0] in (3,4) else 1
    return 2**(len(rs)-1)


if __name__ == '__main__':
    profiles = ((3,), (4,), (5,), (2,2), (2,2,2), (3,2),
                (4,2), (3,3), (3,4), (2,2,3))
    for profile in profiles:
        got, want = abelianization_order(profile), expected(profile)
        assert got == want, (profile, got, want)
    print('VERIFY_OK profiles=10 all_abelianization_orders_match=true')
