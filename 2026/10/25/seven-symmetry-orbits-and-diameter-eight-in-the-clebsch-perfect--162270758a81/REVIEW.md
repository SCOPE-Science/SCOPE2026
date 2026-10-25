# Review: Clebsch perfect-matching flip graph

## Correctness (PASS)
The graph is defined on all sixteen four-bit vectors with five XOR generators. Exact first-free-vertex recursion enumerates precisely 705 perfect matchings; a second independent implementation obtains the same set size. For all 705 choose 2 pairs, a four-edge symmetric difference is equivalent to one alternating quadrilateral. Cross-pairing and symmetric-difference constructions give identical adjacency and exactly 2160 transitions. Exhaustive breadth-first search from **every** configuration yields connectedness, radius 7, diameter 8, five centers, and 8840 diameter pairs. The 1920 automorphisms are proved complete by the five-neighbor stabilizer and explicit translation-linear action; the seven exhaustive orbits and their patterns are checked. Both supplied verifiers passed on their complete source files. These are finite exhaustive proofs, not infinite generalizations.

## Originality (PASS, with residual risk)
The Clebsch matching-complex record already states 705 perfect matchings; the dimension-four prescribed-difference record gives full direction-profile multiplicities. Neither gives flip adjacency, all-pairs distances, geodesic centers or the distinction between orbit types of equal direction profile. Dyer–Müller (arXiv:1705.05790) and Bonamy et al. (arXiv:1904.06184) describe four-cycle switches and broader reconfiguration questions without this exact finite metric. The primary texts and published matching-count claims were materially inspected. Searches additionally used Clebsch, folded five-cube, Greenwood–Gleason, projective cube, switch, and four-cycle flip variants. Publication priority remains uncertain because differently phrased or unindexed calculations may exist; the originality judgment concerns the complete, currently unsupported implication from known results to the new exact 705-state geometry.

## Value (PASS)
This canonical strongly regular graph is a natural benchmark for matching-exchange dynamics. Knowing only how many perfect matchings exist provides no information about path lengths or local mobility; the sharp diameter eight, radius seven, five canonical centers and seven full-symmetry chambers give structural information relevant to navigation by legal local moves. No large-family or mixing-time claim is made.

## Limitations
Finite graph only; exact 705-state enumeration and full shortest-path computation are required. The scalar 705 matching count and XOR-difference multiplicity spectrum are prior knowledge, not claimed discoveries. Possible equivalent unindexed work remains a specific originality risk. There is no independent audit or external verification.

Self-review: passed. Independent audit: not yet performed.
