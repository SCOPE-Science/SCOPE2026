---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently generated the incidence relation in reverse: for each seven-bit output and each of its seven coordinates, replace that output bit by each of the four binary pairs. Transposition gives exactly the claimed forward channel, including positions at either end. All 256 received sets have eight outputs. The 14-word witness uses 112 different outputs; the XOR span of 21, 79 and 164 produces eight different words with 64 different outputs. An independent integer-mask search rules out 15 without relying on the reported C++ run or on a floating-point optimizer. It splits by the least codeword x, and restricts the rest to words above x that avoid every output of x. In each search state it partitions candidates into classes with a shared received word, so a packing may use at most one member of each class. It branches on taking each next candidate in reverse class order, removes that word from remaining sibling branches, and removes all incompatible inputs when taking it. Fewer live classes than required words makes a branch impossible; otherwise every possible packing follows the branch of its first chosen word in that traversal. The run returned no size-15 packing for all possible least words, visiting 49,429 states. This proves the exact unrestricted maximum 14; binary linear cardinalities are powers of two, so the exhibited dimension three is optimal. The frozen C++ search has a valid analogous coloring/pruning invariant; its node count and the auxiliary MILP are not needed for the independent decision.

## originality

PASS

Prior work already defines this channel, gives correcting constructions and proves the constant ball size and packing bound. The checked prior results and exact tables do not determine the unrestricted optimum 14 and its gap to the exact linear optimum 8. The pass is for those optima and their gap, not the constant size of the balls or existence of channel-specific constructions.

## value

PASS

Length eight is a natural short-block benchmark: the constant ball count n means perfect binary (2,1) packing requires n dividing 2^(n−1), hence a power of two. The trivial length-two case is perfect, and 0000 and 1111 are perfect at length four (their distinct outputs have weights at most one and at least two, respectively). Length eight is the next possible perfect length by divisibility. The calculation resolves two concrete issues there: attainable packing is exactly two codewords short of the perfect bound, and linearity further reduces the best size from 14 to 8. The result is useful as an exact benchmark, without extrapolation to other lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
