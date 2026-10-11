---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For one Rademacher probe, \(D_i=z_i(Hz)_i=H_{ii}+\sum_{j\ne i}H_{ij}z_iz_j\); orthogonality of distinct Rademacher monomials gives mean \(H_{ii}\) and variance \(\sum_{j\ne i}H_{ij}^2\). Independent probe averaging divides only the variance by \(m\). The bias-corrected RMS-square is a convex combination of identically distributed squared estimates whose weights sum to one, giving the exact time-independent expectation. In two dimensions, writing one coordinate's squared projection onto the small-eigenvalue eigenspace as \(p\) reduces the squared inflation to a one-variable rational function with unique maximum at \(p=\kappa/(\kappa+1)\), giving the claimed sharp factor and its \(m\)-probe version. Fresh exhaustive Rademacher enumeration for several random symmetric matrices and independent evaluation of the condition-number maximizer reproduced the formulas.

## originality

PASS

AdaHessian defines Hutchinson diagonal estimation, spatial averaging, and the bias-corrected RMS Hessian momentum but does not state the resulting mean-square target on a fixed Hessian. Diagonal-estimation papers establish that off-diagonal energy controls Hutchinson error, but do not propagate it through AdaHessian's RMS state or give the optimizer-specific sharp two-dimensional condition-number inflation. The underlying moment identity is standard; originality is restricted to the exact optimizer-state consequence and sharp conditioning law.

## value

PASS

AdaHessian explicitly uses RMS smoothing and spatial averaging to manage stochastic Hessian-diagonal noise. The theorem identifies a persistent, exact consequence of that design: off-diagonal curvature becomes the RMS mean-square target, quantifies its worst conditioning distortion, and shows precisely how multiple probes suppress it. That is a motivated optimizer-structure invariant rather than a bare estimator variance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
