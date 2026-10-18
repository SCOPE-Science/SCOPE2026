---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Enumerate ternary squarefree prefixes to length 13 by rejecting newly formed suffix squares; factor closure guarantees exhaustive 342 words. Independently for every deletion of each word scan all square factors and require that all eleven interior deletions make a square: exactly 30 irreducible words. Radius max over deletions of minimum square period splits 18 at 3 and 12 at 6; quotient each by all 6 letter permutations and reversal gives orbit representatives 0102012101202 (12,3), 0102012102010 (6,3), 0102120102012 (12,6). Every last-orbit word has one unique period-6 deletion site; the displayed 11th deletion produces (010212)^2, with no smaller square period. Full finite word enumeration is exhaustive and proves this NATURAL length-13 result, not a general n claim.

## originality

PASS

Harju established ternary irreducibly squarefree existence and exactly three symmetry classes at length 13, so those facts are prior; the new precise minimum-square-period deletion radius profile and unique global deletion site do not follow from a three-class count. Przybocki length classification likewise does not provide period profiles.

## value

PASS

At the first length beyond the final forbidden length 12, the exact local-vs-global deletion witness distinction reveals a nontrivial qualitative split among the already known three classes; least required square period is a meaningful deletion-certificate invariant, not merely recounting the known class total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
