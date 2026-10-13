# Scientific assessment: cone-image rigidity and bounded-morphism rank spectra

## Correctness — PASS

The proof uses precisely the bounded-morphism (monotonicity plus back) definition, never ordinary monotonicity alone. Cone-image equality is equivalent to those requirements; the root's entire successor cone is the domain. The first-level decomposition is disjoint and exhaustive: a source child landing at the target root already covers every target node, while if none does, each immediate target child must be realized by a distinct source child. The two cases give the stated recurrence. The idempotent proof fixes the entire image cone pointwise and forces the spine to be constant at its root; side branches are independent and satisfy back conditions because the fixed cone already supplies every target descendant above each spine vertex. The zero-height and equal-height boundary cases are explicit. Exhaustive function-table checks through the binary seven-vertex frame agree with the recurrence and show the height-two closed forms are correctly normalized. The general theorem rests on the structural proof, not on finite testing.

## Originality — PASS (provisional literature comparison)

The closest primary paper, Goldblatt–Hodkinson (arXiv:2207.12596v1, July 2022), has primary MSC 03B45 and develops finite-width/achronal-width modal logic and canonicity. Its complete HTML text was inspected for endomorphism and p-morphism topics, the finite-frame semantics sections and the finite-width sections; it does not present a recursion or census of bounded endomorphisms on regular rooted frames. Almeida–Bezhanishvili (arXiv:2406.10649v1) develops p-morphism-based coalgebraic semantics and recovers the known categorical principles but does not specialize to the two rank-polynomial enumerations. Bezhanishvili et al. (arXiv:2103.02530v1) discuss finite Esakia duality, whose general theorem makes these maps algebraically relevant but does not itself imply the explicit coefficients. Several searches for finite rooted-tree bounded endomorphism counts and p-morphism rank spectra, plus semantic searches of mathematical-result records and the current cumulative ledger, uncovered related but not dominating findings. Standard automorphism wreath-product counts are deliberately treated as antecedents. A hidden or unindexed enumeration remains plausible; this is not a claim of exhaustive bibliographic priority.

## Value — PASS

Bounded morphisms, rather than arbitrary order-preserving functions, preserve modal truth under pullback and are the morphisms of finite Esakia-style duality. Complete rooted trees are canonical test frames of controlled width and depth. The theorem supplies an all-height exact count for every possible image rank and for idempotent retracts, identifies a strict noncontiguous rank support, and supplies closed height-two formulas with nontrivial counts. It distinguishes endomorphisms from automorphisms, addresses image classification and idempotence in a natural model-theoretic category, and is not merely a familiar Bell/Catalan sequence relabelled. It does not claim a complexity-theoretic consequence, a modal completeness theorem, or a formula for nonuniform trees.

## Risks and bounds

The remaining risk is an unindexed or implicit prior count of bounded morphisms of finite regular tree frames; the identified primary literature does not resolve it. Independent proof review has not occurred. The calculations are exhaustive only for the listed small frames, and exact generality follows from the elementary but nontrivial two-case decomposition. All cited dates refer to first public preprints rather than later journals.

Self-review: passed. Independent audit: not yet performed.
