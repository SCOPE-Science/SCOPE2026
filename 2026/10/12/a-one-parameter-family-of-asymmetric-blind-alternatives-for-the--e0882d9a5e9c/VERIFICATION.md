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

The proof was checked from the defining formulas rather than from simulation.

For \((r,n)=(1,3)\), exact expansion gives
\[
W_3(u)=\rho_{2\mid3:F}(u)^2-\rho_{2\mid3:G}(u)^2
=-12u^3+18u^2-4u-1
=\frac12(2u-1)\left(5-3(2u-1)^2\right).
\]
With
\[
h(u)=(2u-1)^3-\frac{15}{28}(2u-1),
\]
one has exactly
\[
\int_0^1 W_3(u)\,du=0,
\qquad
\int_0^1 W_3(u)h(u)\,du=0.
\]
The second identity follows from the exact moment ratio
\[
\frac{\int_{-1}^1 z(5-3z^2)z^3\,dz}{\int_{-1}^1 z(5-3z^2)z\,dz}
=\frac{8/7}{32/15}=\frac{15}{28}.
\]

Positivity is global, not sampled: the only interior stationary points of \(z^3-15z/28\) occur at \(z^2=5/28\), their absolute values are smaller than the endpoint value \(13/28\), and therefore \(|h|\le13/28\) on the whole interval.

For \((r,n)=(1,4)\), exact expansion and integration give
\[
\int_0^1\left(\rho_{3\mid4:F}(u)^2-\rho_{3\mid4:G}(u)^2\right)h(u)\,du=\frac{2}{35},
\]
so \(\mathcal X_{1,4}=\varepsilon/35\).

`verify.py` replays these polynomial and rational-arithmetic checks and must print `VERIFY_OK`.

The source scope was checked directly: its equations (11)--(14) define the system weights and extropies, equation (24) defines the population contrast, Theorem 5.1 establishes convergence of the estimator to that contrast, and Section 5 fixes \((r,n)=(1,3)\) for implementation. The result here does not infer anything from simulation tables.

Unproved limit: no asymptotic distribution or limiting rejection probability of the sample statistic is derived for the constructed alternatives.
