---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

In the specified unordered smooth coefficient chart over C and a+b!=0, u=(a+b)/4, v=(ab+4)/(a+b) transform the supplied involution into (u,v)->(-1/u,-v). Writing q=u-1/u,z=u+1/u,t=v^2,w=vz gives invariant ring C[q,t,w]/(w^2-t(q^2+4)); localization by t-4 and q^2+4-2w+t preserves invariants and removes fixed points. On projectivization W^2 Z=T(Q^2+4Z^2), the four exact partials show only affine q=+/-2i nodes and infinity [0:1:0:0]; completing square gives A3. Setting boundary N=0 yields (w-q^2-4)^2=0, and the contact with t=4 has length four. Symbolically rederived gradient (-2QT,-Q^2-4Z^2,2WZ,W^2-8TZ) and the infinity analytic A3 identity.

## originality

PASS

The coefficient-level degree-two involution exact invariant ring and boundary scheme are different claims from a Prym moduli map or its general compactification.

## value

PASS

The cubic del Pezzo quotient is geometrically motivated by a published degree-two Prym coefficient correspondence. Its ADE singularity basket and doubled boundary with exact contact refine the moduli-geometry picture as an independently meaningful coefficient-level compactification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
