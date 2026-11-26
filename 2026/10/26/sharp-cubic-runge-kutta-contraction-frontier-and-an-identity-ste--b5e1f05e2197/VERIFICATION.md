---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The stage abscissae and weights satisfy the order-two conditions, and direct substitution on a linear equation gives the cubic. The characteristic polynomial λ²+bλ+a² and symmetric part diag(0,−b) give asymptotic stability and semidissipativity. Independently reduced R to pI+qL via L²=−bL−a²I, with p=1−a²h²/2+βa²bh³ and q=h−bh²/2+β(b²−a²)h³. The defect entries are A=p²+a²q²−1, B=A−2bpq+b²q², and −abq² off diagonal. Exact expansion gives trace slope −2b, determinant coefficients a²b²(1−4β) at h⁴ and a²b(8a²β−a²−b²)/2 at h⁵, and zero lower determinant coefficients. These give the two strict regimes and the β=1/4 sign split away from a=b, with the step size quantified pointwise. At β=1/4 and a=b, the exact factorizations have positive determinant except at x=ah=2 for x>0 and trace sign sign(x−2); at x=2 one has p=1,q=0 so there is exact identity, not merely unit spectral radius. The unequal-rate h=1 trace and determinant are the stated negative and positive rationals; openness gives an interval. The invertible leading term L³/4 makes the smallest singular value grow at infinity. Read the frozen checker without executing it. Replay of the independent identities and rational certificate: `python /workspace/branches/review-computations/check_finite.py`. This is not a uniform step bound or an all-parameter count of windows.

## originality

PASS

The strict β>1/4 threshold is substantially covered by the published non-strong-stability criterion, including its singleton implication, and is not treated as new. Verified comparisons support the distinct marginal result at β=1/4: the b/a dichotomy, exact equal-rate all-step trichotomy, and intermediate strict-contraction witness for the same cubic despite small-step indefiniteness. Catalogue analogues have other stability polynomials or matrix classes; their dates are not relied on as priority evidence.

## value

PASS

Resolving the equality in a known strict-coefficient obstruction is mathematically motivated. The minimal rank-one damped planar system isolates a fixed-matrix contraction boundary and distinguishes small-step behavior, exact identity, and strict contraction at intermediate steps. The finite-step phenomena invalidate plausible extrapolations from the initial norm defect and are stated with exact certifiable parameters, rather than as a numerical curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
