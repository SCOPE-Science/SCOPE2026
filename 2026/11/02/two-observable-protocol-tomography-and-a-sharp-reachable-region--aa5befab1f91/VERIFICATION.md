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

# Verification evidence and scope

The result is established by the mathematical proof in `RESULT.md`. A separate, self-contained executable `verify.py` (Python 3 standard library only) performs 6,015 computational checks. It tests exact rational matrix products for the two covariance contrasts, multi-stage propagation composition, the zero-reference-contrast degeneracy, numerical bounded-control realization and inverse recovery, and the Jacobian sensitivity identities. It then independently integrates the driven three-variable equal-time Lyapunov covariance differential equation and all four time-ordered covariance components across multiple driven intervals with time-dependent bath noise, checking the final contrast recovery against independently integrated state values.

Reproduction: `python3 verify.py`.

Expected terminal output:

```text
PASS: 6012 deterministic assertions
PASS: 6015 assertions including independently integrated driven covariance
```

Computational tests are finite and cannot verify every admissible time protocol, prove a universal quantified statement, or certify priority. No machine-checked formal proof or independent expert audit is claimed. The theorem relies on the exact matrix and inequality proof.
