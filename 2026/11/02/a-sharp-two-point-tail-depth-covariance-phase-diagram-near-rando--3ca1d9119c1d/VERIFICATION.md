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

# Verification of the finite depth-covariance phase diagram

Run `python3 verify.py`. The script uses standard-library integer polynomial coefficient accumulation over every parent-type vector for 2 through 5 noncyclic vertices, and independent enumeration of complete mappings for total sizes 3 through 6. Its assertions verify the four symbolic moment tables, exact covariance formulas, conditional normalization, direct mapping counts, and all sign thresholds in the stated domain. Exact polynomial coefficient checks prove the identities for arbitrary positive integer root count; direct low-order checks are additional witnesses, not a substitute for the polynomial proof. The asserted domain excludes six or more noncyclic vertices. No independent validation has been performed.
