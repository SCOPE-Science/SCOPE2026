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

# Reproducibility and verification

Run `python verify.py` in the directory containing the packaged files with the Python packages listed in `requirements.txt`. The test does not require network access or external data. The run completed successfully with the message `PASS: 700113 exact/numerical/direct randomized checks`.

The checker verifies the sketched-quotient cross-product factorization by symbolic expansion, evaluates the incomplete-beta integral independently of the hypergeometric series across ten row counts and five overlaps, checks the explicit one- and two-row formulas, compares the large-row normalization, and directly constructs shared Gaussian sketches for 700,000 trials using a fixed random seed. Each randomized comparison checks equality of the numerator sign and observed quotient order, with probability estimates compared to the exact formula using a documented six-standard-error allowance. Additional finite algebraic Gram examples check the sign orientation. Direct Monte Carlo evidence is finite and is not a substitute for the analytic gamma/Wishart and dominated-convergence arguments in `RESULT.md`.

The formulas use the modulus convention for the elliptic integral \(E(\rho)\), while SciPy's `ellipe` accepts the parameter \(\rho^2\). Special-function numerical evaluation can underflow for extremely large row counts in ordinary floating point; the verifier's stated finite range is explicitly tested. Independent external audit remains unperformed.
