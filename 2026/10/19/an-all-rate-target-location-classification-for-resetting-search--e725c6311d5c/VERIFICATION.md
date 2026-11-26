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

The frozen blanket no-optimal-finite-positive-rate statement is false: M=1 for the left bridge, so all rates minimize it. The local nonbridge improvement is a supremum, not attained. The complete replacement RESULT.md and companion REVIEW.md correct these claims; the four formulas and their signs are unchanged. Independent check via the reset-inclusive backward equations: write A for the mean at the start lump and b,c,d for the other three means minus A. For a local nonbridge target b=A−1, c=(m+1+r)b, (n+r)c−b−(n−1)d=1 and (1+r)d−c=1, giving D(r)b=n+r. For a right nonbridge target b=−1, c=−(m+1+r), A=(n+r)(m+1+r)+(n−2)d and (r+2)d=−A−(m+r). Thus A=(m+1+r)(r+2)−(n−2)(m+r)/(n+r), identical to the stated formula, including n=2 when the extra right lump is absent. The left bridge has constant unit hazard; the right bridge backward equations give A=1+m+r. D is positive and the local derivative numerator has strictly negative constant term and all other coefficients negative. In the far derivative the subtracted fraction is either nonpositive or strictly less than one. These arguments include r=0. The corrected minimizer statements now follow exactly. Frozen verify.py was read, not executed; its 600 comparisons are recorded consistency evidence, not the proof.

## originality

PASS

Credit is limited to the single-edge barbell's exact target-wise classification for unit edge clocks and resetting to a nonbridge source. Existing general restart and hitting-time identities do not settle the direction of change for all four classes. The corrected optimum statements add no priority claim.

## value

PASS

The corrected result gives a complete target-response classification for two directly connected communities. It quantifies how resetting circumvents arbitrarily large excursions when the target is local, but imposes increasing cost for accessing the other community. The exact unattained fractional gain n/(m+n), flat local bridge and distinct linear/quadratic remote delay provide interpretable benchmarks beyond a generic formula or a numerical global average.

The dated certificate retains the supplied scientific assessment, sources and limitations.
