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
The analytic verification starts from the published eigenvalues of the interpolation matrix and the published scalar scattering map. For \(j\ge1\), exact half-angle algebra gives
\[
\mu_j(k,t)=\frac{k-i\cot(\beta_jt/2)}{k+i\cot(\beta_jt/2)},
\]
so the only scaling retained in the singular corner is \(kt\). The exceptional even-degree mode \(\beta_{n/2}=0\) equals \(-1\) exactly for all \(k,t\).

The limiting Fourier eigenvalues all have modulus one, so the limiting matrix is unitary. Pairing \(\beta_{n-j}=-\beta_j\) makes the common diagonal amplitude real. Each paired contribution has derivative
\[
\frac{16\beta_j^2\xi}{(\beta_j^2\xi^2+4)^2}>0
\]
for \(\xi>0\), while the endpoint values have opposite signs. This proves one and only one reflectionless crossover scale.

`verify.py` checks the exact finite source formula against the half-angle formula, checks convergence for representative \(n\), \(\alpha\), and \(\xi\), verifies the paired formulas for the diagonal amplitude, and checks \(\xi_3=2\sqrt3/\pi\) and \(\xi_4=4/\pi\). Finite numerical checks do not establish the quantified limit or uniqueness; those are proved analytically above and in `RESULT.md`.
