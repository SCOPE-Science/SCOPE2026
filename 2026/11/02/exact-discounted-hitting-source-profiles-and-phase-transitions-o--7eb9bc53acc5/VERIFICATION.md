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

# Reproducible verification

Execute `python3 verify.py` with Python 3 and only the standard library.

The script constructs every friendship graph on \(2m+1\) labelled vertices for \(1\le m\le5\), builds the unweighted adjacency from triangle edges, and independently solves the first-step support equations with exact `fractions.Fraction` Gauss–Jordan elimination for every one of its \(2^{2m+1}-1\) nonempty source sets. The separate occupancy formula predicts the entire feasible-set size histogram for each chosen fidelity and threshold. All coefficients must agree with direct graph computation. It also checks the minimum-size and optimizer-count phase diagram, including threshold equality.

Tests cover \(\lambda=1/2,2/3,4/5\) and 202 choices of exact rational \(\tau\), including all relevant critical thresholds and interval midpoints. The terminal success marker is `VERIFY_OK`. The test has been run successfully. The checked \(m\) values are finite; the infinite theorem requires and receives the mathematical proof in `RESULT.md`. These tests are not an independent mathematical audit.
