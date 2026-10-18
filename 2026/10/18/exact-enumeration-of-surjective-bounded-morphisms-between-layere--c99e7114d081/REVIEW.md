# Scientific review

## Correctness
The claim is a precise count of surjective maps satisfying the equality of complete upward-successor images. The proof partitions maps by the final target antichain size. With at least two terminal target points, the last source level must map onto them and can be peeled off. With a singleton terminal target, the unique final source level containing a lower-target image yields an invertible decomposition into a selected terminal subset plus a lower-prefix bounded morphism. These bijections justify both recurrence tables, including zero-size boundary conventions and singleton cases. A separately implemented brute-force program agrees with the recurrence on 687 parameter pairs, and six additional arithmetic anchors agree. The enumeration is corroborative, not a substitute for the general proof.

## Originality
The 2011 coalgebraic overview supplies the frame-morphism equation but not the weak-order enumeration. The published cardinality recurrence for weak-order mapping spaces counts *all* order-preserving maps, lacking both surjectivity and upward-back restrictions. Published finite-space homotopy-class formulas also do not count this map class, especially with singleton target levels. Exact-phrase, alias, equivalence, broader-coverage, database and implication searches yielded no dominating statement. One plausible surjective-homomorphism paper could only be inspected at the abstract level, so a hidden equivalent under alternate terminology remains possible.

## Value
Surjective bounded morphisms are the natural quotient maps of Kripke frames: they require the source successor set to cover every target successor, not merely preserve reachability. An exact count for all weak-order level vectors, with one auxiliary subset state, resolves the interplay between nontrivial antichain levels and singleton gates. This provides a reusable counting method and a structural rigidity consequence for frames lacking singleton levels; it is not just a small-instance census or a restatement of unrestricted order-preserving map enumeration.

## Scope and remaining risks
The theorem assumes finite labeled ordinal sums of nonempty antichains with reflexive accessibility, no extra valuations, and onto frame maps. Complexity is measured in table operations after computing surjection weights, not bit operations. The author manuscript of Huczynska and Ruškuc was unavailable through the attempted public access route, leaving a limited residual literature risk. Other unindexed equivalent formulas cannot be categorically excluded.

Self-review: passed. Independent audit: not yet performed.
