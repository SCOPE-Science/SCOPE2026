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

# Verification record

The theorem is established by the self-contained four-step algebraic proof in `RESULT.md`. Exact characteristic-two polynomial identities and characteristic-four finite tests are independently reproducible from `check_gr4.py` using `python3 check_gr4.py` (standard library only).

Actual executed output:

```text
Exact polynomial identities verified for all admissible m<=11.
Canonical coefficients: all 32 exceptional unit rows have sixteen cells of multiplicity 64.
Coefficient lift 1: all 32 exceptional unit rows verified.
Coefficient lift 2: all 32 exceptional unit rows verified.
CERTIFICATE_OK
```

The code enumerates every input in the concrete size-1024 Galois ring and every exceptional unit direction for those three coefficient lifts. It does not exhaust all finite fields, all lifts, or all parameters: the general statements follow from the proof. No external independent validation has been performed.
