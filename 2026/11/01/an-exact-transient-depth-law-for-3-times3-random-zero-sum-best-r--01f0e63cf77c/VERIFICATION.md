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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and its standard library. The checker enumerates all \(9!\) strict rank matrices and separately computes linear extensions for every row-minimum/column-maximum map using the nine-cell subset recurrence. It checks full agreement in eight cycle/depth classes and five vertex-depth totals, verifies both exact probability laws, the mean \(179/315\), and the structural \(72\times96\) maximal-chain count. The test terminates successfully with `EXACT_VERIFY_OK`.

Every strict rank matrix has positive probability \(1/9!\) under i.i.d. atomless payoffs. Thus this finite enumeration exhausts the stated probability space, rather than sampling it. The maximum-depth bound of four follows from the existence of a directed cycle on at least two vertices in a six-vertex functional graph; a displayed rank matrix attains it. Neither the code nor this review provides independent peer validation, claims about larger strategy spaces, or claims about other learning dynamics.
