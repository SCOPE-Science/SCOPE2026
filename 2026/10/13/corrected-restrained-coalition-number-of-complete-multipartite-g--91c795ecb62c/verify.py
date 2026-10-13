from functools import lru_cache

def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for tail in integer_partitions(n - x, x):
            yield (x,) + tail

def part_map(profile):
    out = []
    for i, size in enumerate(profile):
        out.extend([i] * size)
    return out

def is_restrained_dominating(mask, profile):
    n = sum(profile)
    if mask == 0:
        return False
    parts = part_map(profile)
    full = (1 << n) - 1
    outside = full ^ mask
    for v in range(n):
        if outside & (1 << v):
            if not any((mask & (1 << w)) and parts[w] != parts[v] for w in range(n)):
                return False
    for v in range(n):
        if outside & (1 << v):
            if not any(w != v and (outside & (1 << w)) and parts[w] != parts[v] for w in range(n)):
                return False
    return True

def set_partitions(n):
    blocks = []
    def rec(v):
        if v == n:
            yield tuple(blocks)
            return
        bit = 1 << v
        for i in range(len(blocks)):
            blocks[i] |= bit
            yield from rec(v + 1)
            blocks[i] ^= bit
        blocks.append(bit)
        yield from rec(v + 1)
        blocks.pop()
    yield from rec(0)

def valid_rd_partition(blocks, profile):
    rd = {b: is_restrained_dominating(b, profile) for b in blocks}
    for b in blocks:
        if rd[b]:
            if b & (b - 1):
                return False
        else:
            if not any(c != b and not rd[c] and is_restrained_dominating(b | c, profile) for c in blocks):
                return False
    return True

def brute_rc(profile):
    best = 0
    checks = 0
    for blocks in set_partitions(sum(profile)):
        checks += 1
        if len(blocks) > best and valid_rd_partition(blocks, profile):
            best = len(blocks)
    return best, checks

def predicted(profile):
    n = sum(profile)
    p = sum(x >= 2 for x in profile)
    u = sum(x == 1 for x in profile)
    if p != 1:
        return n
    if u == 1:
        return 2
    return u + 2

def main():
    profiles = 0
    partition_checks = 0
    for n in range(2, 9):
        for profile in integer_partitions(n):
            if len(profile) < 2:
                continue
            got, checks = brute_rc(profile)
            want = predicted(profile)
            assert got == want, (profile, got, want)
            profiles += 1
            partition_checks += checks
    got, _ = brute_rc((1, 1, 3))
    assert got == 4
    print(f"ALL CHECKS PASSED; profiles={profiles}; partition_checks={partition_checks}; K_1_1_3={got}")

if __name__ == '__main__':
    main()
