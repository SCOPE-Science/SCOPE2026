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

Run `python3 verify.py` using Python 3 and the standard library. The script checks all residue subsets for primes 2, 3, 5, and 7; checks the full-density bound for reduced fractions with moderately sized denominators; verifies the obstruction family for zero-density sets; and tests a natural-density 99/101 example. It prints `VERIFY_OK`, followed by the number of cases. No network downloads, random choices, or external proof engines are used.

These exact finite checks supplement, but do not prove, the theorem for all primes and arbitrarily large rational denominators. The universally quantified result is supported by the proof in RESULT.md, including the modular inversion and coprimality identities.

Independent audit and expert validation have not been performed.
