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

## Reproducible checks

- Reconstructed the spin-1 singlet projector and the exact dimensionless Hamiltonian block.
- Derived the three exact 2×2 partial-transpose positivity conditions.
- Ran `verify_threshold.py` from the package path; output:

```text
eps, x_ac, 0.5*log(4/eps), difference, other_block_crossings
1e-02, 2.978270256448, 2.995732273554, -1.746e-02, 3.672815174379;5.243079740355
1e-03, 4.144701321835, 4.147024820051, -2.323e-03, 5.262329706100;7.593054556417
1e-04, 5.298027449371, 5.298317366548, -2.899e-04, 6.817524256256;9.902472239484
1e-05, 6.449575164968, 6.449609913045, -3.475e-05, 8.361192870051;12.205948085218
1e-06, 7.600898409089, 7.600902459542, -4.050e-06, 9.900145094091;14.508642979870
```

- The numerical table is a finite sanity check only. The asymptotic conclusion follows from the perturbative eigenpair and block inequalities in `RESULT.md`.
- Scope limits: \(J>0\), \(h>0\), \(k_B=1\), and \(h/J\to\infty\); NPT is tested, not full separability.
- No independent audit or independent validation has been performed.
