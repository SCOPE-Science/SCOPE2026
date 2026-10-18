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
# Reproducibility and finite completeness

Run `python3 verify_bijections.py` and `python3 verify_pairings.py` from this directory. Both scripts use only Python's standard library and explicitly construct the Fano incidence graph from the nonzero three-bit vectors.

The first script traverses `itertools.permutations(range(1,8))`, which consists of exactly \(7!=5040\) bijections, checks nonincidence for all seven line-point pairs, builds all \(21\) incidence-edge colour pairs for each remaining assignment, and compares their set cardinality to \(21\). Independently it traverses all \(5040\) point permutations to find the \(168\) preserving the Fano block system, transports the first optimum, and checks that its orbit equals the entire eight-element optimum set.

The second script recursively pairs the least unpaired vertex with each other remaining vertex. That recurrence enumerates each partition into seven unordered pairs exactly once, giving \((14-1)!!=135135\) partitions with no up-front restriction on pair types. It separately checks propriety and the uniqueness of \(21\) edge-colour pairs. It finds \(23412\) proper pair partitions and eight exact harmonious ones. The independent enumeration corroborates the bijection reduction and the final count.

The two `.stdout` files contain the observed exact outputs and `VERIFY_OK` sentinels. This is a complete finite check over the stated domain; it is neither a formal proof of any infinite generalisation nor an independent external audit.
