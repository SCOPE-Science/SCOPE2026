---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For a>=2, type A count a, type B count two and utility opposite-type count divided by full coalition size, strict blockers must be mixed. If both B in one block with p A and r outside, density comparison yields a one-B blocker iff r>=floor(p/2)+1 with minimum size floor(p/2)+2; any two-B blocker implies a smaller one-B blocker. If the two B are in separate p>=q blocks and r outside, the lower-density B can strictly improve with q+1 eligible A exactly iff p>=q+2 or r>=q+1, yielding min size q+2. Larger single-B or two-B blockers imply one of these cases. Optimizing the two formulas over unstable partitions yields max min-size floor(a/2)+1; p=q+2, q=floor((a-2)/2), r in {0,1} attains it with exactly binom(p+r,q+1) eligible blockers. Brute-force independent integer-utility cross multiplication enumerated all labeled set partitions and candidate subsets for a=2..6 (15,52,203,877,4140 partitions) and checked minima and maxima. These are finite checks; the all-a inequalities in RESULT.md prove the theorem.

## originality

PASS

The source fractional hedonic games literature establishes core/strict-core conventions and broad q-core relaxations. Prior size-resolved blocker-generating polynomial on general K_{a,b} computes per-partition blocker counts, so that component is prior art. The present structural proof evaluates the sharp maximum across all unstable partitions with two minority players and classifies every instability case, which is not stated by these general bounds or per-instance enumeration.

## value

PASS

The exact cutoff floor(a/2)+1 is a natural tight limit on what coalition sizes must be searched to detect strict-core instability in the two-minority-player game; the extremal witnesses show profitable deviations can be linear size yet exponentially rare among uniformly sampled subsets. This gives substantive algorithmic and cooperative-game motivation beyond an isolated partition example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
