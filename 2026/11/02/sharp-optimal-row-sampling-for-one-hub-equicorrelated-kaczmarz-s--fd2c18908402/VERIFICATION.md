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

# Verification of the one-hub fixed-probability theorem

The proof provides three exact symbolic identities: a square factor for the radial characteristic polynomial at the claimed optimum, a leaf/radial characteristic crossing polynomial, and the factorization of the branch-switch condition. They are checked by the standalone `artifacts/verify_kaczmarz.py` script using symbolic expansion.

The script additionally reconstructs the eigenvalues of the full \((m+1)\)-dimensional sampled Gram matrix, checks that the claimed value matches the minimum eigenvalue, compares against independently drawn probability vectors, and evaluates a rational example exactly at the branch transition. These finite samples are diagnostic checks and do not certify the quantified theorem. The global uniqueness claim is justified analytically by equality of Rayleigh quotients and invertibility, not by sampling.

The command used for replay after extraction is:

```text
python artifacts/verify_kaczmarz.py
```

Recorded replay result: `PASS: 9616 assertions; both spectral branches and exact phase boundary covered.`

Unverified domains: no formal proof assistant verification; no independent mathematical audit; no independent comprehensive historical priority certification. All publication dates refer to public source evidence, not to this document.
