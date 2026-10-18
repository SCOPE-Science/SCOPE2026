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

# Reproduction and limits

The package includes a complete standard-library Python 3 verifier, `verify.py`, executed with `python3 verify.py`. Expected output:

```
VERIFY_OK rational_identity_cases=7 global_orbit_cases=33 finite_amplitude_reversal=PASS
```

Exact rational certificates check the phase ratio and two-cycle equations, the arithmetic-mean formula and its factorized constant-policy comparison for three sign regimes and their degenerate boundary. High-precision decimal trajectories separately test 33 parameter/initial-value combinations, including the persistence boundary and the critical extinction case. This is a finite reproducibility check; the proof of all-parameter convergence relies on the logarithmic-coordinate strict-contraction argument and the extinction monotonicity calculation in `RESULT.md`.

The two explicit same-mean survival-policy instances are \((7/10,3/10)\) and \((8/10,2/10)\) at \(R=10\); their long-run mean-square abundances are \(2\sqrt5\) and \(2\sqrt{10}-5/2\), respectively, compared with the constant policy's value \(4\). The verifier checks the sign reversal; elementary radical comparisons are exact.

This file records implementation checks and mathematical limits, not an independent external audit or formal certification.
