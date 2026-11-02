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

# Verification evidence

Run `python verify.py` with Python 3 and the SymPy package installed. The checker builds the specified \(16\times16\) transfer matrix from the four row-coverage classes and compares its symbolic characteristic polynomial with the stated cubic-sextic factorization. It separately enumerates *every* subset of the \(3n\)-vertex graph and calculates closed-neighborhood domination directly for \(n=3,4,5,6\), comparing all coefficients. It then tests the signed transfer trace for \(1\le n\le64\). The actual execution returned:

`VERIFY_OK: symbolic degree-16 determinant, direct graph enumeration n=3..6, period n=1..64`

The finite tests are consistency checks. The infinite claim is established by the local coverage equivalence, exact characteristic polynomial identity, and trace/power-sum argument in `RESULT.md`. The signed transfer checks at \(n=1,2\) are not assertions about simple cycle graphs; the theorem assumes \(n\ge3\). No independent audit or external formal proof certificate is claimed.
