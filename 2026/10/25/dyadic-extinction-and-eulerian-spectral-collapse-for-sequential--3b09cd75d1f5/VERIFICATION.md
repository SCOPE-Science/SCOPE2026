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

The standalone `verify.py` uses only the Python standard library. It reconstructs every sweep matrix for sizes 3–7 and directly expands the characteristic determinant by a subset dynamic program, independently of the matching-cycle derivation. It checks the orientation count, all characteristic-polynomial classes, Eulerian multiplicities, and nilpotency by powering the actual matrix. It also runs reproducible samples in dimensions 8, 9, 10, 11, 12, 16, and 20. A separate exact count of the 8-site balanced orders returns 19,328. The analytical proof, not these bounded tests, establishes all dimensions.

The program has been executed successfully from this package. Limitations: no finite collection of examples proves the universal quantifiers, and the result does not classify the finer periodic-point or nilpotency-index distributions within a spectral class.
