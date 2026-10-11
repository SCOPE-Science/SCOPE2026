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
The chord-mean identities are exact, not numerical estimates:
\[
F_{\ell_1^n}(x)=2-\min_i|x_i|,\qquad
F_{\ell_\infty^n}(z)=1+\frac{a_1+a_2}{2}.
\]
The first follows by reducing a convex maximization to signed coordinate vertices; the second reduces a convex maximization to cube corners and optimizes the range of \(\varepsilon_i z_i\). The sharp distance bounds are
\[
2\delta_1\le\operatorname{dist}_1(x,U_n)\le2(n-1)\delta_1,
\qquad
\operatorname{dist}_\infty(z,E_n)=2\delta_\infty.
\]
The proof explicitly constructs vectors giving equality in either bound at every \(0<\delta_1\le1/n\).

The standalone `verify.py` requires only the Python standard library. It performs all computations over exact rational numbers, checks the original pointwise norm optimization on all signed vertices for many rational unit vectors in dimensions \(2\) through \(6\), and replays the sharp equality families and the duality-gap arithmetic. This finite test is not substituted for the analytic proof.

No independent audit or independent validation has been performed.
