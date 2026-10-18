---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For centered Y=P(x-X1)/Delta the selected-pair contraction Aij=I-mu(ei-ej)(ei-ej)^T and centered pair noise yield exact conditional squared-norm drift E[S_{k+1}|Y]=[1-4mu(1-mu)/(N-1)]S+2(N-1)/N under constant utility, with unique stationary second moment (N-1)^2/[2Nmu(1-mu)]. The exact random-pair quadratic difference average is 2S/(N-1); the fast mean is (N-1)/[Nmu(1-mu)]. For nonlinear smooth log U, pair bias is tanh[(ell_j-ell_i)/2], and near-consensus localization by fourth moments makes rejected interactions negligible on k=O(Delta^-2). A centered-fast-observable telescoping/martingale estimate replaces pair squares by stationary moment; Gaussian selected-pair mean noise gives diffusion coefficient 1/N under accelerated time s=kDelta²/N. The drift is (N-1)ell_prime/[N(1-mu)], hence the integrable invariant Gibbs density has exponent (N-1)/(1-mu). Independent exact-rational contraction/mean-drift tests for N=2,3,5,10 and mu=1/4,1/2,3/4 corroborate coefficients, not the functional CLT. Hypotheses ensure Lipschitz drift and a unique diffusion; finite-horizon limitation is honored.

## originality

PASS

Siebenmorgen–Restrepo arXiv:2605.21844v1 original Eq.(15) and Appendix F use approximate pair decorrelation, yielding N/(1-mu). The exact finite-population projection covariance and rigorous fixed-N weak-noise path limit are not supplied there. The N-1 shift is a genuine different statement at every fixed N; it vanishes relatively as N grows and is not falsely presented as contradicting the original leading approximation. Gossip with stubborn agents and stochastic approximation does not dominate the same utility-driven fixed-N finite-horizon theorem.

## value

PASS

Exact finite-population correction determines the invariant law of the limiting diffusion in a widely motivated stochastic interaction model and separates a rigorous weak-noise statement from a heuristic large-N closure. This changes quantitative prediction at small N (e.g., N=2), supplies a natural covariance identity, and proves concentration failure probability vanishes on finite horizons; importance does not rely on full stationary interchange.

The dated certificate retains the supplied scientific assessment, sources and limitations.
