# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  The proof was checked by separating subalgebras according to whether they contain the one-dimensional center.  Center-avoiding subalgebras are exactly graphs of linear functionals on totally isotropic subspaces.  For two graph subalgebras, direct computation shows that failure of permutability is equivalent to a nonzero symplectic cross-pairing together with equality of the two functionals on the intersection.

The intersection count was checked in two independent ways: Möbius inversion on the subspace lattice gives the number of isotropic pairs with a prescribed intersection, while counting inside the totally isotropic sum gives the mutually orthogonal subfamily.  Their difference times the functional count gives the displayed formula for nonpermutable pairs.

The formula specializes exactly to the published rank-one expression.  A standalone exhaustive computation over the complete subspace lattices of the 5-dimensional rank-two algebra verifies the formula for q=2 and q=3: respectively 158 and 693 Lie subalgebras, with 6000 and 187920 nonpermutable ordered pairs.  The asymptotic statements follow from explicit degree comparison and from a uniform product-formula bound for Gaussian coefficients and isotropic-subspace counts.

## Originality

**PASS, to the best of our knowledge.**  arXiv:2609.19086v1 explicitly asks for the values of the Heisenberg family and proves only the rank-one formula; it also transfers that rank-one result to the extraspecial group of order p^3.  Searches by the exact invariant name, Heisenberg terminology, symplectic-subspace formulations, extraspecial p-groups, factorization number, and subgroup permutability did not locate the all-rank formula, the rank-two rational function, or either asymptotic transition.

The 2023 spectral-invariant paper of Muhie et al. gives general expressions for subgroup commutativity degree but does not supply this Heisenberg/extraspecial enumeration.  The count of totally isotropic subspaces is standard finite symplectic geometry and is treated as prior art.

The principal residual risk is old subgroup-lattice literature on extraspecial p-groups.  Such literature can encode subgroups through symplectic data, so an equivalent enumeration may exist without the terminology “subgroup commutativity degree.”  Targeted searches did not identify one, but that possibility prevents an absolute first-discovery claim.

## Value

**PASS.**  The result closes the concrete all-rank Heisenberg question left open by the source paper with a finite exact formula, gives the first next-rank closed expression, and reveals two non-obvious asymptotic phenomena: a sharp q→∞ rank transition and sd→1 as rank tends to infinity over any fixed finite field.  Via the source paper's Lazard theorem, it simultaneously gives exact subgroup commutativity degrees for the exponent-p extraspecial family and shows that these increasingly large nonabelian groups have subgroup commutativity degree tending to one.

## Limitations

The exhaustive artifact checks only H_2 over the prime fields F_2 and F_3; it does not replace the general proof.  Literature search cannot exclude equivalent older formulas hidden in detailed extraspecial-group subgroup classifications.  No independent, formal, or peer-reviewed validation is claimed.
