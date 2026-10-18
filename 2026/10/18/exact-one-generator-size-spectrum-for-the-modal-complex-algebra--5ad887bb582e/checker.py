#!/usr/bin/env python3
"""Finite but exact exhaustive tests of the ultimately constant cases."""
from itertools import product

def closure(prefix):
    # Coordinates 0,...,L-2 are finite points; L-1 is an infinite constant tail.
    L=len(prefix)
    full=(1<<L)-1
    gen=sum(v<<i for i,v in enumerate(prefix))
    def diamond(z):
        if not z: return 0
        return (1<<z.bit_length())-1
    vals={0,full,gen,gen^full}
    while True:
        larger=set(vals)
        larger.update(full^v for v in vals)
        larger.update(diamond(v) for v in vals)
        larger.update(a&b for a in vals for b in vals)
        if larger==vals: break
        vals=larger
    # Points lie in the same Boolean atom iff no generated element separates them.
    signatures={tuple(int(bool(v&(1<<i))) for v in sorted(vals)) for i in range(L)}
    return len(vals),len(signatures)

tests=0
for L in range(1,9):
    for prefix in product((0,1),repeat=L):
        switches=sum(prefix[i]!=prefix[i-1] for i in range(1,L))
        sz,atoms=closure(prefix)
        assert (sz,atoms)==(1<<(switches+1),switches+1), (L,prefix,sz,atoms)
        tests+=1
print('OMEGA_MODAL_ONEGEN_VERIFY_OK',tests)
