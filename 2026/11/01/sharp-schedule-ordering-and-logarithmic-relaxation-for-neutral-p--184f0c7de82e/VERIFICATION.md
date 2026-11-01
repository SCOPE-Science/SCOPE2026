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

The standard-library Python file `verify.py` was executed against the exact source embedded in this package. It passed 172 finite checks, including 96 exact rational state/conjugacy comparisons, formal large-coordinate coefficient identities for six words, the exact four-step constants, all six word permutations, nine exact general-block formulas, and two numerical logarithmic-residual convergence checks. Printed check counts are according to the program's own counter and are not an exhaustive mathematical verification of arbitrary words.

The proof in `RESULT.md` establishes the infinite-time result analytically from an exact recurrence, a positive linear drift, a finite asymptotic expansion, summability, and strict adjacent-swap comparison. The numerical stabilization checks do not prove the existence of the limit. No external independent audit has been performed; no claim of machine formalization or independent certification is made.
