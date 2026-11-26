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

The H^(1/2) unit ball is locally bounded by the Hardy point-evaluation estimates and closed under locally uniform limits by taking radial means at each radius and then the supremum. Coefficients are continuous in that convergence, so the nonzero bounded functional attains its positive supremum with unit quasi-norm. Brevig–Søvik Theorem 1 explicitly covers any attained extremal for a nontrivial bounded linear functional at 0<p<1; scalar phase reduces absolute maximization to that convention. An outer extremal has an analytic fourth root g with ||g||_2=1 under the stated normalization. Only the first three coefficients b_j of g enter: 4b_0^3b_1, 4b_0^3b_2, 6b_0^2b_1^2 comprise the objective. The triangle estimate is attained on the positive real sphere by a normalized polynomial fourth power, and Parseval plus positive homogeneity eliminates higher coefficients at equality. The optimum has b_0 nonzero (otherwise zero objective), and positive moduli of b_1,b_2 (at a zero component a positive perturbation gains to first order while normalization changes only to second order). With ratios u,v, N=4u+4lambda v+6lambda u^2 and D=1+u^2+v^2, the stationary equations are (1+3lambda u)D=uN and lambda D=vN. Their ratio gives v=lambda u/(1+3lambda u); substitution and clearing positive factors gives the exact stated quartic. The sign pattern has one change, so the positive root exists and is simple; the endpoint evaluations are -lambda^2-2lambda/sqrt(3) and 1+2sqrt(6)lambda/3, yielding the strict u bounds and 0<v<1/3. This is the sole interior optimum. Equality of the three nonzero term phases gives a common phase of the b_j, hence precisely the stated class of f. Zero-freeness on the closed disk follows by deforming u to zero: for a boundary root the imaginary part after dividing by z forces z=±1, each ruled out by u<1 and v<1. Parseval verifies the candidate's exact quasi-norm. Simplicity gives analytic dependence, stationarity gives C'=a_2 at the normalized positive representative, and the supremum of affine functions gives convexity. Affinity on an interval would give a shared maximizer at distinct weights, excluded by lambda=v/[u(1-3v)]. The compact root bounds and the quartic at zero and after dividing by lambda^2 at infinity give (u,v)→(1/sqrt(3),0) and (sqrt(2/3),1/3), respectively; substitution gives all three limit constants including C'(0+)=9/8. This proves the full positive-weight statement, not a complete coefficient-body description. The attached symbolic/numerical checks were inspected, not executed or used in place of the algebra and theorem.

## originality

PASS

The distinct result is the finite positive-weight exact support of (a_1,a_2), with all equality cases and its strict convexity. Known single-coefficient endpoints, the outer-extremal reduction and similar weighted problems for other coefficient pairs are not claimed as new.

## value

PASS

Separate coefficient bounds do not describe which coefficient pairs a single function can expose. The exact interior curve and uniquely phased extremals give quantitative joint constraints, a derivative selecting the exposed coefficient, and a smooth, strictly convex interpolation between previously known sharp endpoint problems. This is a natural coefficient-body question at an exponent where a complete calculation is possible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
