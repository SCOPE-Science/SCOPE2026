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

# Verification

The analytic argument in `RESULT.md` establishes the general statement through a weighted Matrix–Tree determinant, an explicit categorical-occupancy representation of all excess degrees, and a covariance row-sum identity. No unproved conjecture is invoked.

`python verify.py` runs with the Python standard library. Its two independent calculations use (i) ordinary Prüfer codes to enumerate valid complete-multipartite spanning trees and sum observed integer degrees and leaves, and (ii) exact rational categorical-occupancy formulas predicted by the determinant factorization. Eight graph families of up to seven vertices compare counts and every marked covariance. A further finite grid checks extreme-part sign logic. Current execution result: `PASS 165 exact assertions`.

The exact finite computations establish the listed test cases, not a proof for unbounded part sizes. The displayed determinant reduction, conditioning identity, and strict probability comparison supply that proof. A historical-priority search cannot provide independent audit or guarantee no earlier implicit derivation.
