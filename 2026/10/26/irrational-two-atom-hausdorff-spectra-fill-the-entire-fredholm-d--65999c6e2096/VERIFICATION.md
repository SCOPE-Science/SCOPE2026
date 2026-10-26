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

The result is an analytic theorem with no computational prerequisites. To reproduce the proof, first check the affine identity \(1-\psi_t(z)=e^{-t}(1-z)\); it gives \(T(t)(1-z)^{-s}=e^{ts}(1-z)^{-s}\). The cited 2026 preprint contains the needed Hardy \(H^1\) and Dirichlet \(D^1\) semigroup estimates, the \(J:D^1\to A^1\) similarity, and both BMOA/Bloch predual transfers. The binomial theorem gives the upper bound.

For the reverse bound, pick any complex \(\lambda\) with \(0<|\lambda|<ae^u+be^v\), solve a one-dimensional positive exponential equation, and verify the strict triangle inequalities. Select non-collinear phases. Check that \(G'(x)\ne0\), then use classical density of an irrational linear flow on the two-torus followed by Rouché's theorem on a disk lying in \(\operatorname{Re}s<1\). Each sufficiently good phase return creates another distinct **exact** eigenvalue parameter, not an approximate eigenvalue. Powers of \(1-z\) produce independent eigenfunctions. Fredholmness and closedness complete the conclusion.

The argument does not depend on numerical observations, finite simulations, code execution, a publisher full-text claim not actually inspected, or an independent audit. The full text of the earlier 2024 generalized-Hausdorff paper was not available for a decisive priority comparison.
