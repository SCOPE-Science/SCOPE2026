---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Over F2 the partial derivatives of G=x^5y+y^5z+z^5x imply x!=0 and y=u^5,z=u where u^21=1. These are 21 simple roots since derivative of u^21-1 is u^20, and w=u^13 has square u^5. Mixed second derivative G_yz=y^4 !=0 gives 21 A1 ordinary double points; Shimada supplies established singularity-to-K3 criterion. Frobenius squares u, yielding cycles of lengths 1,2,3,3,6,6. Each F_(2^n) base-plane point has unique square root in pure inseparable double cover; replacing a rational node by its split conic adds q points, giving #X=q²+q+1+q*gcd(21,q-1). Formal exponential of fixed Frobenius cycles yields exactly Z=[(1-T)(1-4T)(1-2T)^2(1-4T²)(1-8T³)^2(1-64T^6)^2]^{-1}. Independent check generated r_n and point totals n=1..12, e.g. (2,9),(4,33),(8,129),(64,5505). All n follows from order modulo 21, not test range.

## originality

PASS

Dolgachev–Kondō and Shimada already establish the general characteristic-two 21-node A1 supersingular K3 geometry; do not credit it as new. The specific cyclic sextic root scheme, arithmetic Frobenius orbit list and all-extension zeta have not been found in inspected explicit examples or the smooth-quartic zeta census. A hidden isomorphic twist or specialist zeta table could subsume the explicit arithmetic invariant, documented as residual risk.

## value

PASS

The zeta function/Frobenius cycle type is a canonical arithmetic invariant of a natural cyclic sextic K3 presentation; an explicit all-extension formula and minimal splitting field for 21 exceptional curves are substantive finite-field geometry rather than a known abstract K3 existence corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
