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

# Verification and limitations

Run `python3 checker.py` using a standard Python 3 interpreter. The independently written exhaustive finite checker verifies: unique reconstruction for all partitions on discrete sets of sizes one through six; failure of every nonadaptive query collection of size below \(n-1\) on discrete sets of sizes at most five; and direct confluence plus unique recovery on several nondiscrete partial orders. It prints `ALL_CHECKS_OK` and requires no external packages, source files, network calls, or previously generated logs.

The proof in `RESULT.md`, not the finite checker, establishes the claim for all finite orders and all admissible relations. It uses real linear algebra only to produce two finite indistinguishable partitions; the kernel vector itself is not an external certificate. The scope excludes adaptive measurements, unlabelled or partial outputs, unrestricted compound formulas and multiple-agent joint observations. The scientific review is not an independent audit.
