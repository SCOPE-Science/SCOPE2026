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

The analytical argument uses four reproducible steps: (1) diagonalize the direction-weighted cube Laplacian on Walsh characters, (2) insert \(1/a=\int_0^\infty e^{-at}\,dt\), (3) use strict positivity of every factor \(1\pm e^{-c_kt}\) for \(t>0\), and (4) sum absolute matrix entries over each input direction before maximizing the row sums. For positive weights this proves the sharp norm, the sign law and all equality/limit statements, without numerical approximation.

`verify.py` reconstructs a grounded weighted Laplacian and its Green inverse in Python's standard-library `fractions.Fraction`; it builds the full edge projector by incidence products, **not** by using the Walsh formulas. It checks for every edge and input direction the exact absolute row mass, the strict entry signs, matrix symmetry, idempotence and the final row norm. Cases: dimensions one through five, twelve square-integer conductance patterns. Expected successful output: `PASS total 31006 exact-rational assertions over 12 graphs`.

The finite checks corroborate—but do not certify—the universal result. In dimension one, only the routine boundary identity is checked; the theorem about nontrivial amplification and its complete range requires dimension at least two. Verification is an in-package reproducibility exercise, not an external audit or a proof of historical originality.
