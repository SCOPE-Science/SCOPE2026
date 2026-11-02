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

The established planar convex Cheeger equation |Omega_t ominus sB|=pi s^2 uniquely defines radius s=1/h; support functions imply for s<=t the erosion is P+(t-s)B, and otherwise P ominus(s-t)B. At s=t the residual is A-pi t^2, giving exact universal threshold. Steiner area yields s=(A+Lt+pi t^2)/(L+2pi t) above threshold. For u small, |P ominus uB|=A-Lu+Cu^2 by corner-triangle area, C=sum cot(alpha_i/2). The implicit subthreshold equation has derivative -(L+2pi T), so differentiable roots with b1=2pi T/D, b2=pi(4pi C T^2-L^2)/D^3; direct independent SymPy differentiation verified the boxed h second derivative jump. Exterior-angle Jensen yields C>pi and hence strict non-C2 behavior. The local inner area polynomial is used only before edge extinction.

## originality

PASS

The Cheeger radius characterization and self-Cheeger threshold are already direct consequences of known convex Cheeger theory, and first derivative smoothness for parallel bodies is already established. The narrower surviving mathematical contribution is the exact universal nonzero second-derivative angular jump and two-term inner-rounding gap for all genuine polygons, not the threshold as standalone novelty.

## value

PASS

The exact universal second-derivative defect, valid for every genuine convex polygon, detects the intrinsic corner functional C=sum cot(alpha_i/2) from physically natural disk-offset Cheeger response. Sharp regularity loss at a universal area-normalized scale extends known first-variation theory and supplies a shape-sensitivity benchmark. The bound and geometric object are motivated independently of finite numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
