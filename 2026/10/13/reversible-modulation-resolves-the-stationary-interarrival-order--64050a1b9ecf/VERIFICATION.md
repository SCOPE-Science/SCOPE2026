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

The proof is driven by the identities
\[
A=-Q+D,
\qquad
\langle f,Af\rangle_\pi
=
\frac12\sum_{i,j}\pi_iq_{ij}(f_i-f_j)^2
+
\sum_i\pi_i\lambda_i f_i^2,
\]
and
\[
S_\alpha(t)
=
-\frac{S_\pi'(t)}{\lambda_*}.
\]
For a reversible modulator, the first identity makes \(A\) positive self-adjoint in \(L^2(\pi)\). Its spectral decomposition gives
\[
S_\pi(t)
=
\sum_jw_je^{-r_jt}
\]
with positive weights, and therefore
\[
h_\pi'(t)=-\operatorname{Var}_t(r)\le0.
\]

The bundled `verify.py` checks a nonsymmetric reversible three-state generator,
\[
Q=
\begin{pmatrix}
-1&1&0\\
2&-5&3\\
0&4&-4
\end{pmatrix},
\qquad
\pi=
\left(\frac8{15},\frac4{15},\frac3{15}\right),
\]
with event rates
\[
(1,4,2).
\]
It verifies detailed balance, weighted symmetry, positive spectral rates and weights, the Palm derivative identity, decreasing hazard, and strict survival ordering at several deterministic times.

It also verifies the equal-rate case, where \(\alpha=\pi\) and the two interarrival survivals coincide.

Expected successful output begins with:
`VERIFY_OK lambda_star=2.000000000000`.

The numerical checks are finite-dimensional replay checks. The theorem for all finite irreducible reversible MMPPs is proved analytically in `RESULT.md`.
