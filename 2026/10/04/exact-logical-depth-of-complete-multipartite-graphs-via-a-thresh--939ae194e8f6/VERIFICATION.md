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

The proof is mathematical; computation is supplementary. `verify.py` carries out two independent finite checks. A recursive Ehrenfeucht--Fraisse game solver is compared with the triangular rank profile for every pair of integer partitions of total size at most six and ranks at most three. Separately, the threshold-path criterion is compared with exhaustive same-profile uniqueness over canonical bounded class-count vectors for small maximum class sizes and ranks. The script also checks the uniform and complete-bipartite corollaries on small parameter grids.

Recorded output:

`VERIFY_OK ef_cases=1305 criterion_cases=469 uniform=36 biclique=20`

These computations do not prove the infinite theorem. They are intended to catch mistakes in the EF profile reduction, path orientation, tight-threshold conventions, and boundary cases.
