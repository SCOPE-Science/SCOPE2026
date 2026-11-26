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

The frozen proof and self-review incorrectly claim that a coupling event with one switch at the lower persistence and none at the higher persistence always has positive probability: when p1=0 and n>2, the lower walk makes n−1 switches deterministically. The corrected RESULT.md and REVIEW.md separate this case. If p1=0, the alternating endpoint has absolute value d=n mod 2; at p2>0 no switches have probability p2^(n−1)>0 and give absolute displacement n. For 0<p1<p2≤1 the original zero-versus-one event has probability (n−1)(p2−p1)p1^(n−2)>0. The corrected claim is unchanged. Independently, conditioning on m gives 2 binom(n−1,m) equiprobable words. Odd 2a−1 gives a runs of each sign; the even 2a sum differ by the composition-count factor (n−2a)/a before division by total word count. This gives identical normalized signed masses, including their support. The adjacent pair likelihood ratio on the older absolute support is a positive constant times (n−2a)^2−|s|², vanishing at the old support edges. A decreasing ratio normalized to mean one gives weak tail order by the covariance inequality; the zero-switch point mass is maximal. The uniforms order the switch counts, which proves the unconditional weak order; the repaired strictness proof covers all nontrivial thresholds and endpoints. The rest of the thresholds are deterministic.

## originality

PASS

The corrected attribution treats the run-count formulas and their normalized signed parity identity as antecedent or direct algebra from published counts. The distinct result is the conditional absolute likelihood-ratio ordering and the resulting strict distribution-wide comparison across the entire persistence interval, including anti-persistence; this is not a bin-level or marginal-shape result.

## value

PASS

Absolute endpoint tails at every finite length are significantly more informative than variance growth or single-bin crossovers. Conditioning on switch counts reveals a mechanism that works through the anti-persistent regime as well as the persistent regime and proves strictness at every nontrivial cutoff. This is a natural distributional statement and remains valuable without crediting the known counting formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
