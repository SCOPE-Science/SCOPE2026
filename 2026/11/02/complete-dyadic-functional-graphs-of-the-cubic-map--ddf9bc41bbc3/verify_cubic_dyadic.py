"""Exhaustive finite checks for the dynamics of f(x)=x+x^3 on dyadic residue rings."""
from collections import Counter


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def check(k):
    modulus = 1 << k
    f = [(x + x*x*x) % modulus for x in range(modulus)]
    # Finite functional graph, without using any claimed cycle formula.
    even = set(range(0, modulus, 2))
    assert {f[x] for x in even} == even
    cycles = []
    unseen = set(even)
    while unseen:
        x = min(unseen)
        orbit = []
        y = x
        while y not in orbit:
            assert y in unseen
            orbit.append(y)
            y = f[y]
        assert y == x
        for z in orbit:
            unseen.remove(z)
        cycles.append(orbit)
    observed = Counter((v2(orbit[0]), len(orbit)) for orbit in cycles if orbit[0] != 0)
    expected = Counter()
    for r in range(1,k):
        length = 1 << max(k - 3*r, 0)
        count = (1 << (k-r-1)) // length
        expected[(r,length)] = count
    assert observed == expected, (k, observed, expected)
    assert sum(z == 0 for orbit in cycles for z in orbit) == 1
    # Odd points must be depth-one leaves. For k>=5 the map has two
    # classes modulo 32, each value having exactly eight odd preimages.
    odd_images = Counter(f[x] for x in range(1,modulus,2))
    claimed_images = {z for z in even if z % 32 in (2,30)}
    assert set(odd_images) == claimed_images
    assert set(odd_images.values()) == {8}
    indegrees = Counter(f)
    assert Counter(indegrees[z] for z in range(modulus)) == Counter({0:modulus//2,1:7*modulus//16,9:modulus//16})
    return len(cycles), len(odd_images)

if __name__ == '__main__':
    for k in range(5,17):
        cycles, images = check(k)
        print(f'LEVEL_OK k={k} cycles={cycles} odd_image_targets={images}')
    print('VERIFY_OK exhaustive_levels=5..16 all_cycles_odd_fibers_and_indegrees')
