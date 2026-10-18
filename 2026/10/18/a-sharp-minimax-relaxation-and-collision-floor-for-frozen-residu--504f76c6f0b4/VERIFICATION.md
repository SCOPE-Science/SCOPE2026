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

# Reproducibility and scope

Run `python verify.py` with Python 3. The checker uses only standard-library rational arithmetic, complete multinomial count enumeration in finite verification cases, and seeded pseudorandom multinomial sampling. Its reported total is `ALL_CHECKS_PASSED 98917`. The simulation with \(d=3\), \(k=6\), \(p=(0.61,0.25,0.14)\) gives approximately \(0.264191\) versus the exact moment \(0.264518\). The checker also exercises boundary and transition cases over a wide finite set of dimensions and batch sizes.

For the unrestricted theorem, read the pair-affine cubic-simplex proof and the two quadratic minimization in `RESULT.md`. Finite experiments neither prove a global simplex extremum nor substitute for the uniqueness argument. The exact assertions concern conditional one-batch squared error, with a separately derived geometric upper bound on repeated refreshed batches. The limit with many simultaneous workers is **not** a lower bound on long-run attainable accuracy. Bibliographic equivalence to an unindexed treatment cannot be excluded by the recorded searches. Independent verification has not been performed.
