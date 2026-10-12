---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The scientific proof is symbolic and self-contained in `RESULT.md`. The accompanying `verify.py` replays the critical polynomial identities with exact arithmetic.

It checks that the tangent cross product of the published affine normalization has common factor \(u(u^3+2)\) and leaves the dual map \([4u^3-1:2u^2:-u^4]\); that the map satisfies \((B^2-4AC)^2+128BC^3=0\); that the rational inverse identity recovers \(u\) on \(BC\ne0\); that the displayed partial derivatives are correct; that the local coordinates at \([1:0:0]\) have leading orders \(2\) and \(7\); and that the Wronskian of the original parametrization is \(-4u^3(u^3+2)^2\).

The checker does not by itself certify the global singular-locus case split or the interpretation of a Puiseux pair as an ADE label; those are proved in the text and compared with the cited rational-quartic classification. It also does not constitute independent validation.
