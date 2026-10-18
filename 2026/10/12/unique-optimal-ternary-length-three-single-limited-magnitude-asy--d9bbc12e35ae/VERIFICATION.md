---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: The 27 ternary words under at-most-one nonwrap +1 coordinate error have exact balls of size 1..4. Nine explicitly displayed three-word conflict blocks partition all 27 and are pairwise incompatible within each block, giving |C|<=9. The parity-corner eight plus 111 achieves nine with disjoint balls. Independent search rebuilt the balls, verified every pair in all nine blocks, and found exactly one labeled compatible nine-code; this is finite EXHAUSTIVE over all 27 words. It matches Cassuto et al residue-mod-2 lift of binary {000,111}.

## originality

PASS

PASS best-of-knowledge: Cassuto-Schwartz-Bohossian-Bruck 2007 explicitly gives the modulo-2 lifted construction and its correction property, so the nine-word code is preexisting and NOT novel. Its inspected entire five-page preprint discusses construction, general decoding, perfect wraparound cases and length7 Hamming instance, but states no nonwrap ternary length3 sharp bound or unique labeled maximum. Exact finite classification is not implied by construction alone; residual risk of an unindexed enumeration.

## value

PASS

PASS, narrowly: This is the exact complete extremal classification for the smallest ternary length-three nonwrap one-up-error flash model; it establishes optimality and uniqueness, which the classical modular construction by itself does not, and supplies a concise human-checkable nine-part upper-bound certificate. It does not claim a general coding family advance or priority over the known optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
