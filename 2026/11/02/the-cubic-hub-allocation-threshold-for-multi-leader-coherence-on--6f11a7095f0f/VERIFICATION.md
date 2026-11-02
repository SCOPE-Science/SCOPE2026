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

# Verification of the cubic hub-allocation threshold

The complete mathematical proof is in `RESULT.md`. Executing `python3 verify.py` (standard Python library only) independently constructs grounded graph Laplacians, takes exact rational inverses and compares their trace with the spectral formula and the stated optimizer classes. The captured output appears in `verification.log`.

This confirms 258 orbit representatives, all 1,474 admissible labeled leader sets for the bounded family with \(4\le q\le8\), and a further table of optimal classes through \(q=15\). The polynomial signs were checked for integer \(4\le k\le150\). The exact derivation, root uniqueness for all integers \(k\ge4\), and asymptotics are proved analytically, not inferred from finite checks.

The program does not check novelty or independent mathematical validity. Scientific limits and priority risks are stated in `RESULT.md` and `REVIEW.md`.
