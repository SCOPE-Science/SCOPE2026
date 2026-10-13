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

# Reproducibility and mathematical checks

Execute `python3 verify.py` in a Python 3 environment with no third-party dependencies. The verifier evaluates all reduced automorphisms and all constant infinitesimal corrections in the stated sample rings using multiplication reduced by \(x^n=\varepsilon x^r\), rather than using the proof's power-congruence test. It compares the observed image counts and constant-correction multiplicities with the theoretical expressions. It outputs:

```
EXHAUSTIVE_PARAMETER_CASES= 43 VERIFY_OK
INCLUDING_EXTENSION_FIELD_CASES= 52 VERIFY_OK
```

These \(52\) cases include every \(r\) for \(2\le n\le6\) over \(\mathbb F_2\), \(2\le n\le5\) over \(\mathbb F_3\), \(2\le n\le4\) over \(\mathbb F_5\), and \(2\le n\le4\) over \(\mathbb F_4\). The general field and dimension claims follow from the defining-relation identity, free-module invertibility, and the finite-field Frobenius count in the proof; only these bounded small parameter cases are computationally enumerated.
