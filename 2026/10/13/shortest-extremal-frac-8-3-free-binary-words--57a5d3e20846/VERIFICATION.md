---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Every exponent-at-least-8/3 factor with least period p has a period-p threshold subfactor of length ceil(8p/3). Prefix generation rejecting newly created forbidden suffixes is exhaustive: a newly invalid word must have a forbidden suffix. Independently compiled and ran a separate C++ period-threshold generator for lengths 1..30. It reproduced all 30 populations (ending 34,880;48,020;66,102), found no extremal word below 30, and exactly the two stated length-30 words. Both words were independently checked under every one-letter insertion. Exhaustion proves this finite minimum, but neither larger-length classification nor higher-threshold existence.

## originality

PASS

Mol–Rampersad–Shallit prove arbitrarily long extremal words at threshold 8/3 by morphic constructions, not a sharp shortest length, exhaustive short-length census, or the exact unique complementary pair. Their Prop. 4.2(e) construction starts at a substantially longer length under the prescribed nonempty source. Existence of long instances does not imply the least length.

## value

PASS

The endpoint 8/3 is the upper explicitly established general extremal-freeness threshold in the motivating source. Its first extremal binary witness and the uniqueness/symmetry classification are independently useful finite boundary data, not an arbitrary cutoff; full exhaustive search is mathematically substantive here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
