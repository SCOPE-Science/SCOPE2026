# Scientific review: bounded-morphism rigidity of finite layered orders

## Correctness
PASS. The proof compares preimages of two incomparable target points to show that an entire target level has preimage in a unique source level. The upward back condition, applied to an alternative point of a higher target level, forces different target levels to use strictly increasing source levels. Exhaustion of the source by nonempty levels then proves equality of heights, level correspondence, and the converse by direct verification. Standard surjection counting gives the Stirling product. The singleton-level construction proves the exact boundary of the uniform hypothesis. The independent brute-force enumeration in `artifacts/verify.py` checks 181 small configurations and a singleton-target witness. Enumeration is supportive, not the proof.

## Originality
PASS, with a residual literature risk. Pouzet–Zaguia study weak orders and monotone endomorphisms, not p-morphism back conditions. Rzążewski–Stronkowski study the general NP-hard bounded-morphic-image decision problem but do not state the closed layered-order classification. The 2024 pseudosphere paper studies joins/topological structure. Three closely related publicly available 2026 results describe ordinary mapping-space counts and homotopy, not surjective bounded morphisms; their conclusions neither explicitly state nor directly imply the levelwise quotient classification. Actual semantic research-record searches and published-primary-text comparisons included alternative terms p-morphism, bounded morphism, weak order, complete multipartite order, ordinal sum of antichains, and surjective quotient. Specialized unindexed frame literature could contain an equivalent statement.

## Mathematical value
PASS. The theorem gives a **complete** p-morphic-image preorder and an exact labelled morphism census for natural finite pseudosphere/complete multipartite frames, with a sharp condition identifying when height is invariant. It makes an otherwise generally difficult Kripke-frame quotient decision problem directly decidable from the level vectors. This is more than an arbitrary instance count or a restatement of the ordinary monotone-map enumeration. The boundary phenomenon at singleton target levels explains exactly why the level-rigidity mechanism requires nontrivial antichains.

## Limitations and comparison
The theorem does not cover singleton target levels, infinite posets, non-surjective bounded morphisms, or general finite frames. Its novelty claim is qualified by the possibility of older specialist results not indexed by the searched terms. The finite verifier cannot replace the quantified proof, and independent external review has not occurred.

Self-review: passed. Independent audit: not yet performed.
