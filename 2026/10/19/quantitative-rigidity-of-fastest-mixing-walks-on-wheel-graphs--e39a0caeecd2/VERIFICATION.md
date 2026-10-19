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

# Verification and scope

The analytic proof in `RESULT.md` is the evidence for the infinite-family claim; finite checks alone would not establish the theorem.

Run `python3 verify.py` with Python 3.9 or later, requiring no third-party packages. The script builds each trial wheel matrix from independently generated spoke and rim weights, checks nonnegative rows and symmetric stochasticity, diagonalizes with a separate Jacobi rotation implementation, and tests (i) the exact optimal spectral value for invariant matrices, (ii) the universal SLEM lower bound, and (iii) both quantitative root-mean-square edge bounds. The deterministic seed makes it reproducible.

Observed run: `VERIFY_OK 22532 finite assertions; wheel m=4..19`.

Numerical eigensolvers and trigonometric evaluations use floating-point tolerances. The script is not a formal proof, does not exhaust uncountably many edge assignments, and does not provide independent mathematical validation. The analytic spectral and Poincaré arguments address those quantifiers.
