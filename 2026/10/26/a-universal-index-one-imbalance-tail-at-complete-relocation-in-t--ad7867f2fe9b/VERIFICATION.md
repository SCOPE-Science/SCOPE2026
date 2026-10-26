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

# Reproducibility and analytical limits

Run `python3 verification.py` with a standard Python 3 interpreter. Its output is recorded in `verification_output.txt`. The script checks the ancestor-family smoothing identity against direct numerical integration, the analytic joint-transform factorization, and exact finite-step probability conservation and reflection symmetry for the original walk. It additionally tests the low-order characteristic-function moment coefficients. Those checks are **not** an infinite-time proof; the proof depends on the martingale convergence theorem, the exponential-Yule branching decomposition, uniqueness of the smoothing-transform solution, Laplace inversion, and the tail sandwich, as written in `RESULT.md`.

For the actual walk, before the first relocation the random initial urn state is one origin ball and an independent optional fair-signed side ball with Bernoulli parameter \(a\). This boundary condition is essential: omitting it changes the exact transform and removes the leading index-one heavy tail. The side-seed correction is verified independently in the finite-state original-walk recursion. No external certification or independent audit is asserted.
