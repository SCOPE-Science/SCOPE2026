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

The five cases hold with open neighborhoods and the whole cyclic vertex set as both sample ground set and center set, including radii above the diameter. In the complete case a two-point set cannot have an empty trace; at n=2r+2 an empty trace would require an antipodal pair, which has no singleton trace. At n=2r+3, multiplication by the inverse of r+1 converts complements to consecutive triples: a full three-point trace would require one such triple and its endpoints cannot occur without its midpoint. For n>=2r+3 the pair {0,r+1} has all four traces. In the four-point obstruction each membership bit has four change positions, with the two center-hole transitions consecutive. Sixteen different traces would force sixteen runs with precisely one changed bit at each boundary; the consecutive flips undo each other and repeat a trace in separate runs. At r=2, n>=9, requiring the full trace reduces the candidate triple to a subset of {-2,-1,1,2}; the witnesses for joint inclusion of the designated pair are confined to center 0, where the third vertex is also included. The wrap-around distances in the two uniform witness tables give their eight stated traces up to and including n=3r+2 and starting at n=3r+3, respectively; the C8 square witness checks directly. The fresh replay matched 297 pairs (3<=n<=24, 1<=r<=n) and the eight-trace witnesses on 295 pairs (3<=r<=12, 2r+4<=n<=5r+10). This is finite corroboration of the symbolic proof, not its basis.

## originality

PASS

No equivalent or dominating result was found in the inspected sources. The assessment credits only the exact fixed-radius open-neighborhood classification, not publication priority.

## value

PASS

A canonical graph family gives a complete exact benchmark for the effect of removing the center from a circular ball. In particular the square changes from three to two between n=8 and n=9, unlike the stable higher-radius regime. The center-hole argument explains an obstruction that the generic transition budget alone does not, and the exact witnesses distinguish every boundary without a cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
