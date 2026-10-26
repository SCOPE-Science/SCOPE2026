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

The source `annular_szego_metric_checker.py` requires Python 3 with `mpmath` and runs as `python annular_szego_metric_checker.py` from the directory containing the file. The code computes the elliptic parameter from the Jacobi theta functions, verifies the nome relationship, and compares the closed metric formula against the variance of the independent Laurent half-integer summands. The truncation cutoff is chosen from the distance to the annular boundaries. It also tests exact optimizer-value formulas, reciprocal symmetry, sampled global lower bounds, and the quartic critical expansion. The completed run reported 1284 successful numerical checks at 65-digit working precision, using six annular widths including the critical value.

The proof of the all-parameter theorem instead uses the exact Jacobi Fourier series and a one-variable global optimization. No finite run certifies a universal statement; nor does absence of a database match establish historical novelty. Only the ordinary Euclidean-boundary-arclength Hardy kernel is addressed. No independent audit or independent validation was performed.
