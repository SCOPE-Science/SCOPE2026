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

The proof uses the published exact ODE
\[
-r_n''=r_n^{n-1}(r_n-tr_n')^{n+2}
\]
and endpoint values
\[
r_n'(-1+)=k_n^{-1/n},
\qquad
r_n(1)=k_n^{1/n},
\qquad
r_n'(1-)=-\infty.
\]

At the lower endpoint, putting \(s=t+1\) gives
\[
r_n''=-k_n^{-(2n+1)/n}s^{n-1}+o(s^{n-1}),
\]
so two integrations determine the first nonlinear term. At the upper endpoint, with \(q=-r_n'\), division of the ODE by \(q^{n+2}\) gives
\[
\frac{q'}{q^{n+2}}\longrightarrow k_n^{(n-1)/n},
\]
which determines the blow-up exponent and coefficient of \(q\), then of \(r_n-r_n(1)\).

Both are substituted into the exact projective sublevel-radius identity
\[
R_n(z)=\frac{1+z}{\sqrt2}r_n\!\left(\frac{z-1}{z+1}\right).
\]
The resulting asymptotic series are inverted by the elementary rule that if \(R(z)=Az+Bz^p+o(z^p)\) with \(0<p<1\), then \(R^{-1}(\rho)=\rho/A-(B/A^{p+1})\rho^p+o(\rho^p)\), with the analogous power-series inversion at zero.

The packaged checker verifies all coefficient identities for \(2\le n\le40\). This finite calculation is not the proof of the asymptotic theorem.

Limits not proved: no closed formula for \(a_n\), no quantitative blow-up asymptotic for the Legendre dual near \(\lVert y\rVert_2=c_{\infty,n}\), and no stability result for near-extremizers.
