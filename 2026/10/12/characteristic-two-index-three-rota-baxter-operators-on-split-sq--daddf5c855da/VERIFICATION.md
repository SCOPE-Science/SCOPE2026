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

# Verification

Run `python3 verify.py`. The executable enumerates every linear map in the proven normal form for \((n,q)=(1,2),(2,2),(3,2)\), tests the defining bilinear identity on basis pairs, computes the rank stratification and formula for the total and index-three loci, and reports `VERIFY_OK` when all conditions hold. Observed counts are \((2,0)\), \((16,6)\), and \((176,84)\). The proof covers all \(q=2^e\) and \(n\ge1\); finite experiments are corroborative, not a general proof. No independent audit has been performed.
