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

# Reproducibility

Run `python verify.py` using Python 3's standard library; a successful replay prints `VERIFY_OK`. It directly assembles the \((n^2+n)\times(n^2+n)\) adjoint matrices and tests (1) against rank computations, exhaustively for \((n,q)=(2,2),(2,3),(3,2)\) and on deterministic samples for \((3,3),(3,4)\). The characteristic-two extension-field arithmetic in the last test uses the polynomial relation \(\alpha^2+\alpha+1=0\).

Run `python derive_n3.py` with SymPy installed; it enumerates seventeen rational-canonical strata symbolically, tests the complete dimension-three polynomial spectrum, the coefficient sum \(q^{12}\), and the commuting-pair count. Successful replay prints `SYMBOLIC_VERIFY_OK`. Each test uses only the embedded programs. These checks cannot replace the all-field proof and are not independent external audits.
