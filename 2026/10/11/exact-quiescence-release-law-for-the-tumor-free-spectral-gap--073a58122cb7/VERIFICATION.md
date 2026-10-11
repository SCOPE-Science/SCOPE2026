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

The source characteristic polynomial was rewritten algebraically into three copies of
\[
\lambda^2+(g+\beta_1+m)\lambda+gm=0.
\]
The source stability inequalities imply \(m>0\) for all three blocks. The discriminant identity
\[
(g+\beta_1+m)^2-4gm=(g+\beta_1-m)^2+4\beta_1m
\]
proves the roots are real and negative. Direct differentiation of the slow root gives the strict first- and second-derivative signs used in the finding. The slowest tumor block follows from strict monotonicity in \(m\), and the full spectral gap includes the three scalar eigenvalues through the minimum with \(\kappa\).

The crossover equation was solved symbolically by imposing \(\rho(g,m_*)=\kappa\). Its finite positive solution exists exactly for \(0<\kappa<m_*\). Limiting formulas were checked by direct series expansion of the exact root.

Only local linear behavior is verified. No finite simulation, virtual-patient output, or empirical trajectory is used to establish the theorem.
