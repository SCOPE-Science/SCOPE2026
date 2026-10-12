# Scientific review: reachability-volume factorization

## Correctness — PASS

The claim fixes the combinatorial Laplacian, vertex order, input, and sign convention. The reflection decomposition makes one block independent of the defect weight and the other an affine rank-one update. Endpoint controllability within each Jacobi block provides nonzero constant factors. A cross-spectral Vandermonde/resultant identity then reduces the full determinant to factors indexed by the symmetric sector. At unit weight, all nonzero symmetric eigenvalues meet simple antisymmetric eigenvalues, generating exactly \(\lfloor(n-1)/2\rfloor\) nonvanishing-slope factors. The antisymmetric zero mode occurs at the signed path-resistance weight, and evaluation at the open path fixes the overall sign. Exact-rational checks of 112 cases confirm the normalizations, including both singular parameter values. Finite checks are not used as a universal proof.

## Originality — PASS, with residual uncertainty

The closest direct same-object source is Grudsky–Maximenko–Soto-González (arXiv:2205.12457), whose eigenvalue and eigenvector statements make a spectral approach possible but do not state the ordered Kalman determinant or its exact factorization. Xiang–Zhu–Chen–Chen (DOI:10.1155/2013/405034) provide general controllability theory and a directed-cycle result; they do not cover the symmetric one-defect volume law. Zelazo–Bürger (arXiv:1408.2187) cover the negative-weight singularity through effective resistance, not the high-multiplicity unit-weight factor. Searches for one-defect cycle reachability, walk-matrix determinants, Gram volumes, and algebraically equivalent forms did not locate an exact matching theorem. Published spectral formulas might nevertheless yield this identity after nontrivial elimination, and unindexed historical treatments remain a real residual risk.

## Value — PASS

The fact quantifies, rather than merely asserts, structural controllability restoration by a single edge perturbation on an infinite graph family. It gives the exact determinant and hence the determinant of the squared Krylov Gram matrix, and identifies a dimension-dependent order of collapse on return to rotational symmetry. This is a natural reachability-sensitivity invariant with a plausible role in actuator fragility assessment, not an arbitrary finite table or a small numerical improvement.

## Scope and limitations

The input is at a distinguished-edge endpoint, the Laplacian is unnormalized, and the result concerns algebraic Krylov volume rather than minimum-energy control in physical time. The signed root is already explained by effective-resistance theory; it is not claimed separately as novel. Same-object spectral literature is an especially important historical-priority caveat.

Self-review: passed. Independent audit: not yet performed.
