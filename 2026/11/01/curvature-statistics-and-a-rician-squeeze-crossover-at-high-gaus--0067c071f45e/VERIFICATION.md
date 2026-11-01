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

The theorem's proof is in `RESULT.md`. It identifies the Kac–Rice Palm density exactly and proves the weak-convergence assertions by conditional density limits and real symmetric eigenvalue perturbation. The supporting standalone Python 3 checker is `checker.py` (standard library only). Execute `python3 checker.py` in a directory containing this file. A successful execution prints `PASS: 79 supplementary assertions including independent weighted samples`.

Checks include: normalization and a closed tail for \(|c|^2\), exact algebra converting this into the curvature condition-number tail, a Gamma integral, equality of the analytic and matrix-eigenvalue formula at zero squeeze, numerical comparison of the finite-height, height-conditioned squeezed eigenvalue ratios with their near-critical Rician scaling for various positive and negative squeeze parameters, and independent Kac–Rice importance-weighted sample checks. The random generator has a deterministic local seed and the assertions are reproducible.

Finite simulations do not prove asymptotic convergence, generic nondegeneracy or historical novelty. The proof requires Gaussian whiteness and the usual smooth-field Kac–Rice hypotheses; these are fulfilled for the entire-function Gaussian field. Full independent mathematical audit and experimental replication have not been performed.
