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

Run `python artifacts/verify.py` with SymPy installed. The program derives all coordinate defects from the original Rota–Baxter identity and checks the nine displayed polynomial formulas. It checks the tangent Jacobians of the unreduced and reduced schemes at a nonzero-weight base operator, verifies the dual-number direction and the exact obstruction polynomial, and independently exhausts all field-valued operators over \(\mathbf F_2\) and \(\mathbf F_3\) at zero and nonzero weight.

The full ambient counts are
\[
\#\mathscr R_0(\mathbf F_2)=64,\qquad
\#\mathscr R_1(\mathbf F_2)=80,
\]
\[
\#\mathscr R_0(\mathbf F_3)=729,\qquad
\#\mathscr R_1(\mathbf F_3)=810.
\]
It also checks all reduced matrix fibers for weights zero, one and two over \(\mathbf F_3,\mathbf F_5,\mathbf F_7,\mathbf F_{11}\), always matching \(q^6\) or \(q^6+q^4\).

The checker prints `VERIFY_OK`. These finite tests do not establish the arbitrary-field results: the symbolic defect equations, geometric irreducibility argument, smoothness Jacobian proof, and Grothendieck stratification do.
