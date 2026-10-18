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

The supplied `verify.py` uses Python 3 and SymPy 1.14.0 (the integer Smith-normal-form routine) and requires no network connection. Execute `python verify.py` from a directory containing the file. It constructs a symmetric integer matrix from the seven shift terms, computes its exact Smith normal form, and compares free rank and non-unit invariant factors with the formulas in RESULT.md. It was executed successfully on 154 valid pairs: all coprime \((n,a)\) with \(3\le n\le22\), and six additional cases through \(n=36\).

The proof for all \(n\) uses the integral cyclic-difference image identity, the exact module sequence, elementary two-group extensions, and a primitive-kernel covolume calculation. The finite tests do not establish the infinite theorem by themselves. No independent audit, external mathematical validation, or computer-assisted formal proof is claimed.
