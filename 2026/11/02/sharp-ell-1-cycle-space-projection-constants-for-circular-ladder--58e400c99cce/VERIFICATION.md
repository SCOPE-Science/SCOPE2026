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

# Verification of the circular-ladder circulation projection theorem

Run `python3 verify.py` using Python 3's standard library. The script uses exact rational arithmetic for the explicit cycle vectors and projection matrices. It checks, for every integer \(10\le n\le30\), that every constructed edge-basis column is divergence-free, that all column \(\ell_1\) norms equal \(12/5-16/(5n)\), and that the operator fixes all \(n\) square cycles and the independent global rim cycle. It also checks the two exact cyclic coefficient-class norms and 400 fixed-seed arbitrary-coefficient instances of the universal lower inequality.

Recorded execution:

`CHECK_OK exact_projection_and_norm_assertions= 2122 dimensions=10..30 random_lower_inequality_samples=400`

The proof for all integers \(n\ge10\) is analytic. In particular, the crucial lower certificate is \(4H+V\ge12-16/n\) for any invariant projection and the upper certificate is the explicit operator attaining equality. The numerical or finite exact checks do not establish this infinite statement or historical novelty. No Lean, external certificate, independent audit, or expert verification is claimed.
