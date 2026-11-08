---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Write W increments D_i independent N(0,1/n). Constraint W_((i+1)/n)−2W_(i/n)+W_((i−1)/n)=0 is exactly D_(i+1)=D_i; Gaussian conditioning at zero projects each independent block onto its constant-increments one-dimensional subspace. Block endpoint sums have independent N(0,length/n) Brownian increments, grid nodes become affine interpolants I_(F_n)B. Original independent fine-grid Brownian bridges survive constraints, with max tail <=2n exp(−2nu²). For any Hausdorff F_n→F, uniform continuity of affine interpolation for continuous f gives I_(F_n)B→I_F B pathwise and bridges vanish, so Q_n weakly converges. Every closed F containing endpoints is grid-approximable. d_H(F_n,[0,1])=δ_n/2 proves sufficiency; macroscopic surviving gap gives a subsequential law with deterministic affine paths on an interval, unlike Wiener, proving necessity. Any nonempty constraint yields finite-n singularity; covariance is Brownian covariance minus independent gap bridge. Independently checked Gaussian Schur complement conditional covariance for every subset of n−1 adjacent second-difference constraints with n=2..6 and continuous midpoint witnesses; finite tests do not replace the tightness/converse proof.

## originality

PASS

Raket 2026 Section 7 Corollary 7.4 handles a single shrinking fixed finite-difference observation and vanishing effect; it is not a many-simultaneous-overlapping-observation result. Wilson et al 2021 provides a general pathwise Gaussian conditional representation, not this exact contiguous-block and closed-set Hausdorff subsequence classification in inspected portions. Resultary Brownian searches found separate path-conditioning questions. This is best-of-knowledge novelty for the sharp δ_n iff and complete weak limit family.

## value

PASS

Sharp necessary-and-sufficient cluster-size criterion for conditioning infinitely many Brownian second differences and complete closed-set limit classification are natural Gaussian process/weak convergence statements. It highlights finite singularity coexisting with weak Wiener convergence and identifies exact covariance of every possible non-Wiener limit. The result is structural and nontrivial, not a mere one-point conditional covariance example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
