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

The proof uses an induction on all terms and an explicit finite disjunctive construction of each support-selection function. It does not rely on an exhaustive sample to make an all-size claim.

Run `python3 verify.py` using Python 3 standard library. Verified outputs include `DIRECT_UNARY 1 4`, `DIRECT_UNARY 2 16`, `DIRECT_UNARY 3 16`, `REFINEMENT 2 2 dimension 16 rounds [4, 16]`, and `ENDPOINT_TEST_TERM_CLONE_VERIFY_OK`.

The checker uses two different finite reconstructions: raw unary operation-table closure and refinement of coordinate partitions under the consistency operator. Their mathematical independence is limited because both implement the stated semantics; neither is external certification. General formulas, stabilization and sharpness are established in RESULT.md. The cited general discriminator theory was not re-proved or needed for the direct constructive proof.
