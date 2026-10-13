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

# Verification of exact two-qubit marginal covariance

## Reproducible calculation
The included `verify.py` uses only the Python 3 standard library. Run `python verify.py` from the directory containing this file. The executable enumerates every labeled simple graph on four, five, and six vertices: 64, 1024, and 32768 samples. For each graph, it forms two-row binary cuts and counts maximally mixed two-site marginals; it separately calculates isolated vertices. Accumulated expectations, second moments, mixed defect-isolation moments, and representative overlapping/disjoint pair covariances are compared with the closed formulas using exact rational arithmetic.

A distinct direct-quantum calculation constructs graph-state computational-basis signs and performs exact reduced-density-matrix sums on all 64 four-vertex graphs plus 100 five-vertex and 100 six-vertex graphs. It compares each marginal's equality to the maximally mixed density matrix with the cut-rank prediction. The documented execution result was `VERIFY_OK`.

## Scope of the checks
Exact finite enumeration is not a proof for arbitrary qubit counts, and computational checks are not independent validation. The complete all-size proof is in `RESULT.md`, including conditional independence for two event-pair overlap types and the separate isolation covariance calculation. The asymptotic statements follow from explicit symbolic polynomial identities with \(t=2^{-(n-3)}\). Reproduction requires no downloaded datasets or external dependencies.
