---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The two affine branches map the unit-area triangle onto itself with determinants ±2. I independently integrated the coordinate moments, reconstructed P(x-1)=0 and P(y-1/3)=((x-1)-(y-1/3))/2, verified the stated covariance matrices at 39 positive lags, and summed the infinite geometric kernel to Σ=(1/6)[[1,1/3],[1/3,1/9]]. The exact algebraic identity x-3y=(x-y)-(x-y)∘T holds on both branches, and H=x-y ranges over [0,2], with attained endpoint bound. P(x-1)=0 supplies bounded reverse martingale differences; full-branch contraction gives ergodicity, ergodic conditional variance 1/6 and Lindeberg, proving the coordinate martingale CLT. The other coordinate differs by a bounded coboundary and thus has the stated degenerate bivariate CLT.

## originality

PASS

The original t=1 map is from Pumariño and coworkers and studied by Alves-Etubi (2025) for invariant-density/entropy regularity. Its inspected full article explicitly has the same tent branches but does not give rank-one linear-coordinate CLT, all-lag matrices, or the sharp coboundary. Standard martingale CLTs explain the limit once transfer identities are derived; they do not imply the exact null direction. 2026 paper on rare events for d-dimensional chaotic maps has unresolved possible intersection; priority conditional on its fuller comparison.

## value

PASS

Exact coordinate fluctuations and an all-orbit bounded coboundary describe a nontrivial rank degeneracy despite both branches expanding spatially. The complete lag matrices and sharp nullspace are useful dynamical invariants, independently of perturbation theory or higher-order mixing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
