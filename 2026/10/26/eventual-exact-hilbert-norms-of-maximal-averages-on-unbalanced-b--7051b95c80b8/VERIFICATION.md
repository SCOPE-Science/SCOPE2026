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

The analytic proof reconstructs all three ball-average branches, proves a unit-sphere bound uniform in the large vertex class, and uses it to force every maximizing input into the unique radius-zero/radius-one branch configuration. The resulting linear operator has a two-dimensional singular-value reduction. The explicit threshold is a sufficient bound, not an optimized value.

Running `python check.py` with Python 3 and NumPy completed 2,658 finite assertions: full enumeration of three possible radius choices at each vertex for six small bicliques, direct numerical singular-value calculations, maximal-branch checks, and exact-rational checks of the trace and determinant identities in additional parameter configurations. The small examples fall outside the proven large-imbalance threshold and do not imply it. The correctness of universal claims is supported by the analytic argument in `RESULT.md`, not by sampling.

No independent audit or publication-priority certification has been performed.
