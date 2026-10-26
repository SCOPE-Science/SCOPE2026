---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible mathematical checks

The decisive proof is in `RESULT.md`: the positive maximal-disjoint-support argument and the three-case exact-cover reduction. The checker `verify.py` constructs election ballots from the reduction, checks the quota and supporter restrictions, and then checks JR directly by intersecting each candidate's support with the unrepresented voters, without using the logical reduction as its acceptance predicate.

The checker enumerates every eligible committee for an X3C YES family with two sets and a NO family with four sets, including all 12,870 subsets of the latter eight-seat instance. A separate bounded-support sweep verifies the positive greedy selection with a direct implementation of DR on small explicit supporter systems. All arithmetic is exact integer arithmetic, with no external dependencies.

Verification is finite and does not settle the NP-completeness theorem: the infinite-domain proof is analytic. The limitations include the source restriction \(t\ge2\), at least \(t\) triples, and the particular four-copy family. No independent scientific validation is claimed.
