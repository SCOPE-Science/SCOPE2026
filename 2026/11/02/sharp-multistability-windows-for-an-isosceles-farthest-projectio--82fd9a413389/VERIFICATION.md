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

# Verification and limits

The standalone `verify.py` needs only the Python 3 standard library and computes with `fractions.Fraction`, so its geometric branch tests use exact rational arithmetic. It independently reconstructs each ordinary perpendicular projection from the side vertices and the squared-height metric, rather than using the six simplified projection formulas in the proof. For every candidate itinerary it checks the projected successor parameter exactly, tests that all target squared distances strictly exceed competitor squared distances precisely when the stated algebraic admissibility conditions hold, and verifies interior point coordinates for legal words. The checked words are `012`, `0102`, and `01210212`; the checker reports `CHECK_OK exact projected itineraries: 2145 ; endpoint brackets and rational grid verified`.

The proof, not this finite sample, establishes the exact root count of the quintic, the signs of all branch margins, the sharp admissibility intervals, primitive least periods, and strict return contraction for every real parameter in the stated windows. No computer-assisted infinite certification, global orbit-count classification, or independent scientific audit is claimed. The prior result on primitive three-cycles is credited separately from the new even-period coexistence conclusion.
