---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Strict upper cones are exactly x+H_+. If y<x, y+m (m=min H_+) is in the upper cone of y but not of x, so inclusion fails. For d=y−x≥0, translated upper-cone inclusion iff d+H_+⊆H_+, equivalent to d∈H or d pseudo-Frobenius. Adding all PF numbers preserves additive closure: for d1,d2 in PF and s in H_+, d2+s lies in H_+, so d1+(d2+s) lies in H; therefore d1+d2 is either already in H or itself is PF. This handles PF+PF products and makes induction valid. Frobenius number is PF, thus each stage removes >=1 gap; exact gap-count telescoping gives genus=sum of types. Independently enumerated H=<4,7> gaps [1,2,3,5,6,9,10,13,17], PF=[17]; this is a check, not a proof.

## originality

PASS

Known mathematical constituents are Jagiella reverse upper-cone preorder extension and numerical-semigroup PF-adjunction; their matching via exactly the same P_H translation class does not appear in inspected open MED-closure article or Resultary hits. The cross-subject identification is new best-of-knowledge. Jagiella full primary text could not be read; a hidden equivalent in it would defeat priority, explicitly residual risk.

## value

PASS

Supplies a concrete natural model-theoretic closure normal form and a finite computable semigroup invariant for stabilization of definable order representatives. Though algebraically elementary, it is a motivated exact identification of two nontrivially different closure definitions with stage-by-stage genus/type accounting, not a random parameter restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
