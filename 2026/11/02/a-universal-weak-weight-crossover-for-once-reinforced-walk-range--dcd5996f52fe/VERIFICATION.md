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

# Verification record

The analytical argument in `RESULT.md` provides the mathematical proof. Its finite-dimensional components are independently checked using only Python's standard library by `checker.py`. Run `python checker.py` in the directory containing the accompanying files and compare with `checks.txt`.

The verifier performs **608 assertions in total: 584 exact-rational assertions and 24 deterministic numerical convergence comparisons**, comparing direct finite-state enumeration and an independently computed geometric excursion renewal distribution for both the full line and reflected half-line, with independently solved discounted first-hitting equations. It also evaluates finite-size convergence examples from the exact product transform in critical and weak-weight regimes. The exact counts, source, and sample numerical results are included as reproducible attachments.

The finite computations establish only the tested identities and examples. The asymptotic theorems require the independent mathematical proof: uniform logarithmic product bounds, Laplace convergence, and inversion using Brownian first-passage distributions. Historical priority is not certified, and no independent audit or external validation has been performed.
