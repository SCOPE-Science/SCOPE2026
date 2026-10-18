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
Execute `python verify.py` from the directory containing this file using Python 3 and its standard library. The checker directly enumerates all binary words with positive symbol counts at most six per symbol, independently checks the fixed-margin counting coefficients and rational moments, and checks the two exact variance-gap identities for all \(2\le m\le 24\) and \(m\le h\le80\). All equalities are exact rational arithmetic; no floating-point tolerances or random seeds are needed. Exit code 0 and a final `PASS` line indicate successful finite checks.

The mathematical proof for unrestricted integers is in `RESULT.md`. Finite enumeration alone cannot certify an infinite family. The earliest public source date pertains to the cited research lineage, not a claim that the present finding was externally published. Independent audit has not been performed.
