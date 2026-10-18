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

# Reproduction and limits

Run `python3 verify_zinbiel.py` in a directory containing that standalone file. Python's standard library is sufficient.

The program constructs the finite field from either a prime field or an explicit monic irreducible polynomial; constructs the four-dimensional Zinbiel multiplication using integer binomial coefficients reduced modulo the characteristic; obtains the images of \(e_2,e_3,e_4\) by actual iterated multiplication from each possible image of \(e_1\); checks the defining relations for all basis pairs; and enumerates orbits of \(\langle e_2,e_3,e_4\rangle\) under every possible restriction of an automorphism. It then adds the one orbit with nonzero \(e_1\)-coefficient, whose transitivity is proved in `RESULT.md`.

Verified field orders: \(2,3,4,5,7,8,9,11\). Verified orbit counts respectively: \(7,11,13,9,9,19,25,7\). The program prints `VERIFY_OK` on success. The exhaustive checks cover only these finite fields; the characteristic-uniform proof is symbolic and is contained in `RESULT.md`.

No independent external audit or machine-formal infinite-field proof has been conducted.
