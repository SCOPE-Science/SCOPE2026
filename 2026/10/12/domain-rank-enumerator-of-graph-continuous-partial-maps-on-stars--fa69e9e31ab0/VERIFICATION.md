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
# Verification of the star domain-rank enumerator

The theorem is proved symbolically for all \(n\ge1\) in `RESULT.md`. Reproduce the finite independent check by executing `python3 verify.py` using a standard Python 3 installation. The script first forms the proposed polynomial from binomial-coefficient sums and separately exhausts all partial maps for each \(n\in\{1,2,3,4,5\}\); each target singleton and each target center-leaf edge must pull back to an empty set, singleton, or source edge. The resulting complete domain-rank coefficient vectors agree.

Expected output is `EXHAUSTIVE_STAR_CASES=5 VERIFY_OK` after per-case totals \(9,36,185,1278,10857\). This proves only the five finite checks. The infinite theorem needs the six-case proof; the script is not an independent review or independent audit. The exact source of the object's definition is Margolis–Rhodes, arXiv:2005.02606, Section 2; full access to the 2026 follow-up's body was unavailable, so independent prior-art exclusion has not been established.
