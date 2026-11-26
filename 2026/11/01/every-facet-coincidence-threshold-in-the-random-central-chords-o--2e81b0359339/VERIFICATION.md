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

The chord law is for the central line with Haar direction; T=1/max_i|U_i|. Normalized independent Gaussians give squared coordinates with Dirichlet parameters 1/2, and inclusion–exclusion of exceedances gives the exact CDF. For k<d the translation by a=t^(−2) and scaling by δ=1−ka gives Jacobian and remaining-mass power δ^(k+(d−k)/2−1); the fixed-simplex beta integral gives Γ((d−k)/2)/Γ((d+k)/2). Together with k^(k/2) from the limiting coordinate densities and δ∼2ε/√k, this yields precisely B_(d,k). At k=d the direct (d−1)-simplex volume gives the same formula. Earlier overlap terms and the extracted local factor are analytic across the active threshold (fixed domain, uniformly positive coordinate arguments, with an integrable fixed beta weight). Thus the nonzero right-onset term determines the claimed integer differentiability, and no other term at the threshold cancels it. The left upper-end tail is a separate complement-event simplex, of mass coordinate sum da−1, with the same limiting density and coefficient. There are no boundary atoms. The d=3 closed form checks by conditioning on one coordinate and integrating by parts. The code and VERIFICATION.md report finite simulations and quadratures, not an all-dimensional proof; these were inspected, not rerun.

## originality

PASS

The supported distinct claim is the exact fixed-dimensional knot hierarchy and upper-end asymptotic for the central chord law. The maximum-coordinate alias, Gaussian normalization, individual beta tails, and basic inclusion–exclusion are standard. The inspected same-distribution maximum paper concerns growing dimension, and the closest catalogue source covers one- and two-coordinate tails as ingredients of a count covariance, not all overlap coefficients or the CDF singularities. The unavailable random-intercept papers remain explicit risks to historical priority, not negative evidence.

## value

PASS

There is a natural geometric question at every radius where another coordinate can reach the boundary, also visible in an exact Dirichlet maximum law. The hierarchy identifies where the CDF is nonanalytic, how much differentiability survives, the signed nonzero amplitude, and where the upper tail terminates. This is more informative than the standard representation or support bounds, and is useful independently of finding elementary CDF formulas in every dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
