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

The eleven edges are exactly the stated join, with vertex 0 isolated in its original three-vertex part. Independent enumeration tested the outside-neighbor and proper-subset conditions on all 64 masks and recovered eight rooted triples and the six rootless minimal forts 24,15,123,134,235,345. Testing the 32 peripheral masks recovered the stated 17 admissible masks, with counts (2,3,8,4) by root-neighbor count. For a global fort omitting 0, each nonempty peripheral intersection is admissible. Those with count 1 contain 24; those with count other than 1 are themselves local rootless forts and contain a local minimum. These local minima remain forts and remain minimal in the bouquet, so any minimal rootless global fort lies in a single petal. For a fort containing 0, restrictions are independent rooted local forts. There is no rooted fort of size at most two, and the only pairs not completing a rooted triple are 15 and 24, so every rooted fort contains one of the eight triples. Hence each global rooted minimum must use one such triple per petal. The unions are minimal: keeping 0 would require keeping each whole triple, and dropping it leaves subsets of the selected pairs, none of which has a nonempty peripherally admissible subset. This proves 8^k+6k for all k. The independent enumeration did not execute the supplied checker; the supplied 14,76,530 are recorded corroboration only. Taking roots with |V|=5k+1 gives the exact subsequence limit 8^(1/5), strictly above 3^(1/3); no all-orders or extremality result is claimed.

## originality

PASS

The broad claim that a connected family can exceed the windmill base is already indexed and is not credited as original. The supported distinct claim is the explicit shared-root, five-new-vertices petal, its exact split count and the larger base 8^(1/5), not a first resolution of faster-than-windmill growth.

## value

PASS

The numerical improvement over the indexed cocktail-party benchmark is small, but has a structural reason: rooting inside the petal rather than adding a universal hub yields eight independent local choices per five new vertices; the rootless admissibility analysis prevents combinations spanning petals from generating spurious minima. The exact family and split give a useful stronger lower bound in the motivated connected extremal problem, without assuming all better examples must take this form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
