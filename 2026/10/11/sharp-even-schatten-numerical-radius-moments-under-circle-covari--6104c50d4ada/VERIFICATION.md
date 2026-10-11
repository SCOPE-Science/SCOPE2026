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

# Verification notes

The standalone Python 3 checker `verification/verify_even_schatten.py` uses `fractions.Fraction` for every scalar operation. Execute it with `python3 verification/verify_even_schatten.py` from the containing directory. Successful output is `GRADED_SCHATTEN_EXACT_BALANCED_WORDS_AND_COMMUTATOR_OK`.

It reconstructs the balanced-word coefficient for integer \(1\le m\le8\) at six rational weights, tests finite nilpotent unilateral shifts of size \(2\le N\le9\) and a non-scalar block shift for moments \(1\le m\le5\), verifies the strict and endpoint cases there, and checks the exact fourth-moment commutator deficit. The analytic proof, not any finite check, establishes the general Schatten-space inequality, the nonattainment statement, and sharpness over unbounded dimensions. No independent audit has been performed.
