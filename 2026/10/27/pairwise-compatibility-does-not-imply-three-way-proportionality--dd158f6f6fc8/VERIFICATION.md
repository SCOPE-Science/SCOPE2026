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

The integer thresholds are exactly the lower quotas floor(ks/n). I independently encoded positive quotas by event family and evaluated all 295240 multisets, including repeats, using union, majority, and intersection of event bit sets for quotas 1, 2, and 3. The three displayed witnesses pass their respective pairs, and pair and triple counts are (5,44,6,0). All eleven obstruction supports agree. In the deduction, the two mandated top-two sets define distinct outputs A and B; B cannot contribute to the 5-before-3 quota, so C must. If A omits 1 from its top three, B must have tail 1,5,4 and the quotas give 2>4>5>1 in C, impossible. Once A has 1 third, C needs 3 in the top three; either 1 or 5 third in B would give 2>4>5>3 in C, impossible. So B has tail 4,5,1, and C must start 5,3,1. All then rank 5 above 1, contrary to the final quota. Replication scales numerator and denominator equally. Appending a common tail preserves witnesses; deleting tails from any alleged new joint solution keeps each witnessed original top-two set, cannot worsen any original top-position membership, and preserves original pairwise orders. This proves the whole stated existence family.

## originality

PASS

Bounded evidence supports the distinct separation in the unrestricted output-multiset model. Prior failure of the pairwise axiom itself, or obstruction after restricting all output rankings to input rankings, does not give pairwise feasibility for all three pairs together with triple infeasibility.

## value

PASS

The explicit obstruction answers a natural compatibility question left open by knowing that each axiom may work separately or that pairwise proportionality can fail by itself. It distinguishes genuine three-way interference from incompatible pairs in a small, unrestricted example. The exact counts quantify how often pair compatibility occurs on this fixed instance; the replication and padding are scope extensions, not the main contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
