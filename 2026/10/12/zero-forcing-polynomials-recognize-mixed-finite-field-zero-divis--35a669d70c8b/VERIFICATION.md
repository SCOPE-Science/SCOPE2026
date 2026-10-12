---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone `verify.py` artifact was read from its actual packaged path before replay.

It exhausts all at-most-one-white support profiles in representative mixed binary/nonbinary products through four factors, computes Boolean-disjointness quotient ranks exactly through six factors, and enumerates every vertex subset for four small mixed products to reproduce the complete zero forcing polynomial.

It independently reconstructs adjacency by coordinatewise multiplication in three products of prime fields and replays the root-multiset recovery algorithm on repeated and unequal field orders. It also checks the pure-binary two-factor failure boundary.

Exact replay output:

```text
profile theorem (2, 3): 4 profiles
profile theorem (2, 2, 3): 64 profiles
profile theorem (2, 3, 3): 64 profiles
profile theorem (2, 2, 2, 3): 16384 profiles
profile theorem (2, 2, 3, 5): 16384 profiles
quotient rank r=2: 2
quotient rank r=3: 6
quotient rank r=4: 14
quotient rank r=5: 30
quotient rank r=6: 62
full polynomial (2, 3): N=3, Z=1, coeff_min=2
full polynomial (2, 2, 3): N=9, Z=3, coeff_min=8
full polynomial (2, 3, 3): N=13, Z=7, coeff_min=64
full polynomial (2, 2, 5): N=15, Z=9, coeff_min=64
direct product (2, 3): vertices=3
direct product (2, 2, 3): vertices=9
direct product (2, 3, 5): vertices=21
recover (2, 3): r=2, binary=1, unit_product=2, fields=(2, 3)
recover (2, 2, 3): r=3, binary=2, unit_product=2, fields=(2, 2, 3)
recover (2, 3, 5): r=3, binary=1, unit_product=8, fields=(2, 3, 5)
recover (2, 2, 3, 4): r=4, binary=2, unit_product=6, fields=(2, 2, 3, 4)
recover (2, 2, 2, 3, 5): r=5, binary=3, unit_product=8, fields=(2, 2, 2, 3, 5)
pure binary boundary F2xF2: {1: 2, 2: 1}
VERIFY_OK
```

The computations are finite corroboration. The arbitrary-factor theorem is established by the two-stage support forcing proof, the Boolean quotient determinant argument, and exact subset-product inversion.
