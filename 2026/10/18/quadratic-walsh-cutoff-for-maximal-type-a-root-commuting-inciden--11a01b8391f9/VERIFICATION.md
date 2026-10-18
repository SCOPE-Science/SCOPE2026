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

# Reproducibility

Run `python3 verify.py` in the same directory. The standard-library-only program constructs actual elementary matrices, multiplies them, and tests exhaustive maximal-clique enumeration for \(2\le n\le6\), independently of the source/sink classification. For \(2\le n\le9\), it constructs the full Boolean incidence matrix, checks its rank modulo two large distinct primes, evaluates all high-degree rational Walsh and integral finite-difference null vectors against the actual columns, and independently compares maximal-clique size frequencies with the Gaussian-binomial recurrence.

The observed terminal output is:

`VERIFY_OK_ROOT_WALSH n=2..9; exact maximal cliques n=2..6; modular rank, Walsh and integral-difference kernels n=2..9`

The characteristic-zero and integral general assertions follow from explicit column operations and Boolean Möbius inversion in `RESULT.md`, not from finite tests or their execution logs. Modular rank checks alone do not prove an integral Smith-normal-form statement; the proof constructs a unit minor. No independent mathematical audit is claimed.
