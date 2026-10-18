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

The algebraic proof establishes the incidence formula for every odd prime power. The standalone finite enumerator `verify.py` computes the Jordan product directly, identifies all idempotents by squaring, forms every primitive Peirce image, and compares each of the \(q^3\) matrices with the pointwise and aggregate predictions.

Checks completed successfully for \(q=3,5,7,11,13\) (prime fields) and \(q=9\) (a quadratic extension of \(\mathbb F_3\)); each field's full matrix set is enumerated. Small-field word reachability was additionally enumerated for \(q=3,5,7,9\), and the resulting sizes were \(22,74,218,418\), matching the Peirce upper-bound counts in these examples. These tests do not imply saturation for all odd prime powers.

No computation is used to extrapolate an infinite-field-family theorem. The converse characterization of all representable Jordan words is **unproved**, and the result claims only the necessary obstruction and the exact terminal-factor incidence distribution. External full-text inspection of the most relevant recent paper was unavailable; bibliographic incompleteness remains possible.
