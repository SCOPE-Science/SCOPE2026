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

The proof uses an exact conditional Bernoulli identity, a nonnegative supermartingale, square-summable martingale series, a conditional-variance stopping argument, and an exact harmonic-number telescope. No infinite limit is inferred from computation.

Run `python3 verify.py` from the same directory. Its executable checks are standard-library-only. One completed execution produced `EXACT_IDENTITIES_OK 27224` and `EXACT_DISTRIBUTIONS_OK 1521`. The seeded path output is illustrative, not inferential. The checks do not establish the distribution or nondegeneracy of the limiting random constant.
