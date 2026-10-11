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

The universal proof is algebraic. The packaged verifier `artifacts/verify_extreme3.py` enumerates 8,176 normalized three-point supports in a family of small product groups, checks the repeated-difference classification, and verifies explicit constant-modulus witnesses for every encountered order-three and order-four candidate. It reports:

`VERIFY_OK triples=8176 multiplicity_candidates=169 good_C3_C4=133 V4_obstructions=36`

The finite enumeration is a regression test only. The proof for arbitrary discrete abelian groups rests on Fourier uniqueness, the exhaustive directed-difference case split, and the exact Klein-four phase contradiction. No claim of independent validation is made.
