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

Run `python3 verifier.py` with a standard Python 3 interpreter. It reconstructs the vertices and disjointness adjacency of \(KG(n,2)\), enumerates all supports with \(2r\) not exceeding the claimed optimum for orders \(7\), \(8\), and \(9\), and computes their minimum possible perfect Roman weights. A separate direct interpretation of unique adjacency checks the central support identity for supports of sizes \(1\) through \(3\) in graphs with orders \(7\) through \(11\). The fixed, deterministic output is embedded as `verification_output.txt`.

The support-size cutoff is exhaustive **only for the question of minimum functions at each tested order**, since any support of size \(r\) has weight at least \(2r\). The code does not enumerate arbitrary three-valued label assignments; the exact support reduction proves that this is unnecessary for finding minima and that a minimizing support has a unique minimum labeling extension. Computation at finitely many orders does not establish the all-order result; that conclusion follows from the mathematical proof in `RESULT.md`. No independent audit has been performed.
