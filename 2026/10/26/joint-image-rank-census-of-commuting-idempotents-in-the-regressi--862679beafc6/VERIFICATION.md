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

Run `python3 verification.py` with Python 3.10 or later. The program uses only the standard library. It constructs the exact polynomial recurrence and a separate exhaustive enumeration of all regressive idempotents, and compares coefficient dictionaries indexed by the three image ranks for every \(1\leq n\leq7\).

The independent enumeration checks the identities \(e^2=e\), \(f^2=f\), \(ef=fe\) by direct evaluation, not by assuming the fiber theorem. Its output lists the idempotent count, commuting pair count, number of rank-one products, and local polynomial total. Expected commuting totals are \(1,4,21,139,1114,10465,112513\).

The exact all-degree theorem is established by the bijection and weighted set-partition exponential formula in RESULT.md, not by this bounded calculation. A missing or failed check must not be interpreted as mathematical impossibility. No independent audit has been performed.
