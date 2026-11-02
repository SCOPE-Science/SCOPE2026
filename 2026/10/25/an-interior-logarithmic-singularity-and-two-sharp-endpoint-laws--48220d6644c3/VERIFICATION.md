---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

A Haar-random unit normal U determines octahedron section area via the exact six edge-intersection polygon and F=2(ab+ac+bc)/((a+b)(a+c)(b+c)), a,b,c=|U_i|. The homogeneous expression includes sqrt(a^2+b^2+c^2), essential before differentiating. Stationary-gradient differences force at least two equal positive components, and (1,1,t) has derivative 3t(t-1)/((1+t)^3 sqrt(2+t^2)); the body diagonals give minimum 3sqrt3/4, equatorial midpoints yield interior critical sqrt2, and axes yield maximum 2. Independent SymPy second derivatives give diagonal quadratic coefficient sqrt3/16 along (1+t,1,1), and saddle coefficients +sqrt2/2, -3sqrt2/2 in unit area coordinates; eight wells give 64/(9sqrt3) times epsilon, and 12 saddles normalized by 4pi yield sqrt6/pi times log reciprocal distance. Six axial corners have conical deficit 2(b²+bc+c²)/(b+c); an independent exact integral of (1+t)^2/(1+t+t²)^2 over [0,infinity] equals 2/3+4pi/(9sqrt3), yielding upper constant 1/(2pi)+sqrt3/9. Coarea regularity away from critical levels proves nonatomic density. These symbolic local identities corroborate but are not a proof of global critical exhaustiveness; the derivative factoring and compactness argument in RESULT.md provide it.

## originality

PASS

A central-section area pushforward under Haar orientation is not the affine random-line chord-length distribution or section diameter; at fixed min and max normal-coordinate ratios, changing the middle coordinate changes area. Meyer–Pajor general deterministic section inequalities do not visibly entail a sharply normalized random 3D law; full primary paper is inaccessible and risk retained, not treated as automatic failure.

## value

PASS

Haar-distributed central-section area is an intrinsic shape statistic different from chord length, diameter or perimeter. The theorem locates and quantifies a genuine logarithmic interior singularity and both endpoint orders with exact coefficients for this canonical polytope; it is neither a bounded numerical table nor a rephrasing of section extremizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
