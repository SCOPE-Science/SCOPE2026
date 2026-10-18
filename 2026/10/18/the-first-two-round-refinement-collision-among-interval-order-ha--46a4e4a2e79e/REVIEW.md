# Scientific review

## Correctness — PASS

The exact domain consists of all finite nonempty interval orders of cardinality at most eight, encoded only by their directed cover relations. The classical Fishburn correspondence makes enumeration by upper-triangular nonnegative integer matrices with positive row and column totals exhaustive and isomorphism-free. The verification code generates all positive row-sum weak compositions, filters exactly the necessary column constraints, expands each cell, derives strict interval precedence, and removes an arc precisely when a genuine intermediate element exists. Directed refinement counts incoming and outgoing vertex colours separately, uses canonical nested signatures with no hashing, and groups complete multisets. The counts are 1, 2, 5, 15, 53, 217, 1014, 5335 types and 1, 2, 5, 15, 53, 217, 1014, 5333 two-round fingerprints. Two pairs of size two are the only collisions; a third round distinguishes each pair. Independent maximal-element extension enumeration and brute-force witness isomorphism checking reproduce the relevant conclusions. The finite search is a complete proof once the cited classical encoding and these inspectable elementary loops are accepted; it does not extrapolate to larger inputs.

## Originality — PASS (qualified)

Targeted searches of primary literature and research records did not identify the exact two-round directed Hasse-graph collision classification. Dukes et al. and Jelínek establish the Fishburn encoding and interval-order background, not this finite refinement-depth census. Krebs and Verbitsky discuss depth and counting colour refinement for general graphs, not this sharp interval-order cover-layer result. The closest accessible historical work on finite poset refinement studies other poset families or the full strict order relation; neither formulation implies the present cover-arc classification. Earlier specialized small-order tables remain a publication-priority risk; no independent novelty certification is asserted.

## Value — PASS

Cover relations are a standard economical encoding of a finite poset; two rounds of incoming/outgoing counting are a natural fixed-depth local invariant. The finding establishes the first order where that invariant loses isomorphism information on an entire classical combinatorial family and classifies **every** ambiguity at the boundary, not just one example. Its precise dual pairing and sharp separation by a third round explain the first nontrivial refinement-depth transition. The finite cutoff is mathematically forced by minimality rather than chosen arbitrarily. No general theorem or larger-order claim is needed for the exact first-obstruction classification.

## Prior work and residual limitations

The matrix normal form and Fishburn numbers are classical and explicitly credited. Directly inspected sources: arXiv:1006.2696, arXiv:1501.05157, arXiv:1407.3175; benchmark OEIS:A022493. The claim is restricted to oriented cover predicates and orders with at most eight elements. Specialized unpublished or unlocated earlier enumerations remain possible.

Self-review: passed. Independent audit: not yet performed.
