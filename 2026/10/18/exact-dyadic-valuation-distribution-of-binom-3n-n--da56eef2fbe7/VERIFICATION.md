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

# Reproducibility and verification

With a standard Python 3 installation, run `python3 verify.py` in the directory containing this file and the companion verifier. It uses only the standard library, including `fractions`, `math`, and `collections`.

The executed verifier returned:

`BINOMIAL_3N_N_VALUATION_EXACT_OK dyadic_lengths=0..30 direct_inputs= 8191 rational_recurrences=28 moments=31`

Verification covers the weighted four-state carry transition, the exact first and second factorial moments, the missing one-valuation fiber, and direct Legendre-factorial counts. These are finite regression checks of the infinite algebraic proof in `RESULT.md`, not exhaustive verification of infinitely many cases. The proof relies on Kummer's theorem and a rational matrix identity. The previously known limiting normal law was not independently reassessed here.
