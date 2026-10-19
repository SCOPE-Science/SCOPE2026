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

# Verification instructions and exact scope

Run `python verify.py` with NumPy installed (NumPy 1.24 or newer). The program constructs seven explicit connected positively weighted bipartite graphs, computes the top Laplacian eigenpair and quartic coefficient, and uses Newton iteration in an orthonormal basis of the sum-zero space to solve the local period-two equation.

Four positive values of \(\mu=h\lambda-2\) are tested on each graph. Each calculated pair is checked against its two-cycle equation, leading square-root amplitude, transverse remainder, full quotient Jacobian spectral radius, and critical-multiplier expansion. The program also samples 500 phase vectors per graph at the threshold and compares the actual potential before and after one step. Its expected final line is:

`VERIFY_OK: 7 connected positive-weight bipartite graphs, 3689 checks`

The graph examples include a single edge, a five-vertex weighted path, a six-vertex weighted star, a six-vertex weighted even cycle, two complete bipartite graphs with nonuniform weights, and a nine-vertex weighted path. All values are floating-point numerical checks; the tests are neither exhaustive over graphs nor a proof of strict descent for all states. The proof of spectral simplicity, endpoint strictness, analytic branch existence, and return-map attraction is given in `RESULT.md`, including the unrestricted quantifiers and asymptotic error terms. No independent audit has been performed.
