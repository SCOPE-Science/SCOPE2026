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

The frozen complete-cycle law is valid: normalizing the OU endpoint conditional on its exponential duration gives an independent standard normal, U=e^(−2μT) has CDF u^β, and E=(1−U)Z²/2. Conditional Gaussian integration gives the frozen moment criterion (the critical integral is β∫₀¹u^(β−3/2)du); a Mills bound and the scaling v=wU give the tail and conditional gamma law. Selection of the maximum over iid pairs multiplies the exact joint density by n(1−S)^(n−1), which also checks the independent limit and the frozen age scale. The duration maximum has order log n, and even its selected normal mark is standard normal because the duration vector is independent of all normal marks. The repaired RESULT.md additionally proves a local joint-density correction. After wU=z, the Gaussian-tail multiplier has first coefficient −z/2−z²−1/2; integrating against Gamma(β,1) gives −κ(β+1). Split at z=w/2 and bound the Taylor error by an integrable polynomial times w^(−2), with the rest exponentially small. The exact quantile nS(b_n)=1 therefore gives nS(b_n+x)=e^(−x)[1−κx/b_n+O(b_n^(−2))]. Expanding the exact winner density then gives the recorded joint coefficient and compact-uniform remainder. As a separate sign check the logarithm of the four-point density ratio is exactly −(x1−x2)[(1−v1/b_n)^(−1)−(1−v2/b_n)^(−1)] when all four points are in the support. The limiting density has unit mass, giving total-variation convergence by Scheffé. The supplied finite checks concern the frozen one-cycle identities and tail; no uploaded scripts were used to establish the new expansion.

## originality

PASS

For the repaired claim only: the compact-uniform inverse-logarithmic correction to the joint law in exact-quantile coordinates, including its mixed term, was not found or obtained by direct substitution into the inspected sources. The frozen marginal, leading tail and critical moment are materially covered; the leading selection mechanism is related to known contraction proofs and the shared-age gas. They are background or corollaries in the repair, not separate novelty claims.

## value

PASS

Asymptotic independence alone conceals how the energy level biases the age at a finite cycle count. The repaired density identifies both the order and nonzero coefficient of that bias, with a ratio that cancels all separate marginal adjustments. This is a quantitative distinction in a natural reset extremum, rather than a recalculation of the known stationary marginal or its moment boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
