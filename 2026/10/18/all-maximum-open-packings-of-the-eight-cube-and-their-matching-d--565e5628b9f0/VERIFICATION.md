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

Each parity half contains at most sixteen centers because their disjoint open neighborhoods have eight elements each and lie in the opposite 128-vertex half. Appending the parity-determining bit to a seven-word maps distances 1,2 to distance 2 and all larger punctured distances to at least 4; distinct centers on one side have a common neighbor exactly at distance 2. Thus equality on each side is a length-seven 1-perfect code, by radius-one ball size, and the punctured even/odd pair is unique relative to the stated coordinate. The two sides do not conflict. Every selected vertex has exactly one selected neighbor because a maximum packing partitions the whole cube by open neighborhoods; this induces a matching. A zero-containing perfect code has seven weight-three words covering each pair of coordinates once. Their Fano lines exclude 28 distinct four-subsets; coverage of the 28 other weight-three words forces the seven line complements. A weight-five or weight-six vector is respectively at distance one or two from a line complement, leaving the all-ones word as the last codeword. The unique Fano plane up to labels has 7!/168=30 labels, and the corresponding parity-check kernels each have eight cosets. Thus there are 240 possible codes per side. For affine codes a+U,b+V, the edges in a direction count an affine intersection (shift by one punctured basis vector, or no shift for the appended direction), so each nonzero count is 2^dim(U∩V), with sum 16. The intersection consists of zero, all-ones and the weight-three/four complementary words associated to common lines; the allowed shared-line counts are 0,1,3,7. For fixed F, the zeroth, first, second binomial moments across F' are 30,42,42 (six planes per triple, two per intersecting pair), with one self-intersection. This gives frequencies 8,14,7,1; multiplying by 8 cosets and 240 first codes gives the profile table and identifies the 1920 one-direction fibers. Independently, python3 /tmp/opencode/q8_frozen_review_exact.py enumerated all 240 exact covers directly on the even half using 256-vertex neighbor bit masks, a deterministic uncovered-point choice, and every currently disjoint incident block. Translation by one coordinate produces all odd covers. Direct neighbor tests of all 57600 pairs reproduced 1920,13440,26880,15360 and confirmed the matching for each. The replay uses no Fano or perfect-code assumption; saturation proves its exhaustion of the maximum packings but it is not a claim about smaller packings or automorphism orbits. The frozen script/output were inspected, not executed.

## originality

PASS

The prior scalar 32, existence of a fiber-form optimum, and classical seven-bit perfect-code ingredients are not credited as original. The simple ordered-pair size product by itself is not the basis for the pass. The core distinction is the complete direction-resolved classification of optimum vertex subsets, including the exact sizes and relative frequencies of non-fiber profiles, furnished by connecting matching intersections with the Fano overlap moments. No inspected prior statement covered that classification or supplied that implication; one potentially relevant older paper remains uninspected in full.

## value

PASS

The cube coordinates give a natural invariant of an induced matching, with sorted profiles unchanged by cube automorphisms. The profile classification distinguishes the known fiber optima from the much larger non-fiber population and shows that all active directions carry equal multiplicity, with only four possible support sizes. These exact counts answer which extremizers can occur in a natural optimum problem, and the affine-intersection explanation makes this a structural finite classification rather than a recalculation of the scalar bound or a census without a reason for its statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
