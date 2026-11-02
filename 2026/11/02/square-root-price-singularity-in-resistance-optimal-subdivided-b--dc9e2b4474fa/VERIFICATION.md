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

# Verification of the two-price subdivision theorem

Run `python verify.py` with the versions stated in `requirements.txt`. A successful execution prints `ALL_OK: 63 test groups; complete Laplacian checks, root minimizers, symbolic derivatives and asymptotics`.

The implementation constructs the full weighted Laplacian on the edge-subdivided biclique, diagonalizes it numerically and compares the resulting nonzero reciprocal eigenvalue sum against the derived exact rational-function formula. It also evaluates stationary roots, tests strict local optimality by perturbations, checks a symbolic trace identity and the critical-profile derivative, and tests both fixed-price and critical-window asymptotics at finite sizes.

The 63 groups passed on a clean execution of the packaged script. The finite matrix and asymptotic tests are not exhaustive across arbitrary graph sizes or a substitute for the mathematical proof; the unrestricted allocation assertion relies on strict convexity and graph automorphisms, and the asymptotic claim relies on algebraic limiting arguments.
