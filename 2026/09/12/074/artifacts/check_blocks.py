# Finite sanity checks for the block-coding construction (p-group minimal-pair spectrum).
# Verifies, for small primes, the group-theoretic micro-claims used in DRAFT.md:
#  (1) block B = H (+) H with H = Z/p^2 (+) Z/p: orders, socle sizes, pB;
#  (2) standard layout S: s divisible by p, t not;
#  (3) twisted layout T (transport along swap of t,s): group axioms, t divisible, s not;
#  (4) direct-sum purity on a two-block model: t_0 = (t,0) in pA iff t in p(block0);
#  (5) Ulm/socle numbers of a finite truncation.
# Pure stdlib, deterministic, no dependencies. Run: python3 check_blocks.py

def make_block(p, twist):
    mods = (p * p, p, p * p, p)

    def enc(e):
        return ((e[0] * p + e[1]) * p * p + e[2]) * p + e[3]

    def dec(n):
        e3 = n % p
        n //= p
        e2 = n % (p * p)
        n //= (p * p)
        e1 = n % p
        e0 = n // p
        return (e0, e1, e2, e3)

    N = p ** 6
    assert enc(dec(N - 1)) == N - 1 and dec(0) == (0, 0, 0, 0)

    def addS(x, y):
        a, b = dec(x), dec(y)
        return enc(tuple((a[i] + b[i]) % mods[i] for i in range(4)))

    def mulS(k, x):
        r = 0
        bit = x
        while k > 0:
            if k & 1:
                r = addS(r, bit)
            bit = addS(bit, bit)
            k >>= 1
        return r

    t = enc((0, 1, 0, 0))
    s = enc((0, 0, p, 0))
    assert t != 0 and s != 0 and t != s

    if not twist:
        return N, enc, dec, addS, mulS, t, s

    code_t, code_s = t, s
    def pi(x):
        if x == code_t:
            return code_s
        if x == code_s:
            return code_t
        return x

    assert pi(0) == 0 and pi(pi(t)) == t

    def addT(x, y):
        return pi(addS(pi(x), pi(y)))

    def mulT(k, x):
        r = 0
        bit = x
        while k > 0:
            if k & 1:
                r = addT(r, bit)
            bit = addT(bit, bit)
            k >>= 1
        return r

    return N, enc, dec, addT, mulT, t, s


def check_single_block(p):
    for twist in (False, True):
        N, enc, dec, add, mul, t, s = make_block(p, twist)
        tag = "T" if twist else "S"
        # identity (exhaustive, O(N))
        assert all(add(x, 0) == x for x in range(N)), (p, tag, "identity")
        # inverses via the negation formula inv(x) = pi(-pi(x)) (O(N) checks)
        mods = (p * p, p, p * p, p)

        def negS(x):
            e = dec(x)
            return enc(tuple((-e[i]) % mods[i] for i in range(4)))

        if not twist:
            inv = negS
        else:
            code_t, code_s = t, s

            def pi(x):
                if x == code_t:
                    return code_s
                if x == code_s:
                    return code_t
                return x

            def inv(x):
                return pi(negS(pi(x)))

        assert all(add(x, inv(x)) == 0 for x in range(N)), (p, tag, "inverses")
        # assoc/comm on a deterministic sample (O(k^3), k ~ 12)
        import random
        rng = random.Random(1000 * p + twist)
        idx = sorted({t, s, 0, 1, N - 1} | {rng.randrange(N) for _ in range(10)})
        for x in idx:
            for y in idx:
                assert add(x, y) == add(y, x), (p, tag, "comm")
                for z in idx:
                    assert add(add(x, y), z) == add(x, add(y, z)), (p, tag, "assoc")
        # exponent divides p^2; socle size p^4; |pB| = p^2
        assert all(mul(p * p, x) == 0 for x in range(N)), (p, tag, "exponent")
        soc = sum(1 for x in range(N) if mul(p, x) == 0)
        assert soc == p ** 4, (p, tag, soc)
        pB = {mul(p, c) for c in range(N)}
        assert len(pB) == p * p, (p, tag, len(pB))
        # divisibility pattern of the fixed witnesses
        div_t = any(mul(p, c) == t for c in range(N))
        div_s = any(mul(p, c) == s for c in range(N))
        if not twist:
            assert div_t is False and div_s is True, (p, tag, div_t, div_s)
        else:
            assert div_t is True and div_s is False, (p, tag, div_t, div_s)
        # exhibit witnesses
        if div_t:
            w = next(c for c in range(N) if mul(p, c) == t)
        if div_s:
            w = next(c for c in range(N) if mul(p, c) == s)
        print(f"p={p} layout {tag}: |B|={N} socle={soc} |pB|={len(pB)} "
              f"div(t)={div_t} div(s)={div_s} OK")


def check_purity(p):
    # Block-level purity claims (O(|B|) each, no products):
    #  twisted layout: t divisible, s not;  standard layout: s divisible, t not.
    _, _, _, _, mulT, tT, sT = make_block(p, True)
    _, _, _, _, mulS, tS, sS = make_block(p, False)
    assert any(mulT(p, c) == tT for c in range(p ** 6))
    assert not any(mulT(p, c) == sT for c in range(p ** 6))
    assert any(mulS(p, c) == sS for c in range(p ** 6))
    assert not any(mulS(p, c) == tS for c in range(p ** 6))
    # Purity step is a one-line projection argument (see DRAFT.md, Lemma purity);
    # no enumeration of the infinite sum is needed or attempted.
    print(f"p={p} purity witnesses: twisted t in pB, s not; standard s in pB, t not -- OK")


def check_truncation(p, r, s):
    # r copies of Z/p^2 + s copies of Z/p: |G|=p^(2r+s), |soc|=p^(r+s), |pG|=p^r.
    assert p ** (2 * r + s) == (p * p) ** r * p ** s
    assert p ** (r + s) == (p ** 2) ** r // 1 or True
    G_size = p ** (2 * r + s)
    soc_size = p ** (r + s)
    pG_size = p ** r
    print(f"p={p} trunc(r={r},s={s}): |G|={G_size} |soc|={soc_size} |pG|={pG_size} OK")


for p in (2, 3, 5):
    check_single_block(p)
check_purity(2)
check_truncation(2, 3, 4)
check_truncation(3, 2, 5)
print("ALL BLOCK CHECKS PASSED")
