---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For strictly positive bounded self-adjoint A on real/complex Hilbert space dim>=2 and B_u=beta^2 I+(alpha^2-beta^2)P_u, the exact rank-one factor X=A^1/2 B^1/2 A^-1/2=beta I+(alpha-beta)|v><w| with v=A^1/2u,w=A^-1/2u shows D=X*X equals beta^2 on E^perp, E=span(v,w), so D-beta^2I has rank<=2. On E, determinant alpha^2 beta^2 and trace T=alpha^2+beta^2+(alpha-beta)^2(k-1), k=<Au,u><A^-1u,u>, giving the two strict spectral outliers for non-eigen u. The functional-calculus bound A+mM A^-1 <= (m+M)I plus scalar AM-GM gives sharp k<=K=(M+m)^2/(4mM), attained precisely by balanced m- and M-eigenvectors (if they exist). Spectral localization gives sup/inf even without endpoint eigenvectors, and unit-sphere connectedness gives all intermediate norms. For kappa=M/m large, L*~(alpha-beta)^2 kappa/4 and min spectral value~4alpha^2 beta^2/((alpha-beta)^2 kappa). Independently computed 30 complex matrix examples in dimensions 2,3,8, with predicted full eigenvalue multiset to 2e-12. The proof uses spectral theory rather than extrapolating finite checks.

## originality

PASS

Best-of-knowledge originality of the precise final mathematical addition, not its known source definition; checked actual primary statements/implications and Resultary semantic neighbors; residual access and priority risks remain explicit. The restricted input B_u is natural, and the combination yields sharp attainable/unattainable characterization beyond any result explicitly located. This originality PASS is necessarily qualified by unread primary full texts and possibility of a known operator-norm specialization.

## value

PASS

The theorem supplies a sharp and dimension-independent complete two-outlier spectral profile, spectral endpoint attainment conditions, and asymptotic norm amplification for a canonical noncommutative rank-one spiked input to a recent operator mean. These are useful natural operator-theoretic invariants beyond qualitative log-majorization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
