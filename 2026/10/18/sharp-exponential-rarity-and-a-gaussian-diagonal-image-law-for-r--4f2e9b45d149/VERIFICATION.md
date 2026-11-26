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

Equivariant regularity is equivalent to lifting fixed image points to fixed preimages: an equivariant section can be chosen independently on image orbits and extended off the image into the diagonal. Independent unordered off-diagonal pairs therefore give exactly the stated regularity factor given d diagonal labels. For d/n in an interior compact set, the truncated Poisson coefficient estimate is uniform: its centered characteristic function has a uniform quadratic term with variance bounded away from zero and bounded cubic remainder, and a uniform modulus gap away from zero by span one and compactness. Stirling normalization gives the local prefactor in (73). The n^0 term in the log regularity factor is (1-x)/2-(1-x)^2/4=(1-x^2)/4. The strictly concave F has the stated unique stationary point; the coefficient upper bound with the same saddle and the direct d=n term separate the tails exponentially. In an interior neighborhood, a quadratic envelope bounds the rescaled tails, and the lattice Riemann sum yields both the sharp prefactor and the normal law. As an independent numerical cross-check, the generating function for occupancy tilted by e^(d/2) is proportional to [z^n](1+e^(1/2)(e^z-1))^n. At its saddle the exponent simplifies to lambda_*-1; the saddle count has variance lambda_* and the indicator of a nonempty bin has covariance 1-x_* with the count. The resulting simplified expressions I=1-lambda_*, C=exp((1-x_*^2)/4)/sqrt(lambda_*) and kappa^(-1)=x_*(1-x_*)-(1-x_*)^2/lambda_* reproduce 0.171897973381, 1.256970100571 and 0.093950190004, respectively.

## originality

PASS

Pass is for the sharp probability and conditional limit under regularity only. The finite enumeration and structural regularity criterion are published, as is the occupancy/Stirling saddle-point technique, including local coefficient asymptotics. The closest inspected formulas do not already give the regularity-weighted theorem: the regularity tilt changes the saddle by an order-one fraction, its subexponential factor changes the leading constant, and the conditional fluctuation law depends on the curvature at the new saddle. The use of standard asymptotic methods is not an originality claim.

## value

PASS

For the natural uniform operation-table law, the exact count alone does not explain exponential rarity, the non-typical diagonal occupancy of regular operations, or its fluctuations. The joint sharp probability and conditional fluctuation law quantify these together and include an order-one correction from off-diagonal pairs. This is more than recomputing the finite enumeration or giving an occupancy rate without the conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
