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
# Verification summary

The symbolic argument in `RESULT.md` directly derives the associator and proves the necessary and sufficient conditions for membership in the left, middle, and right nuclei. It computes the full nucleus via the action of the endomorphism on coset sums. The principal subtlety is resolved through support comparison in the proper-subgroup case, a test valid even in modular characteristic.

The standalone Python 3 verifier reconstructs the *original quandle operation* and its associators, rather than using the group-ring formulas as computation input. Modular Gaussian elimination yields the three separate nullities and their common nullity. The program covers all \(346\) specified cyclic and two-dimensional elementary-abelian cases; `VERIFY_OK` indicates that all predictions agree. For \(G=\mathbb Z/4\mathbb Z\) with \(\phi=-1\), it detects the full-nucleus dimensions \(0\) in characteristic \(3\) and \(2\) in characteristic \(2\). These tests are finite checks, not exhaustive verification for arbitrary fields and groups.

No independent audit has been performed. An equivalent older nucleus calculation formulated for twisted group-ring multiplications cannot be excluded absolutely.
