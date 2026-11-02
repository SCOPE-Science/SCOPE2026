"""Exact finite orbit/stabilizer verification for a three-pole curve family."""
from itertools import product

def actions(u, v, p):
    inv_u = pow(u, -1, p)
    return (v, u), (inv_u, (-v * inv_u) % p)

def orbit(point, p):
    seen = {point}
    queue = [point]
    while queue:
        u, v = queue.pop()
        for image in actions(u, v, p):
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return seen

def check_prime(p):
    torus = {(u, v) for u in range(1, p) for v in range(1, p)}
    assert len(torus) == (p-1)**2
    trans = {(u, v) for u, v in torus if u == v or u == p-1 or v == p-1}
    cycle = {(u, v) for u, v in torus if (u**3 + 1) % p == 0 and v == pow(u, -1, p)}
    assert len(trans) == 3*p-5
    h = 3 if p % 3 == 1 else 1
    assert len(cycle) == h
    assert cycle.intersection(trans) == {(p-1, p-1)}
    remaining = set(torus)
    by_size = {1: 0, 2: 0, 3: 0, 6: 0}
    while remaining:
        point = next(iter(remaining))
        o = orbit(point, p)
        assert o <= remaining and len(o) in by_size
        by_size[len(o)] += 1
        remaining -= o
    assert by_size[1] == 1
    assert by_size[2] == (1 if p % 3 == 1 else 0)
    assert by_size[3] == p-2
    expected = (p-1)*(p-4)//6 if p % 3 == 1 else (p-2)*(p-3)//6
    assert by_size[6] == expected
    assert 1*by_size[1] + 2*by_size[2] + 3*by_size[3] + 6*by_size[6] == len(torus)
    assert all(any(x in trans or x in cycle for x in o) if len(o) < 6 else all(x not in trans and x not in cycle for x in o) for o in [orbit((u,v),p) for u,v in torus])
    return by_size

if __name__ == '__main__':
    primes = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for p in primes:
        orbits = check_prime(p)
        if p in (5,7,11,13):
            print('p', p, 'orbit counts by S3 orbit size', orbits)
    print('VERIFY_OK')
