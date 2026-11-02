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

# Reproducibility and boundaries

Extract `verify.py` alongside this file and execute `python3 verify.py` with Python 3 standard-library modules only. The program computes directed Laplacian principal minors by integer-preserving Bareiss elimination for \(2\le q\le6\), compares them with the symbolic tree formula, and uses an independent exhaustive edge-mask traversal for \(q=2,3\). Every completed traversal is checked against its exact set of cyclic length-three windows. Successful verification ends with the line `VERIFY_OK`.

Checks actually run: for \(q=2\), 4 vertices, 4 edges, tree count 1 and 1 Euler circuit; for \(q=3\), 9 vertices, 18 edges, tree count 108 and 108 directly enumerated circuits; for \(q=4\), 16 vertices, 48 edges, tree count 3538944; for \(q=5\), 25 vertices, 100 edges, tree count 45562500000000; for \(q=6\), 36 vertices, 180 edges, tree count 332791666011065548800000. The corresponding cycle counts for \(q=4\) and larger use the mathematical BEST factor rather than brute-force enumeration.

Finite tests cannot establish the infinite theorem. The proof depends on the exact invariant-subspace calculation and standard directed matrix-tree/BEST theorems, as supplied in RESULT.md. No independent scientific assessment has been performed.
