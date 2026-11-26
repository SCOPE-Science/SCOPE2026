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

The unit-sphere fourth moments give inner product (2/15) times Frobenius on trace-free symmetric tensors. Azimuthal averaging and the normalized polar weight dr/2 give exactly the three densities and integrated differences a(c), b(c). I independently constructed the rotation by Q -> R Q R^T and computed the commutator in the reflection-even and reflection-odd bases for the plane containing the axes; their dimensions are 3 and 2. The squared independent entries are exactly U,V,W in the even block and b(c)^2 b(d)^2 t(1-t) in the odd block. Real skew blocks have the asserted imaginary eigenvalues and norm. Since a,b are odd, the norm is unchanged by negating either threshold. For the strict block, the independent script /workspace/branches/independent_caps_certificate.py derives the angular polynomials from tensor matrices, substitutes each box afresh in the power basis (rather than replaying de Casteljau subdivision), and checks Bernstein coefficients with exact rationals. The nine boxes at depth at most four cover the cube and have minimum coefficient 223228347/7340032000000 > 1/40000. The proof uses the Bernstein partition of unity, not sample positivity. For the odd block, |b(c)| attains its unique positive maximum in |c| at 1/sqrt(5), and t(1-t) uniquely maximizes at t=1/2. This gives exactly 9/250 and all sign/axis equality cases. Collinear, perpendicular and zero-threshold cases are included in the block formulas. The result is on the exact-degree space only.

## originality

PASS

The single-cap spectra and harmonic localization framework are covered, including in an equivalent indexed antipodal-cap formulation. The independently oriented two-cap sharp operator commutator, its strict competing sector and equality classification are distinct in the bounded literature and indexed comparisons.

## value

PASS

The two cap compressions are canonical concentration operators, and their commutator measures the difference between applying them in the two possible orders. Pure degree two is the first harmonic degree with competing nontrivial reflection sectors in this geometry. An optimized constant is useful independently of the general concentration framework: neither scalar angular maximization nor a bound based only on spectral diameters excludes the other sector. Giving all aperture and angle equality cases identifies precisely how noncommutation is maximized. No reconstruction or higher-degree conclusion is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
