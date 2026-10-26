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

# Reproducibility and checked limits

The exact primary verifier is `artifacts/verify.py` and its recorded output is `artifacts/verification_output.txt`. Run it with Python 3. It has no third-party dependencies; it generates the complete unlabeled target-tree classes through fourteen vertices and the complete unlabeled source-tree classes through seven vertices. The output checks expected order counts, all path-profile equivalence classes, all source-size minima, the exact fourteen-vertex exceptional graphs, and the two positive witnesses. The generated tree count is \(5447\).

The separate `artifacts/independent_check.py` uses `networkx.nonisomorphic_trees`, does not import the primary verifier, and independently recomputes the thirteen-to-fourteen gap with its own homomorphism recurrence. Run with NetworkX 3 or later; recorded output is `artifacts/independent_output.txt`.

The finite path comparison is exact for **all** path lengths because the difference of two size-\(n\) walk-count sequences obeys a recurrence of order at most \(2n\). It is enough to compare the first \(2n\) terms. Unbounded host-order behavior and novelty beyond inspected sources have not been verified. The scientific review is self-review only; no independent audit is asserted.
