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

# Verification scope and reproducing the checks

The mathematical proof appears in `RESULT.md`. Its critical steps are the exact one-clock Laplace transform, renewal reduction, the hyperbolic-sine canonical product, the inequality \(Q_2/Q_1^2\leq2/5\), and strict positivity of the blind-rate second derivative. The arguments apply to every allowed continuous parameter; no finite run can replace them.

Run `python3 check_hybrid.py` using Python 3's standard library. The script separately evaluates a two-region backward mean boundary-value solution and the renewal expression, samples curvature and the product-inequality margin, checks the threshold signs, and compares the near-critical optimizer with the analytic asymptotic coefficient. On the supplied program's test cases, it reports `PASS: 5325 finite diagnostics` with critical dimensionless strength `1.479815748755145` and optimizer slope `3.465571330427`.

A diagnostic run does not independently certify the analytic proof, publication priority, or behavior outside tested numerical parameters. No external mathematical certification or independent scientific audit has been performed.
