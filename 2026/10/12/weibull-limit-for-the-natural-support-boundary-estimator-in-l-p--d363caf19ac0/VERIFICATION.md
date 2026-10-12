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

The analytic proof reduces the estimator to an endpoint maximum.

For one observation write \(X=RU\), \(W_i=U_i^p\), and
\[
Y=R^p\sim\operatorname{Beta}\!\left(\frac dp,b\right),
\qquad
b=1-\frac{d-1}{p}.
\]
The angular vector satisfies
\[
W\sim\operatorname{Dirichlet}\!\left(\frac1p,\ldots,\frac1p\right).
\]
For a parameter decrement \(t\), the conditional radial threshold is
\[
r_t^p
=
\left(\sum_iW_i^{1-t/p}\right)^{-p/(p-t)}.
\]
Thus, with \(z_t=1-r_t^p\),
\[
\frac{z_t}{t}
\to
\frac{-\sum_iW_i\log W_i}{p}.
\]
The bound
\[
0\le\frac{z_t}{t}\le\frac{\log d}{p-t}
\]
follows from \(\sum_iW_i^{1-t/p}\le d^{t/p}\) and \(1-e^{-x}\le x\).

The beta endpoint expansion is
\[
\Pr\{Y>1-z\}
\sim
\frac{z^b}{bB(d/p,b)}.
\]
Dominated convergence therefore gives the one-observation coefficient
\[
\kappa_{d,p}
=
\frac{\mathbb E[(H(W)/p)^b]}
{bB(d/p,b)}.
\]
The iid maximum then gives the stated Weibull survival function.

The standalone script `verify.py` checks the \(d=2,p=2\) constant by deterministic quadrature and confirms that the exact one-observation tail ratio approaches that constant. It also checks the directional derivative at several fixed probability vectors. Finite computations are not used to establish the theorem.

Expected successful output begins with:
`VERIFY_OK kappa_2_2=0.4061168441`.
