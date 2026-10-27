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

# Verification

The accompanying `verify.py` runs using only the Python 3 standard library. Invocation: `python3 verify.py` from the directory containing the file. It checks 125 exact rational identities on the stationary second-moment system, characteristic-polynomial sign, and correlation-time formula. It also compares direct two-dimensional matrix propagation with the two-mode decomposition and samples the distinct high-reset asymptotic regimes using numerical tolerances. On the packaged version it completed 268 deterministic assertions.

The exact proof requires neither floating-point calculations nor sampling. The infinitely many parameter choices are covered by the displayed algebraic factorization and exact generator identities. The limiting claims are justified by explicit fixed-\(g\) asymptotics, and the Fourier transform is taken before the strong-reset limit. The check does not establish a bound uniform in all frequencies, convergence at lag zero under the fixed-lag normalization, or any behavior outside the stated model.

No independent validation has been performed.
