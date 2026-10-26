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

# Reproducibility and scope

Execute `python3 verify.py` with standard Python. The checker uses rational arithmetic for the moment identities over 60 mixtures (ten integer variance scales and six rational mixing weights); it verifies positivity, two even moments, normalization, and cancellation of all odd degrees through five by symmetry. For the contamination \(\varepsilon_L=L^{-3}\) it compares a bounded smooth test integrand across four scales and checks three limiting predictions numerically.

Observed execution output:

```
PASS: 60 exact parameter checks, four bounded-integrand comparisons, three asymptotic checks
L=10000: direct=0.999966663333, componentwise=0.683262356123, integral=0.577350269189
```

The symbolic derivations, the all-rate weak-limit theorem and the minimal five-node lower bound require the analytic proof in `RESULT.md`; no finite computational test or log is offered as an infinite proof. Full texts of some relevant background papers were not accessible in this review, and novelty has not been independently established.
