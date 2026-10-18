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
# Verification and boundaries

The analytical proof is in `RESULT.md`. The separate `verify.py` program uses exact rational arithmetic to check the finite-state transitions through 12 steps (each attainable integer state), \(\mathbb E B_n=2n\), \(\mathbb E B_n^2=5n^2-n\), the exact first-jump probability on a logarithmic grid, the reciprocal post-jump transformation, and the stationary moment recursion for the first nine integer moments. It passed 9,360 finite identities on the tested ranges. Execute with `python3 verify.py` from the package directory.

**Limits.** These checks do not certify uniqueness of invariant probability measures, ergodicity, the infinite-time weak limit, or priority. The proof derives those from the explicit continuous-time generator, compact single-jump minorization plus drift, and the vanishing-grid semigroup coupling. There is no claimed independent audit.
