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

# Verification and reproducibility

The standard-library checker is `wheel_checker.py`. Run `python3 wheel_checker.py`; it reports `PASS: 91 exact identities and numerical diagnostics`.

Exact rational checks enumerate complete independent configurations of the \(2n\) wheel edges for \(n=3,4,5,6,7\) and two rational retention parameter pairs. They independently compute the hub component for every case, compare the exact mean with the root-component sum, and verify the exact zero-connection probability. Additional rational checks compare the cyclic-word weights with traces of powers of the transfer matrix through length eleven. Truncated exponential-series and root-length integral checks are numerical diagnostics.

The infinite Poisson point-process convergence, almost-sure continuity of the hub-mass functional, and transfer-matrix limit are verified by the mathematical proof rather than by bounded enumeration. Historical priority is not independently certified.
