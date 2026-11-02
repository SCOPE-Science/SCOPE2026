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

The theorem is proved by a characteristic-free block-rank decomposition of the multiplication Gram matrix and a finite-field branch-height enumeration. The provided standalone Python program builds all algebra multiplication tables directly; its explicit finite-field Gaussian elimination produces the 18 complete rank distributions, including extension-field cases, and checks each reduced rank-locus set equality pointwise.

Run `python verify_multibranch_forms.py`. Observed terminal marker: `MULTIBRANCH_ASSOCIATIVE_PAIRING_RANKS_OK 18`. Cases: the exponent vectors `(2,2)`, `(2,3)`, `(3,3)`, `(2,2,2)`, `(2,2,3)` over fields of orders 2, 3 and 4; `(2,3,3)` over orders 2 and 3; and `(2,2,2,2)` over order 2. This finite enumeration does not prove the general theorem; that proof is in RESULT.md.

Only the reduced rank loci are classified. No assertion is made about determinantal scheme structures, homothety classes or arbitrary local Artin algebras. Independent validation has not been performed.
