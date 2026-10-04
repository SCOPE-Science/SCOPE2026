# Review of Fourier-support spectrum of a ternary affine 3-simplex

## Correctness
PASS. Translation and affine-linear normalization reduce every admissible support to \(\{0,e_1,e_2,e_3\}\), and every local character triple occurs exactly \(3^{d-3}\) times. The only nontrivial finite lemma is the hyperplane-section classification on \(\mu_3^3\). The exact verifier proves that every four evaluation rows have rank at least three; hence any zero set of size at least four contains an independent triple. Cofactor enumeration over \(\mathbb Z[\omega]\) then proves that an admissible hyperplane through such a triple has exactly five, never four or more than five, grid points. Explicit coefficient vectors give zero counts \(0,1,2,3,5\).

## Originality
PASS with stated residual risk. Delvaux--Van Barel give global Hamming-number minima and constructions for Kronecker Fourier matrices, not this complete fixed-column spectrum; their report explicitly separates the Hamming-number problem from uniqueness of rank-deficient submatrices. Bonami--Ghobber treat equality cases in two-dimensional prime groups and cyclic/product families, not \(\mathbb F_3^3\) fixed affine-simplex spectra. Searches using the phrases “F_3^3 four sparse Fourier support affine simplex tetrahedron exact spectrum”, “four point support affine simplex finite Fourier uncertainty F3 cube”, “rank deficient submatrix F3 tensor F3 tensor F3 four columns prescribed support”, “F_3^d affine independent four point support Fourier support 22 24 25 26 27”, “ternary Fourier simplex four sparse support 22 3^(d-3)”, and “hyperplane section cube roots unity mu_3^3 five zeros linear form” did not return a statement implying the claim. The residual risk is unindexed coding-theory or finite-geometry literature under different terminology.

## Value
PASS. A four-point affine 3-simplex is the unique affine-rank-three support geometry for four points in ternary vector spaces, so its fixed-support uncertainty profile is structurally natural. The complete spectrum is substantially more informative than a global four-sparse minimum: it gives the sharp minimum \(22\,3^{d-3}\), identifies an exact forbidden intermediate value \(23\,3^{d-3}\), and isolates how affine geometry changes Fourier sparsity.

Same-model review: passed. Independent audit: not yet performed.
