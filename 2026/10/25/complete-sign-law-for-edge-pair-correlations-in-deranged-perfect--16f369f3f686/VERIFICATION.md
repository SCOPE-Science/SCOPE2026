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

Run `python deranged_matching_edge_covariance_check.py` with Python 3.9 or newer. It uses only the standard library and prints per-order counts and assertion totals. The expected total is **19,267 exact assertions**, with counts of deranged matchings \(D_2=2,D_3=8,D_4=60,D_5=544,D_6=6040,D_7=79008\).

The enumerator independently lists all pairings of \(2n\) vertices for \(2\le n\le7\), rejects forbidden original pairs, and compares exact rational covariances for every pair of distinct allowed edges with the symbolic predictions. It separately checks the count recurrence and exact sign relations through \(n=300\). Verification is finite; the full parameter theorem follows from the conditional counting argument and recurrence proof in RESULT.md, not from extrapolation. Asymptotic constants rely on the previously established deranged-matching count asymptotic. Historical priority and independent review have not been conclusively resolved.
