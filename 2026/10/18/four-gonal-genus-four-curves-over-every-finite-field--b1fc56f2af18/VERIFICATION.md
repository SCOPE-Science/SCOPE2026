---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For each finite k, the proposed quadric Q is the sum of a hyperbolic XY plane and anisotropic rank-two quadratic form: Z²-cW² for nonsquare c in odd characteristic, or Z²+ZW+aW² with absolute trace(a)=1 in characteristic two. Thus smooth Q is nonsplit over k but P1xP1 over algebraic closure. The three explicit cubic F forms have no geometrically singular intersections, proved not just by sample tests: when p>=5, Jacobian proportionality forces Z=0 and then c³=1/4, contradicted by nonsquare c; p=3, the affine equations reduce a hypothetical singularity to z³=0 then y=0, impossible, and the W=0 gradient W-component eliminates boundary singularities; p=2 the nonzero dQ/dZ=1 on W=1 forces dF=0 at x=y=z=0, impossible since trace(a)=1, and W=0 proportionality gives t²=0 with t³=1. Independently tested all four homogeneous charts with exact Groebner ideal [1] for sample (p,c)=(2,1),(3,2),(5,2),(7,3), supporting but not proving uniform smoothness. On split Qbar the smooth (3,3) divisor is geometrically connected/integral and by adjunction genus 4 with canonical O_C(1); unique nonsplit smooth canonical quadric excludes a k-rational degree-3 pencil, and canonical nonhyperellipticity excludes lower gonality. The displayed k-rational P gives a degree<=4 k-pencil via h0(K-2P)>=2 (a basepoint-free nonconstant subpencil after removing fixed parts), so k-gonality exactly 4. Nothing asserts geometric gonality four; it is three after field extension.

## originality

PASS

The universal genus-four existence assertion is exactly the g=4 instance of Faber–Grantham–Howe Question 1.3, beyond their general gonality bound and small q<=4 examples. Faber–Grantham 2020 gives the canonical quadric criterion and a binary example; it does not supply cubics smooth over every finite field. The new F equations prove existence over all odd and even extensions and characteristic three explicitly, not merely a rewording of nonsplit-quadric geometry. The 2025 published paper continued to frame odd-field smooth cubic sections as a possible route, not a construction theorem. No stronger all-field solution found in targeted searches; unindexed later solutions remain possible.

## value

PASS

It settles the g=4 case of a published natural existence question by uniform explicit k-rational genus-four canonical models of gonality exactly four, including every prime-power extension in characteristics two and three. Removing dependence on a field-by-field search is a substantive construction with independent utility, not an isolated small example or a known quadric criterion restated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
