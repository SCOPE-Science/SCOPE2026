#!/usr/bin/env python3
"""Finite checks accompanying an all-length theorem on paperfolding minimal absent factors.

Run with Python 3.9+; no third-party dependencies. This verifier checks
finite instances, not the infinite inductive proof or the literature theorem
on factor complexity. Its two generators use independent formulas.
"""

def paperfolding_oddpart(size):
    out = bytearray(size)
    for i in range(size):
        x = i + 1
        while x % 2 == 0:
            x //= 2
        out[i] = int(x % 4 == 3)
    return out


def paperfolding_recursive(size):
    out = bytearray(size)
    for i in range(size):
        out[i] = ((i // 2) % 2) if i % 2 == 0 else out[i // 2]
    return out


def factors(seq, k):
    acc = set()
    x = 0
    mask = (1 << k) - 1
    for i, bit in enumerate(seq):
        x = ((x << 1) | bit) & mask
        if i + 1 >= k:
            acc.add(x)
    return acc


def ext_profile(F, k, u):
    left = {a for a in (0, 1) if ((a << k) | u) in F[k+1]}
    right = {b for b in (0, 1) if ((u << 1) | b) in F[k+1]}
    ext = {(a, b) for a in left for b in right if ((a << (k+1)) | (u << 1) | b) in F[k+2]}
    return left, right, ext


def minimal_absent(F, n):
    return {((u << 1) | b) for u in F[n-1] for b in (0, 1)
            if (((u << 1) | b) & ((1 << (n - 1)) - 1)) in F[n-1]
            and ((u << 1) | b) not in F[n]}


def main():
    seq = paperfolding_oddpart(2048)
    assert seq == paperfolding_recursive(2048)
    assert b'0101' not in bytes(seq).replace(b'\x00', b'0').replace(b'\x01', b'1')
    assert b'1010' not in bytes(seq).replace(b'\x00', b'0').replace(b'\x01', b'1')

    F = {k: factors(seq, k) for k in range(7, 131)}
    # Allouche's published theorem gives |F_k| = 4k for k >= 7.
    # These equalities certify completeness of the observed sets; they
    # are NOT proved by the following finite computations themselves.
    assert all(len(F[k]) == 4 * k for k in range(7, 131))
    Fshort = {k: factors(seq[:256], k) for k in range(7,19)}
    assert all(len(Fshort[k]) == 4*k and Fshort[k] == F[k]
               for k in range(7,19))

    base = {}
    for k in range(7, 17):
        bis = {}
        for u in F[k]:
            left, right, ext = ext_profile(Fshort, k, u)
            if len(left) == 2 and len(right) == 2:
                bis[format(u, f'0{k}b')] = ''.join(str(2*a+b) for a, b in sorted(ext))
        base[k] = bis
        if k not in (7, 15):
            assert not bis, (k, bis)
        else:
            assert len(bis) == 4 and sorted(bis.values()) == ['0123','0123','12','12'], (k, bis)

    assert base[7] == {
        '0010011': '0123', '0011011': '0123',
        '0110001': '12', '0111001': '12',
    }
    assert base[15] == {
        '001001100011011':'0123', '001001110011011':'0123',
        '001101100010011':'12', '001101110010011':'12',
    }

    for n in range(9, 129):
        want = 4 if n >= 9 and n - 1 >= 8 and (n-1) & (n-2) == 0 else 0
        # n - 1 is power of two precisely when n - 1 & (n - 2) == 0.
        assert len(minimal_absent(F, n)) == want, (n, len(minimal_absent(F, n)))

    # Compare extension-profile induction on nontrivial sampled lengths:
    # the even-origin lift u of v takes 2m+1 letters; its flexible track
    # is v and its rigid track is the parity of the occurrence position.
    for m in range(8, 64):
        k = 2*m + 1
        lift = {}
        for t in range(1, len(seq)//2 - m - 2):
            v = bytes(seq[t:t+m])
            idx = int(''.join(str(bit) for bit in v), 2)
            u = bytes(seq[2*t:2*t+k])
            if idx in lift:
                assert lift[idx] == u, (m,t)
            else:
                lift[idx] = u
        assert len(lift) == 4*m, (m,len(lift))
        for v, u in lift.items():
            uidx = int(''.join(str(bit) for bit in u), 2)
            lp, rp, ep = ext_profile(F,m,v)
            lq, rq, eq = ext_profile(F,k,uidx)
            assert (lp,rp,ep)==(lq,rq,eq), (m,v)

    words9 = sorted(format(w,'09b') for w in minimal_absent(F,9))
    words17 = sorted(format(w,'017b') for w in minimal_absent(F,17))
    assert words9 == ['001100010', '001110010', '101100011', '101110011']
    assert words17 == ['00011011000100110', '00011011100100110',
                       '10011011000100111', '10011011100100111']
    print('VERIFY_OK paperfolding two_generators=2048 base_factor_sets_7_18=complete '
          'base_bispecial_7_16=checked MAW_lengths_9_128=checked '
          'extension_lifts_m_8_63=checked')

if __name__ == '__main__':
    main()
