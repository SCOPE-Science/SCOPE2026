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

# Reproduction

Run `python3 checker.py` from the directory containing this file and the checker. It needs only the Python standard library; no downloads or imported local dependencies are necessary. It checks the classification by 50,001 independently iterated odd denominators, period translations for eight numerator/horizon pairs, the numerator bound, a separate reduced-`Fraction` implementation for nine numerators, and exclusion of all maximal proper divisors of 60 as periods. All checks passed with exact integers.

The proof of the infinite conclusions is in `RESULT.md`, not in this finite checker. Its central invariant is \(A_{j+1}=A_ju_j-B_j\in[0,2A_j)\) for the least-odd ceiling \(u_j\), together with congruence preservation by the explicit product period. The finite enumeration tests these calculations, but no finite enumeration is offered as proof of an infinite claim.

Independent audit: not performed.
