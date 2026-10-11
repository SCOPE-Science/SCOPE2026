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

# Reproducibility and verification

Run `python verify.py` with Python 3 (standard library only). The code builds every allowed oriented rooted forest and its automorphism action for page counts 2 through 6, checks all 56 classes from the two hub states and every partition of each page count, and computes mod-two boundary ranks independently for page counts 2 through 4.

Observed results: for 2 pages, nonempty faces 74 and boundary ranks {1:9,2:23}; for 3 pages, nonempty faces 323 and ranks {1:13,2:56,3:84}; for 4 pages, nonempty faces 1322 and ranks {1:17,2:103,3:265,4:263}. The 5- and 6-page nonempty-face counts are 5183 and 19682. The script prints `CONJUGACY_CHECKS= 56` and `VERIFY_OK` and raises an exception if a check fails.

These finite computations do not certify the claim for every page count. The general proof uses complete-source shellability, the signed Hopf trace identity, the matrix-forest theorem and exhaustive orbit cases for arbitrary permutation cycle lengths. Integral module structure and equivariant homotopy type have not been determined.
