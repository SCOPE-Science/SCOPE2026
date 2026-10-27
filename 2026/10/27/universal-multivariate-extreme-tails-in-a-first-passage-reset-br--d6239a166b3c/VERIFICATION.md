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
# Reproducible checks

Run `python verify_first_passage_tail.py` with Python 3.9 or newer. Only the Python standard library is needed. The program numerically integrates the exact finite-threshold stationary renewal formula after scaling out physical units, rather than merely re-evaluating the limiting gamma integral. It includes unequal negative thresholds, distinct particle-number cases, conditional tail ratios, positivity checks, and gamma-function recurrence checks.

Observed output:

```text
N=3: J_N=0.757602154835 C_N=0.840308819484; k=2 limit=0.707106781187
N=4: J_N=0.434349127692 C_N=0.93308518132; k=2 limit=0.5
N=5: J_N=0.324277723328 C_N=1.24980751194; k=2 limit=0.353553390593
N=7: J_N=0.233294242991 C_N=3.31785652519; k=2 limit=0.176776695297
PASS: 52 deterministic quadrature/algebra checks
```

The finite ratios tested are \(R/L=60,250\), while the limiting theorem is proved separately by an integrable dominating kernel and a gamma-integral evaluation. The numerical tolerances are finite-threshold consistency checks, not numerical error bounds for the infinite limit. No independent mathematical audit has been performed.
