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

# Verification of the hypersimplex small-resolution classification

Execute `python3 verify.py` in the directory containing this text. The script uses only exact integer and rational arithmetic and Python's standard library.

The checker verifies that, for each vertex cone of the samples \((n,k)=(4,2),(5,2),(6,2),(6,3)\), all maximal cones in both possible circuit triangulations have signed lattice determinant \(\pm1\). It then computes the number of chambers of the strict subset-sum arrangement for \((4,2)\) and \((5,2)\) by the exact Whitney subset formula and Zaslavsky's theorem, obtaining \(46\) and \(332\). The output is `VERIFY_OK: exact ray-basis determinants for (4,2),(5,2),(6,2),(6,3); central arrangement regions 46,332`.

The statement for arbitrary \(n\) and \(k\) follows instead from the signed-circuit triangulation and toric support-function proofs in RESULT.md. Finite verification does not certify the theorem in every rank and characteristic. No independent external audit has been performed.
