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

Run `python3 verify.py` using the Python standard library. The program applies two distinct finite checks: an exact recursive first-arrival enumeration of terminal count moments, and direct priority-permutation checks of the two eventwise coupling identities on small wheel and gear instances. The exact rational recursions reproduce the finite wheel mixture formula, verify sign differences of both mean responses, and independently check nonunit hub rates. They do not certify an infinite-size limit; those follow from the pathwise estimates in `RESULT.md`. The one-dimensional variance constant is credited to Penrose–Sudbury, Theorem 11, rather than to extrapolation.
