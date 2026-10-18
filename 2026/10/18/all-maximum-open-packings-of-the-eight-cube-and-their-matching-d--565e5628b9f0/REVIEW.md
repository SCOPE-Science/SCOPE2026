# Scientific review — maximum open packings of the eight-cube

## Correctness: PASS

The statement counts labeled vertex subsets, not automorphism orbits. A packing has at most sixteen vertices in either parity half, because their eight-element open neighborhoods cannot overlap within the opposite half. Saturation turns the two parity halves into independent length-seven radius-one perfect codes. The ordered-pair correspondence is bijective. The code census is reconstructed from the seven weight-three codewords and their forced Fano triple system; the only sixteen-word code extending such a system is its affine Hamming code, giving thirty underlying linear codes with eight cosets each. The local matching follows from the unique nearest codeword of a perfect code. Direction multiplicities arise from intersections of affine cosets of dimension-four subspaces; the Fano-line intersection census has distribution \((1,7,14,8)\), hence the four stated profile counts. The proof checks all boundary and uniqueness assertions, including the all-one word in a centered code.

The included verifier independently enumerates the thirty labeled Fano systems by exact cover, recovers all 240 perfect codes, checks the intersection distribution, and explicitly validates all 240 open packings and their matching profiles for a fixed first code. The factor of 240 for the complete labeled enumeration comes from the proven transitive action, not an unverified extrapolation. Finite checking does not constitute a separate proof of the bijection or the general completeness argument.

## Originality: PASS

The closest primary article, Brešar–Klavžar–Rall (arXiv:2309.04963v1), already supplies the numeric maximum \(\rho^{\mathrm o}(Q_8)=32\), the prism packing equality and a reduction to the existence of a product-form maximum. It does not enumerate all optimal vertex subsets or determine directional induced-matching profiles; existence of one product-form maximum does not classify the non-product optima. Brešar–Samadi–Yero (arXiv:2106.09823v2) treats injective colorability but not these extremizer statistics. Classical Fano and Hamming classifications are deliberately used as prior inputs, not passed off as new. Searches under alternative coding, graph-theoretic and matching terminology did not reveal an equivalent complete census or profile distribution. The possibility of an unindexed or differently named equivalent coding classification is a residual risk, not a claim of proven universal novelty.

## Value: PASS

This gives a complete, natural and nontrivial enumeration for a canonical eight-dimensional hypercube, one of the first dimensions with a genuinely rich family of maximum open packings. Beyond the previously known optimum size, the result says every optimal set induces a perfect matching in one of exactly four direction-support patterns, quantifies each class, and exhibits that \(29/30\) of all optima are not doubled-code fiber constructions. The Fano-plane intersection distribution explains the counts structurally. The conclusion is specific to dimension eight and does not imply an unbounded-dimensional theorem, but a complete finite extremal classification with a motivated structural invariant has mathematical value on its own.

## References and limitations

The primary source's exact-number theorem and product existence theorem are preserved and distinguished from the new classification; supporting code and Steiner-system facts are independently derived in the proof. Unindexed equivalences and possible prior coding-theoretic enumeration remain scientific originality risks. This document reports a self-review only.

Self-review: passed. Independent audit: not yet performed.
