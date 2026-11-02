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

The algebraic proof in RESULT.md establishes the infinite parameter ranges; this note gives independent reproducible checks and their scope. The attached `verify.py` is Python 3 standard-library-only code using integer arithmetic and `fractions.Fraction`.

Run `python verify.py` to compare every attainable two-party winning-seat split to the closed-form FJR+ optimum for every \(2\le n\le60\), \(1\le L\le50\), and \(1\le b\le\lfloor n/2\rfloor\), including degenerate zero lower quotas and tied parties. The same program checks every finite profile against the horizon envelope and verifies the maximizer is among the grid indices adjacent to \(L(1-1/\sqrt2)\) for horizons through 90. It also verifies five asserted exact rational horizon values.

Expected stdout: `VERIFY_OK finite_profiles=45000 feasible_seat_counts=87082 horizons=90 exact_examples=5`.

Finite computation does not establish the statement beyond the checked ranges; the derivative and quota-boundary arguments in RESULT.md do. No independent audit or formal-assistant certification has been performed.
