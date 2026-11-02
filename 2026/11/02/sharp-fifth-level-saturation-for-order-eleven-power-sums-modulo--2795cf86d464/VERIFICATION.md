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

# Verification record

Execute `python3 verify_order11.py` alongside the manuscript. The program is self-contained, generates the exact list of admissible primes below 2155, produces order-eleven residues by modular exponentiation, visits all 352715 nonnegative coefficient vectors of total weight between one and ten at each of 31 moduli, and asserts the claimed minima. It verifies the exceptional witnesses explicitly and independently enumerates multisets of length at most four for four sample prime cubes.

Expected output:

```
VERIFY_OK primes=29 levels=31 coefficient_vectors=10934165 k3_exception=23:9 k4_exception=23:9 k5_all=11
WITNESS p=23 k=3 length=9 q=12125 counts=0,0,1,0,2,0,0,4,1,0,1
WITNESS p=23 k=4 length=9 q=60793 counts=0,0,1,0,2,0,0,4,1,0,1
```

The mathematical argument additionally requires irreducibility of the eleventh cyclotomic polynomial, the standard integer resultant Bézout identity, and uniqueness of the order-eleven subgroup in the cyclic unit group of an odd prime power. The finite code does not certify these standard facts; their consequences are proved explicitly in the manuscript. No external verification or independent audit is claimed.
