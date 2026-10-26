# Scientific review: sharp initial-rank tomography of alternating-adjoint paths

## Correctness — PASS

The conjugating unitary is explicitly the alternating left/right singular-vector basis, which changes both edge types to the same nonnegative diagonal matrix. Coordinate regrouping decomposes the path into scaled Jordan shifts. The phase-gauge identity and real Jacobi eigenvalues provide the complete, sign-sensitive Hermitian spectral list. The Li–Sze half-plane formula gives disks for nonnegative ordered eigenvalues and the empty set for negative ones. For the inverse, each next largest singular value times the largest cosine factor lies within the first \((d-1)\lfloor m/2\rfloor+1\) ordered products. Deletion with multiplicity covers ties; zero radii determine all remaining zeros. Two diagonal inputs with distinct small final singular values prove optimality of the exact initial-prefix cutoff. Computations are corroborative, not infinite proof.

## Originality — PASS, qualified

The October 2026 alternating-path paper computes only rank-one numerical radius. Gaaya's full accessible paper analyzes individual Jordan shifts and general contraction bounds, not exact scaled-direct-sum inverse identification. Gau–Wu prove a general all-matrix Kippenhahn-polynomial determination theorem using a longer initial chain, which does not by itself furnish the shorter optimal measurement count here. Argerami–Mustafa analyze one Jordan-like block plus scalar blocks, not these paths. Targeted semantically indexed and primary-literature searches did not identify the full disk spectrum together with the optimal inverse cutoff. Unindexed specialized inverse presentations remain a residual priority risk.

## Mathematical value — PASS

The motivating exact norm formula loses all singular-value information except the largest singular value. Higher-rank compression measurements make it possible to reconstruct the entire singular spectrum, and the theorem determines the **minimal** number needed uniformly over all complex input matrices. The sharp counterexample makes the cutoff an exact information threshold, not an arbitrary parameter slice. The result is an analytically closed finite-dimensional inverse theorem rather than a table recomputation.

## Boundaries and sources

The theory assumes known finite path length and block size and noiseless sets; no singular vectors, perturbative conditioning, or infinite-dimensional conclusions are established. Scientific comparison focused on arXiv:2610.15242v1, arXiv:1004.3751v1, arXiv:1208.1333v1, and arXiv:1908.05692v3. Independent scientific priority and proof certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
