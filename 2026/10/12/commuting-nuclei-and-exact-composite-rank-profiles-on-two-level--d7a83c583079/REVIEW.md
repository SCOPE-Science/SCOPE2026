# Scientific review — commuting nuclei on two-level Heyting algebras

## Correctness — PASS
The statement fixes the domain, the notion of nucleus, ordering of pairs, and the rank convention. The proof establishes a support bijection for *all* nuclei from finite-meet preservation and idempotence, derives the necessary and sufficient two-containment condition by testing composite maps on each kind of point, and gives a disjoint weighted enumeration of equal, strictly nested, and incomparable lower supports. The image-rank formula uses an explicit bijection with upper sets of the intersection support, and the level-width exchange follows from direct polynomial algebra. Independent direct small-lattice enumeration reproduces the statements and checks the support parametrization in the smallest cases. Finite verification is not treated as an infinite proof.

## Originality — PASS, subject to historical-search uncertainty
Erné's 2022 full-text treatment gives general nuclear-range theory and commutation/composition implications (notably Lemma 3.6); it does not specify the two-level support conditions, the exact bivariate polynomial, or the rank-spectrum involution. Cīrulis's modal-operator paper treats structurally related notions, not the displayed exact finite-family census in the sections inspected. Searches for height-two upsets, commuting nuclei, nested subset supports, and numerical/polynomial aliases in other mathematical records and primary literature did not identify a logically equivalent or stronger result. Relevant finite-space mapping counts concern maps of posets rather than closure nuclei on their upset Heyting algebras. The possibility of a historical formula expressed in alternative terminology remains a real residual risk; absence of a search hit is not proof of absolute novelty.

## Mathematical value — PASS
General nucleus-composition theory gives neither a closed rank census nor a distinction between comparable and incomparable support data for this non-chain family. The two-level setting is a natural minimal departure from chains where new incomparability arises. The resulting exact parameter-uniform classification separates compatibility from rank, and the width-exchange symmetry yields a concrete pair of nonisomorphic finite Heyting algebras with identical full commuting-composite image-cardinality distributions. This structural boundary and spectrum equivalence are stronger than a routine numerical computation.

## Verification and limitations
`python3 verify.py` directly enumerates composite transformations on the finite upper-set lattices and independently enumerates nuclei in the smallest cases. The proof covers all integers \(m,n\ge2\); tests do not. Results concerning longer ordinal sums, automorphism orbits, and multi-operator commutation are not asserted. A separate literature auditor has not examined priority.

Self-review: passed. Independent audit: not yet performed.
