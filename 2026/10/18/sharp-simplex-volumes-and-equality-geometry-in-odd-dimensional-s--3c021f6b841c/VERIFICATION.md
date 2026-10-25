---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

For d+1 vertices in Euclidean unit ball, centered Gram-covariance identity (d!V)^2=(d+1)det(C) and trace bound give the unique regular simplex equality bound c_d. For t<=1/sqrt(d), the enclosing ellipsoid with horizontal squared semiaxis A=d(1-t^2)/(d-1) and vertical B=d t^2 contains K, and the difference A(1-z^2/B)-(1-z^2)=[(1-dt^2)/(d-1)](1-z^2/t^2)≥0. For odd d=2k+1, two orthogonal centered k-simplices on layers z=±t transform to regular unit sphere simplex, saturating the ellipsoid bound; equality and parity force balanced counts, and for t>=threshold the full-sphere regular simplex bound attains. Normalized t(1-t^2)^k/integral_0^t(1-s^2)^k ds strictly decreases by rescaling integration; for t>=threshold numerator constant and slab volume grows. Independently checked exact rational Gram determinants for d=3,5,7,9 and exact threshold identities. Finite checks supplement the global determinant argument.

## originality

PASS

Prior regular-ball simplex volume equality and full-sphere results are credited. Odd-dimensional sharp radius-dependent slab optimum, parity-specific two-layer extremizer geometry, and strictly decreasing occupied fraction are not implied by a ball-only theorem. Central convex set theory (McKinney) may contain stronger equivalent slices; full text unavailable, recorded as limited priority risk.

## value

PASS

The largest inscribed simplex in a truncated ball is a natural optimization invariant bridging thin cylindrical slices and a full Euclidean ball. The exact sharp transition at t=1/sqrt(d), rigidity and occupancy monotonicity provide a complete odd-dimensional phase classification and clarify parity constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
