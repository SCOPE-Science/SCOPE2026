---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independent differentiation of the Cartesian field and symbolic expansion confirm c_2,c_1,c_0, the completed square, all three highest-degree terms of (c_2 c_1−c_0)/μ, and κ_1. The cubic criterion with c_0,c_2>0 is sufficient as well as necessary: c_1>0 follows from c_2c_1>c_0. c_2 has a uniform positive lower bound for small μ; c_0 is positive outside a compact set by positive definite leading forms of f_3,f_4, and on the compact set by g→10 uniformly. Dividing H by s²(1+μs²+μ²s⁴) gives a convex combination of strictly positive leading forms on the unit semicircle, with uniform O(1/s) error. Thus no zeros or near-zero minima can escape to infinity. Near the limiting unique interior minimizer (10/sqrt(62),1/(2sqrt(62))) the Hessian is positive definite, and outside that neighborhood the limiting square gives a positive compact gap. The analytic minimizer has value with κ-derivative u_0/5, giving a local analytic strict threshold; its first correction is −5P_2/u_0=428.396613755040596…>0. At equality the positive cubic coefficients yield (λ+c_2)(λ²+c_1) exactly on a single u>0 orbit of rotation. For fixed κ away from κ_0 the leading sign is decided on the compact region using the same tail bound (or by a negative value at the limiting minimizer); at κ_0 the first correction excludes strict Hurwitz. On z=−u/10, S=−25(u−1)(u−4)/21, yielding the two period-2π circles and opposite signs of the transverse Jacobian determinant; the trace at u=4 is negative for small μ.

## originality

PASS

The supported distinct result is the everywhere-Cartesian-Hurwitz boundary germ of this exact family, its two coefficients and its unique equality circle. The original field, two cycles, cubic coefficients and a globally Hurwitz open set are prior. The strongest same-family primary and indexed spectral findings inspected do not supply a global minimum or the boundary germ. The conclusion is best of current knowledge, not a priority certification.

## value

PASS

The known counterexample is specified by an isolated certified pair plus an unspecified open region. A necessary and sufficient local shear boundary across all space identifies how the counterexample can stay everywhere Hurwitz as dissipation vanishes. The first correction decides the critical fixed ray itself, and the equality locus describes how strict stability fails. These are structural refinements of a motivated stability problem, not arbitrary parameter tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
