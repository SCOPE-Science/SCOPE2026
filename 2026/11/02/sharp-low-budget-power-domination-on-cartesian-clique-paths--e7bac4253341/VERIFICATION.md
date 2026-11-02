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

# Reproducibility and verification

The standalone `verify.py` uses only Python's standard library. Run it as `python verify.py`. It constructs the Cartesian product directly, computes the closed-neighborhood initialization, and repeatedly applies the observed-vertex unique-unobserved-neighbor rule until the state stops changing. It does not use the layer criterion to implement the graph dynamics.

For each \(3\leq n\leq6\), \(3\leq L\leq7\), and each seed subset of size \(0\leq k\leq n-2\), the checker compares direct propagation with the claimed endpoint-or-consecutive-layer criterion. It separately computes the independent-set polynomial coefficients using elementary binomial identities and compares those coefficients to the direct success counts. It also checks a size-\(n-1\) successful witness that violates the support condition for each parameter pair.

Observed execution result: `PASS direct forcing, sharp cutoff and all low-degree coefficients: 257426 subsets across 20 dimension pairs`.

The proof for arbitrary parameters is in `RESULT.md`. A successful finite census is not an infinite proof, and no external or independent audit has been performed.
