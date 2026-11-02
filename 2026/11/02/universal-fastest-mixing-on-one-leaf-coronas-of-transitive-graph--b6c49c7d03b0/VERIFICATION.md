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

# Computation and verification record

The self-contained `verify.py` was run in Python with numerical and symbolic dependencies listed in `requirements.txt`; the output ended with `PASS 1768 symbolic/numeric grouped assertions`.

The program builds full \(2n\times2n\) transition matrices for 42 graph cases, including cycles, complete graphs, hypercubes, balanced complete bipartite graphs, Petersen and Johnson examples. It checks stochasticity, edge support, spectral formulas, one-dimensional numerical minimizers, nonsymmetric feasible samples, and exact symbolic stationarity identities. The test program's random generator is seeded and reproducible.

These finite computations do not prove the global theorem, do not rule out unenumerated asymmetric optimum matrices, and do not constitute independent mathematical audit. The analytic proof establishes the global optimum via symmetry averaging, spectral envelope domination and strict scalar convexity. The separate exact symbolic identity uses \(s^2=2c\).
