---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

First-force local structure excludes any 3-set (new initial force needs two blue neighbors in triangle-free cubic graph, after first force no further move) and reduces four-sets to local fourth placements; propagating explicit seeds and dihedral symmetries produces seven orbit representatives, six of size 2n and one size n. Intersection-three exchanges are reduced to at most 16 candidate translations and affine congruences An+B=0 mod 2n; |B|<=12 gives uniform stabilization beyond n=13. The seven-by-seven incidence matrix yields degree enumerator, 48n edges, and connectivity through the A-family cycle. Independent exhaustive forcing of every four-set and reconfiguration adjacency for n=6..11 reproduced exactly 13n and degree histogram, and did not substitute for infinity. The n=6 sixth adjacency trace was recomputed using an independently implemented exhaustive construction and length-2-through-6 closed-walk recurrence; both reported trace vectors agreed exactly.

## originality

PASS

Z(M_2n)=4 is explicitly prior (Duong et al Theorem 5.2); token-jump reconfiguration definition is prior (Geneson–Haas–Hogben). Neither inspected source contains the complete seven-orbit minimum-set census, its exchange graph degree formula/connectedness or n=6 sixth-trace distinguishing invariant. Originality asserted for these structural extras only, with older zero-forcing literature risk.

## value

PASS

Knowing minimum controllability placement size does not enumerate configurations or whether a controller can be moved one at a time without loss of forcing. Complete 13n orbit census, connected 48n exchange graph and twist-detecting sixth moment give natural reconfiguration structure on an infinite, classical cubic family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
