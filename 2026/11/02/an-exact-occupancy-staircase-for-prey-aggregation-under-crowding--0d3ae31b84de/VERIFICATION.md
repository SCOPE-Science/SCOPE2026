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

The analytic proof in `RESULT.md` supplies the global claim for all integers \(n\ge2\) and all positive continuous parameters. Its critical steps are strict convexity of the second derivative, the transfer-direction maximality contradiction, and the exact formula comparing successive equal-support allocations.

The included `checker.py` is standalone Python 3. On the final extracted package, `python3 checker.py` returned `PASS 4963 exact rational assertions`. It checks the adjacent-value algebra, all open intervals and exact tie boundaries for several rational test families, plus finite-grid allocation comparisons for small habitats. The exhaustive finite-grid checks are not exhaustive over the real simplex and do not constitute an infinite proof. No independent audit or field-data validation is claimed.
