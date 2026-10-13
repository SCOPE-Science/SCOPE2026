# Scientific review: generic scalar Heisenberg-type Leibniz subalgebras

## Correctness — PASS

The central dichotomy is exhaustive because a subalgebra intersects the one-dimensional derived center either trivially or in the whole center. In the trivial-intersection case, its projection is injective and gives a unique graph. Two ordered bracket equations form a linear system in the cross-pairing values with determinant \(1-\lambda^2\ne0\), forcing the projection spaces to be orthogonal. Counting their subdirect products via intersection kernels and an induced quotient isomorphism produces the claimed Gaussian formula, without assuming odd characteristic. Direct reduced-row-echelon enumeration in the included `checker.py` agrees with all coefficients in five finite examples, including characteristic two; the general proof is algebraic rather than computational.

## Originality — PASS, with residual bibliographic risk

Mancini and La Rosa, *Two-step nilpotent Leibniz algebras* (arXiv:2106.12904), classify the bilinear-form setting and define Heisenberg-type families, but the inspected construction and surrounding results give no subalgebra-dimension enumerator. Siciliano and Towers, *On the subalgebra lattice of a Leibniz algebra* (arXiv:2010.12254), analyze order-theoretic properties, notably modularity and extraspecial Leibniz algebras; these do not supply the cardinalities of every embedded dimension stratum. The closest published search results on Heisenberg Lie-algebra subalgebra commutativity degrees concern alternating brackets and a different invariant. The generic condition here excludes that alternating case, and the orthogonal subdirect-product sum is additional information not furnished by these results. Literature under alternate terminology may still contain an equivalent enumeration.

## Value — PASS

Complete subalgebra-dimension distributions are natural invariants of finite nilpotent non-Lie algebras, not an arbitrary selection of examples. The theorem gives every coefficient in all generator ranks and all admissible finite-field characteristics, identifies the two geometric ingredients—orthogonal pairs and subdirect products—and proves that the entire distribution is constant across the generic scalar-parameter locus. The exclusion of the singular parameters is structurally motivated by the precise determinant in the proof. No general isomorphism-type census or lattice-permutability theorem is claimed.

Self-review: passed. Independent audit: not yet performed.
