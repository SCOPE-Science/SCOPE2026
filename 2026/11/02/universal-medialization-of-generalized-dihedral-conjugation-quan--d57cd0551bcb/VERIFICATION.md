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

# Verification record

The included standard-library script `verify.py` reconstructs the semidirect-product group multiplication independently of its closed conjugation formula. For twelve finite abelian kernels it enumerates all quadruples of quandle elements, generates every equality forced by the medial identity, closes the resulting equivalence relation under multiplication, and confirms equality with the predicted rotations-singleton/reflections-modulo-\(4A\) classes.

Command: `python3 verify.py`.

Observed output: `VERIFY_OK`; all twelve case-level checks reported `OK`. Tested kernels were cyclic of orders 2, 3, 4, 5, 6, 7, 8 and products with invariant orders (2,2), (2,3), (2,4), (3,3), (2,2,2). The broad theorem for arbitrary abelian groups, including infinite groups, is verified by the explicit four-variable algebraic identity and minimality witness in `RESULT.md`, not by finite enumeration.

An independent audit or formal proof certification has not been performed.
