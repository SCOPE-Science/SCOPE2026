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

# Reproducible checks

Run `python verify_heisenberg.py` with an ordinary Python interpreter (no external packages). The script checks all quotient matrices and central-coordinate functionals for \((m,q)=(1,2),(1,3),(1,5),(2,2)\), evaluates the Lie endomorphism equations directly and compares the rank distribution to the closed formulas. The \(m=1\) tests are boundary consistency checks; the new classified family is \(m\ge2\). It also checks the optimizing rank formula for \(1\le m\le30\). Expected output ends with `CHECK_OK rank-degree phase transitions m=1..30`.

The theorem for arbitrary \(m\) and arbitrary finite field \(\mathbb F_q\), including fields of characteristic two and prime-power extension fields, is proved by linear-algebraic arguments in RESULT.md. Prime-field finite enumeration cannot independently establish the infinite family and is not offered as such. Field-extension arithmetic is not exercised by the standalone script. No independent mathematical audit is claimed or supplied.
