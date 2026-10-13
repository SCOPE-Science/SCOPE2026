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

The exact checker starts from the two matrices printed in the initiating source:
\[
A_{\mathrm{pr}}=
\begin{pmatrix}
1&3&11&18\\
0&1&6&11\\
0&0&1&3\\
0&0&0&1
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
1&3&7&6\\
0&1&6&7\\
0&0&1&3\\
0&0&0&1
\end{pmatrix}.
\]
It performs fraction-exact Gauss--Jordan inversion and forms
\[
T_*=-A^{-t}A,\qquad N=T_*-I.
\]
For each matrix it verifies \(N^4=0\). For the right-dual matrix it obtains
\[
e_i^tAN^ke_i=
(1,38,108,72),\,
(1,146,432,288),\,
(1,146,432,288),\,
(1,38,108,72)
\]
for \(i=1,2,3,4\) and \(k=0,1,2,3\). For the standard matrix all four rows equal \((1,38,108,72)\).

Because \(N^4=0\), the identity
\[
T_*^p=\sum_{k=0}^3\binom pkN^k
\]
is exact for every integer \(p\ge0\); the checker is therefore verifying a closed proof, not extrapolating from sample degrees.

The source's geometric-helix vanishing is the non-computational input that turns these Euler pairings into actual Hom dimensions. The checker also verifies the two rational Hilbert-series numerators and the factor-four ratio of leading coefficients.
