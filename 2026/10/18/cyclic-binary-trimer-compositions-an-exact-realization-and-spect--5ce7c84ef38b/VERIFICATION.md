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

# Finite checks and proof boundary

Run `python3 verify.py` using Python 3.9 or later. The program uses the standard library only. It enumerates every circular binary word of lengths \(1\) through \(16\), computes each trimer-composition vector directly, and compares the complete attainable set with the closed characterization. A separate finite-state dynamic program propagates two-symbol contexts and triples, including the two closing cyclic windows, for lengths \(1\) through \(48\); it independently checks the same feasible sets and the exact counting-series coefficients. Both procedures executed successfully and reported `FINITE CHECKS PASSED`.

The result for all positive lengths is not inferred from this finite experimentation. It follows from a constructive cyclic run-length decomposition and exact rational generating-function summation in `RESULT.md`. The verification program does not check the existence of external equivalent theorems or provide an independent audit. The earliest cited public paper concerns a related but distinct composition-reconstruction model.
