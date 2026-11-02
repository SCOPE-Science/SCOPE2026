---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Restricted invariant coordinate axis of quadratic f=μ||x||²/2 yields exact nonlinear y_next=βy+x, x_next=x−I ημ y_next/max{μ|y_next|,sqrt(m)} with Bernoulli I of parameter q=ℓ/n. At equilibrium, floor-active derivative matrices A0=[[1,0],[1,β]], A1=[[1−s,−sβ],[1,β]], s=ημ/sqrt(m). Independent symbolic matrix expansion reproduced all 9 entries of the 3x3 covariance operator M(s) and polynomial identity det(I−M)=qs[2(1−β²)−(1+β−2βq)s]. Perron theorem for positive-semidefinite cone ensures covariance spectral radius is a nonnegative real eigenvalue, so any spectral radius 1 requires eigenvalue +1 (no hidden -1/complex crossing). Root at s=0 is simple with derivative -2q/(1−β)<0; other eigenvalues β,β² lie inside disk. Unique positive determinant zero s*=2(1−β²)/(1+β−2βq); high-s trace growth and no additional unit crossings show stable iff 0<s<s*. q=1 gives deterministic bound 2(1+β), q<1 is strictly lower. This is local mean-square derivative stability, NOT nonlinear global divergence; at equality rho=1. Source verifier is exact-rational polynomial evaluation, independent symbolic algebra agrees.

## originality

PASS

Qualified PASS: 2023 Simba method provides the preconditioning/coarse random restriction and convergence estimates; generic switching-system covariance spectral-radius methods are classical. The exact Bernoulli coordinate sampling plus momentum frontier is a new parameter-specific statement not supplied by the accessible primary algorithm summary or related but algebraically different published optimizer results. Complete primary paper not retrievable during this run; specialized optimizer priority remains open.

## value

PASS

Sharp, explicit stability boundary and its high-momentum collapse quantify a concrete stochastic tax in a natural reduced model of an actual optimization method; dependence on q and β is not a routine restatement of deterministic momentum stability. The exact single-axis threshold informs interpretation of stochastic coarse restriction without overstating the nonlinear algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
