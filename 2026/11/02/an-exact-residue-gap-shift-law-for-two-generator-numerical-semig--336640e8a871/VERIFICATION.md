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

# Reproducibility and boundaries

Execute `python3 verify.py` with Python 3.9 or newer; only the standard library is required. The program computes the defining gap sets by a dynamic-programming representability table, not by the Fourier proof, and compares each of the predicted differences for 5,005 admissible parameter triples, covering 57,323 residue classes. It also independently checks CRT multiplicities, the exact sharp spread, balance criterion, quotient-genus transition, and population variance using `fractions.Fraction`.

Observed output:

```text
VERIFY_OK parameters=5005 residue_instances=57323 independent_dp=yes CRT_and_variance=yes exact_rationals=yes
```

The computations cover only these finite ranges. The theorem for all admissible positive parameters follows from the finite polynomial and exact roots-of-unity proof. No independent mathematical audit or historical-priority certification has been performed.
