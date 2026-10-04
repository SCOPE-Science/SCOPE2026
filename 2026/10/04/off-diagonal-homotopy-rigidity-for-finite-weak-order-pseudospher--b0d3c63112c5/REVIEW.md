# Review

## Correctness
PASS. The proof reduces every nonspecial map to a contractible image by tracking the least and greatest target levels met by each source level. A shared boundary level forces a singleton image there; avoiding singleton occupied levels forces the separated level intervals to use exactly one target level each, hence exact level preservation. Isolation follows from downward and upward induction using the presence of at least two images in each adjacent target antichain. The class count is then a product of nonconstant-function counts. The top-homology rank follows from the join decomposition and the rank of the induced map on reduced degree-zero homology.

The computation exhaustively checks four unequal source-target examples, but the infinite family rests on the symbolic proof rather than enumeration.

## Originality
PASS. The closest inspected finite-space source supplies the poset homotopy framework, not this mapping classification. The inspected Hom-poset paper treats Möbius functions, the pseudosphere source identifies the objects and their order-complex structure, and the inspected ordinal-sum endomorphism paper treats polymorphism/endomorphism questions rather than off-diagonal homotopy classes. Existing nearby results checked for overlap cover arbitrary height only on the diagonal, or arbitrary source and target only in height two. Neither implies the unequal-source/unequal-target theorem for height at least three.

Residual risk remains that an equivalent formula appears under different terminology for finite spaces, weak orders, or pseudospheres; no such statement was found in the checked sources or semantic searches.

## Value
PASS. The theorem closes a natural structural gap between diagonal arbitrary-height rigidity and off-diagonal height-two mapping results. It gives a complete exact homotopy-class count for arbitrarily varying unequal level sizes in every height at least three, together with a top-homology rank formula. This is not a single numerical extension or a parameter-table recomputation: it identifies the mechanism—singleton boundary levels versus rigid level preservation—that governs the whole off-diagonal family.

## Closest literature and limitations
The central framework is Barmak–Minian, arXiv:math/0611156. Speed studies the Möbius function of the order-preserving-map poset; Alberto identifies pseudospheres with ordinal sums of trivial posets; Kunos–Larose–Pazmiño Pullas study endomorphism and polymorphism properties of ordinal sums of antichains. The theorem does not address unequal heights, singleton levels, or the full homotopy type of the non-isolated mapping-space component.

Same-model review: passed. Independent audit: not yet performed.
