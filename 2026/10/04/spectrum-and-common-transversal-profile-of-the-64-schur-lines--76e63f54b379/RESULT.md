# Spectrum and common-transversal profile of the 64 Schur lines
## Finding
Let \(X\subset\mathbf P^3_{\mathbf C}\) be the Segre--Schur quartic
\[
x_0^4-x_0x_1^3-x_2^4+x_2x_3^3=0.
\]
Let \(\Gamma\) be the simple intersection graph of its 64 lines. Two vertices are adjacent exactly when the corresponding distinct lines meet. Then \(\Gamma\) is connected, 18-regular, has diameter two, and its adjacency characteristic polynomial is
\[
(\lambda-18)(\lambda-2)^{44}(\lambda+4)^8(\lambda+6)^9(\lambda+10)^2.
\]
For adjacent pairs the common-neighbor count is 0 for 144 pairs and 2 for 432 pairs. For skew pairs the common-neighbor count is 4, 6, 7, 8, or 10, occurring for 240, 648, 384, 144, and 24 pairs respectively.

Consequently, if \(M\) is the 64-by-64 intersection matrix of the line classes on \(X\), then
\[
\operatorname{Spec}(M)=\{16^1,0^{44},(-6)^8,(-8)^9,(-12)^2\},
\]
so \(M\) has rank 20 and inertia \((1,19,44)\).

## Assumptions and scope
All calculations are over \(\mathbf C\), but the incidence reconstruction is performed exactly in \(\mathbf Q(i,\sqrt3)\). The 64 lines are the complete Segre--Schur line set in the explicit Bauer--Schmitz parametrization: 16 lines of the first type and 48 of the second type. A common neighbor of two vertices means a third Schur line meeting both; for a skew pair this is therefore a Schur-line transversal, not an arbitrary line in \(\mathbf P^3\).

## Proof
Bauer and Schmitz give equations for all 64 lines. Write \(\xi=(-1+i\sqrt3)/2\) and \(\eta=\sqrt3/3\). Their first 16 lines join the four zeros of the binary quartic on each of the two coordinate lines. Their other 48 lines are indexed by \(Z^kT_j\), \(0\le k\le2\), \(1\le j\le4\), and the four fourth-root factors indexed by \(0\le m\le3\).

Each projective line is represented by two independent homogeneous linear equations. Two distinct such lines meet if and only if the determinant of the stacked four coefficient rows vanishes. Evaluating all \(\binom{64}{2}=2016\) determinants exactly in \(\mathbf Q(i,\sqrt3)\) gives the adjacency matrix \(A\). Every row sum is 18, there are 576 edges, and breadth-first search from every vertex gives diameter two.

For the spectrum, exact integer matrix multiplication verifies
\[
(A-18I)(A-2I)(A+4I)(A+6I)(A+10I)=0.
\]
The matrix \(A\) is real symmetric, so it is diagonalizable, and its eigenvalues lie among these five distinct roots. The exact trace moments are
\[
\operatorname{tr}(A^0),\ldots,\operatorname{tr}(A^4)
=(64,0,1152,1728,139392).
\]
The resulting Vandermonde system has the unique multiplicity vector \((1,44,8,9,2)\) at eigenvalues \((18,2,-4,-6,-10)\), proving the displayed characteristic polynomial.

The off-diagonal entries of \(A^2\) count common neighbors. Exhausting all unordered vertex pairs gives the two stated distributions. Finally, on a smooth quartic K3 surface each line has self-intersection \(-2\), while two distinct lines have intersection 1 exactly when they meet and 0 otherwise. Hence \(M=A-2I\), so shifting the adjacency spectrum by \(-2\) gives the stated intersection spectrum, rank, and inertia.

## Verification
Run `python3 verify_schur_spectrum.py`. The verifier uses only the Python standard library. It reconstructs all 64 line equations over the exact four-dimensional \(\mathbf Q\)-basis \(1,i,\sqrt3,i\sqrt3\), checks every pair determinant, verifies regularity and diameter, checks the full common-neighbor distributions, verifies the degree-five annihilating polynomial by exact integer matrix multiplication, and checks the five trace moments that determine the multiplicities. The recorded output ends in `VERIFY_OK`.

## Relationship to prior work
Naskręcki and Pokora isolated one connected \((24_4,32_3)\) half of the 48 second-type lines and supplied exact incidence data; their arXiv record lists MSC 14J28 first and dates the first public version to 2026-07-08. Nurowski subsequently analyzed the complete 64-line incidence geometry, including its multiplicity census and automorphism group. Bauer and Schmitz earlier gave explicit equations and the complete intersection matrix, proving that this matrix has rank 20. Benedetti, Di Marca, and Varbaro observed that every Schur line meets exactly 18 others. Thus 18-regularity and rank 20 are prior facts; the finding here is the full spectral factorization together with the exact adjacent/skew common-neighbor profile and the resulting inertia refinement.

Targeted searches for the exact characteristic polynomial, the five eigenvalues, adjacency spectrum terminology, and common-transversal counts did not locate a prior statement. The closest inspected sources state the incidence formulas, rank, regularity, multiplicity census, or symmetry, but not these spectral/common-neighbor invariants.

## Limitations
This is a theorem about the fixed Segre--Schur quartic and its complete 64-line configuration. It does not classify line-intersection spectra of other quartic K3 surfaces, and it does not identify the automorphism orbits of all skew pairs within each common-transversal count. Literature searches can miss unindexed computations, so residual originality risk remains for specialized databases or unpublished computational notes.

## References
1. B. Naskręcki and P. Pokora, *A \((24_4,32_3)\)-configuration on the Schur quartic with logarithmic Chern slope \(14/5\)*, arXiv:2607.07898, first version 2026-07-08.
2. P. Nurowski, *The Reye geometry inside the 64 lines of the Schur quartic*, arXiv:2609.10751, first version 2026-09-09.
3. T. Bauer and D. Schmitz, *Zariski chambers on surfaces of high Picard number*, LMS J. Comput. Math. 15 (2012), 219--230, doi:10.1112/S1461157012001040.
4. D. Benedetti, M. Di Marca, and M. Varbaro, *Regularity of line configurations*, arXiv:1608.02134.
