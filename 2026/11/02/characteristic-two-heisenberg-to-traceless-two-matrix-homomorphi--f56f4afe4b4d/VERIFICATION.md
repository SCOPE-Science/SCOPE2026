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

The enclosed `verify.py` directly enumerates all linear maps from the three- and five-dimensional Heisenberg Lie algebras to traceless two-by-two matrices in the specified finite fields, using full generator-relation checks and separate candidate-condition checks. Exhaustive cases are \((n,q)=(1,2),(1,3),(2,2),(1,4)\). Expected map counts are \(64,105,736,4096\), respectively, and the script checks their image-rank distributions. A successful run prints `HEISENBERG_TO_SL2_HOM_OK 4 exhaustive field/rank cases`.

No finite enumeration establishes the general theorem. The general field and unbounded-rank arguments use the rank of an alternating two-form and determinantal geometry. The potentially nonreduced homomorphism scheme for characteristic two and Heisenberg rank at least two is outside the claim. Independent audit: not performed.
