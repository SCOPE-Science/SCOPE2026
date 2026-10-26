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

The theorem is a formal-generating-function identity for all positive lengths and is proved structurally in `RESULT.md`; finite checks are only supplementary.

Run `python3 checker.py` in this directory. The standard-library checker performs independently coded exact cyclic-word enumeration for every binary word of lengths \(1\) through \(15\), balanced integer flow enumeration with a separate positive-support connectivity predicate for lengths \(1\) through \(19\), and five-family coefficient expansion for the same range. Both exhaustive enumerations match the generating-function coefficients. A direct word enumeration for one fixed \(n\) covers all \(2^n\) binary words and hence all cyclic multispectra at that length, but does not prove the infinite identity. The Eulerian-circuit and connected-support proof addresses all positive lengths.

Known external result: the leading coefficient \(1/288\) appears in Kiah–Puleo–Milenkovic (2015) Table I; its agreement with the derived pole coefficient is a cross-check, not evidence of priority for a new constant.

No independent audit, experimental external certification, or review by another mathematician is asserted.
