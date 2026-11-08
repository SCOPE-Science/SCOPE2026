---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For fixed t>0 and real C^3 mean-zero h, the radial-squared perturbation has area pi*t and the top-two Fock Toeplitz eigenvalue sum admits an O_{t,h}(|epsilon|^3) expansion. The exact disk eigenvalues lambda_n=1-e^{-t} sum_{j=0}^n t^j/j! decrease with isolated gap lambda_1-lambda_2=e^{-t}t^2/2. Differentiating the coherent-state trace-class integral gives T_1(n,m)=e^{-t}sqrt(a_n a_m)*hhat_{m-n}; isolated-cluster perturbation cancels occupied-plane mixing. Direct second order term -t e^{-t}sum|hhat_k|^2 and cross-cluster gaps give the coefficient D_k(t). D_1=0, D_2=t(3+2t)/((t+2)(t+3))>0 and D_k strictly increases to t via decreasing Poisson-tail ratios. The trace-class remainder and fixed smooth h justify the infinite sum. Independent exact SymPy D2 and Dk monotonic samples plus separate finite-section quadrature at t=1, k=1,2,3,5 agree with quadratic coefficients to <4e-7. Finite matrices alone do not prove the infinite claim; no global shape optimality is asserted.

## originality

PASS

Rank-two nonradial disk Hessian is not a consequence of known rank-one stability or circularly symmetric Ky-Fan inequalities. The 2026 peer-reviewed Nicola–Riccardi–Tilli article is explicit that the disk maximization is shown among circularly symmetric sets; its source work leaves nonradial problems open. Prior 2017 accumulated-spectrogram formulas supply the disk spectrum but not this cross-cluster shape Hessian.

## value

PASS

The sum of the two largest Fock localization eigenvalues is an intrinsic orthonormal-pair concentration objective. An open nonradial issue motivates testing the disk against all angular Fourier modes. The exact positive transverse Hessian, translation null mode and sharp quadrupole constant are structural, nontrivial information not contained in the known circularly symmetric K-sum inequality or the top-one Faber–Krahn theorem; the result is expressly local and fixed-deformation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
