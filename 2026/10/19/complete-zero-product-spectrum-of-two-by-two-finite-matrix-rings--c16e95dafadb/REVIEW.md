# Scientific review

## Correctness — PASS

The claim has been reconstructed from the exact zero-product criterion for rank-one matrices. The formula \((Bf)_{ij}=s(r_j+c_i-f_{ji})-\mathbf 1_{i=j}f_{ii}\) is verified by inclusion-exclusion, and the complete \(n^2\)-dimensional symmetric/skew invariant decomposition is accounted for by exact dimensions. The characteristic polynomial is the product of two explicitly computed two-by-two block polynomials and the one-dimensional scalar branches, with exact within-type eigenspaces. The signs and discriminants give inertia/energy and nonzero reduced determinant gives sharp nullity. The standalone standard-library checker exhaustively agrees for \(q=2,3,4,5\), but the infinite result is proved algebraically.

## Originality — PASS (literature-limited)

Rather (arXiv:2603.20947v1) computes the type block and a spectral-radius quotient for odd primes, but only bounds nullity and leaves a \((p+1)^2\)-order spectrum unresolved (Theorem 4.1, Corollary 4.2, Table 1). Masalkar–Khairnar–Lande–Kadam (arXiv:2312.09934v1) reduce the same graph and give Weyl bounds; they explicitly describe the corrected quotient as difficult to diagonalize. Masalkar–Khairnar–Lande–Patil (arXiv:2106.15977v1) gives a broad quotient-matrix method for finite semisimple rings, including these matrix rings, but not the uniform complete symbolic factorization and sharp invariants. An indexed same-graph domination result deals with a different invariant. published-finding corpus semantic searches and targeted external searches found no equivalent polynomial or stronger closed form. The 2021 work makes instancewise computation possible; this is acknowledged, not mischaracterized as an unknown algorithm. Residual risk: equivalent formulas could occur in unindexed literature, or be implicit in an independently diagonalized form of the earlier general quotient.

## Value — PASS

The kernel/image ordered-pair model has a large unresolved quotient in a recent study. The finding collapses it to two explicit quadratic factors for **every** finite field, sharpens an established rank/nullity bound to equality, and yields the exact adjacency inertia and energy. Those are natural invariants for the same well-motivated family, not isolated small-field cases or a mere numerical refinement.

## Scope and limitations

The graph is undirected, loopless and includes precisely nonzero singular matrices. The underlying coefficient field may have characteristic two, but this does not assert anything about even-modulus quaternion rings. Independent external mathematical validation is not asserted.

Self-review: passed. Independent audit: not yet performed.
