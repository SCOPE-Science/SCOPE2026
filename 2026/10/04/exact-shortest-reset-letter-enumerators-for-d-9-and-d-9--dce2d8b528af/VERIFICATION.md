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
# Verification

`verify.py` is a standalone Python verifier using only the standard library. It performs two exact computations from the stated transition tables.

First, a bit-mask breadth-first search computes minimum distances from the full state set and propagates a polynomial on the shortest-path DAG, multiplying by \(z\) on an \(a\)-edge. This proves the first-singleton distances and the complete shortest-word \(a\)-weight distributions.

Second, an independently represented `frozenset` layer propagation tracks integer histograms by \(a\)-weight without using the bit-mask BFS tables. It reaches its first singleton at the same lengths and produces the same coefficients and unique targets.

The verifier expands \(z^8(1+z)^{30}(2+z)^6\) and \(z^7(1+z)^{30}(1+z+z^2)^6\) by integer arithmetic and compares them coefficient-for-coefficient with both computations. It also checks that each coefficient sum is \(782{{,}}757{{,}}789{{,}}696\).

The computation is exhaustive for the finite nine-state power automata. It does not prove an analogous formula for arbitrary \(n\). A successful run ends with `VERIFY_OK`.
