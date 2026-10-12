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

Tufo's Theorem 3.1 identifies the fourfold as the blow-up of \(\mathbf P^2\times\mathbf P^2\) along a general Enriques surface, and Corollary 3.2 records a free middle rank of \(13\) together with one \(2\)-torsion summand. The source passage was inspected in full.

For the blow-up, the exceptional degree-four classes are \(j_*p^*H^2(S,\mathbf Z)\). The Gysin identity \(j^*j_*(1)=c_1(N_{E/Y})=-\xi\) gives the negative Enriques pairing on this summand, and degree reasons make it orthogonal to \(\pi^*H^4(\mathbf P^2\times\mathbf P^2,\mathbf Z)\).

The ambient Gram matrix in the basis \((h_1^2,h_2^2,h_1h_2)\) is
\[
\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}=U\oplus\langle1\rangle.
\]
Dolgachev's Enriques-lattice calculation gives \(H^2(S,\mathbf Z)/\operatorname{tors}\cong U\oplus E_8(-1)\). Therefore the free middle matrix is isometric to \(U^{\oplus2}\oplus E_8\oplus\langle1\rangle\).

`verify.py` reconstructs that exact integer Gram matrix and checks rank \(13\), determinant \(1\), odd parity, and inertia \((11,2)\). Its stored output ends in `VERIFY_OK`.

The finite replay does not prove the blow-up formula or the classification theorem; those are used explicitly in the written proof. No claim is made about the torsion linking form or the full cohomology ring.
