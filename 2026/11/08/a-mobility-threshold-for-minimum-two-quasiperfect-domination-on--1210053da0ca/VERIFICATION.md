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

## Reproducibility

Run `python check_exhaustive.py` and `python check_independent.py` with Python 3.10 or newer. Neither script needs network access or third-party packages. Compare their JSON stdout with `exhaustive_output.json` and `independent_output.json`. Both programs include hard assertions for all claimed finite counts, exchanges and sampled distances. They construct the feasible sets by different methods (literal subset enumeration and row/column-mask generation).

The symbolic proof in RESULT.md covers all integers \(3\le m\le n\); the computations cover finitely many labelled boards, and do not constitute a proof of all-order claims. In particular, the exact arrangement-graph distance formula also has its own dependency-cycle proof in RESULT.md. Independent scholarly audit has not been performed.
