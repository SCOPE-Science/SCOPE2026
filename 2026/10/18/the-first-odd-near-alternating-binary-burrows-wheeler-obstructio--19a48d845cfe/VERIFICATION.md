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

# Reproduction and limits

Run `python3 CHECK.py` with Python 3 and no third-party dependencies. The checked finite universe comprises each singleton equality-position set at odd lengths \(3\) through \(49\) and every three-element equality-position subset among the \(48\) gaps at length \(49\). Assertions verify the complete orbit-length exclusion for \(48\) runs at length \(49\), successful witnesses at every earlier odd length, exact count \(1128\) among all \(17296\) three-equality candidates, direct BWT reconstruction for every accepted candidate, and the explicit extremizer. The included `CHECKS.txt` is the recorded result of executing the bundled program. This computation is an exhaustive proof of the stated finite cases only when combined with the proven completeness of the gap parametrization and the standard single-cycle criterion. No assertions are made for larger lengths. Independent audit or external validation has not been performed.
