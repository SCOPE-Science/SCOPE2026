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

The symbolic proof establishes the universal statement. The accompanying `verify.py` is an exact-integer replay of its finite algebraic checks; it does not certify infinitely many levels by enumeration. It checks levels through \(N=6\) for all positive \(c<80\) with \(c\equiv2\pmod4\), including both squarefree and nonsquarefree cases.

The monogeneity classification depends on Theorem 1.8 of arXiv:2610.02111v1. The irreducibility part does not: it follows directly from Eisenstein after the parity-dependent translation. No claim is made for \(c\not\equiv2\pmod4\).
