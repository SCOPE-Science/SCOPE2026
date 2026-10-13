#!/usr/bin/env python3
"""Independent exhaustive set-packing census by output-bitmask dynamic programming."""
N = 6
RX_SIZE = 1 << (N-2)
MASK_LIMIT = 1 << RX_SIZE
# Encode a word as an integer, left-to-right most significant first.
def burst_mask(x):
    receivers = 0
    for j in range(N-1):
        top = x >> (N-j)
        bottom = x & ((1 << (N-j-2))-1)
        recv = (top << (N-j-2)) | bottom
        receivers |= 1 << recv
    return receivers
masks = [burst_mask(x) for x in range(1 << N)]
assert len(set(masks)) == 64
best = [-1000] * MASK_LIMIT
ways = [0] * MASK_LIMIT
best[0], ways[0] = 0, 1
for word_mask in masks:
    bnew, wnew = best[:], ways[:]
    for occupied in range(MASK_LIMIT):
        if best[occupied] < 0 or (occupied & word_mask): continue
        newmask = occupied | word_mask
        sz = best[occupied] + 1
        if sz > bnew[newmask]:
            bnew[newmask], wnew[newmask] = sz, ways[occupied]
        elif sz == bnew[newmask]:
            wnew[newmask] += ways[occupied]
    best, ways = bnew, wnew
maximum = max(best)
number = sum(c for size,c in zip(best,ways) if size == maximum)
assert (maximum,number) == (8,2), (maximum,number)
print('DP_VERIFY_OK max=',maximum,'exact_labeled_optima=',number,'states=',MASK_LIMIT)
