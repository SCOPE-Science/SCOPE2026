# Complete exact-support five-point Fourier spectrum on \(\mathbb F_3^2\)
## Finding
Let \(G=\mathbb F_3^2\). For every five-element set \(A\subset G\), as \(f:G\to\mathbb C\) ranges over functions with \(\operatorname{supp}f=A\), the attainable Fourier-support sizes are exactly
\[
\boxed{\{5,6,7,8,9\}}.
\]
Thus every exact five-point support has Fourier-support minimum \(5\), and every integer from \(5\) through \(9\) occurs on every fixed support.

## Assumptions and scope
The Fourier transform is taken on the additive group \(G\); its normalization is irrelevant to support. The statement concerns exact support: all five coefficients on \(A\) are required to be nonzero. Affine changes of variables, translations, and modulations preserve both spatial-support size and the number of Fourier zeros.

## Proof
Write \(\omega=e^{2\pi i/3}\) and, for a fixed five-set \(A=\{a_1,\ldots,a_5\}\), form the \(9\times5\) evaluation matrix
\[
M_A(\xi,j)=\omega^{\langle\xi,a_j\rangle},\qquad \xi\in\mathbb F_3^2.
\]
For a coefficient vector \(c\in\mathbb C^5\), the Fourier zero set is the set of rows of \(M_A\) annihilating \(c\).

The affine group \(\operatorname{AGL}(2,3)\) has exactly two orbits on the \(\binom95=126\) five-subsets, of sizes \(54\) and \(72\). Representatives may be taken as
\[
A_1=\{(0,0),(0,1),(0,2),(1,0),(2,0)\},
\]
which is the union of two intersecting affine lines, and
\[
A_2=\{(0,0),(0,1),(0,2),(1,0),(1,1)\}.
\]
This finite orbit statement is exhaustively checked in `artifacts/verify.py`.

For a set \(Z\) of Fourier rows, let \(R_Z\) be their span in \(\mathbb Q(\omega)^5\). A coefficient vector annihilating every row in \(Z\) lies in \(\ker M_Z\). Every additional row already in \(R_Z\) must then vanish as well, so an actual Fourier zero set is row-span closed. Conversely, if \(\ker M_Z\) has positive dimension, is not contained in any coordinate hyperplane \(c_j=0\), and no row outside the closure belongs to \(R_Z\), then a vector in \(\ker M_Z\) can be chosen outside the finite union of all those proper hyperplanes. Such a vector has all five coefficients nonzero and has exactly the closed zero set.

The exact rank computation over \(\mathbb Q(\omega)\), performed for all \(2^9=512\) row subsets for each representative, gives precisely the possible closed zero-set cardinalities
\[
0,1,2,3,4
\]
for both affine orbit types, and no larger closed zero set admits a kernel vector with all five coordinates nonzero. Hence the possible Fourier-support sizes are exactly \(9,8,7,6,5\). Explicit Eisenstein-integer coefficient vectors realizing each of the five zero counts for both representatives are also replayed by the verifier.

## Verification
`artifacts/verify.py` uses exact rational arithmetic in the quadratic field \(\mathbb Q(\omega)\), represented by pairs \(a+b\omega\) with \(\omega^2+\omega+1=0\). It enumerates all \(126\) five-subsets, all \(432\) affine transformations, and all \(512\) prospective Fourier-zero row sets for each canonical representative. It checks orbit sizes \(54\) and \(72\), closure sizes exactly \(0,1,2,3,4\), and explicit nonzero coefficient witnesses for each zero count.

## Relationship to prior work
Delvaux and Van Barel study rank-deficient submatrices of Kronecker Fourier matrices and the associated Hamming-number uncertainty invariant, which minimizes over supports of size at most a given bound. That invariant does not determine the exact-cardinality-five layer: in \(\mathbb F_3^2\), smaller subgroup-supported functions can dominate a ``size at most five'' minimum.

Bonami and Ghobber determine equality cases for the uncertainty function on groups including \(\mathbb Z_3\times\mathbb Z_3\). Their general formula gives the global minimum at support bound \(5\), and their equality theorem addresses when that minimum is attained. It does not classify the complete Fourier-support spectrum for every fixed exact five-point support. The present result supplies that exact-support refinement: the minimum is \(5\), not merely the global bound inherited from smaller supports, and every larger size through \(9\) occurs on every five-set.

## Limitations
This theorem is specific to exact five-point supports on the ternary affine plane. It does not classify coefficient vectors up to symmetry, nor does it give the corresponding complete spectra for larger fields or higher-cardinality supports. The two-orbit and rank-closure steps are finite exhaustive certificates; they are exact rather than numerical, but they are not replaced here by a case-free geometric classification.

## References
S. Delvaux and M. Van Barel, “Rank-deficient submatrices of Kronecker products of Fourier matrices,” KU Leuven Report TW 477, 15 November 2006; later Linear Algebra and its Applications 426 (2007), 349–367.

A. Bonami and S. Ghobber, “Equality cases for the uncertainty principle in finite Abelian groups,” arXiv:1003.5060v1, 26 March 2010.
