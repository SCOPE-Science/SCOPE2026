
def subsets(t):
    return list(range(1, (1 << t) - 1))


def incomparable(a, b):
    return (a & ~b) != 0 and (b & ~a) != 0


def valid_cff(blocks, edges):
    m = len(blocks)
    if len(set(blocks)) != m:
        return False
    for a in range(m):
        for b in range(a + 1, m):
            if not incomparable(blocks[a], blocks[b]):
                return False
    for i, j in edges:
        u = blocks[i] | blocks[j]
        for h, c in enumerate(blocks):
            if h not in (i, j) and (c & ~u) == 0:
                return False
    return True


def parse(t, words):
    out = []
    for word in words:
        m = 0
        for ch in word:
            d = int(ch)
            if not 1 <= d <= t:
                raise ValueError(word)
            m |= 1 << (d - 1)
        out.append(m)
    return out


def path_edges(n):
    return [(i, i + 1) for i in range(n - 1)]


def cycle_edges(n):
    return path_edges(n) + [(n - 1, 0)]


def wheel_edges(n):
    r = n - 1
    return [(0, i) for i in range(1, n)] + [(1 + i, 1 + ((i + 1) % r)) for i in range(r)]


class FixedGroundSearch:
    def __init__(self, t):
        self.t = t
        self.subs = subsets(t)
        self.pos = {m: i for i, m in enumerate(self.subs)}
        s = len(self.subs)
        self.inc = [0] * s
        for ia, a in enumerate(self.subs):
            mask = 0
            for ib, b in enumerate(self.subs):
                if ia != ib and incomparable(a, b):
                    mask |= 1 << ib
            self.inc[ia] = mask
        self.cover = {}
        for ia, a in enumerate(self.subs):
            for ib, b in enumerate(self.subs):
                if ia == ib:
                    continue
                u = a | b
                mask = 0
                for ic, c in enumerate(self.subs):
                    if ic not in (ia, ib) and (c & ~u) == 0:
                        mask |= 1 << ic
                self.cover[(ia, ib)] = mask

    def path_exists(self, n):
        for size in range(1, self.t):
            first = self.pos[(1 << size) - 1]
            if self._path_from(first, n):
                return True
        return False

    def _path_from(self, first, n):
        seq = [first]
        def dfs(chosen, last, forbid, common, depth):
            if depth == n:
                return True
            cand = common & ~chosen & ~forbid
            while cand:
                bit = cand & -cand
                cand -= bit
                b = bit.bit_length() - 1
                if self.cover[(last, b)] & (chosen & ~(1 << last)):
                    continue
                nf = forbid | self.cover[(last, b)]
                nc = common & self.inc[b]
                future = nc & ~chosen & ~(1 << b) & ~nf
                if future.bit_count() < n - depth - 1:
                    continue
                seq.append(b)
                if dfs(chosen | (1 << b), b, nf, nc, depth + 1):
                    return True
                seq.pop()
            return False
        return dfs(1 << first, first, 0, self.inc[first], 1)

    def cycle_exists(self, n):
        for size in range(1, self.t):
            first = self.pos[(1 << size) - 1]
            if self._cycle_from(first, n):
                return True
        return False

    def _cycle_from(self, first, n):
        def dfs(chosen, last, forbid, common, depth):
            if depth == n:
                if not ((self.inc[last] >> first) & 1):
                    return False
                return not bool(self.cover[(last, first)] & (chosen & ~(1 << last) & ~(1 << first)))
            cand = common & ~chosen & ~forbid
            while cand:
                bit = cand & -cand
                cand -= bit
                b = bit.bit_length() - 1
                if self.cover[(last, b)] & (chosen & ~(1 << last)):
                    continue
                if depth == n - 1 and not ((self.inc[b] >> first) & 1):
                    continue
                nf = forbid | self.cover[(last, b)]
                nc = common & self.inc[b]
                if dfs(chosen | (1 << b), b, nf, nc, depth + 1):
                    return True
            return False
        return dfs(1 << first, first, 0, self.inc[first], 1)

    def wheel_exists(self, n):
        r = n - 1
        for center_size in range(1, self.t):
            center_mask = (1 << center_size) - 1
            center = self.pos[center_mask]
            representatives = []
            for rim_size in range(1, self.t):
                for inter in range(0, min(center_size, rim_size) + 1):
                    outside = rim_size - inter
                    if outside > self.t - center_size:
                        continue
                    m = ((1 << inter) - 1) | (((1 << outside) - 1) << center_size)
                    if m in self.pos:
                        j = self.pos[m]
                        if j != center and ((self.inc[center] >> j) & 1):
                            representatives.append(j)
            for first in representatives:
                if self._wheel_from(center, first, r):
                    return True
        return False

    def _wheel_from(self, center, first, r):
        chosen = (1 << center) | (1 << first)
        forbid = self.cover[(center, first)]
        common = self.inc[center] & self.inc[first]

        def dfs(chosen, last, forbid, common, depth):
            if depth == r:
                if not ((self.inc[last] >> first) & 1):
                    return False
                return not bool(self.cover[(last, first)] & (chosen & ~(1 << last) & ~(1 << first)))
            cand = common & ~chosen & ~forbid
            while cand:
                bit = cand & -cand
                cand -= bit
                b = bit.bit_length() - 1
                nf = forbid
                ok = True
                for a in (center, last):
                    if self.cover[(a, b)] & (chosen & ~(1 << a)):
                        ok = False
                        break
                    nf |= self.cover[(a, b)]
                if not ok:
                    continue
                if depth == r - 1 and not ((self.inc[b] >> first) & 1):
                    continue
                nc = common & self.inc[b]
                future = nc & ~chosen & ~(1 << b) & ~nf
                if future.bit_count() < r - depth - 1:
                    continue
                if dfs(chosen | (1 << b), b, nf, nc, depth + 1):
                    return True
            return False

        return dfs(chosen, first, forbid, common, 1)


P13 = parse(7, ["12","34","156","157","137","367","236","235","257","245","246","467","147"])
P14 = parse(7, ["12","34","356","156","145","457","245","246","467","167","137","357","237","236"])
P15 = parse(7, ["12","34","356","156","145","157","357","237","367","167","467","247","245","256","567"])
C13 = P13
C14 = P14
C15 = parse(7, ["12","247","245","256","567","467","167","367","237","357","157","145","156","356","34"])

assert valid_cff(P13, path_edges(13))
assert valid_cff(P14, path_edges(14))
assert valid_cff(P15, path_edges(15))
assert valid_cff(C13, cycle_edges(13))
assert valid_cff(C14, cycle_edges(14))
assert valid_cff(C15, cycle_edges(15))

s6 = FixedGroundSearch(6)
assert not s6.path_exists(11)
assert not s6.cycle_exists(10)

s7 = FixedGroundSearch(7)
assert not s7.wheel_exists(11)

print("P11 has no 6-point G-CFF: verified")
print("C10 has no 6-point G-CFF: verified")
print("W11 has no 7-point G-CFF: verified")
print("Explicit 7-point G-CFFs for P13,P14,P15,C13,C14,C15: verified")

# Positive controls matching previously known exact small cases.
assert FixedGroundSearch(6).path_exists(10)
assert FixedGroundSearch(6).cycle_exists(9)
assert FixedGroundSearch(7).wheel_exists(10)
print("Previously known boundary cases P10@6, C9@6, W10@7: verified")
