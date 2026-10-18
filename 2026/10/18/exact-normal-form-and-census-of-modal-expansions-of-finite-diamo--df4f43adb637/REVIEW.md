# Review of the diamond-lattice modal-expansion census

## Correctness: PASS

The claimed carrier is the \(n\)-atom diamond lattice \(M_n\) for every integer \(n\ge3\), with exactly the four kinds of equations in Bezhanishvili–Dmitrieva–de Groot–Moraschini Definition 4.10. The proof derives the meet-map alternatives from their bottom image, reduces the Dunn inequality to diagonal and cross-atom comparisons, and exhausts all pairs of bottom images. The five case contributions are mutually disjoint and sum to the displayed \(N_n\). The proof does not replace an infinite statement by finite evidence. The self-contained checker directly tests all modal equations on \(M_3\) and \(M_4\), giving \(574\) and \(5054\), and computes independent Burnside fixed-point counts yielding \(126\) and \(325\) isomorphism classes. The larger evaluations follow from the proved formula.

## Originality: PASS, with residual risks

The claimed new object is *the exact normal form and its family-wide counting formula*, not the axioms of modal lattices or the duality that motivated them. A full-text comparison with [1] finds the definition, representation, completeness, and Sahlqvist results but no count or equivalent finite-diamond classification. Dmitrieva [2] works with stronger and different diamond axioms, including join- and bottom-preservation, and likewise develops duality rather than this count. Moraschini [3] addresses positive subreducts of Boolean modal algebras, hence distributive lattices, which cannot be the non-distributive family here. Searches for diamond/M-lattice aliases, Dunn normality, exact numbers and lattice expansion counts in published research records found no stronger theorem implying the claimed formula; the nearest records concern chains, Gödel algebras, and modal frames. The accessible earlier findings are distinct in carrier or operators. A potentially unindexed table or an unnoticed different normalization remains possible; search noncoverage is evidence with a limit, not a proof of uniqueness.

## Value: PASS

The family \(M_n\), beginning at the smallest non-distributive lattice at \(n=3\), is a canonical stress test for modal-lattice semantics beyond distributivity. An explicit five-case classification of all two-operator expansions across every width is mathematically more informative than a computed five-element example: it produces a formula with an unbounded parameter and exact orbit counts for the two smallest non-distributive widths. The formula discriminates the unrestricted top-preserving, merely monotone diamond semantics from the more restrictive join-preserving semantics of earlier work and provides reproducible finite examples of the newly studied class. The exact counts and normal form answer a natural classification question without presuming downstream theorems.

## Closest literature and limits

[1] N. Bezhanishvili, A. Dmitrieva, J. de Groot, and T. Moraschini, *Positive Modal Logic Beyond Distributivity*, arXiv:2204.13401, especially Definition 4.10, §§4.2–4.5. [2] A. Dmitrieva, *Positive Modal Logic Beyond Distributivity: Duality, Preservation and Completeness*, 2021, Definition 5.1.1. [3] T. Moraschini, *Varieties of Positive Modal Algebras and Structural Completeness*, 2019, arXiv:1908.01659. The initial publication date of [1] is 2022-04-28, not its later revision date. Enumeration of isomorphism classes is proved only for the widths explicitly checked, \(n=3,4\); the arbitrary-width result is the labelled count. Hidden alternative presentations and external independent mathematical checking remain residual risks.

Self-review: passed. Independent audit: not yet performed.
