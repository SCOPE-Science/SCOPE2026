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

# Reproducible exact checks

Run `python3 CHECK.py` from the directory containing this file. The script uses only Python's standard library and exact fractions. It constructs a grounded inverse of the vertex Laplacian for each of the intact and one-edge-deleted hypercubes in dimensions two through four, and constructs the full projection matrix independently through Walsh characters. It verifies the exact rank-one update, all complete deleted-graph row-sum multiplicities, the formulas for the changed row, and actual maximizing input sign vectors. Success produces the terminal line `PASS: all claimed finite-dimensional exact certificates`.

The calculations are finite and exhaustive **only in dimensions two through four**. The all-dimensional damaged-row formula and strict sensitivity increase for dimensions four and higher follow from the analytical heat-kernel and rank-one-update proof in RESULT.md. The stated first-order limit follows from direct asymptotics of the explicit rational coefficient. No independent audit or external theorem-proving certification was performed.
