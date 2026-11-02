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

Run the packaged `verify.py` with Python 3, without third-party dependencies. The script checks the displayed generator equations and boundary laws using exact fractions at 16 positive rational reversal parameters, and separately expands the published first-passage Laplace transform using exact power-series arithmetic. It isolates the quartic and cubic positive roots with rational bisection intervals narrower than \(10^{-9}\).

Expected output: `VERIFY_OK: 16 exact-rational independent parameter checks; 0.975331842868 3.168966855139`.

These checks corroborate but cannot replace an analytic all-parameter proof. The theorem's quantifiers follow from explicit polynomial solutions of the backward equations, strict convexity of the mean and variance, uniqueness of positive roots under Descartes' rule, and direct derivative sign factorization for squared relative uncertainty. There is no Lean proof, external expert assessment, or independent audit in this package.
