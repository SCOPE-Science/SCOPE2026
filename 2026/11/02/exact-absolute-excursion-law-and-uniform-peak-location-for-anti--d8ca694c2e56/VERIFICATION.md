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

Conditionally on W₁=z the process is a unit-time bridge from −z/2 to z/2; the free endpoint density exactly cancels in the killed-kernel ratio. The change of variable z=−2x contributes 2, and reflection of the Dirichlet eigenfunction contributes (−1)^(k+1). Independently, in the interval (0,L) with L=2h, the killed kernel from x to L−x is the sum over integers k of φ(L−2x+2kL)−φ((2k+1)L), with φ the standard normal density. Twice its integral over x∈(0,L) is 1−2L times the sum of the reflected densities: the translated intervals in the first term partition the real line. This gives the image law directly. The CDF is continuous on h>0, S>0 a.s., and termwise nonnegative tail integration gives the moments for q>0. Brownian path extrema are individually unique; the strict extrema and endpoint have an interior joint density by differentiating the smooth two-barrier killed kernel, with no boundary mass by local oscillation at both time endpoints. Hence max W+min W=W₁ has probability zero. The signed rotation preserves Gaussian covariance, and therefore the joint law of the height and the unique circular location. For every height event the corresponding finite location measure must be its total mass times Haar measure, proving independence.

## originality

PASS

The anti-periodic process is known, and the theta law in isolation is classical. The distinct result identifies that law for the supremum of this path and combines it with the unique uniform independent peak. The closest matched same-process source studies an unrelated quadratic functional, and the closest matched classical supremum is for a differently pinned path.

## value

PASS

The supremum is the natural confinement statistic of a standard anti-periodic Gaussian path. The result supplies all thresholds and moments with complementary formulas useful in different tail regimes, and an exact spatial law for the peak even conditional on a rare height. The path-specific identification and peak comparison matter even though the scalar distribution, once identified, is a transform of a classical one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
