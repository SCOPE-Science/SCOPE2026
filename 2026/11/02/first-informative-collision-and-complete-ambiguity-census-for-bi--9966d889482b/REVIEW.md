# Scientific review

## Correctness
**PASS.** Define the observation as all fourteen exact embedding multiplicities for patterns of lengths one, two and three with consecutive indices at least three apart. Appending the final symbol splits the valid embeddings into those omitting it and those ending there; the latter correspond bijectively to prefix embeddings ending no later than three positions earlier. The derived exact recurrence is used to visit every binary prefix through length seventeen. The standalone executable checks the full fiber census (including absence of triple collisions), verifies the sixteen enumerated pairs, and proves that simultaneous reversal/complement partition them into four size-four orbits. Direct literal enumeration separately checks all 1920 words of lengths seven to ten and all sixteen collision pairs. The exhaustive finite result is not asserted to hold at larger lengths.

## Originality
**PASS, with residual literature risk.** Golm, Nahvi, Gabrys and Milenkovic, *The Gapped \(k\)-Deck Problem* (arXiv:2201.12671), introduce this type of observation but present explicit small values for two-separated decks and a general upper bound. Their instance \(G_2(3)=13\) is a different gap constraint; their general bound at separation three and pattern length three is \(41\), not the exact informative minimum \(17\). Day, Kosche, Manea and Schmid (arXiv:2206.13896) consider sets of gap-admissible patterns and matching/equivalence complexity, not complete multiplicity-fiber counts. Targeted searches for the three-separated threshold, aliases and matching exact tables located no dominating statement. This negative search is not proof of global uniqueness: an unindexed or synonymously formulated finite census remains a risk.

## Mathematical value
**PASS.** The first point where length-three, gap-three multiplicity observations stop uniquely identifying binary sources is a natural reconstruction boundary, motivated by the gapped-deck literature. The complete first-failure partition and symmetry taxonomy go beyond isolated witnesses and identify the precise information loss at the boundary. It is finite but not an arbitrary slice: every shorter informative length is certified injective. The restriction to the informative range is essential.

## Limits of the review
The proof is a reproducible exhaustive finite certificate, with no independent human audit and no conclusion about lengths beyond seventeen. The primary paper's short-length convention and vacuous small lengths are not silently treated as informative. Any equivalent unindexed prior result could alter the originality assessment.

Self-review: passed. Independent audit: not yet performed.
