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

# Reproducibility and mathematical limits

Run `python3 verify.py` with Python 3.9 or newer; no packages or network access are needed. The script derives conditional edge-pair moment sums independently of the simplified symmetric-polynomial expressions and tests 21,844 exact-rational positive-length vectors for up to seven petals. It verifies the three-petal differential identity on a 25-node rational interpolation grid; because both sides have degree at most four in each free coordinate, those exact evaluations establish the polynomial identity. It also tests the explicit four-petal majorization witness and the stated raw-moment and variance differences, and checks differential coefficients at equal lengths and at the critical boundary.

The infinite-dimensional quantifiers over all positive petal lengths, and the positivity of the Schur-transfer coefficients for every admissible parameter, are established by the written analytic inequalities in RESULT.md. Finite checking is not a substitute for those proofs. No claim about the absolute minimum of variance when there are four or more petals, or about other metric graphs, is verified. No independent review is asserted.
