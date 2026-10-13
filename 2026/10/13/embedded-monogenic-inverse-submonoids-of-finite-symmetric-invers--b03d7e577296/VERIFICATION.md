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

# Reproducibility and limits

Run `python checker.py` with Python 3.10 or newer; no third-party packages or network access are required. The program builds each partial bijection on \([n]\) for \(1\le n\le6\), computes its generated inverse submonoid as an explicit finite set, compares every common generating fiber and its chain/cycle profile with an independently calculated exact rational coefficient of the stated exponential generating function, and prints `VERIFY_OK` if all assertions succeed. This verifies the small cases, the full \(n=4\) profile, and exact generator-fiber cardinalities. It does not by itself prove the formulas for unbounded \(n\); that follows from the componentwise generator-rigidity and labeled exponential-formula proof given in `RESULT.md`.

The public literature review compares isomorphism-type enumeration with labeled embedded enumeration and retains the possibility of equivalent earlier computations under alternative terminology. Independent audit: not performed.
