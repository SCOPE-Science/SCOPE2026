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

# Verification and reproducibility

Run `python3 verify.py` in the extracted file directory, using Python 3.10 or later and no third-party packages. The program runs exact Fraction arithmetic on independently enumerated compatible permutation allocations for eleven finite multilayer examples, verifies the eigenvalue determinant reduction, and tests the specialized two-layer determinant identity. Numerical computations further check the constant-term asymptotic for nine two-layer and seven additional profiles, including three- and four-layer cases. Successful completion prints `CHECK_OK_MULTILAYER 27`.

Analytical proof dependencies are: the standard order-statistic second-moment identities, the finite block contrast calculation, the Brownian-bridge Riemann sum limit, and Stirling's formula. The verifier checks examples rather than proving any of the infinite-dimensional asymptotic assertions. The statement and proof require strictly positive layer sizes; the asymptotic requires a fixed number of layers with positive limiting proportions.

No independent audit has been conducted.
