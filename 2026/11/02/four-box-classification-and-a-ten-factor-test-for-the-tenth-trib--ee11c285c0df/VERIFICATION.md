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

The revised word, positions, factor-hit predicate and restriction to exactly three distinct positions match the replay. Of 80,559 nonempty factors with 79,983 distinct support masks, the twelve inclusion-minimal masks suffice since each support contains one. The full test and the listed ten tests accept 416 triples apiece, so their solution sets are equal by inclusion. The count groups signature classes with binomial weights for repeated classes, not repeated positions. Witness W_i misses support i and hits the other eleven. Each original support contains a minimal support, so if W_i misses an original support, support i is the only possible minimal support it contains. A single factor predicate thus cannot reject two witnesses; ten predicates are necessary even when nonminimal supports are allowed. The fresh replay confirmed these assertions and the original four-box and T_9 counts; the repaired table's twelve factors and ten witnesses were checked exactly against the tested certificate.

## originality

PASS

This decision applies only to the revised extremal theorem about the minimum number of factor-hit predicates. The strongest indexed match already gives the full attractor list and even the underlying twelve-mask count, so those are credited, not relabelled as novelty. That prior method does not show that ten predicates suffice on triples or that nine arbitrary factor predicates cannot suffice. No covering result for the revised theorem was identified in the bounded comparison.

## value

PASS

The remaining question asks for the smallest exact factor test at a canonical morphism iterate. It distinguishes support minimality from indispensability on the fixed-size domain, and provides a usable optimal test together with a reusable obstruction argument against arbitrary factor choices. The usefulness is in the extremal test size, not in repeating the known census or just recertifying a known count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
