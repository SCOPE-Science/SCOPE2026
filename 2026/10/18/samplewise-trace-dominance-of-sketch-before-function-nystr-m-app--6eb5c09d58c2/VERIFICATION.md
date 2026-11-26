---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The pseudoinverse formula gives N_G(X)=X^(1/2)P_X X^(1/2) between 0 and X. The function vanishes at zero, so one can take its trace on the compression to the range of A^(1/2)G; compression Jensen gives the lower bound tr(P_A f(A)). For the remaining comparison, restrict to the common support of A and f(A) and choose a fixed full-column-rank basis for the projected sketch range. Along the positive diagonal interpolation D_t, the evolving basis Y satisfies Y'=H_tY. Differentiating P_tY=Y and P_t²=P_t gives the two off-diagonal blocks of P_t′ in (7). Since (P_t)_ii=∑_j |(P_t)_ij|², symmetrizing produces exactly the covariance sum (8). Each product is nonnegative by monotonicity of f and monotonicity of λ/f(λ) from scalar concavity and f(0)=0. Integrating proves the stated orientation. The empty support or projected sketch gives zero on both sides; rank deficiencies otherwise are handled by the same range argument. Both residuals are PSD, making the nuclear equivalence exact. In the two-dimensional witness the trace comparison squares to 153>125 and the determinant of the difference of the two scaled rank-one outer products is −4/(15√(17/5)), excluding Loewner dominance.

## originality

PASS

The supported distinction is all continuous nonnegative operator-monotone functions for the shared standard Nyström sketch, including log and ridge kernels, and the ordered projector reweighting behind it. The closest indexed record gives the same comparison at q=1, and a stronger eigenvalue comparison, for fractional powers; this subfamily is not distinct from that result. Neither that statement and its power-specific argument nor the inspected primary papers imply the full function-class result as stated.

## value

PASS

When the same fixed sketch is available for both orders, the theorem answers which order gives smaller nuclear error for every realized sketch, rather than which has a better tail estimate in expectation. The ordered reweighting lemma explains the comparison and extends beyond the fractional powers to practically relevant log and ridge functions. The explicit indefinite difference marks a meaningful limit of the guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
