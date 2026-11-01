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

The finite checker `verify.py` can be executed with `python verify.py` (Python 3.9 or later). It constructs actual binary translation orbits, checks maximum Hamming distances between cosets, and compares these values to the proposed complete orbit-graph models. It checks 89 parameter/scale combinations across four action types, independently computes finite boundary ranks for scale-two and scale-three complexes, and checks 116 signed character evaluations directly from the oriented graph action.

Successful execution prints `VERIFY_OK 6 size cases, 116 character evaluations` and `MODEL_OK 89 full-filtration threshold models`. The test covers hypercubes through seven coordinates and first-homology boundary calculations at the smaller sizes stated by the checker. It does not verify the infinite ranges: these follow from the orbit-distance identities, cubical-square contraction, and triangle-shortening proofs in `RESULT.md`.

Relevant source comparisons are documented in `REVIEW.md` and `AUDIT.json`. Independent validation and further review of inaccessible source full text remain outstanding.
