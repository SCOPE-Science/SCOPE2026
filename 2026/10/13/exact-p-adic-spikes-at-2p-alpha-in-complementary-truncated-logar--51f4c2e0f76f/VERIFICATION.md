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

The direct exact-arithmetic script `verify.py` evaluates the original rational sum using `fractions.Fraction`, strips numerator and denominator powers of the chosen prime, and compares the resulting valuations with the theorem. It also checks the telescoping binomial identity for 120 integer cases. See `verification_output.txt` for the executed output.

These finite calculations detect coding/transcription errors; they do not establish the infinite theorem. The unrestricted justification is the coefficient identity and the uniform valuation bounds in `RESULT.md`. The only outside mathematical input for the **adjacent-index interpretation** is Farhi's published Theorem 1; the exact even-index formula has a self-contained proof.
