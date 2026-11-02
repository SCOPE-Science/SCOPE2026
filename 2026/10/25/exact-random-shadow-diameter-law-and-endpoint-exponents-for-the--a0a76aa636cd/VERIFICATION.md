---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The convex projected diameter is attained by projected original vertices, so one maximizes six projected unit edge lengths. Those edges have directions (0,1,±1)/sqrt2 and permutations. Thus D/ell=sqrt(1-(min(x-y,y-z))²/2) for sorted absolute normal coordinates x>=y>=z. The bound 1=x²+y²+z² >= 5m² gives m<=1/sqrt5 with equality only at signed permutations of (2,1,0)/sqrt5. A signed/permutation fundamental spherical chamber has normalized area density 12/pi in (z,phi); imposing x-y>=r and y-z>=r yields the stated elementary angular integral up to z*=sqrt((1-2r²)/3)-r. Six great-circle small bands give upper tail 6sqrt2 sqrt(eps); uniform bivariate Taylor expansion of the shrinking chamber gives lower tail 150sqrt5/pi delta². Independent projected-vertex comparisons matched coordinate-gap formula for 2000 random directions. The unbounded exact CDF and endpoint limits follow from analytic geometry, not Monte Carlo.

## originality

PASS

Best-of-knowledge PASS for random PLANAR SHADOW diameter rather than tetrahedral line-caliper width, planar projected area/perimeter, or silhouette vertex count. Finch’s relevant primary texts analyze those distinct observables, and a complete Resultary tetrahedron shadow-area record covers conditional area moments, not the maximum projected edge. A separate published octahedral central-section diameter concerns another body and operation. No materially inspected prior primary source gives the tetrahedral diameter CDF plus both endpoint constants. Residual risk includes unindexed shadow-diameter/stochastic-geometry sources and the more recent general random-diameters work with incomplete access.

## value

PASS

Euclidean diameter is a basic geometric functional of an orthogonal shadow; its complete law and exact minimizers distinguish a discrete 12-plane minimum set from a great-circle maximum set, generating different quadratic and square-root endpoint exponents. This is a natural full geometric-probability distribution, with independently meaningful sharp endpoint behavior, rather than a generic numerical moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
