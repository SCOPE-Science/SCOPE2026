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

# Reproduction
The self-contained accompanying \(`verify.py`\) reads no external research files. Run with Python 3 and NumPy, SciPy and SymPy: \(`python verify.py`\).

It constructs complete weighted Laplacians from all individual edges; checks the direct eigenvalue formula against the analytic optimizer and budget; tests the exact \(n=4\), \(\tau\ge2\), \(B=1\) algebraic allocation and objective symbolically; computes marginal derivatives from the full shifted Laplacian inverse; and compares random asymmetric feasible allocations plus direct constrained nonlinear optimization against the theorem value.

All floating-point comparisons are finite tests with explicit tolerances. They do not prove statements over all integers, prices or budgets. The mathematical certificate is the strict-convexity and equality-case argument in RESULT.md. In particular, no statistical sample is treated as an exhaustive optimization proof, and no independent audit has occurred.
