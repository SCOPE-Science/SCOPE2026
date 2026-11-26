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

The facet area times the absolute normal component gives sqrt(m)/(m-2)! times |u_i|, before the factor 1/2 in Cauchy's formula. At a minimum, positive and negative coordinates each have total magnitude 1/sqrt(2), with exactly one coordinate of each sign. In the k=m-2 free tangent coordinates y, the Gram determinant is 1+k/2=m/2 and Z-sqrt(2)=||y||_1+O(||y||_1^2). The area of each near-minimum component is therefore sqrt(m/2) times the volume of a k-dimensional cross-polytope of radius t, with O(t^(k+1)) error. There are m(m-1) components. Within a sign chamber with r positive coordinates, the projected sign vector has norm 2 sqrt(r(m-r)/m); the largest norm is L_m and only the stated N_m chambers attain it. On any coordinate wall the value is at most D_m, and unbalanced chambers are bounded by E_m. Both bounds are strictly less than L_m for m>=3. A cap above these two bounds cannot leave its chamber: at a first wall crossing along a shortest geodesic the chamber's linear functional still agrees with Z. Area integration gives (3), and sigma_(k-1)/k=kappa_k gives the leading coefficient of (2). At m=3 the six caps meet only on boundaries at the minimum and the derivative of the exact circle law there agrees with (1). The analytical reconstruction does not rely on the inspected seeded simulation. The supplied replay path is check_brightness.py; it was not executed.

## originality

PASS

Credit the simplex projection normalization, extrema and equality directions to prior work; credit only the fixed-dimensional probability laws with constants and explicit upper cap window here. The spherical cap integral is standard. The lower tangent sublevel volume and the explicit upper window require geometry beyond the prior extremal values. The closest indexed probability results concern a different polytope or a different projection statistic.

## value

PASS

The two endpoint probabilities quantify how often Haar viewing directions nearly attain extreme projected volume. The differing exponents distinguish nonsmooth nearly sparse directions from smooth cap neighborhoods of balanced signs. The constants and explicit exact-law window make that distinction quantitative for every fixed simplex dimension, not simply another proof of the extremizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
