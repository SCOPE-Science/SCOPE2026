---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For eigenvalues t_i, F=2D_KL/k=mh−1−log h−mean log t with m=mean t, h=mean 1/t. At fixed others S,R, strict coordinate convexity follows F_tt=2S/(k²t³)+R²/(Rt+1)²−(k−1)/(kt²)>0 using SR≥(k−1)² and AM–GM 2a²/y+y²≥3a^{4/3}>2a²+a. Thus maximizers on compact [1,κ]^k have only {1,κ} eigenvalues, and nonconstant spectra give positive KL. Substitution yields explicit Hκ(j/k); derivative has one root by convexity and endpoint signs. Uniform fixed-k asymptotics follow expansions. Independent rational curvature and 280 random bound/attainment tests agree, but proof is analytic.

## originality

PASS

The cited Fifen–Karambal–Hennig trace-matched Lanczos bound is (κ−1)²/2 per dimension; supplied synopsis of Theorem 13 does not state sharp two-level maximizers or k-dependent envelope. The source full text could not be inspected; this is explicit residual priority uncertainty rather than a claimed whole-paper noncoverage. General Gaussian KL extremals use different constraints.

## value

PASS

Sharpens a crude quadratic condition-number bound to exact k-dependent constants with discrete multiplicities and linear high-contrast growth; relevant for quantifying isotropic inverse-covariance compression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
