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

For a weight-two support (a,b), deleting one of its two ones yields weight-one output positions a and b-1: adjacent words consume one distinct weight-one descendant, separated words consume two. For any code with t adjacent and s separated supports, t+2s≤n-1. Adjacent starts cannot be consecutive because then their zero-deletion weight-two shadows collide, hence t≤floor(n/2). Thus |C|≤floor((n-1+floor(n/2))/2)=floor((3n-2)/4). The proposed even-start adjacent and mod-four spaced pairs consume disjoint weight-one descendants; their zero-deletion output pair distances and first-coordinate residue blocks prevent all weight-two collisions. The construction attains the bound for all n, including short boundary n=2,3. Independent exhaustive single-deletion shadow simulation validates n=2..45; independently computed exact compatibility-graph independence numbers for n=2..8 match the formula. Infinite conclusion comes from analytic shadow argument, not finite tests. The modified-VT color size ceil(n/2) for n≥4 is a separate residue pairing count; compare same Hamming layer.

## originality

PASS

Published constant-weight modified-VT optimal coloring is a different graph invariant from the all-n maximum independent set; the exact weight-two alpha and larger explicit construction were not located in inspected primary sources, with a concrete thesis-overlap risk.

## value

PASS

Maximum cardinality in a fixed-weight zero-error deletion channel is a natural coding-theoretic invariant. The complete exact all-blocklength formula and explicit optimal code separate optimal colorings from maximum independent sets with an asymptotically 3/2 gain over a standard construction; substantive despite the specialization to weight two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
