"""Explicit weight-7 X- and Z-logicals for Q16 => d(Q16) <= 7 (stdlib only).
Support W = {0,80,160,240,256,320,384} (4 left-block + 3 right-block qubits).
Checks (exact, bitmask arithmetic):
  (a) syndrome of W under HX is 0 and under HZ is 0;
  (b) W is not in the row space of HZ (so it is a genuine X-logical);
  (c) W is not in the row space of HX (so it is a genuine Z-logical).
Row-space membership is decided by exact RREF reduction of the indicator vector.
"""
A = [[14, 1, 9, 6], [12, 10, 6, 0], [4, 4, 8, 3]]
L = 16
W = [0, 80, 160, 240, 256, 320, 384]

def build_masks():
    HXc = [0] * 400  # HX column masks over 192 checks
    HZc = [0] * 400
    for a in range(3):
        for x in range(4):
            for k in range(16):
                r = (a * 4 + x) * 16 + k
                for b in range(4):
                    HXc[(b * 4 + x) * 16 + ((k - A[a][b]) % 16)] |= 1 << r
                for j in range(3):
                    HXc[256 + (a * 3 + j) * 16 + ((k - A[j][x]) % 16)] |= 1 << r
    for b in range(4):
        for y in range(3):
            for k in range(16):
                r = (b * 3 + y) * 16 + k
                for x in range(4):
                    HZc[(b * 4 + x) * 16 + ((k + A[y][x]) % 16)] |= 1 << r
                for a in range(3):
                    HZc[256 + (a * 3 + y) * 16 + ((k + A[a][b]) % 16)] |= 1 << r
    return HXc, HZc

def rref_pivots(rows, ncols):
    R = rows[:]
    piv = {}
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(R)) if (R[i] >> c) & 1), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        for i in range(len(R)):
            if i != r and ((R[i] >> c) & 1):
                R[i] ^= R[r]
        piv[c] = r
        r += 1
    return R, piv

def reduce_vec(v, R, piv):
    for c in sorted(piv):
        if (v >> c) & 1:
            v ^= R[piv[c]]
    return v

def main():
    HXc, HZc = build_masks()
    wmask = 0
    for j in W:
        wmask |= 1 << j
    sx = sz = 0
    for j in W:
        sx ^= HXc[j]
        sz ^= HZc[j]
    assert sx == 0 and sz == 0, "W must be in ker HX and ker HZ"
    print("syndromes of W under HX and HZ: both 0")
    HZr = [0] * 192
    for j in range(400):
        b = HZc[j]
        while b:
            lsb = b & (-b)
            HZr[lsb.bit_length() - 1] |= 1 << j
            b ^= lsb
    HXm = [0] * 192
    for j in range(400):
        b = HXc[j]
        while b:
            lsb = b & (-b)
            HXm[lsb.bit_length() - 1] |= 1 << j
            b ^= lsb
    Rz, pz = rref_pivots(HZr, 400)
    Rx, px = rref_pivots(HXm, 400)
    assert reduce_vec(wmask, Rz, pz) != 0, "W must NOT be in rowspace(HZ)"
    assert reduce_vec(wmask, Rx, px) != 0, "W must NOT be in rowspace(HX)"
    print("W not in rowspace(HZ) and not in rowspace(HX)")
    print(f"QLOGICAL_W7_OK: weight-7 logical {W}; d(Q16) <= 7")

if __name__ == "__main__":
    main()
