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

The analytic proof is given in RESULT.md. Run `python verify.py` from a directory containing the standalone included program. Python 3 suffices for its exact-arithmetic checks; `mpmath` is an optional dependency for independent high-precision matrix-exponential diagnostics.

The exact-arithmetic checks construct Gaussian-integer Hamiltonian matrix powers with total magnetic flux \(\pi/2\), including nonuniform positive hopping, and verify Taylor coefficients and weighted entropy prefactors for the odd sizes \(N=3,5,7,9\). Execution passed 328 exact rational checks. With `mpmath` available, 19 additional high-precision checks passed for both odd- and even-size rings. The high-precision entropy ratios approach one as \(\tau\) decreases in each tested case.

No finite computation proves the theorem for arbitrary size. The bound on unexamined sizes depends on the graph-theoretic fact that the first odd closed walk on a chordless odd cycle has length exactly \(N\), followed by analytic Taylor expansion and an evenness argument for the entropy observable. The finite-time diagnostics do not certify error constants uniformly in \(N\) or address partial dephasing.
