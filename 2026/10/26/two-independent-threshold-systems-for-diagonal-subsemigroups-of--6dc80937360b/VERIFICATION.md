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

# Verification record

Executed the standalone standard-library `verify.py`, extracted from the new finding package. For n=1,2,3,4 it enumerates **all** reflexive binary relations, checks coordinatewise minimum closure, counts symmetric/equivalence relations, and compares their full rank profiles with the theorem. Exact diagonal counts were 1, 4, 36, 576; symmetric counts 1, 2, 6, 24; congruences 1, 2, 4, 8. It checks that reconstruction from every threshold tuple agrees with the complete exhaustive set. For n=5 it constructs all 14,400 threshold pairs, checks each is closed and all are distinct, and validates the generating-polynomial total. The checker ended with `VERIFY_OK`.

These computations cannot exclude exotic relations for n>5; the independently written mathematical necessity/sufficiency proof establishes that no such exceptions exist. Originality comparisons used the actual motivating full text, older 1983 primary paper, and actual semantic/database queries. Older unpublished/unindexed equivalents remain a residual risk. Independent audit has not been performed.
