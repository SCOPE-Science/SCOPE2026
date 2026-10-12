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

For \(0<\varepsilon<2\), define independent Poisson variables with intensities \(\varepsilon\) and \(1-\varepsilon/2\), and let \(X_\varepsilon=N_\varepsilon+2M_\varepsilon\). The exact checks are
\[
\mathbb EX_\varepsilon=2,
\qquad
\operatorname{Var}(X_\varepsilon)=4-\varepsilon,
\]
so
\[
1<\sqrt{4-\varepsilon}<2.
\]
Hence the closed one-standard-deviation event is exactly \(X_\varepsilon\in\{1,2,3\}\). Direct enumeration gives
\[
\Pr\{X_\varepsilon\in\{1,2,3\}\}
=e^{-1-\varepsilon/2}\left(1+\frac{3\varepsilon}{2}+\frac{\varepsilon^3}{6}\right).
\]
The right-hand side converges to \(e^{-1}\) as \(\varepsilon\downarrow0\), proving \(P_{\mathcal I}\le e^{-1}\).

The standalone script `verify.py` checks these identities by direct summation for several deterministic values of \(\varepsilon\) and checks the limiting numerical behavior. Successful output ends with:
`VERIFY_OK target=0.367879441171442 formula_error<1e-14`.

The script is a regression check only. The proof of the infinite family and the limiting upper bound is analytic.
