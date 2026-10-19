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

# Reproducibility checks

Run `python3 verify.py` with Python 3. The program computes substitution and valuation constructions through a length-32768 prefix, confirms their identity, constructs all signature classes of factors of lengths three times a power of two through the ninth scale, and independently constructs the classes from the substitution factor recurrence. It verifies the number of zero-count tiers, two outer cardinalities, middle arithmetic progression, and total class count. The actual successful run reported `VERIFY_OK substitution_depth=15 direct_scales=9 recurrence_scales=9`.

The exhaustive computation is over a specified finite prefix only, not all infinite factors. The separately written mathematical induction gives exhaustive coverage for every depth. This self-review does not constitute independent review or machine-checked proof.
