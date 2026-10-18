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

From Git RESULT.md blob 40046ba7, check the stationary anomalous covariance equation 0=-gamma B-iJ(sigma_x B+B sigma_x)+gamma diag(M1,M2): substitution B_11=mu q+d, B_22=mu q-d, B_12=-i chi q gives exact zero using mu=gamma^2/(gamma^2+4J^2), chi=2gamma J/(gamma^2+4J^2). Normal N is stationary by symmetry and damping. The quadrature covariance has local determinants u=a^2-h^2(mu^2 c^2+s^2), intermode det=-w^2 and detV=(u-w^2)^2, where w=h chi|c|. Since mu^2+chi^2=mu, u>=w^2; standard two-mode Gaussian PT invariant gives nu_tilde_minus=sqrt(u)-w. With K^2-S^2=1, 2nu=y[sqrt(1+(1-mu^2)z^2)-chi z]. R(z) strictly convex, derivative vanishes only at z*=sqrt(mu/(1-mu^2)) and R(z*)=1/sqrt(1+mu). Restrict z to [0,S] for optimal phase. The entangled phase interval roots follow exactly from quadratic R(z)<1/y; the arccos difference scales 1/S=Theta(exp(-2r)). Direct independent numerical parameter check with mu=.4, chi=sqrt(.24), y=1.2,S=2.5 and cos delta=.3 confirmed covariance determinant and PT eigenvalue within numerical precision. Limits J,gamma>0, r>=0 and y>=1 are respected.

## originality

PASS

Statement-level best-of-knowledge comparison found no stronger prior theorem implying the complete final claim; source-specific exclusions and reading limits documented.

## value

PASS

Sharp phase-dependent entanglement boundary turns a previously fixed-alignment high-squeezing ceiling into a tunable nonzero optimized plateau while rigorously quantifying the exponentially shrinking phase tolerance. Physically natural and not a tiny numerical improvement; defines an exact control-vs-resource frontier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
