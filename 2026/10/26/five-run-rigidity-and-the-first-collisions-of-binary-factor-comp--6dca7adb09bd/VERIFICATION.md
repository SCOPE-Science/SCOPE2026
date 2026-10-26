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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.8 or newer; no external packages are needed. The program builds all nonempty factors directly instead of invoking the closed-form reconstruction formulas to produce its Parikh supports. It verifies every binary word with at most five runs at lengths one through sixteen (13,768 words) for full-support uniqueness modulo reversal, and tests the explicit inverse's output against the original word or its reversal. It separately enumerates every positive five-run parameter tuple in the cube of side seven (16,807 tuples), checks the interior and pairing formulas, and validates the six-run collision spectrum for all parameters from two through sixty-nine. Finally it exhaustively checks that no nonreversal collisions occur at lengths one through six, and that at least one occurs at length seven.

Expected output: `VERIFY_OK exhaustive_low_run_words=13768 n=1..16 five_run_parameter_tuples=16807 six_run_collision_t=2..69 first_ambiguous_length=7`.

These finite enumerations are reproducibility checks, not an exhaustive computer proof of claims quantified over arbitrary positive integers. The unrestricted statements use the reconstruction and factor-interval reasoning in RESULT.md. Independent human validation has not been performed.
