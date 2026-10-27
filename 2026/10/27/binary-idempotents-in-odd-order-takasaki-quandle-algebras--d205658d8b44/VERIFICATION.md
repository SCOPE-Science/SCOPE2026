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

# Reproducible checks

Run `python3 verify.py` using Python 3 standard library. An independently written coefficient-mask multiplication census checks each odd cyclic size 1, 3, 5, 7, 9, 11, 13, 15 against the GF(2) reciprocal-irreducible factorization count. A separate Cartesian-coordinate table checks the nine-element group \(C_3\times C_3\). The complete transcript from the executable test ends with `VERIFY_OK` and the exact results 2, 8, 12, 16, 80, 68, 132, 768 and 512. These are exhaustive finite tests, not a proof for unbounded groups.

The mathematical proof is the independent justification for arbitrary odd-order finite abelian groups: it reduces the nonassociative square to \(x^*x^2\) in a semisimple binary group algebra and solves every involution orbit component. Characteristic two, odd group order, and the inclusion of zero are essential conventions.
