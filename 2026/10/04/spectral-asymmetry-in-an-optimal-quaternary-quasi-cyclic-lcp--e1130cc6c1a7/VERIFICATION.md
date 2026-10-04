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
`artifacts/verify.py` is a standalone Python-standard-library replay.

It represents \(\mathbb F_4\) as \(\mathbb F_2[\omega]/(\omega^2+\omega+1)\), expands the two \(R\)-module generators through all seven cyclic shifts in each block, and row-reduces the resulting ordinary length-\(14\) generator matrices.

The replay verifies \(\dim C=9\), \(\dim D=5\), \(\operatorname{rank}(C+D)=14\), constructs the Euclidean dual \(D^\perp\), and verifies its dimension \(9\). It enumerates every one of the \(4^9\) words in both \(C\) and \(D^\perp\), checks their full Hamming distributions and minimum distance, then exhausts all \(2^{14}\) coordinate subsets to recompute all generalized Hamming weights from exact restricted-column ranks.

The finite computations are exhaustive for this row. No sampling, timeout inference, or external algebra package is used.
