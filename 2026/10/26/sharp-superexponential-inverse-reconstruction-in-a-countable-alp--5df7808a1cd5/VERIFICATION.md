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

The analytic proof gives a coordinatewise finite inverse and a conditional Bayes lower bound for every fixed radius. For geometric rank probability \(p_n=(1-q)q^n\), the rank-cylinder probabilities sum to an exact geometric series. The term at degree \(R^2\) in the logarithm is \(\tfrac12\log q\).

`CHECK.py` was executed with Python 3 and standard-library exact `Fraction` arithmetic. It checked \(32{,}768\) five-site inversion instances with bounded ranks; finite-support tail formulas at three rational choices of \(q\) and five depths; and independently enumerated Bayes posterior masses for radius zero, one, and two under a truncated geometric rank law. The captured `CHECK_OUTPUT.txt` ends in `CHECKS_PASS`.

These finite computations do not assert an infinite proof, global priority, or external certification. Independent audit is not performed. The probability/error optimization presupposes independent ranks and conditionally iid fair output data, and is specifically same-input fixed-window prediction.
