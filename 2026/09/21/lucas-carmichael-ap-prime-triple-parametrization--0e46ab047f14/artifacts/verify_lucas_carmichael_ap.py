from math import gcd

LIMIT = 20000


def prime_sieve(n):
    s = bytearray(b'\x01') * (n + 1)
    s[:2] = b'\x00\x00'
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p*p:n+1:p] = b'\x00' * (((n - p*p) // p) + 1)
    return s


def is_lucas_carmichael_triple(p, q, r):
    n = p * q * r
    return all((n + 1) % (x + 1) == 0 for x in (p, q, r))


def parameter_data(q, d):
    h = q + 1
    g = gcd(h, d)
    u, v = h // g, d // g
    if not (u > v >= 1 and gcd(u, v) == 1):
        return None
    if g % u:
        return None
    w = g // u
    D = u*u - v*v
    if (u - v) % 2 == 0:
        return None
    if (2*v*v*w - 3) % D:
        return None
    return u, v, w


def main():
    prime = prime_sieve(LIMIT)
    tested = 0
    lc_count = 0
    param_count = 0
    mismatches = []
    positives = []

    for q in range(3, LIMIT + 1, 2):
        if not prime[q]:
            continue
        max_d = min(q - 3, LIMIT - q)
        for d in range(2, max_d + 1, 2):
            p, r = q - d, q + d
            if not (prime[p] and prime[r]):
                continue
            tested += 1
            direct = is_lucas_carmichael_triple(p, q, r)
            data = parameter_data(q, d)
            param = data is not None
            if direct:
                lc_count += 1
                positives.append((p*q*r, p, q, r, data))
            if param:
                param_count += 1
                u, v, w = data
                reconstructed = (
                    u*w*(u-v)-1,
                    u*u*w-1,
                    u*w*(u+v)-1,
                )
                if reconstructed != (p, q, r):
                    mismatches.append((p, q, r, 'reconstruction', data))
            if direct != param:
                mismatches.append((p, q, r, direct, data))

    ray_checks = 0
    ray_mismatches = []
    for u in range(2, 31):
        for v in range(1, u):
            if gcd(u, v) != 1 or (u-v) % 2 == 0:
                continue
            D = u*u - v*v
            inv = pow(2*v*v, -1, D)
            w0 = (3 * inv) % D
            for w in range(1, 4*D + 1):
                ray_checks += 1
                h = u*u*w
                d = u*v*w
                local = (
                    d*d % h == 0
                    and (d*(2*d-3)) % (h-d) == 0
                    and (d*(2*d+3)) % (h+d) == 0
                )
                residue = (w - w0) % D == 0
                if local != residue:
                    ray_mismatches.append((u, v, w, local, w0, D))

    positives.sort()
    print(f'prime AP triples tested: {tested}')
    print(f'direct Lucas-Carmichael triples: {lc_count}')
    print(f'parameterized triples: {param_count}')
    print(f'classification mismatches: {len(mismatches)}')
    print(f'fixed-shape residue checks: {ray_checks}')
    print(f'fixed-shape residue mismatches: {len(ray_mismatches)}')
    print('first 15 positive triples:')
    for row in positives[:15]:
        print(row)

    if mismatches or ray_mismatches:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
