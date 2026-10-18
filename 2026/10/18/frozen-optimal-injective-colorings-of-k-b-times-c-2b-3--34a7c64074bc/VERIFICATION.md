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

# Reproducibility and proof scope

Execute `python3 verify.py` using a standard Python 3 installation. A successful replay ends with `ALL_CHECKS_PASSED`. The script independently enumerates the deficient \(b\)-sets for \(b=3,4,5,6,7,8\), builds all asserted independent color supports and palette constraints, tests every candidate new color at every fiber, and compares the complete canonical recoloring-degree histogram. For \(b=3,4\) it also checks the literal direct-product common-neighbor graph and independently counts all ordered palette colorings with a transfer-style closed-walk dynamic program.

Expected canonical histogram for \(b=3\): \(\{0:3,3:18,6:9\}\); for \(b=4\): \(\{0:11,4:33,8:11\}\). The separate transfer counts of palette assignments are \(151200\) and \(19958400\), respectively. Full vertex colorings multiply those by \((b!)^{2b+3}\).

The program verifies only finitely many parameters and does not supply an exhaustive computation for arbitrary \(b\). The infinite theorem follows from the mathematical proof in RESULT.md. There is no independent scientific validation or external formal proof certification.
