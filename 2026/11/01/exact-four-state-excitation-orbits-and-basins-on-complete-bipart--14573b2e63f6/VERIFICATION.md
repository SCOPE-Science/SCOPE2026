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

# Reproduction details

The attachment contains `verify.py`, `support_table.csv`, and `verification_output.txt`. Run `python3 verify.py` with Python 3 using only its standard library. The script uses the exact per-color support-image rule, exhaustively visits \(15\times15=225\) nonempty support pairs, detects all directed cycles, and confirms every transient reaches a designated recurrent support in no more than six steps.

It also enumerates all \(115,600\) labelled microscopic colorings for the \(16\) ordered pairs \((a,b)\in\{1,2,3,4\}^2\), independently computes actual trajectory period and transient, and verifies the support quotient gives the same classification. Further exact checks of the full orbit/basin formulas and sharp five/six capacity rule cover the \(36\) ordered size pairs \((a,b)\in\{2,\ldots,7\}^2\). The transient proof for arbitrary sizes uses the fact that possible support masks have cardinalities at most four, so all graph-size regimes reduce to this finite support certificate. The main theorem applies only when both shores have at least two vertices.

Limits: finite labelled-state tests are not infinite-family proofs; the proof rests on an exhaustively given 225-state quotient and surjection counting. An external independent audit has not been performed.
