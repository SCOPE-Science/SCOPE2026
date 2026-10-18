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

The proof in `RESULT.md` is the basis for the theorem for all integer parameters and all real exponents. Its independently stated arithmetic subclaims are tested by the accompanying executable `verify.py`, using exact rational arithmetic and standard-library Python.

Execute `python3 verify.py` in the directory containing both files. A successful run reports 20 tested parameter pairs, 2,970 projected edge columns, 5,353 exact idempotence-entry identities, and 780 exact finite-difference identities. Laplacian potentials and both claimed endpoint column norms are verified in those instances. The finite test range is \(3\le r\le7\) and \(2\le p\le5\); it does **not** certify the universal theorem, its representation-theoretic lemma, or the literature originality assessment.

The earliest public source for the motivating invariant-projection problem is arXiv:2305.12582v1, submitted 21 May 2023 UTC. Related earlier work is arXiv:2007.07949v1, submitted 15 July 2020 UTC.

Independent scientific audit: not performed.
