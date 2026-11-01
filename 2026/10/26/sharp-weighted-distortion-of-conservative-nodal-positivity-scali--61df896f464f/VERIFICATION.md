---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Let i index a minimal u_i=-a<0, m>0, p=(u+a1)/(m+a), hence L=mp and u-L=a(p-1). Since p_i=0, p>=0 and sum w p=1, concentration of weighted mass at the smallest remaining weight w_j yields ||u-L||_w^2 <= a^2(1-w_j)/w_j. For any feasible z, h=z-u has h_i>=a and sum w h=0; Cauchy-Schwarz on complementary coordinates yields ||h||_w^2 >= a^2 w_i/(1-w_i). The resulting bound is maximized at the two smallest weights. A single-negative-coordinate family with u_i=-epsilon and other small positive coordinates approaching zero concentrates p at j; the actual weighted orthogonal projection zeros i and shifts all other coordinates by a common offset, giving asymptotic equality. LGL endpoint weights 1/[N(N-1)] are minimal because |P_{N-1}(x)|<=1. For N=2 ratio=1. Independently verified near-sharp examples with weights (.05,.07,.18,.7), (.1,.1,.3,.5), (.3,.7), and LGL endpoints for N=2..10.

## originality

PASS

Best-of-knowledge noncoverage after comparing the precise statements and implications, original scope, related general theorems and aliases, with the specific residual priority limitations below; lack of a search hit is not itself evidence of novelty.

## value

PASS

Distinguishes the exact and potentially quadratically large correction cost of a standard nodal positivity limiter from the least weighted Euclidean modification under identical conservation. It quantifies a real design tradeoff beyond the tautology that projections minimize distance, with degree-dependent sharpness for standard LGL discretizations. No claim about entropy or full PDE evolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
