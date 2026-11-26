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

The affine partials are nonzero on UV=1, and at x=∞ the equation is (1−t²)(v³−v)=t³ at each y in F_3, giving three distinct smooth branches; the other side is symmetric and the corner is absent. The Artin–Schreier right side has simple poles, so it is not an additive coboundary; the completion is geometrically irreducible. Adjunction gives genus four and K=O_M(1,1). With s=x−x(P), inverse-series comparison gives y coefficients −A^{−2}, −A^{−3}, −A^{−6}−A^{−4}+A^{−2}. In the basis 1,s,z,sz the order-(0,1,2,3) determinant is a_2²−a_1a_3=(A⁴−1)/A⁸, not identically zero. Its affine zeros are simple since dA/ds=−1 and A⁴−1 is separable; each of four A has 3×3 preimages. The first three jet rows have rank three because a_1≠0, giving uniqueness of z+A^{−2}s−A^{−1}sz=0. Independently expanding with d=1−s/A and n=−s/A² gives A^{−1}d³+n³−nd²=A^{−1}+A²s+As²−A²s³ at A⁴=1. Multiplying by A+s³−s and subtracting d³ gives −As⁴(As²−s+A). It is nonzero at d=0; the root lengths 4+2 account for the full canonical degree. Factoring gives s=−A twice if A²=1, and s=A±1 simply otherwise; evaluation of z=n/d verifies the specified points. Coordinate Frobenius F sends P to P+(A,A^{−1}). In the first stratum the residual map is F inverse and has order three without fixed points, hence six directed triangles. In the second stratum the neighbors are τ^{±1}F(P), with τ simultaneous translation by (1,1). F swaps the two values of A, F²=1 there, and τ has free order three and commutes with F, so τF has six-element orbits and its inverse is τ^{−1}F: three hexagons. At infinity the local canonical basis is 1,t,v,tv with v=−t³−t⁵+O(t⁷); its D1 and D3 begin t⁴ and −1 and D2 has order three, so the Wronskian starts at t⁴. The six boundary points are F_3-rational. Thus Frobenius cycle type on the reduced support is 1^6 2^9 3^6, yielding the displayed orbit-factor zeta function. These checks are symbolic; the frozen exact finite checker was inspected, not executed.

## originality

PASS

Credit the complete two-regime residual divisors and their incidence graph, not the Artin–Mumford model, its translations, or the general osculating-conic template. The closest primary paper in fact gives an explicit equation and more than local order sequences. Its stated order theorem assumes q≥5, and it neither states nor proves the characteristic-three residual divisors or graph. At q=3 the equation specializes to the frozen plane in centered coordinates, but the relevant jet verification, residual multiplicities, and incidence classification are separate. The assessed novelty is bounded, not a priority claim.

## value

PASS

Genus four is the degree-six canonical case where an order-four osculating section naturally leaves degree two. The theorem tells exactly when that residual scheme is nonreduced, identifies all residual points, and classifies the incidence on the entire affine high-contact locus. This distinguishes geometrically meaningful regimes not determined by the local order at the contact point or by Frobenius orbit counts. It is a reusable exact characteristic-three test case, not an arbitrary finite sample or a recount of the known local orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
