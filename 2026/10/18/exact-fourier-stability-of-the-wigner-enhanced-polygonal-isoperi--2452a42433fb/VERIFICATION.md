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

# Reproducibility and verification limits

Run `python3 CHECK.py` in the same directory. The standard-library program constructs polygons from cyclic edges and checks their signed shoelace areas, Wigner-caustic signed areas, independent Fourier sums, the variance lower bound, and the minimizing-mode equality patterns. It reported `PASS: 1163 polygons, orders 2..21; max absolute residual 5.98e-12`, followed by `PASS: sharp soft-mode constructions at all orders 2..21`. Numerical tolerances are explicit in the code.

The identity for arbitrary \(n\ge2\) is proved by the sine-kernel circulant calculation in `RESULT.md`; no finite test or successful log constitutes an infinite proof. The independent audit status above is an unperformed channel, not a judgment of correctness. The exact sharp coefficient and equality case are subject to the specific historical-literature priority risks stated in `REVIEW.md` and `AUDIT.json`.
