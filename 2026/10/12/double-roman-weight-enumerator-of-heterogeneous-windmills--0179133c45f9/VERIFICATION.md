---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The cases center s=3, s=2 and s=0/1 partition all labelings. For s=3 each clique labeling is unconstrained (A). For s=2 only blades with labels restricted to 0/1 and at least one zero are forbidden (B). For s=0/1, no-2/no-3 labelings and one-2/no-3 labelings containing at least one zero are forbidden (C). Every C-admissible blade contains a 2 or 3; for r>=2 this guarantees that the center itself is defended even when s=0. Thus product factorization follows exactly; minimum weight3 occurs only for center3 and all-zero periphery. Independent brute-force direct definition enumeration confirmed every polynomial coefficient for five blade profiles (2,2),(2,3),(3,3),(2,2,2),(2,3,3), including 25 positive nonzero-weight coefficients at last profile; proof supplies all r,m quantifiers. Original RESULT.md at exact inspected Git blob SHA contains four ASCII BEL controls in the paragraph naming center-label regimes; verified exact 6940-byte source Git SHA and replaced only those malformed tokens with plain center-label-[3,2,0,1] in full supplied corrected scientific file.

## originality

PASS

Beeler/Haynes/Hedetniemi established double Roman function definitions; Cariaga/Jamil 2023 full join paper establishes scalar minimum3 when a universal vertex exists, not an all-weight distribution. Published SCOPE windmill dissociation polynomial and Roman-variety enumerators count different legal label classes; they do not imply the exact double Roman three-product enumerator on heterogeneous blades. The known scalar minimum is expressly credited rather than presented as new.

## value

PASS

The graph family naturally includes friendship graphs and windmills with unequal clique sizes. The product gives every coefficient and exact total feasible-function count, a genuine refinement beyond the already known minimum3 and exposes the structural center-label regimes. The finite tests verify representative profiles but do not replace the uniform proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
