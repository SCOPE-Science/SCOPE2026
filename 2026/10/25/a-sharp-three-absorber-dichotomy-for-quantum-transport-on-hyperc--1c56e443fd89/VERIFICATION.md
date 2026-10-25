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

The analytical proof in `RESULT.md` establishes the theorem for all \(d\ge2\). Run `python verify_three_hypercube_traps.py` with Python 3; no third-party dependencies are needed. The checker uses exact integer arithmetic modulo 1000003, evaluating independent Walsh-shell and adjacency-Krylov ranks. It reports 3, 21, 105 and 465 anchored triples for dimensions 2–5, and 166 sampled anchored triples for dimension 6, with `PASS 1388 exact finite rank checks (two independent formulations)`.

A modular rank can in general be lower than its rational characteristic-zero counterpart, so those checks only corroborate the theorem; the explicit parity-combinatorial rank proof, valid over the complex numbers, is decisive. The test suite does not verify infinite-volume limits, arbitrary loss-rate time traces, or novelty. The observational content comes from the all-dimensional proof and is independent of the numerical enumeration. Independent scientific audit is not yet performed.
