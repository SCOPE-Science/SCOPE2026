# The integral critical group of the 64 lines on the Schur quartic

## Finding
Let \(X\subset\mathbb P^3_{\mathbb C}\) be the Segre–Schur quartic
\[
X:\quad x_0^4-x_0x_1^3-x_2^4+x_2x_3^3=0.
\]
Let \(M\in\mathbb Z^{64\times64}\) be the intersection matrix of the classes of its complete set of \(64\) geometric lines, numbered in any order. Then the integral matrix \(16I_{64}-M\) has corank one and its torsion cokernel is
\[
\operatorname{Tor}\operatorname{coker}(16I_{64}-M)
\cong (\mathbb Z/4\mathbb Z)^2\oplus(\mathbb Z/16\mathbb Z)^{32}
\oplus\mathbb Z/32\mathbb Z\oplus\mathbb Z/64\mathbb Z
\oplus\mathbb Z/192\mathbb Z\oplus(\mathbb Z/4224\mathbb Z)^6
\oplus(\mathbb Z/118272\mathbb Z)^2.
\]
Equivalently, the reduced \(63\times63\) Laplacian of the line-intersection graph has **Smith normal form**
\[
\operatorname{diag}(1^{\times18},4^{\times2},16^{\times32},32,64,192,
4224^{\times6},118272^{\times2}).
\]
These are invariant factors in divisibility order. In particular the graph critical group has exponent \(118272\), and the number of spanning trees is
\[
\tau=2^{209}3^9 7^2 11^8
=170097506621696854106380049543382914280125945374401312881249253029888995098624.
\]
The *order* \(\tau\) follows already from the previously known adjacency spectrum; the new classification here is the **integral elementary-divisor and invariant-factor structure**, which does not follow from the spectral data alone.

## Assumptions and scope
Work over \(\mathbb C\). The quartic is smooth and contains precisely \(64\) lines. Distinct lines have intersection number \(1\) if they meet and \(0\) otherwise; every line has self-intersection \(-2\). Define \(A\) as their \(0\)-\(1\) intersection-adjacency matrix, so \(M=A-2I_{64}\). The graph is \(18\)-regular, whence
\[
16I_{64}-M=18I_{64}-A=:L.
\]
The finite group in the theorem is the **graph critical group**, or equivalently torsion in the indicated integral shifted-intersection cokernel. This is **not** the Picard torsion of \(X\), nor its Néron–Severi discriminant group. Relabeling the \(64\) lines conjugates the matrices by a permutation and does not alter the group.

## Proof
**Geometric reconstruction.** Bauer–Schmitz, Section 2 and Proposition 2.2, provide all \(64\) line equations: \(16\) lines joining the four zeros of \(u(u^3-v^3)\) in each of two coordinate planes, and \(48\) lines indexed by twelve Möbius transformations \(Z^kT_j\) and four fourth-root choices. Let \(\omega^2+\omega+1=0\), \(i^2=-1\), and \(\eta=i(-1-2\omega)/3\), so \(\eta^2=1/3\). The explicit \(2\times2\) matrices \(T_j\), the scale \(i^m\omega^{-k}\eta\) for \(j>1\) (or \(i^m\omega^{-k}\) for \(j=1\)), and the coordinates are in the accompanying standalone verifier. All arithmetic is performed in the exact field \(\mathbb Q(\omega,i)\). Two lines meet precisely when their stacked four linear equations have vanishing determinant. The resulting symmetric adjacency matrix has \(64\) vertices, \(576\) edges, and constant degree \(18\).

**Rational spectral check and group order.** Direct integer-matrix multiplication verifies that \(A\) is killed by
\[
(A-18I)(A-2I)(A+4I)(A+6I)(A+10I)
\]
and that its traces in degrees \(0,1,2,3,4\) are \((64,0,1152,1728,139392)\). As \(A\) is symmetric, these five traces determine eigenvalue multiplicities \((1,44,8,9,2)\) for eigenvalues \((18,2,-4,-6,-10)\), respectively. The \(18\)-eigenspace is one-dimensional, so the graph is connected. Kirchhoff's matrix-tree theorem yields
\[
\det L_{\mathrm{red}}=\frac{16^{44}\cdot22^8\cdot24^9\cdot28^2}{64}
=2^{209}3^9 7^2 11^8.
\]
This scalar order check is not a substitute for the integral Smith calculation.

