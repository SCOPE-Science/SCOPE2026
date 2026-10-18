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

For iid positive H compactly supported within (0,2), T(h)=[[1,h],[-h,1-h²]] has determinant 1 and positive invariant S_h=[[1,-h/2],[-h/2,1]]. Its covariance map F(S)=E[TSTᵀ] has positive-definite primal and dual eigenmatrices: normalized Brouwer eigenmatrices cannot be rank-one because every T(h) lacks a real eigenline. Strict determinant-root concavity at equal positive determinant forces r≥1, with equality only when every support step preserves one and the same S_h, i.e. constant H. The positive dual eigenmatrix gives the claimed uniform two-sided c r^n ≤ E||z_n||² ≤ C r^n and identifies r with the spectral radius of the explicit third-order covariance matrix. Exact symbolic independent checks reproduced S_h invariance, perturbation matrix and coefficient 2h²/(4-h²), and rational example polynomial 64r³−66r²+49r−49 with leading real root ≈1.01797185386451. Fixed constant h gives bounded powers. Infinite horizon is analytic, not extrapolation from finite experiments.

## originality

PASS

The motivating random-time-step method gives conditional finite/polynomial-horizon estimates and symplecticity, not a universal all-horizon mean-square spectral dichotomy. Deterministic varying-step parametric resonances and continuous random oscillator Lyapunov exponents use different hypotheses or statistics. The new part is the exact iid-step criterion, four-moment rate and perturbative coefficient for this update; general matrix-products theory could yield an alternative equivalence not indexed by these searches.

## value

PASS

An exact instability boundary for a canonical geometric time integrator is mathematically and numerically relevant: each single step is elliptic and area preserving, yet any nontrivial iid mixing generates exponentially growing second moments, quantified with a sharp variance coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
