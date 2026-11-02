# Scientific review: central-binomial census and geometric center-defect law

## Correctness — PASS

The carrier and all three defining axioms are written explicitly in `RESULT.md`. The proof first establishes that meet preservation on a chain is precisely monotonicity; positivity is equivalent to nonnegativity at the unique negation center; the consistency equation then forces a constant strictly positive plateau on the negative half whenever the center is displaced. It verifies the converse in all cases, including the boundary input. Two disjoint enumerations by weakly increasing sequences yield the closed formulas for the full class, the normal subclass and the center-preserving subclasses. Ratios of consecutive binomial coefficients prove tight geometric tails, so the conditional geometric limit holds in total variation. The proof is valid for every positive integer parameter, not just the checked instances.

The standalone checker separately implements the original universal equations and the structural criterion. It exhausts all unary functions on the three- and five-element chains, all monotone functions on chains of sizes three, five, seven and nine, and independently checks both summations through parameter 60. Its results match the general expressions. It is finite corroboration, not an infinite mathematical certificate.

## Originality — PASS within the inspected evidence

Celani, Menchón and Miguelez (arXiv:2608.10937, Definition 3.5 and Proposition 3.19) establish the modal Kleene axioms and the centered identity. That identity already implies the plateau normal form for odd chains, and the normal form alone is **not** claimed as new. Their inspected categorical, centered, and topological results do not present the exact all-size counts, asymptotic rarity, or geometric law for the displaced center. Flaminio, Godo, Menchón and Rodriguez (arXiv:2405.19354) analyze a more constrained modal nilpotent-minimum rotation setting and explicitly preserve the negation fixpoint in the centered case; that is not the present unrestricted modal Kleene census.

A previously published exact count on Boolean–Kleene products includes the three-element Kleene chain; its numerical case is credited. Products of two- and three-element algebras are not the five-element-and-larger chains considered here. Research-record and primary-literature searches for chain counts, equivalent parametrizations and stronger encompassing results produced no decisive matching formula. An unlocated historical count or an implicit numerical consequence of older operator-classification theory remains a real originality risk; failure to find one is not a uniqueness proof.

## Mathematical value — PASS

The object is a canonical family of all odd finite De Morgan/Kleene chains and the exact modal signature newly developed in 2026. Counting **all** admissible operators is a natural finite-algebraic invariant. The theorem gives complete formulas for four important algebraic subclasses across every chain length, not isolated small instances. More significantly, center preservation becomes almost certain at a sharply quantified exponential rate even though it is not an axiom. Conditioned on this rare failure, the center displacement follows an exact binomial distribution converging in total variation to a geometric law. Both quantitative phenomena express structural information beyond the motivating qualitative equivalence.

## Sources and limitations

The closest work is the 2026 categorical theory of modal Kleene algebras, the 2024 modal nilpotent-minimum rotation framework, and the earlier finite Boolean–Kleene product census. Unrestricted nonchain Kleene lattices, even chains, and semiring-based Kleene-star modalities are outside the scope. Historical priority beyond the inspected literature and formal independent verification remain unresolved.

Self-review: passed. Independent audit: not yet performed.
