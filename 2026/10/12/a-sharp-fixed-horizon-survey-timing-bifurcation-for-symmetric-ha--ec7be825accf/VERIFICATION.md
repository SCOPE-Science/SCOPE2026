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

# Verification protocol and limits

Run `python verify.py` with Python 3, SymPy and mpmath. The verifier regenerates derivative numerators \(P_2\) and \(P_4\) using exact symbolic recurrences, checks all finitely many negative Taylor coefficients using integer expressions, and verifies the closed-form positivity conditions for the unbounded positive tails by explicit quadratic inequalities. It also brackets the unique derivative roots with 55-digit arithmetic and illustrates several finite-horizon schedules.

The actual executed command was `python verify.py` from the same source that is embedded here. Output included `VERIFY_OK P2_signs=3..7_negative_8plus_positive P4_signs=6..25_negative_26plus_positive`, the inflection \(a=1.5430468848087244617\ldots\), and the long-horizon short gap \(c=0.7968121300200200461\ldots\). The explicit monotonicity proof in RESULT.md, not grid tests or floating point signs, establishes all-horizon optimization.

The result is a conditional theoretical statement about exactly observed Markov occupancy. No experimental ecological data, finite-sample inference calibration, or independent scientific audit has been performed.
