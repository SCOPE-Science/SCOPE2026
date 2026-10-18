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
# Reproducibility

Execute the standalone `verify.py` with a Python 3 interpreter from the same extracted directory. No data downloads or third-party packages are needed.

It computes the polynomial coefficients and sampling signs using exact `fractions.Fraction` arithmetic for all \(2\le d\le15\), verifies the exact three-regime polynomial \(Q_3\) and first three signs, and independently evaluates the first five majority probabilities by conditional binomial sums with 100-digit decimal precision. It tests the increment formula against those independently evaluated differences and checks both average competence and favorable latent mass exceed one half in the displayed example.

Observed output: PASS on each reported computation, with 175 exact sampled sign checks. The Rolle induction and the arbitrary-\(d\) construction are established in `RESULT.md`; this finite script is neither exhaustive over probability measures nor a replacement for the mathematical proof. The bibliographic comparison remains subject to the inaccessible full text of Berend and Sapir (2007).
