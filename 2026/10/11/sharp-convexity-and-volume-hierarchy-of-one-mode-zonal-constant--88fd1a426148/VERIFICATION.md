---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For odd l>=3, the Legendre generating function gives a strictly positive odd cosine expansion P_l(cos theta)=sum_{odd k<=l}a_{lk}cos(k theta), a_{lk}=2 c_{(l+k)/2}c_{(l-k)/2}>0 with c_j=binom(2j,j)/4^j; sum a=1. Thus meridional support curvature rho_m=1-eps sum_{k>=3}(k²-1)a cos(k theta), and C=sum(k²-1)a=(l(l+1)-2)/2 from P_l′(1). The sharp |eps|<=1/C follows from the pole obstruction and the triangle bound. For zonal h, a(theta)=h sin theta+h_theta cos theta satisfies a′=rho_m cos theta, a(0)=a(pi)=0; integrating from the nearer pole shows rho_az=a/sin theta>=0, so meridional positivity is fully sufficient. Oddness makes width exactly 2; |eps|<=1/5 and |P_l|<=1 keep h>0. Spherical harmonic identities and integrated Bochner give V=4pi/3-2pi(l(l+1)-2)/(2l+1)eps²; the cubic integral vanishes by antipodal parity. Exact symbolic independent integration of h*rho_m*rho_az verified the volume for l=3,5,7,9,11, including 128pi/105 at l3. Strictly increasing denominator gives monotonic endpoint volumes. At boundary the positive cosine coefficients require cos(k theta)=1; l3 only k3 gives theta=0,2pi/3, whereas l>=5 has both k3 and k5 so theta=0 alone. Negative eps reflects theta. Algebraic checks for five degrees corroborate, not replace the all-l positive-coefficient proof.

## originality

PASS

The l3 endpoint convexity, intrinsic volume and general harmonic volume formula are already published; they are explicitly treated as known subclaims. The separately reviewed result survives in the uniform sharp convexity classification for EVERY odd zonal degree, strict volume hierarchy and exceptional meridional-degeneracy ring. Neither cited geometric umbrella nor prior cubic paper establishes all those implications.

## value

PASS

Exact maximum feasible amplitude is an invariant of a natural one-harmonic constant-width deformation in all odd degrees. The result gives a complete infinite-degree classification of convex feasibility, strict endpoint volume hierarchy, and the geometric transition from a genuine meridional zero-curvature ring at l3 to isolated axial degeneracy for every higher odd mode. This remains mathematically useful even though l3 and volume spectral formulas are separately known, and is not merely a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
