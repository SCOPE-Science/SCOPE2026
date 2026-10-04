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

The algebraic checks use the equations exactly as printed in the 2023 article.

For the four-dimensional model,
\[
\dot x=yz,\quad \dot y=x-y,\quad \dot z=1-x^2,\quad \dot u=ax+bu,
\]
the checker verifies the two equilibria and the factorization
\[
(\lambda-b)(\lambda+1)(\lambda^2+2).
\]
The proof-level Lyapunov step is structural: the \(u\)-fiber is invariant and has exponent \(b\), while the quotient is the three-dimensional base cocycle.

For the five-dimensional model,
\[
\dot x=cyz,\quad \dot y=x-y,\quad \dot z=1-x^2,
\]
\[
\dot u=ax-bu+k(m+3n\phi^2)z,\quad \dot\phi=y-x,
\]
the checker verifies exactly that \(\dot y+\dot\phi=0\), checks equilibrium residuals for several rational parameter choices and several values of \(\phi\), and verifies the factorization
\[
\lambda(\lambda+b)(\lambda+1)(\lambda^2+2c).
\]
The proof-level cocycle step uses the global coordinate \(h=y+\phi\), after which the tangent system is block lower triangular with diagonal blocks given by the three-dimensional base cocycle, the scalar zero cocycle, and the scalar coefficient \(-b\).

The source's displayed Lyapunov sums are also checked as arithmetic consistency tests. Their agreement with divergence is necessary but not sufficient: the exact triangular decomposition imposes additional asymptotic spectral constraints.

The replay does not numerically integrate trajectories, infer finite-time exponents, or assess the discrete FPGA implementation.
