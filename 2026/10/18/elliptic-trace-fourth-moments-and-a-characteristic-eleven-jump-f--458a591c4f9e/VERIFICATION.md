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

The complete proof is in `RESULT.md`; the standalone finite checker is `verify_sextic.py` and needs Python 3 standard library only. Execute `python verify_sextic.py` from the directory containing the files. The checker reconstructs ordered collisions directly, without calling either formula as a subroutine of the other count. It checks twelve prime fields and three quadratic extensions, evaluates both smooth elliptic traces, checks the exceptional conic factorization pointwise in characteristics eleven, and verifies every reported additive energy against a separate two-sum dictionary.

A completed invocation reported `VERIFY_OK fields=15 total_ordered_pairs=56031 exceptional_characteristic_11=2 elliptic_trace_checks=13 collision_energy=PASS`. Direct computation is not an infinite-field proof; the unrestricted proof consists of the collision factorization, conic/character-count reduction, and characteristic-eleven conic splitting. The sharp operator norm over arbitrary inputs is not calculated. Independent audit and external validation have not been performed.
