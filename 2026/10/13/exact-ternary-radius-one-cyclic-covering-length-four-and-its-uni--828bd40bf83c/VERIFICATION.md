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

Each radius-one Hamming ball has 1+4(3−1)=9 targets, so every cycle of length at most 8 is excluded, including cycles shorter than the window length. In a fresh exhaustive calculation I generated the balls by changing one ternary digit and used rolling base-three indices to visit each cyclic window, including wraparound. The 19,683, 59,049, 177,147 and 531,441 indexed sequences at lengths 9–12 give 0,0,0,48 full covers, with largest coverage sizes 69,76,76,81. The explicit length-12 witness is in the census. Constructing every uniform symbol relabeling and rotation of the witness and of its reversal gives two disjoint orbits of 24 whose union is exactly the full census. Adding reversal exchanges those orbits. The one-orbit statement is for the positional dihedral group together with uniform relabeling, not the positional dihedral group alone.

## originality

PASS

The closest inspected literature has the same cyclic object, binary finite tables, general bounds, or a constacyclic Hamming construction at these exact ternary span and radius parameters. Etzion's paper also explicitly describes how to merge constituent cycles, not just how to construct separate ones. Its merge retains all original windows, and the Hamming construction for these parameters supplies nine pairwise distance-at-least-three centers. Independent checking finds that not even four such centers occur among the windows of any optimal length-12 cycle. Thus that construction, specialized as given, does not supply the length-12 witness, let alone its optimality or the census. The closest indexed classification match is for binary span seven and is not implication-equivalent.

## value

PASS

Span four is the first nontrivial ternary radius-one perfect Hamming parameter: an unrestricted cover needs only nine centers, attained by the kernel of a ternary parity-check matrix with one column from each of the four projective directions in dimension two. Requiring the centers to occur on a single walk of overlapping windows raises this to exactly 12, a sharp one-third overhead. At this natural benchmark the equality description distinguishes the effect of reversal and identifies the unique full-symmetry type. This answers a concrete finite comparison not supplied by the sphere bound or the multicomponent construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
