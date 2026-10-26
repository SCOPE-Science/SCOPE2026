# Scientific review: reachable-colouring code of signed stars

## Correctness

**PASS.** The exhaustive structural argument has only two possibilities for its first ignition. Igniting the centre forces all spokes in round two. Igniting a leaf forces the centre in round two, then allows one other leaf to be ignited, while all remaining leaves burn in round three. This proves both directions of the exact reachable-set characterization for every number of leaves, including the separate \(n=1\) boundary. The polynomial follows by counting distinct reversed-leaf positions. The covering-radius proof maximizes an explicit two-centre-choice Hamming distance over all possible disagreement counts, and the worst-signing consequence uses the already established switching correspondence of [1]. A direct standard-library finite-state simulator checks every signing through seven leaves, without being used as a substitute for the infinite proof.

## Originality

**PASS under the inspected evidence, with residual bibliographic risk.** [1] defines the signed-burning process and gives the general switching/covering-radius identity; these are not claimed as new. Its exact-parameter calculations are for signed paths, not branching stars. Its full accessible text, including the statements of Sections 2 and 3 and the research questions in Section 5, does not provide a signed-star reachable-colouring code, full final-colour enumerator, exact plurality for each signing, or star-specific covering radius. The star calculation requires the explicit two-ignition reachability classification. Related ordinary burning-time and adversarial-burning results use different parameters and cannot supply the final signed colour profile. Exact database and literature queries by the terms in [1] and common alternate terminology did not identify a stated equivalent. Lack of a match is not proof of universal novelty; unindexed results remain possible.

## Mathematical value

**PASS.** The founding paper [1, Section 5] explicitly identifies exact plurality values for classes of signed trees and links to covering radii as worthwhile extensions. Stars are the first naturally branching tree family, not an arbitrary parameter slice. The result gives a complete classification of reachable final colourings and their entire weight distribution for all sign patterns, as well as an exact covering radius and a sharp signed-tree worst case. In contrast to a single small-order example, it identifies a concrete one-leaf-correction mechanism and its dimension-dependent worst-signature loss. It does not purport to settle arbitrary signed trees or produce a general-purpose algorithm.

## Scope and residual risks

The combinatorial proof applies to every labelled finite signed star, using synchronous spreading before ignition with burned colours fixed. The verifier checks orders up to eight vertices. The unrestricted proof is theoretical. Distinct process histories may coincide as final colourings; the result deliberately counts configurations, not histories. Publication-priority uncertainty persists for unindexed or alternative-terminology treatments; an external mathematical audit has not yet been performed.

## References

[1] S. Fallat, H. Gupta, K. Khodamoradi and S. Zilles, *Burning Signed Graphs*, arXiv:2610.02506 (first posted October 1, 2026), especially Sections 2, 3, 5. https://arxiv.org/abs/2610.02506

[2] A. Bonato, *A survey of graph burning*, Contributions to Discrete Mathematics 16 (2021), 185–197. https://doi.org/10.55016/ojs/cdm.v16i1.71194

Self-review: passed. Independent audit: not yet performed.
