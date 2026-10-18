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

# Exact reproducibility
Execute `python3 VERIFY.py` with Python 3 and no third-party dependencies. The output terminates with `VERIFY_OK` if and only if all assertions hold.

The source code reconstructs the six small-case polynomials by two different exact methods (explicit formula and Stern recurrence), differentiates with integer coefficients, constructs rational Euclidean Sturm sequences, computes the number of real roots from the infinite-end sign variations, and tests positive derivative values. It checks the rational negative-derivative identity against direct polynomial differentiation for several larger indices and proves the finite rational inequalities at the base case \(k=14\). The universal negative conclusion for all even \(k\ge14\) additionally uses the transparent analytic ratio estimate from the proof, not merely sampled cases.

All arithmetic is exact (`fractions.Fraction`). No external solver, external validation, or infinite computation is claimed. The theorem concerns the fixed parameter slice \(n=3\) and makes no claim about subsequent fixed-\(k\) values of \(n\).
