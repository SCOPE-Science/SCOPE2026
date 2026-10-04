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

The verification is analytic.

The weak quasiregular hypothesis and
\[
|h'|^2+|g'|^2
=
\frac{\Lambda_f^2+\lambda_f^2}{2}
\]
give the exact differential estimate
\[
\Lambda_f^2
\le
\frac{2K^2}{K^2+1}
\left(
|h'|^2+|g'|^2
\right)
+
\frac{2K_0}{K^2+1}.
\]

For the regularized comparison functions
\[
V_\varepsilon
=
\left(
|f|^2+\frac{4K_0}{K^2+1}|z|^2+\varepsilon
\right)^{1/2}
\]
and
\[
U_\varepsilon
=
\left(
|h|^2+|g|^2+\frac{4K_0}{K^2+1}|z|^2+\varepsilon
\right)^{1/2},
\]
direct differentiation at the endpoint gives
\[
\Delta U_\varepsilon
\le
D_K\Delta V_\varepsilon.
\]
Green's mean identity and \(g(0)=0\) then yield the stated radial integral comparison.

The regularization makes all endpoint derivatives classical. Removal of \(\varepsilon\) uses Fatou's lemma on the left and dominated convergence on the right for each fixed radius.

The failure without quasiregularity is verified by the exact identity
\[
\operatorname{Re}\frac{1+z}{1-z}
=
\frac{1-|z|^2}{|1-z|^2},
\]
whose harmonic \(\mathbf h^1\) norm is one, while its canonical components
\[
\frac1{1-z}
\quad\text{and}\quad
\frac z{1-z}
\]
have logarithmically divergent \(H^1\) integral means.

No numerical experiment or finite truncation is used.
