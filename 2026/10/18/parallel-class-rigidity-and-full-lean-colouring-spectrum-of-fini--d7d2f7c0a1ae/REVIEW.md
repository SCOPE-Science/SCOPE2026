# Scientific review: parallel-class rigidity of affine-plane lean colourings

**Correctness — PASS.** The proof explicitly uses the affine-plane axioms and the nontrivial restriction \(q\ge3\). A repeated pair lies on a monochromatic line. If two such lines meet, choosing a fourth available direction through every external point propagates that shared colour to the entire plane; nonconstant colouring rules this out. Other repeated colours must therefore occupy pairwise parallel lines, and different lines must have different colours or a transversal would force a forbidden intersection. This establishes the biconditional classification and the coefficient polynomial. The order-two exception is separately proved. Exhaustive independent partition enumeration at \(q=2,3\) and checks of every constructed partition at \(q=4,5,7\) corroborate the theorem. The finite computations are not used as an all-order proof.

**Originality — PASS, with priority risk.** The motivating defining paper [1] provides the uniform lower bound \(q\), so that numerical lower bound is credited. It does not classify the full affine-plane partitions, exact palette enumerator or unbounded gaps; its wide-path-connected result has an inapplicable edge-overlap hypothesis. Tuza's survey [2] discusses chromatic-spectrum gaps under C- and mixed-hypergraph constraints that differ from lean colourings. The comparison included terminology for Steiner designs, parallel classes and monochromatic-or-rainbow line patterns. No covering published claim was identified; an unindexed equivalent remains a material bibliographic risk.

**Value — PASS.** An axiomatic two-parameter incidence structure yields a complete nontrivial structural classification rather than a routine scalar minimum. It produces a closed counting polynomial, an exact set of allowable colour counts, and \(q(q-2)\) gaps, in all finite affine planes, without assuming Desarguesian coordinates.

**Limitations.** The theorem does not decide existence of affine planes for arbitrary orders or the analogous classification in higher-dimensional affine geometries. The checks exhaust only orders two and three; at larger tested orders they check all predicted patterns, not all possible partitions. An independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.

**Closest scientific sources.** [1] H. Piehowski, *The Lean Number of a Hypergraph*, arXiv:2607.14015v1 (15 July 2026). [2] Z. Tuza, *Mixed hypergraphs and beyond* (2019); different local colouring constraints.
