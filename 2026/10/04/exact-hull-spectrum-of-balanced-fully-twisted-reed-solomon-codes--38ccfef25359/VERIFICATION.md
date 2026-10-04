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
The verifier uses only the Python standard library and works over prime fields so that all arithmetic and ranks are exact.

For each tested pair \((q,k)\), it constructs the multiplicative subgroup of order \(2k\), builds the source paper's generator rows
\[
C_i=V_{i-1}+\eta_iV_{k+i-1},
\]
builds the rescaled parity-check rows from the published formula, computes the rank of the full \(2k\times2k\) stacked matrix, and sets the hull dimension equal to its rank deficiency.

All nonzero twist vectors are exhausted for \((13,3)\), \((19,3)\), and \((17,4)\). The direct rank histograms are compared against the claimed product enumerator and against the pointwise indicator formula. The replay terminates with `VERIFY_OK`.

The finite computations are not an infinite proof. The all-parameter theorem follows from the exact block decomposition and orbit count in `RESULT.md`.
