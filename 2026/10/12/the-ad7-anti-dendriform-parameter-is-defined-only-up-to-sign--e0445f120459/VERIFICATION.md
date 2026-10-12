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
The proof is exact symbolic linear algebra.

The packaged checker `artifacts/verify.py` constructs
\[
B_\lambda=\begin{pmatrix}1&\lambda\\0&1\end{pmatrix}
\]
and verifies
\[
B_\lambda^{-1}B_\lambda^{\mathsf T}
=
\begin{pmatrix}1-\lambda^2&-\lambda\\\lambda&1\end{pmatrix},
\qquad
\operatorname{tr}=2-\lambda^2.
\]
It verifies the explicit sign congruence
\[
D^{\mathsf T}B_{-\lambda}D=B_\lambda,
\qquad D=\operatorname{diag}(1,-1).
\]
It also checks rank separation from the rank-one models and the non-scalar asymmetry at \(\lambda=\pm2\), excluding the alternating model.

The checker returns `VERIFY_OK`.
