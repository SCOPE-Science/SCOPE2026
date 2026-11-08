---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

All perfect matchings of Q5 correspond bijectively to a perfect bijection from 16 even vertices to 16 odd vertices satisfying Hamming-one adjacency; a depth-first assignment of unused odd partners enumerates each exactly once. Legal square flips are precisely swaps of two even-vertex partners when both cross edges exist; this is exhaustive for every four-cycle move (not long even alternating cycles). Exact disjoint-set traversal over every enumerated state and swap gives N=589185, 3,219,360 reconfiguration edges, component sizes (1×120,4×80,99280×1,489465×1), component edge totals 0,320,359680,2859360. Independently implemented fresh C++ enumeration from source logic, recompiled and executed, reproduced all state/edge/component and degree sums. Four-vertex components are C4 by degree 2, and every move flips the partner permutation sign, giving bipartiteness. Read the separate Python original, which enumerates 80-bit matching-edge subsets and applies all 3840 bit-translation/coordinate-permutation automorphisms to verify two stated exceptional orbits; orbit check not independently reexecuted, with exact scope made explicit. This is truly exhaustive finite n=5, not evidence for n≥6.

## originality

PASS

Static Q5 matching total 589185 was known (Graham–Harary; Östergård–Pettersson). Bonamy et al. study general square-flip reconfiguration complexity; Klivans–Saldanha establish a twist invariant and component phenomena for other high-dimensional boxes, including a 99,280-size component in a different 4D box with 36 cells, which is NOT the 32-vertex five-cube Q5. Hartarsky et al allow longer alternating-cycle moves and cannot imply square-only components. No read primary source supplies the exact 202-component Q5 census, although specialized tiling tables remain a qualified priority risk.

## value

PASS

Exact components, frozen exceptional orbit and giant-component sizes under the most local natural matching switch resolve a sharp finite Q5 reconfiguration invariant. The two large components coexist with 200 small ones; distinguishing square-only flips from larger even-cycle transformations matters for Markov-chain connectivity and tiling geometry. A natural complete finite classification remains mathematically valuable without claiming all dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
