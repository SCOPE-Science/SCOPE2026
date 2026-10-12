# Scientific review: complete abelian-subalgebra census for biclique graph Lie algebras

## Correctness — PASS

The classification follows from the tensor-contraction lemma: a vector with nonzero components in both bipartition summands has a one-dimensional horizontal centralizer. This forces every bracket-zero horizontal subspace to lie in one pure summand or be a mixed line. Each embedded abelian subalgebra has a unique center intersection, horizontal projection, and graph map into the central quotient. Counting those maps, subspaces and mixed lines proves the exact Gaussian-binomial polynomial. Maximal by inclusion subalgebras are identified separately from maximum-dimensional ones. The standalone checker exhausts six prime-field instances and independently verifies their entire RREF subspace lattices and maximality. The proof, not the sample checker, establishes the result for all fields.

## Originality — PASS, with residual risk

The closest same-object source, Godoy Molina–Lagos (arXiv:2308.00272), computes graph-induced ideals/subalgebras and graded derivations of the edge-distinct complete-bipartite family; it does not provide the all-embedded abelian-subspace distribution. The 2025 independence-polynomial work of Aldi et al. (arXiv:2504.19836) does cover the maximum abelian dimension; that consequence is not claimed as original. Its vertex-set polynomial does not enumerate noncoordinate finite-field linear spaces or central lifts. DeCoste et al. (arXiv:2208.09541) study central *abelian factors*, which are different objects, while Rossmann (DOI:10.1112/blms.12665) counts conjugacy classes of graphical groups. Published research-record and primary-literature searches for exact and synonymous formulations located no theorem implying the complete distribution. Equivalent unindexed work remains a risk; the full 2022 abelian-factor paper could only be partially inspected and is not used to claim an exhaustive negative.

## Value — PASS

This provides a complete, naturally defined family of subalgebra incidence invariants over every finite field, not a fixed-parameter computation. The entire polynomial distinguishes nonideal/central-lift subalgebras that graph-induced and ideal-only censuses miss. The projective family of inclusion-maximal abelian subalgebras can have dimensions arbitrarily below the maximum: this structural boundary is invisible from the maximum-dimension invariant alone.

## Scope and verification limits

Only the edge-distinct biclique family is classified. No formula for all nonabelian subalgebras, arbitrary graph Lie algebras, or automorphism orbits is asserted. Finite checks included \((a,b,q)=(1,1,2),(1,1,3),(1,1,5),(1,2,2),(1,2,3),(2,2,2)\); independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
