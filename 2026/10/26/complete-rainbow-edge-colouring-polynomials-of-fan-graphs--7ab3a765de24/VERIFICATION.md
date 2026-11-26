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

Every four-cycle uses the hub and a three-vertex rim interval. Its middle spoke is incident to every perimeter edge, so properness makes the B and D constraints identical. Fixing the distinct spoke colours gives the stated forbidden list on each rim edge; the only rim-to-rim conflicts are between neighbours. In inclusion-exclusion a subset of adjacent equalities partitions the rim into consecutive blocks, with independent pre-exclusion choices given by the complements of the unions of forbidden intervals. The block signs and last-block recurrence follow, including q<n where the falling factorial vanishes. The triangle, diamond, middle rim edge at n=4, and hub degree give the lower bounds; the explicit rim construction respects the lists for n>=5, and changing the first rim colour to 6 when n>=6 preserves legality and gives an inequivalent colouring. Minor proof-text correction, not a change to the Finding: RESULT.md line 60 says the normalized polynomial equals 1 at n=3. In fact R_{3,2}(5)=2, with the two completions exchanged by swapping the two colours not on spokes. Thus there is indeed one class. The independent replay builds actual four-cycles and five-edge diamonds, enumerates fixed-spoke completions for n=2 through 9 and bounded palettes, and checks the recurrence and the optimum counts with the residual colour permutations removed.

## originality

PASS

Pass is for the explicit all-palette fan polynomial and complete optimum enumeration, not for the independently known B/D equivalence or small palette bounds. The strongest compared cone results give other rim structures or only the minimum palette. The all-palette enumeration and its optimal specializations do not follow by specializing those statements.

## value

PASS

The fan is a natural maximal outerplanar family and the full named count at every palette (and exact count modulo colour names at the optimum) is substantially more informative than an index or one construction. It provides an exact family-wide counting benchmark and detects the rigid-to-nonrigid boundary. The value is the interval-sensitive enumeration, not the use of generic inclusion-exclusion or the known existence cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
