"""Standalone deterministic checks for parallel-coset Yang--Baxter dynamics.

Only XOR addition is used; the statements consequently hold for any fixed
identification of the additive group of a characteristic-two field with bits.
"""
from itertools import product


def representatives(q, d):
    return tuple(z for z in range(q) if z < (z ^ d))


def make_chi(q, d, mask):
    reps = representatives(q, d)
    nonzero = tuple(r for r in reps if r != 0)
    selected = {r for i, r in enumerate(nonzero) if (mask >> i) & 1}
    return lambda x: int(min(x, x ^ d) in selected)


def f_table(q, d, c, chi):
    return tuple(x ^ c ^ (d if chi(x ^ c) else 0) for x in range(q))


def step(state, ft):
    *xs, carrier = state
    updated = []
    for x in xs:
        s = x ^ carrier
        z = ft[s]
        x1, carrier = carrier ^ z, x ^ z
        updated.append(x1)
    return tuple(updated) + (carrier,)


def expected(state, q, d, c, chi, t):
    *xs, carrier = state
    N = len(xs)
    out = []
    total = 0
    for j, x in enumerate(xs, start=1):
        bit = 0
        for u in range(t):
            # Characteristic two: (N+1)*u and j*c reduced mod two.
            v = x ^ carrier ^ ((j & 1) * c) ^ ((((N + 1) * u) & 1) * c)
            bit ^= chi(v)
        total ^= bit
        out.append(x ^ ((t & 1) * c) ^ (bit * d))
    return tuple(out) + (carrier ^ (((N * t) & 1) * c) ^ (total * d),)


def order_formula(q, d, c, chi):
    if c == 0 and all(chi(z) == 0 for z in range(q)):
        return 1
    if any(chi(z) != chi(z ^ c) for z in range(q)):
        return 4
    return 2


def fixed_counts(q, d, c, chi, N):
    # Independent analytical formula for the complete finite state space.
    # W=V/<d> has q/2 elements represented uniquely by r=min(v,v^d).
    reps = representatives(q,d)
    m0 = sum(chi(r) == 0 for r in reps)
    m1 = len(reps) - m0
    h0 = sum(chi(r) == chi(r ^ c) for r in reps)
    F1 = q * (2*m0)**N if c==0 else (q*(2*m1)**N if c==d else 0)
    F2 = q**(N+1) if N%2 else q*(2*h0)**N
    return F1,F2


def direct_quantum_ybe(triple, ft):
    """Compare R12 R13 R23 and R23 R13 R12, not the braided equation."""
    def pair(st, a, b):
        out = list(st)
        x, y = st[a], st[b]
        z = ft[x ^ y]
        out[a] = y ^ z
        out[b] = x ^ z
        return tuple(out)
    left = pair(pair(pair(triple, 1, 2), 0, 2), 0, 1)
    right = pair(pair(pair(triple, 0, 1), 0, 2), 1, 2)
    return left == right


def run():
    assertions = 0
    for q in (4, 8):
        total = {1: 0, 2: 0, 4: 0}
        nonlinear_total = nonlinear_order4 = 0
        seen = set()
        for d in range(1, q):
            for mask in range(1 << (q // 2 - 1)):
                if d != 1 and mask == 0:
                    continue  # translations represented once
                chi = make_chi(q, d, mask)
                for c in range(q):
                    ft = f_table(q, d, c, chi)
                    assert ft not in seen
                    seen.add(ft)
                    assert sorted(ft) == list(range(q)); assertions += 1
                    is_affine = all(ft[x ^ y] == (ft[x] ^ ft[y] ^ ft[0])
                                    for x in range(q) for y in range(q))
                    if not is_affine:
                        nonlinear_total += 1
                        nonlinear_order4 += order_formula(q, d, c, chi) == 4
                    for x in range(q):
                        for y in range(q):
                            assert ft[x] ^ ft[x ^ ft[y]] == ft[x ^ ft[y ^ ft[x]]]
                            assertions += 1
                            for z in range(q):
                                assert direct_quantum_ybe((x, y, z), ft)
                                assertions += 1
                    for N in (1, 2, 3):
                        order = 1 if ft == tuple(range(q)) else (4 if N % 2 == 0 and order_formula(q, d, c, chi) == 4 else 2)
                        if N == 2:
                            total[order] += 1
                        inputs = product(range(q), repeat=N+1) if q == 4 or N <= 2 else [tuple((7*i+3*j) % q for i in range(N+1)) for j in range(100)]
                        obs1=obs2=0
                        exhaustive=(q==4 or N<=2)
                        for st in inputs:
                            current = st
                            for t in range(1, 5):
                                current = step(current, ft)
                                if t==1: obs1 += (current == st)
                                if t==2: obs2 += (current == st)
                                assert current == expected(st, q, d, c, chi, t)
                                assertions += 1
                            assert current == st
                            assertions += 1
                        if exhaustive:
                            f1, f2 = fixed_counts(q,d,c,chi,N)
                            assert (obs1,obs2)==(f1,f2)
                            assertions += 1
        predicted_total = q * (1+(q-1)*(2**(q//2-1)-1))
        assert len(seen) == predicted_total
        assert total[4] == (q-1)*(q-2)*(2**(q//2-1)-2**(q//4-1))
        assert total[1] == 1
        assert sum(total.values()) == predicted_total
        assert nonlinear_total == q*(q-1)*(2**(q//2-1)-q//2)
        assert nonlinear_order4 == (q-1)*(q-2)*(2**(q//2-1)-2**(q//4-1)-q//4)
        assertions += 3
        print('q =', q, '; distinct maps =', len(seen), '; even-width exact-order counts =', total,
              '; nonlinear maps =', nonlinear_total, '; nonlinear order-four maps =', nonlinear_order4)
    # Larger-field randomized-deterministic examples including strongly nonlinear masks
    q=16
    for d in (1,3,7,11,15):
        for mask in (0,1,3,21,42,85,127):
            chi=make_chi(q,d,mask)
            for c in (0,1,2,3,8,15):
                ft=f_table(q,d,c,chi)
                for x in range(q):
                    for y in range(q):
                        assert ft[x]^ft[x^ft[y]]==ft[x^ft[y^ft[x]]]
                        assertions += 1
                for N in (2,3,4,5):
                    predicted=1 if ft==tuple(range(q)) else (4 if N%2==0 and order_formula(q,d,c,chi)==4 else 2)
                    for j in range(32):
                        st=tuple((5*i+7*j+i*j)%q for i in range(N+1))
                        r=st
                        for t in range(1,predicted+1):
                            r=step(r,ft)
                            assert r==expected(st,q,d,c,chi,t)
                            assertions += 1
                        assert r==st
                        assertions += 1
    # A concrete nonlinear q=8 example: c=2,d=1, switch only coset {2,3}.
    q,d,c=8,1,2
    chi=make_chi(q,d,1)
    ft=f_table(q,d,c,chi)
    assert ft == (3,2,0,1,6,7,4,5)
    assert not all(ft[x^y] == (ft[x]^ft[y]^ft[0]) for x in range(q) for y in range(q))
    for N, expected_cycle_counts in ((2,(0,64,96)),(3,(0,2048,0))):
        F1,F2=fixed_counts(q,d,c,chi,N)
        assert (F1,(F2-F1)//2,(q**(N+1)-F2)//4) == expected_cycle_counts
        assertions += 1
    print('VERIFY_OK: assertions =',assertions)

if __name__=='__main__':
    run()
