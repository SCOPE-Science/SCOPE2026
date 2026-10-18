---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At the assigned 8f4f... Git tree, reconstruct the actual natural-order forward sweep on unit-diagonal SPD A=[[1,rho],[rho,1]] with 0<=rho<1, 0<omega<2 and Euclidean equation residual, not error or A-energy norm. Direct multiplication yields R=[[1-w+w^2 rho^2,-w rho],[-w rho(1-w),1-w]]. For s=sqrt(1-rho^2), G=I-R^T R has G22=w[2-w(2-s^2)] and det G=w^2[2s-w(1+s-s^2)][2s+w(1-s-s^2)]. The second bracket stays positive for 0<w<2 and the G22 condition follows when w<=2s/(1+s-s^2), giving iff residual safety by the 2x2 PSD criterion; beyond it determinant <0. The SOR error-matrix characteristic polynomial gives the asymptotic spectral-radius crossover w_opt=2/(1+s), hence w_opt<=w_safe iff rho^2<=1/2, equivalently kappa<=(3+2sqrt2). Independently recomputed the determinant as an exact SymPy polynomial and the rho=4/5, w=5/4 rational witness R e2=(-1,-1/4), squared amplification 17/16. Analytic proof, not the finite script, establishes all rho,omega quantifiers.

## originality

PASS

Best-of-knowledge original exact one-sweep residual norm ceiling and its intersection with the SOR optimum; classical SOR papers study spectral/asymptotic error convergence. Published closely related Gauss–Seidel and weighted-Jacobi finite-sweep results use different operators, norm or relaxation criterion. Exact formula was not found by targeted searches, which alone cannot prove priority.

## value

PASS

A sharp worst-direction residual-safety frontier for a canonical SPD iterative solver is independently useful: minimizing asymptotic spectral radius need not preserve one-sweep Euclidean equation residual. The exact condition-number crossover and explicit rational immediate spike distinguish finite-sweep stability from long-term convergence; this is more than renaming the classical spectral optimum or a log-based certification exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
