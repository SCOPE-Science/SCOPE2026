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

The analytic check starts from the exact maximal-coherence formula
\[
s_n(t)=\inf_{z>0}\frac{\sqrt{n!}[1-t+t(-1)^nL_n(z)]}{2z^{n/2}}.
\]
With \(\varepsilon=t^{1/n}\), \(A=(n!)^{1/n}\), and \(z=A u/\varepsilon\), the exact polynomial coefficients give
\[
\frac{s_n(t)}{\sqrt t}=\min_{u>0}\left[\frac12(u^{-n/2}+u^{n/2})-\frac{n^2}{2A}\varepsilon u^{n/2-1}+\frac{n^2(n-1)^2}{4A^2}\varepsilon^2u^{n/2-2}+O(\varepsilon^3)\right].
\]
The leading function has its unique global minimum at \(u=1\), with second derivative \(n^2/4\). Expanding the stationary point gives \(u=1+(n-2)\varepsilon/A+O(\varepsilon^2)\), and substitution gives the claimed coherence coefficients.

`artifacts/verify.py` reconstructs the relevant Laguerre coefficients from the defining finite sum and numerically minimizes the exact objective for representative fixed \(n\). These checks test algebra and normalization only; they do not replace the analytic localization and asymptotic proof.

No uniform-in-\(n\) remainder, global entropy optimum, or classification of all Wigner-positive boundary points is verified or claimed.
