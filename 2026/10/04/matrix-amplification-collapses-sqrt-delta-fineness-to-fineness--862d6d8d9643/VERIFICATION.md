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

The proof was reconstructed directly from definitions and the cited structural theorems.

For a nonzero unital simple ring \(R\), the only possibilities for the ideal \(J(R)\) are \(0\) and \(R\), and the latter is impossible because \(1\notin J(R)\). Thus \(J(R)=0\).

For every \(n\ge2\), Leroy--Matczuk's identity gives
\[
\Delta(M_n(R))=J(M_n(R))=M_n(J(R))=0.
\]
Consequently \(X\in\sqrt{\Delta(M_n(R))}\) exactly when \(X^m=0\) for some \(m\ge1\), i.e. exactly when \(X\) is nilpotent. Combining this with the 2026 matrix-closure theorem proves ordinary fineness.

For the corner step, \(e=E_{11}\) satisfies \(eM_2(R)e\cong R\), and \(E_{22}=E_{21}eE_{12}\), so \(1\in M_2(R)eM_2(R)\); hence \(e\) is full.

No finite computation or probabilistic test is used. No claim is made for \(n=1\), and no converse Morita statement is asserted.
