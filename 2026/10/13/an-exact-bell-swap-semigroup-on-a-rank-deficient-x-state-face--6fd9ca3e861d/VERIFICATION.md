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

The all-length theorem is verified analytically by a direct two-link Bell contraction followed by induction. The contraction preserves the displayed zero-population X-state face and updates the diagonal data by multiplication of the upper-triangular matrices \(T_k\), while multiplying the corner coherences.

For the normalized endpoint state, the standard X-state concurrence expression reduces to \(2|W_L|/Z_L\). Independently, the partial transpose contains the block
\[
Z_L^{-1}\begin{pmatrix}0&W_L\\\overline{W_L}&C_L\end{pmatrix},
\]
whose smaller eigenvalue is strictly negative exactly when \(W_L\ne0\). These are symbolic checks valid for every finite \(L\) under the stated hypotheses.

`artifacts/verify.py` uses only the Python standard library. It performs direct computational-basis Bell contractions for heterogeneous chains of lengths one, two, and three and compares them with the closed formula. It also checks the exact specialization to the rank-three family of arXiv:2609.11021v1. Replaying the file returns `VERIFY_OK`.

The finite replay does not certify the universal quantifier by enumeration; that quantifier is established by the induction in RESULT.md. The verification does not address other Bell outcomes, adaptive protocols, or a classification of all rank-deficient links.
