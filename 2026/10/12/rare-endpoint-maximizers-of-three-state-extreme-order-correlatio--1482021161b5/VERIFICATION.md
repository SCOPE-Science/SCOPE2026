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

The exact formula in `RESULT.md` uses the translated minimum \(M_n\in\{0,1,2\}\), which decomposes as
\[
M_n=\mathbf1\{\min_i(X_i+1)\ge1\}
+\mathbf1\{\min_i(X_i+1)=2\}.
\]
This gives \(\operatorname{Var}(M_n)\ge\ell(1-\ell)\) because the events are nested, and the direct covariance identity is
\[
\operatorname{Cov}(M_n,V_n)=(\ell+e)^2-b.
\]
The global bound in the proof prevents maximizers from escaping the rare-mass window:
\[
0<n\rho_n(t)
\le\frac{4(nt)^2}{e^{nt}-1}
+\frac{3nt^n}{1-e^{-nt}}.
\]
It is this analytic estimate, together with the compact-uniform limiting profile and the uniqueness of its maximizer, that proves the infinite theorem.

The bundled pure-Python `verify.py` makes independent exact-rational checks of the finite formulas by enumerating the entire finite outcome space for selected small samples, including the binary-endpoint case. It confirms
\[
\rho_2(1/3)=8/19,
\qquad\rho_3(3/10)=81/319.
\]
The program additionally uses bisection for the root of \((2-c)e^c=2\) and numerical gridding to illustrate convergence of scaled finite-sample optima. This is a finite numerical illustration only; no finite grid is claimed to exhaust continuum parameters or prove an infinite limit.

Expected success starts with `VERIFY_OK exact_enumeration_cases=`.
