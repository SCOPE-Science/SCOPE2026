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

The arithmetic state (parity of adjacent 11 pairs, last digit) changes on appending b to (r xor (b & last),b). Relabel (0,0),(0,1),(1,1),(1,0) as 0,1,2,3 and the pair of children is exactly the specified substitution. Starting at the first pair, the even and odd start maps inductively cover all consecutive states; every generated pair occurs. For i=32j+t every 26-bit window uses at most the two adjacent 32-bit blocks, and each realized source pair yields every offset. Independent Python replay /workspace/replay_rudin_shapiro.py uses (n & (n>>1)).bit_count(), digital state-pair closure and direct comparisons of the two halves. It matched all 256 CSV rows exactly, 200 distinct factors, histogram 128,32,72,8,4,4,4,4, and the four hard templates giving exactly the two stated strings. The script checks a mathematically exhaustive cover, not extrapolation from a prefix; uploaded code was inspected, not run. The substitution is primitive with uniform letter frequencies (each letter appears in each third iterate and the incidence matrix has uniform row and column sums). Even positions give four internal pair frequencies 1/8; the odd-position map sends the eight source pairs two-to-one onto the four other pairs. The induced pair-frequency equation is a contraction with coefficient 1/2, so the common solution is 1/8 as asserted. Aligned offset occurrences have density 1/(8*32) in the unrestricted prefix limit; summing produces the stated law.

## originality

PASS

Best-knowledge pass for the shortest ordinary abelian-square root at each start, its sharp bound and witnesses, and especially its exact natural-density law. Prior factor-language coverage and template machinery are acknowledged rather than counted as new. Ordinary equality of Parikh counts must not be conflated with 2-abelian or 2-binomial equivalence.

## value

PASS

The minimum radius is a natural local recurrence statistic of the Rudin–Shapiro word, not an arbitrary length cutoff. Sharp uniform locality and its distribution distinguish the rare starts that force long root lengths from the typical short ones. This is useful word-specific structure unavailable from factor complexity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
