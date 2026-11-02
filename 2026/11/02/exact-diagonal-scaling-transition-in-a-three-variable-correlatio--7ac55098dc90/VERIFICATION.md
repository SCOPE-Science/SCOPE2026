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

# Reproducibility and verification

Run `python verify.py` with packages in `requirements.txt`. The packaged script performed symbolic block diagonalization, crossing and phase identities, exact example and limiting ratio checks, then 160 parameter-pair checks and 640 unrestricted numerical minimizations. Output:

```
VERIFY_OK symbolic=8 exact_example=1 asymptotic=1 global_numeric_cases=160 minimizations=640
```

The proof in `RESULT.md` is the basis of the universal claim. Finite optimization runs cannot certify global minimality over all positive diagonal matrices or parameter pairs; the Loewner averaging argument is essential for the unrestricted reduction. A later independent audit was not performed.
