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

# Reproducibility checks

Execute `python verify.py` using a standard Python 3 installation. The program performs exhaustive edge-mask enumeration of graphs on three, four and five vertices; it computes degree-class/motif covariances directly with exact `fractions.Fraction` arithmetic and compares them with an independently coded conditional-probability formula. Patterns include an edge, a path, a triangle, an edge plus an isolated vertex, and an empty three-vertex graph. Five rational edge probabilities and all degrees are checked, with additional exact sign and equality checks for induced and non-induced paths. Expected outcome: `PASS: 608 exact rational independent enumeration/formula comparisons and sign assertions`.

This finite enumeration is a replay check for small cases, not a proof that the formulas hold for all graph orders. The all-order proof uses independent-edge conditioning and a strictly decreasing sign function. No independent external validation has been performed.
