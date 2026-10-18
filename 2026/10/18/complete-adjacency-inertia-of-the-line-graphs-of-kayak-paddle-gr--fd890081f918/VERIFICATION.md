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

# Exact reproducibility

Run `python3 verify_kayak.py` using Python 3.10 or later; no third-party packages or network access are needed. The verifier constructs the twenty base kayak-paddle line graphs and shifted signless Laplacians from separately defined edge incidences, computes all inertias by exact rational congruence, and compares the two methods and all stated table entries. It then performs 1,320 further exact checks with parameters \(3\le p\le q\le17\) and \(1\le r\le11\). The executable output must be identical to `verification_output.txt`:

```text
BASE_CASES_EXACT 20
EXTENDED_CASES_EXACT 1320
ALL_CHECKS_PASS
```

The exact finite base calculations are logically exhaustive because the proof reduces all permitted triples to these twenty bases by invertible congruences. The 1,320 larger calculations are independent checks of the reduction's conclusions, not a substitute for that reduction. No independent human or external audit has been performed.
