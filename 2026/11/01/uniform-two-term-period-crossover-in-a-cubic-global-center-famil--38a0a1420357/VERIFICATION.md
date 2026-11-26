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

The displayed energy is conserved, proper, and has a smooth connected level oval through each (A,0); the vector field never vanishes there. The unchanged-time coordinate q(x) with q'=exp(beta x²/2) eliminates the squared-velocity term. The derivative of xq'(x)/(1+beta x²) is strictly less than q' for x>0. With G'=1+(beta+3gamma)x²+beta gamma x⁴ this gives qG'-G>0 and strict increase of G/q, hence strict decrease of the scaled canonical period integral. Dividing its inner integral by 1-s² leaves a positive smooth factor on local amplitude ranges including s=1, so the period is smooth. The cubic coefficient in the canonical force is gamma+beta/3; expanding the integral yields the stated -(beta+3gamma)A²/8 small-amplitude correction. To check the large-amplitude coefficient, the turning coordinate u=A²-x² yields the exact integrand 2(1-u/A²)^(-1/2)(E0-rE1/A²)^(-1/2) for A sqrt(1+gamma A²) T. For u<=A, a first-order Taylor expansion has error bounded by a constant times A^(-4)u² E0^(-1/2), uniformly in r in [0,1]. For A<=u<=A²/2 the two correction factors are bounded. Beyond A²/2 the weighted exponential integral in the second denominator is bounded below by half its integral over [u/2,u]; the first denominator leaves only an integrable endpoint factor. Both tails are exponentially small uniformly in r. With v=beta u, f(v)=(exp(v)-1)^(-1/2), the needed moments are integral f=pi and integral v f=2pi log 2 by z=exp(-v) beta integrals. Since (exp(v)-1)^(-3/2)=-2f'-f, integrating v times this identity gives 2pi(1-log 2), which yields the stated r-dependent coefficient. Thus the normalized remainder is uniform for fixed beta even when gamma varies with A. The endpoints of the strictly decreasing period are 2pi and 0, proving the claimed bijection and uniqueness at each period.

## originality

PASS

The global center, the restoring-free two-term result, and same-family leading and monotonicity assertions have direct overlap in the inspected records. The supported distinct claim is the gamma>0 explicit relative correction with a uniform O_beta(A^-4) error across the crossover, not these overlapping portions taken separately.

## value

PASS

The positive-restoration term changes the large-amplitude period scale. An explicit correction and an error bound valid through gamma A² of order one, as well as in its small and large regimes, quantify when fixed-parameter laws can be used and what they miss. This is an original-time period invariant in a classified natural cubic family, not merely reidentifying its phase portrait or recomputing the known restoring-free coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
