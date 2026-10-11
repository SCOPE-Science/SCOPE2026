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
The proof was replayed symbolically from the finalized package. The checker verifies the algebraic reduction from the covariance and logarithmic-balance identities to
\[
\frac{m-(n+1)\bar X}{n}(1+\varepsilon\bar X)
=
\frac{n+1}{k}+\varepsilon(V_X+nV_Y),
\]
and confirms that the endemic-equilibrium quadratic has leading coefficient \(-\varepsilon(n+1)/n\), giving the exact factorization
\[
V_X+nV_Y=\frac{n+1}{n}(x_+-\bar X)(\bar X-x_-).
\]

For the printed Figure 5(c) values \(m=2\), \(n=1/3\), \(\varepsilon=5/4\), and \(k=41/200\), the checker reduces the root equation to
\[
1230x^2-861x+124=0
\]
and verifies
\[
x_-=\frac7{20}-\frac{\sqrt{131241}}{2460},
\qquad
x_+=\frac7{20}+\frac{\sqrt{131241}}{2460}.
\]

The checker uses exact symbolic arithmetic. Numerical trajectory integration was used only as a supplementary stress test and is not needed for correctness. The theorem does not cover invariant measures charging \(X=0\), because the \(\log X\) generator is then unavailable.
