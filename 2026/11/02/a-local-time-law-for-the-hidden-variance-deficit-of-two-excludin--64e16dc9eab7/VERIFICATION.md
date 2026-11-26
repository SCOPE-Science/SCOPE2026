---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Off contact four rate-1/2 jumps contribute squared increments 1/4 (centre) and 1 (gap); at contact the two outward jumps remain. In both regimes the centre signs cancel for each available gap direction, so the centre drift and predictable cross bracket vanish. For A equal to time at gap 1, this yields gap drift A, gap martingale bracket 2s−A_s, and centre bracket s/2−A_s/4. The latter is predictable, not the realized sum of squared hops. Since R−1≥0 and continuous A increases only at the zero gap above the wall, it is exactly the Skorokhod regulator of R(0)−1+M^r. Doob's inequality gives E[(A_{n²T}/n)²]≤8T, which both controls bracket errors uniformly by A_{n²T}/n² and gives uniform integrability. Vanishing jumps, diagonal bracket convergence and the martingale FCLT give independent Brownian drivers. The regulator under joint J1 convergence to continuous paths is continuous in the uniform metric (the running negative supremum is 1-Lipschitz), so the same joint limit carries R_n and H_n, with factor 1/4. Reflection gives the stated tail for z≥0, including P(K_t=0)=2Φ(δ/√(2t))−1, and integration gives the coefficient in terms of φ and Φ. The martingale isometry and uniform integrability justify using this coefficient for the actual variance, without inferring moment convergence from weak convergence alone. The frozen checker and its recorded 11482 assertions were inspected, not executed; the functional limit rests on the analytic argument.

## originality

PASS

The random centre predictable-bracket correction at order 1/n, jointly with the centre and reflected gap, is the supported distinction. Neither the leading fixed-particle diffusion nor reflected-walk/local-time convergence alone is original here. The population, observable and limit of the closest collision and noise comparisons differ, and the combination requires the exact contact-to-bracket coefficient, joint martingale covariance calculation and uniform integrability for the mean.

## value

PASS

The leading diffusion loses the contribution of rejected jumps. The result identifies what survives at the next order as a non-Gaussian random contact regulator independent of the leading centre, and gives a measurable first correction to its variance, with the mass at zero explaining the effect of a positive starting gap. It is a precise two-particle benchmark, not a positive-density claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
