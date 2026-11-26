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

For odd dimension 2m+1 the geodesic integration weight is sin^(2m)(theta). The cosine expansion of the weighted Gegenbauer polynomial is supported on n,n+2,...,n+2m by polynomial degree, parity, and orthogonality. Vanishing through derivative order 2m−1 at zero cancels the first m large-a terms in the rational combination of the cosine transforms; after a[1−(−1)^n exp(−pi a)] is factored out, the numerator over the product denominator is constant. The local coefficient C_n^(m)(1) at theta^(2m) fixes that constant to (2m)! C_n^(m)(1). This includes n=0 with its a² denominator factor. The affine correction multiplies the positive transform by 1−bR, with R its logarithmic a derivative. R increases strictly in each parity; the even limit is the larger and is unattained. The difference R_1−R_0 is strictly positive because its first rational term 2/[a(a²+1)] exceeds pi/sinh(pi a), as seen using the cubic Taylor lower bound for sinh. Thus the minimum is R_0<0, and the two reciprocal thresholds are necessary and sufficient. Only degree zero disappears at the lower boundary; at the upper boundary all degrees remain positive and the even coefficients have an extra asymptotic factor 2aU(m+1)/n². The two-parity strictness criterion holds at both boundaries. The coth expansion or the partial fraction series gives R_0=−pi/2+a/(2m)+O_a(m^-2), so L_m increases to −2/pi with the stated correction. Equatorial embedding gives the all-sphere intersection, not a separate sharp interval for each even dimension. Random hemisphere signs supply the stated geometric check. Replay: RESULT.md lines 34–109; VERIFICATION.md, verify_spherical_affine.py and check_output.txt give recorded finite checks (105 integrals, 35 symbolic checks, 1,500 sign checks), inspected, not independently executed or used to prove the infinite claims.

## originality

PASS

The supported distinct claim is the exact free-slope interval with its dimension-specific lower obstruction and upper-end spectral characterization in every covered odd dimension. The universal lower endpoint and the circle obstruction at U(a) have elementary existing-framework explanations; neither is treated as standalone novelty. The strongest same-day matches examined have a different modulator or parameter family. Neither they nor the inspected literature evaluate both spectral obstructions for the asserted family.

## value

PASS

The free affine slope supplies a simple tunable covariance family beyond the known valid exponential and invalid standard geodesic Matérn choice. An exact admissibility interval with strict endpoint behavior, two different sharp spectral obstructions, and explicit dimension dependence answers a natural stability and modeling question; it is materially more useful than a sufficient-only bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
