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

The accompanying `verify.py` is self-contained. It reads no external files, uses no downloaded data and requires only Python's standard library. Execute `python3 verify.py` from the same directory.

The script uses exact rational Gaussian elimination on the graph Laplacian and exact rational execution of the update rule. It checks every connected labeled graph with \(2\) through \(5\) vertices and each possible choice of one negative edge, totaling **4,294 graph-edge instances** (1,067 bridges, 3,227 nonbridges). The strict nonbridge criterion, endpoint max/min potential property, two fixed-point equations and degree-weighted conservation all passed.

The script additionally verifies the exact resistance formulas \(R_{C_n}=(n-1)/n\) and \(R_{K_n}=2/n\) for \(3\le n\le16\), and 45 exact-rational iterations of a perturbed four-cycle polarization. All assertions passed in the recorded run. For the infinite graph family and all parameters, correctness relies on the mathematical proof in RESULT.md, not on these finite checks.

Independent audit and validation have not been performed.
