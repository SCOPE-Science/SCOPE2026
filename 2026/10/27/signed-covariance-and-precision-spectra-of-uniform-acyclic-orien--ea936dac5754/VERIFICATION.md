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

Execute `python3 verify.py` with Python 3. The standard library suffices. The checker applies a graph-theoretic topological-sort test to every one of the \(4^n\) orientations of \(K_{2,n}\) for each integer \(2\le n\le8\), independently comparing this test with the two-forbidden-column characterization. It then checks exact rational first and second moments, every displayed covariance entry, every inverse entry through matrix multiplication, and the strict covariance/precision sign classifications. Exact finite identities are also checked at each \(2\le n\le100\). The recorded execution passed 90,094 exact assertions.

The code neither samples nor estimates probabilities: all enumerated comparisons use integer counts and rational arithmetic. It **does not** exhaust infinite sizes and **does not** establish novelty. The unrestricted proof of the theorem is the inclusion–exclusion, block diagonalization, matrix inversion, convexity, and limit argument supplied in `RESULT.md`. The independently unverified matters are mathematical priority, other graph families, weighted orientation laws, and nonlinear conditional dependence.
