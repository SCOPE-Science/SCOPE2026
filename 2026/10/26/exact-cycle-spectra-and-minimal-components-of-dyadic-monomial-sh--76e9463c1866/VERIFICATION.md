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

# Reproducibility

Run `python3 verify.py` with Python 3.8 or newer; no third-party dependencies are needed. The script independently builds all permutation maps for degrees \(d=3,\ldots,21\) and bit depths \(k=1,\ldots,13\), follows all cycles without using the period formulas to generate the trajectories, and compares every orbit and each complete cycle histogram to the claimed formulas. It reports:

`VERIFY_OK: 247 exhaustive parameter pairs; 311258 total enumerated residues; 121950 independently traced cycles`

The exact all-degree and all-depth result is established by the valuation-doubling and minimality proof in `RESULT.md`, not by the finite checks. Only coefficient \(2\) is covered; general \(2a\) can have different 2-adic dynamics. No independent audit has been performed.
