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

Run `python3 verify.py` in the same directory. Its unbounded-coin dynamic program caps the coefficient of each generated series at two, so it independently finds the first integer of each residue having at least two representations without using the residue-cost proof. It compares all first-repeat thresholds for \(2\le a\le400\), accounting for 80,199 residue classes. A separate check evaluates the exact threshold formula and compares its Frobenius/genus consequences with the twelve small-base pairs and all four quasipolynomial branches for \(2\le a\le1100\). Two `PASS:` lines are expected. No external package or internet connection is needed. The finite tests do not prove the uniform assertions; the accompanying direct proof does.
