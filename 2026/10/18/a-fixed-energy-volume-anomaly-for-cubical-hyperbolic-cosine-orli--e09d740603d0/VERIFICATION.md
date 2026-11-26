---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independently checked RESULT.md §§1–3. The paired-sign Jacobian after log cosh |x| = beta z is 2 beta / sqrt(1-exp(-2 beta z)); relative to the Euclidean change of variables it gives g(beta z). The simplex weight has coordinates of shape 1/2 and slack of shape 1. Therefore the log integrand is beta/2 minus A plus E, with A=(beta/2)Z0+(beta^2/12)Q, Q=sum Zi^2, and |E| bounded by a beta-dependent constant times sum Zi^4. The rising-factorial Dirichlet moments give EZ0=2/(n+2), EQ=3n/((n+2)(n+4)), EA^2=O_beta(n^-2), and E|E|=O_beta(n^-3). Since A and E are bounded for fixed beta, the integrated linear expansion has error O_beta(n^-2), giving both terms. Facet evaluation is exact without any smooth-limit assumption. The frozen check_volume.py lines 65–70 assign ratio2=direct rather than compute a second planar integral: these lines do not establish the two-quadrature agreement asserted in VERIFICATION.md. The analytic derivation above is the evidence for the theorem, independent of that ancillary check.

## originality

PASS

Pass for the two-term dependence on an arbitrary fixed positive level, not for the unit-level formula or the basic Dirichlet method as separately distinct claims. An indexed November record exactly overlaps at beta=1 and uses the same argument there. Its statement does not cover the free level, and no earlier stronger fixed-energy result was identified. Neither the unit-level numerical expansion nor the extensive-energy theorems imply the all-level expansion by a scaling of the x coordinates.

## value

PASS

The natural sublevel parameter matters in a nonhomogeneous body. The result quantifies how the accumulated nonlinear deformation changes volume relative to the tangent prediction at each fixed level, including two distinct contributions to the first correction (radial slack and quartic coordinate fluctuation). This is a quantitative benchmark across levels, beyond a second computation of the known unit-level coefficient; it makes no claim in growing-energy regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
