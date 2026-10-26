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

The reproducibility program `verify_window_two_deletion.py` was run using Python 3 after creation, directly from the package source path. It enumerates all input words for each tested parameter grid, constructs each length-\(\ell\) read sequence, and forms every exact-two-deletion output explicitly before deduplication. It separately checks the deterministic run identity and exact-rational expectation. It checked 294,061 words across 48 complete finite parameter grids and the rational limiting variance coefficient at 16 parameter pairs. The included execution record ends in `VERIFY_OK`.

The mathematical proof, rather than the finite sample, establishes the infinite-family identities and normal limit. The standard stationary finite-dependence CLT is invoked for bounded local indicators, and the fourth-moment bound is justified by the same finite-dependence structure. There has been no independent scientific audit.
