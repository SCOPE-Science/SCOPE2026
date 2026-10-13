from math import comb

def profiles(total):
    out = []
    def rec(rem, last, cur):
        if rem == 0:
            if len(cur) >= 2:
                out.append(tuple(cur))
            return
        for x in range(last, rem + 1):
            cur.append(x)
            rec(rem - x, x, cur)
            cur.pop()
    rec(total, 1, [])
    return out

def graph(profile):
    part_of = []
    for i, n in enumerate(profile):
        part_of += [i] * n
    N = len(part_of)
    adj = [0] * N
    for u in range(N):
        for v in range(N):
            if u != v and part_of[u] != part_of[v]:
                adj[u] |= 1 << v
    return part_of, adj

def dominates(adj, mask):
    full = (1 << len(adj)) - 1
    covered = mask
    for v in range(len(adj)):
        if (mask >> v) & 1:
            covered |= adj[v]
    return covered == full

def co_secure_direct(profile, mask):
    part_of, adj = graph(profile)
    N = len(part_of)
    if mask == 0 or not dominates(adj, mask):
        return False
    outside = ((1 << N) - 1) ^ mask
    for v in range(N):
        if not ((mask >> v) & 1):
            continue
        ok = False
        for u in range(N):
            if ((outside >> u) & 1) and ((adj[v] >> u) & 1):
                swapped = (mask ^ (1 << v)) | (1 << u)
                if dominates(adj, swapped):
                    ok = True
                    break
        if not ok:
            return False
    return True

def co_secure_characterization(profile, mask):
    s = []
    start = 0
    for n in profile:
        count = 0
        for v in range(start, start + n):
            count += (mask >> v) & 1
        s.append(count)
        start += n
    t = [n - x for n, x in zip(profile, s)]
    support = [i for i, x in enumerate(s) if x > 0]
    p = len(support)
    r = len(profile)

    if p == 1:
        i = support[0]
        if s[i] != profile[i]:
            return False
        if profile[i] >= 2:
            return True
        return any(j != i and profile[j] == 1 for j in range(r))

    if p < 2:
        return False

    if r >= 3:
        if p == 2:
            return True
        outside_support = [i for i, x in enumerate(t) if x > 0]
        if len(outside_support) >= 2:
            return True
        if len(outside_support) == 1 and s[outside_support[0]] == 0:
            return True
        return False

    if t[0] == 0 or t[1] == 0:
        return False
    return (s[0] >= 2 or t[1] == 1) and (s[1] >= 2 or t[0] == 1)

def polynomial_coefficients(profile):
    N = sum(profile)
    r = len(profile)
    coeff = [0] * (N + 1)

    if r >= 3:
        for k in range(N + 1):
            coeff[k] += comb(N, k)
        for n in profile:
            for k in range(n + 1):
                coeff[k] -= comb(n, k)
        coeff[0] += r - 1
        coeff[N] -= 1

        for n in profile:
            for omitted in range(1, n):
                coeff[N - omitted] -= comb(n, omitted)

        singleton_parts = sum(1 for n in profile if n == 1)
        for n in profile:
            if n >= 2 or singleton_parts >= 2:
                coeff[n] += 1
        return coeff

    a, b = profile
    if a >= 2 or b == 1:
        coeff[a] += 1
    if b >= 2 or a == 1:
        coeff[b] += 1

    for sa in range(1, a):
        ta = a - sa
        for sb in range(1, b):
            tb = b - sb
            if (sa >= 2 or tb == 1) and (sb >= 2 or ta == 1):
                coeff[sa + sb] += comb(a, sa) * comb(b, sb)
    return coeff

profiles_checked = 0
subsets_checked = 0

for N in range(2, 11):
    for profile in profiles(N):
        profiles_checked += 1
        direct_coeff = [0] * (N + 1)
        for mask in range(1 << N):
            subsets_checked += 1
            direct = co_secure_direct(profile, mask)
            structural = co_secure_characterization(profile, mask)
            if direct != structural:
                raise AssertionError(("characterization", profile, mask, direct, structural))
            if direct:
                direct_coeff[mask.bit_count()] += 1
        formula = polynomial_coefficients(profile)
        if direct_coeff != formula:
            raise AssertionError(("polynomial", profile, direct_coeff, formula))

print(
    "ALL CHECKS PASSED; "
    f"profiles={profiles_checked}; "
    f"subsets_checked={subsets_checked}; "
    "orders=2..10"
)
