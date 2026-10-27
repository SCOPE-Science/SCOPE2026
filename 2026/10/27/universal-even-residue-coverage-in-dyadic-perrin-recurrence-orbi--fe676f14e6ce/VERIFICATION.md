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

The self-contained `verify.py` checks integer powers of the recurrence companion matrix, the seven nonzero parity triples and their unique index choices, and the explicit dyadic lifting matrices at ten levels. It also enumerates all primitive triples modulo 2, 4, 8, and 16, and 103 selected primitive triples modulo 32, independently confirming that each chosen arithmetic-progression subsequence is an exact permutation of the even residues. Run `python3 verify.py` in a directory containing this file.

The verification covers finite moduli only. The unrestricted theorem is proved algebraically in RESULT.md. An independent mathematical audit has not been performed.
