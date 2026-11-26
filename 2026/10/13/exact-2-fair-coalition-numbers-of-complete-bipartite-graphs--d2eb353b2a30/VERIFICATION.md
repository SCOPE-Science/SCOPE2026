---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Directly from the neighbor counts, a set of occupancy (a,b) is fair iff (a=s or b=2) and (b=t or a=2). For s,t>2 every proper fair union is (2,2), and no fair set of size 2 exists. Thus a partition with at least three blocks must use complementary occupancies (0,1)-(2,1), (1,0)-(1,2), (0,2)-(2,0), or two distinct (1,1)-blocks. For s>=4 the excess E=sum(|B|-1) is at least 4: no singletons gives E>=ceil((s+t)/2), both singleton types force two distinct triples, and a single singleton type forces a triple taking two vertices from the opposite shore. With E<=3 the only way to supply the two remaining opposite-shore vertices would be a doubleton on that shore; its required opposite doubleton costs another unit. The two complementary triples with singleton tails attain E=4. For s=3, a block taking two X vertices makes the block containing the remaining X vertex unpartnerable. All blocks then take one X vertex, so there are three, and a self-complementary (1,1) pair cannot occur alongside a mixed family requiring two further X vertices. All (1,1) gives t=3; the (1,0)/(1,2) mix gives t=4, since its only other possibility gives t=2<s. For s=2<t, every proper fair set contains all of X: splitting X between blocks strands all other blocks, while keeping X together makes its block fair and hence unusable as a partner. For K_2,2 the four singletons work. For s=1 the only proper fair set that can occur is Y when t=2, and then the X-vertex's block cannot participate in any proper fair union or be a fair block. Two-block constructions for the residual cases are X,Y when neither has size two, {x1}, {x2} union Y when s=2<t, and X union {y1}, {y2} when (s,t)=(1,2). Each uses two nonfair blocks whose union is all vertices. Read RESULT.md, VERIFICATION.md and verify.py without executing the supplied script. Independent occupancy-multiset enumeration matched all 36 profiles with s+t<=12 (`python3 /tmp/opencode/frozen_math_replay_1_2_4.py 2`); the proof, not the finite check, covers all sizes.

## originality

PASS

The initiating fair paper already covers the degenerate ranges and provides upper bounds in the main regime. The distinct exact results are the small-shore transitions at s=3,4 and the matching constructions for s>=5. Neither the ordinary at-least-two coalition theorem nor the 1-fair theorem determines this parameter. No exact equivalent was established in the checked sources.

## value

PASS

This determines an entire natural graph family where the initiating theorem gives only bounds. In particular, a strict one-block deficit at s=4 and a drop from three to two blocks at t=5 on the s=3 line show where the known bounds fail. The occupancy/complementarity obstruction and matching construction also explain the exact transition to the sharp large-shore formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
