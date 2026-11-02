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

The independent-verification channel is unperformed. The reproducibility artifact `verify.py` requires only Python 3 and its standard library; run `python verify.py` in the same directory as this document.

The program constructs finite fields of orders \(3,5,7,9,11,13,25,27,49\), explicitly enumerates the \(q^2\) repeated-root monic cubics in each field, counts their intersections with shifts of degree two, and independently checks the quadratic-character formula and the exact mean and variance over each complete set of constant-coefficient shifts. Successful execution returned `VERIFY_OK fields=9 shifts=293 independent_repeated_cubic_sets=yes means_variances=exact`.

The proof is the universal symbolic argument in `RESULT.md`, not the finite experiment. Hasse's theorem is used only to bound the elliptic trace, not to prove the exact count. No computer-assisted infinite proof or independent expert assessment is claimed.
