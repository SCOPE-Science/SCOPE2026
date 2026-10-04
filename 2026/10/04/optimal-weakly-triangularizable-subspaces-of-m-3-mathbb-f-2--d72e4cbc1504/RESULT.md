# Optimal weakly triangularizable subspaces of \(M_3(\mathbb F_2)\)
## Finding
There are exactly \(35\) six-dimensional \(\mathbb F_2\)-linear subspaces of \(M_3(\mathbb F_2)\) in which every matrix is triangularizable over \(\mathbb F_2\). Under similarity by \(\mathrm{GL}_3(\mathbb F_2)\), they form exactly three orbits, represented by
\[
\mathrm T_3(\mathbb F_2),\qquad \mathfrak{sl}_2(\mathbb F_2)\vee M_1(\mathbb F_2),\qquad M_1(\mathbb F_2)\vee\mathfrak{sl}_2(\mathbb F_2),
\]
with orbit sizes \(21,7,7\), respectively. There is no seven-dimensional weakly triangularizable subspace of \(M_3(\mathbb F_2)\). Consequently \(t_3(\mathbb F_2)=6\), and the three displayed similarity types are all optimal spaces.

Here \(\mathcal A\vee\mathcal B\) denotes the block upper-triangular joint of square matrix spaces. Explicitly,
\[
\mathfrak{sl}_2(\mathbb F_2)\vee M_1(\mathbb F_2)
=
\left\{
\begin{pmatrix}
a&b&u\\
c&a&v\\
0&0&d
\end{pmatrix}:a,b,c,d,u,v\in\mathbb F_2
\right\},
\]
and
\[
M_1(\mathbb F_2)\vee\mathfrak{sl}_2(\mathbb F_2)
=
\left\{
\begin{pmatrix}
d&u&v\\
0&a&b\\
0&c&a
\end{pmatrix}:a,b,c,d,u,v\in\mathbb F_2
\right\}.
\]

## Assumptions and scope
The statement concerns linear subspaces of the nine-dimensional vector space \(M_3(\mathbb F_2)\). A matrix is called triangularizable when it is similar over \(\mathbb F_2\) to an upper-triangular matrix. Two matrix spaces are regarded as equivalent here only under simultaneous conjugation by an element of \(\mathrm{GL}_3(\mathbb F_2)\).

The dimension equality \(t_3(\mathbb F_2)=6\) is already implied by the general dimension theorem quoted in the recent literature, because \(|\mathbb F_2|=2\geq 3-1\). The new part of the finding is the complete binary \(3\times3\) optimal-space classification and exact orbit census.

## Proof
For a matrix \(A\in M_3(\mathbb F_2)\), triangularizability is equivalent to splitting of its characteristic polynomial over \(\mathbb F_2\). The only split monic cubics are
\[
t^3,\qquad t^2(t+1),\qquad t(t+1)^2,\qquad (t+1)^3.
\]
Thus triangularizability is decidable exactly from the three non-leading characteristic-polynomial coefficients. Among the \(512\) matrices in \(M_3(\mathbb F_2)\), exactly \(352\) satisfy this test.

Every \(k\)-dimensional subspace of \(\mathbb F_2^9\) has a unique reduced-row-echelon basis. Exhaustively enumerating those bases gives
\[
{9\brack 6}_2=788035
\]
six-dimensional subspaces and
\[
{9\brack 7}_2=43435
\]
seven-dimensional subspaces. Testing every element of every subspace against the split-characteristic-polynomial criterion gives exactly \(35\) qualifying six-spaces and no qualifying seven-space. An independent enumeration through three-dimensional trace-orthogonal complements reproduces the same set of \(35\) six-spaces.

The three displayed model spaces are weakly triangularizable. For \(B\in\mathfrak{sl}_2(\mathbb F_2)\),
\[
\chi_B(t)=t^2+\det(B),
\]
and since \(\det(B)\in\{0,1\}\), this is either \(t^2\) or \((t+1)^2\). Hence every such \(B\) is triangularizable; the block-upper-triangular joints are therefore triangularizable elementwise.

The group \(\mathrm{GL}_3(\mathbb F_2)\) has order \(168\). Exact conjugation of the \(35\) qualifying six-spaces gives orbit sizes \(21,7,7\). The three model spaces lie in distinct orbits: \(\mathrm T_3(\mathbb F_2)\) has a common invariant line and a common invariant plane; \(\mathfrak{sl}_2(\mathbb F_2)\vee M_1(\mathbb F_2)\) has a common invariant plane but no common invariant line; and \(M_1(\mathbb F_2)\vee\mathfrak{sl}_2(\mathbb F_2)\) has a common invariant line but no common invariant plane. Their orbit sizes sum to \(21+7+7=35\), so they exhaust the qualifying six-spaces.

## Verification
The standalone checker `artifacts/verify.py` performs two complete enumerations of the six-dimensional case, a direct complete enumeration of the seven-dimensional case, and an exact \(\mathrm{GL}_3(\mathbb F_2)\)-orbit computation. It reports \(352\) triangularizable matrices, \(35\) qualifying six-spaces, \(0\) qualifying seven-spaces, group order \(168\), and orbit sizes \(21,7,7\). The independently generated certificate is stored in `artifacts/certificate.json`.

The computation is finite and exhaustive: no probabilistic sampling, floating-point arithmetic, or unproved search cutoff is used.

## Relationship to prior work
De Seguins Pazzis, *Spaces of triangularizable matrices (III): Perfect non-quadratically closed fields with characteristic 2*, arXiv:2608.28863v1, formulates two remaining tasks: extend the dimension formula to the unresolved characteristic-two finite-field range, and classify optimal weakly triangularizable spaces. Its Theorem 1.1 already covers \((\mathbb F_2,n=3)\) for the dimension formula because \(|\mathbb F_2|\geq n-1\). Its quoted structural Theorem 1.2 for optimal spaces instead assumes \(|\mathbb F|\geq n\), so it does not cover \((\mathbb F_2,3)\). The same paper explicitly notes that the \(\mathbb F_2\) case resists the methods used for larger fields and identifies weak triangularizability over \(\mathbb F_2\) with the corresponding one-nonzero-eigenvalue condition.

The three similarity types found here are precisely the three structural forms that occur in the larger-field classification, but the present result verifies that no additional binary exceptional type appears in dimension three and gives the complete labeled census \(35=21+7+7\).

## Limitations
This is a complete finite classification only for \(M_3(\mathbb F_2)\). It does not classify optimal spaces in \(M_n(\mathbb F_2)\) for \(n\geq4\), nor does it provide a new proof of the already known dimension equality \(t_3(\mathbb F_2)=6\) independent of exhaustive enumeration. The originality assessment is based on the inspected recent source, its stated theorem hypotheses and open classification problem, targeted literature searches, and published-finding database comparisons; an unindexed older small-field classification would be the principal residual literature risk.

## References
1. C. de Seguins Pazzis, *Spaces of triangularizable matrices (III): Perfect non-quadratically closed fields with characteristic 2*, arXiv:2608.28863v1, first posted 2026-08-28.
2. C. de Seguins Pazzis, *Spaces of triangularizable matrices*, Acta Sci. Math. (Szeged) 91 (2025), 369--399.
3. C. de Seguins Pazzis, *Spaces of matrices with few eigenvalues (II)*, arXiv:2605.05849v1, first posted 2026-05-07.
