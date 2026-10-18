# Scientific review

## Correctness

**PASS.** The result concerns the formally extended Euler polynomial, not a claim that every real multiplicity vector is realized geometrically. The Euler coefficient expression is reconstructed from the primary paper's Theorem 4.6, with explicit multiplicity convention and matrix normalization. The polar matrix is circulant; its Fourier diagonalization, trigonometric factorization, strict absence of additional zeros for odd primes, arithmetic negative-mode witness, and positive trace are proved in the manuscript. The independent standard-library checker matches exact shift-matrix identities and all signs in bounded cases.

## Originality

**PASS, with residual risk.** The originating source calculates the Euler form and sorts group actions by displacement coincidences; it does not state a positivity criterion covering all prime-order nonzero weights. General signed-graph Laplacian bounds are not equivalent to this arithmetic iff statement. Existing related specializations concern one weight ratio or integral cokernel invariants. In particular, the fact that the polar matrix has a given Smith form does not determine its real inertia. A complete all-prime classification and explicit inertia count require the separate residue-permutation argument. An unindexed derivation or an implicit treatment elsewhere remains possible.

## Value

**PASS.** The Euler correction governs the dimension formula for equivariant Hilbert schemes, making the definiteness of its signed McKay-graph quadratic form a motivated structural invariant. The result partitions *every* nontrivially weighted odd-prime cyclic quotient plane into precisely two natural symmetry types with a genuine nonnegative energy and all other types with unavoidable negative directions. It also supplies a complete computable inertia formula for every weight ratio, beyond checking isolated examples. The result is not a claim about which formal negative vectors are geometrically realizable.

## Closest literature and limitations

Bachhuber–Gholampour, arXiv:2610.12736v1, Theorem 4.6 and §§6–7; Agbanusi–Bronski–Kielty, arXiv:2005.09608. Related earlier scalar-action inertia and integral cyclic-Euler Smith-form results overlap in examples but do not cover the asserted iff classification. Full historical priority and independent verification remain unestablished. The result excludes composite cyclic orders, zero weights, noncyclic groups, and Hilbert-scheme nonemptiness.

Self-review: passed. Independent audit: not yet performed.
