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

# Reproducibility of the exact strongly regular graph calculation

Run `python3 verify.py` with Python 3.10 or newer, using only the standard library. The program constructs graph adjacency matrices from direct edge rules, checks the defining common-neighbor identity for every vertex pair, builds both stochastic transition matrices as rational arrays, multiplies them exactly, and compares their entries to the claimed closed forms. It also checks the centered spectral objective via the two quadratic adjacency roots and tests a \(41\times41\) grid of feasible gains on each example.

Observed output ends with `VERIFY_OK 20687 assertions; 8 independently constructed graphs`. Example graphs are the five-cycle, Petersen graph, Clebsch graph, rook graph on a \(3\times3\) grid, triangular graph on seven labels, equal-part complete tripartite graph, Shrikhande graph, and four-cycle. The gain-grid and square-root evaluations use floating point and are not exhaustive continuous minimization certificates. The analytic global lower-bound certificate and equality cases are given in `RESULT.md`; independent validation has not been performed.