**Integral prime-adic certificate.** Delete one row and column to obtain \(L_{\mathrm{red}}\in\mathbb Z^{63\times63}\). For each prime dividing its nonzero determinant, carry out invertible row and column operations over \(\mathbb Z/p^{16}\mathbb Z\): at stage \(e\), pivot on every unit modulo \(p\), eliminate its remaining row and column by its inverse modulo the current modulus, and divide the leftover all-\(p\)-divisible block by \(p\). The number of unit pivots in each successive block is exactly the number of integer Smith diagonal entries of \(p\)-adic valuation \(e\), as follows by the elementary-divisor theorem over the discrete valuation ring \(\mathbb Z_p\). Precision \(16\) is sufficient because every diagonal entry is resolved by level \(9\); all \(63\) pivots are found, so no unobserved higher valuation is possible. The exact pivot counts are:

| Prime | \(p\)-adic valuation: multiplicity |
|---|---|
| \(2\) | \(0:18,\ 2:2,\ 4:32,\ 5:1,\ 6:2,\ 7:6,\ 9:2\) |
| \(3\) | \(0:54,\ 1:9\) |
| \(7\) | \(0:61,\ 1:2\) |
| \(11\) | \(0:55,\ 1:8\) |

Their total determinant valuations are \(209,9,2,8\), exactly matching the independently established determinant. No other prime divides it. Align each sorted valuation sequence to form the \(63\) invariant factors; this gives
\[
1^{\times18},\ 4^{\times2},\ 16^{\times32},\ 32,\ 64,\ 192,\ 4224^{\times6},\ 118272^{\times2}.
\]
Successive displayed factors divide their successors. The standard identification of the critical group of a connected graph with the cokernel of its reduced Laplacian proves the result; equivalently it is the torsion cokernel of the full \(L=16I-M\).

## Verification
Run `python3 verification/verify_schur_critical.py` using Python 3 standard library only. The program recreates the published \(16+48\) line geometry with exact algebraic numbers, constructs all \(2016\) possible pairs, verifies the adjacency annihilator and trace moments, performs all four complete modular Smith filtrations, and checks the invariant-factor product against Kirchhoff's tree number. Its last line is `VERIFY_OK`. All entries and calculations are independent of numerical floating point or reliance on a previously saved adjacency matrix.

## Relationship to prior work
Bauer–Schmitz (2012) give the full line equations and intersection matrix, and calculate Zariski-chamber invariants. Nurowski (2026) describes the complete \(64\)-line incidence and its Reye-geometric symmetry; the published published-finding corpus finding on the line graph determines the adjacency spectrum and common-neighbor profiles. Those sources determine the rational spectral data and hence the total number of spanning trees, but do not state the reduced Laplacian's Smith invariants or this graph's finite critical group structure. The invariant-factor calculation is a strict integral refinement: eigenvalues alone do not determine these torsion summands.

## Limitations
This is a result about the single distinguished quartic over \(\mathbb C\), not a uniform family of K3 surfaces. The group is attached to the **line-intersection graph**, not to the Picard group or Néron–Severi lattice of the surface itself. All computations are finite exact certificates, with the structural deductions explained above. An equivalent unpublished or unindexed Smith-form computation could still exist; absence from the inspected sources is not a proof of global historical priority. There has been no independent external audit.

## References
1. T. Bauer and D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373v1, first public 19 April 2012, Section 2, Proposition 2.2.
2. P. Nurowski, *The Reye geometry inside the 64 lines of the Schur quartic*, arXiv:2609.10751v2, 11 September 2026, Sections 3–4.
3. *Spectrum and common-transversal profile of the 64 Schur lines*, published finding and reproducibility files, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-spectrum-and-common-transversal-profile-of-the-64-schur-lines--76e63f54b379.
4. Standard matrix-tree theorem and Smith normal-form elementary divisor theorem over \(\mathbb Z_p\); included proofs identify their precise use.
