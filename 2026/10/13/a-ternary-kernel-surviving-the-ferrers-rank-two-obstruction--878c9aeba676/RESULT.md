# A ternary kernel surviving the Ferrers rank-two obstruction
## Finding
Let \(E=(5,5,5,5,1,1)\). Over \(\mathbb F_3\), form the multiplication spread \(S\subset M_4(\mathbb F_3)\) from
\[
\mathbb F_81=\mathbb F_3[x]/(x^4+x^3+x^2+1),
\]
using the power basis \(1,x,x^2,x^3\), and put \(U=S^\perp\) for the entrywise Frobenius inner product. The explicit basis of \(U\) is recorded in `verify_ferrers_q3.py`.

In coefficient coordinates relative to that basis, let \(K\le U\) be the kernel of
\[
H=\begin{pmatrix}
0&2&1&0&2&1&1&2&1&0&2&2\\
0&1&0&0&1&1&2&1&1&1&0&1
\end{pmatrix}.
\]
Then \(\dim K=10\), and \(K\) contains exactly \(1040\) matrices of rank \(2\). Their right kernels run through all \(130\) planes \(N\le\mathbb F_3^4\), with exactly \(8\) matrices for every plane. Equivalently,
\[
\dim_{\mathbb F_3}\{M\in K:N\le\ker M\}=2
\]
for every two-dimensional \(N\le\mathbb F_3^4\).

Consequently this explicit ternary kernel satisfies the complete plane-balance/rank-two necessary condition obtained by extending the rank-distribution step in Prajapati's binary kernel-lift reduction to \(q=3\). It supplies a concrete survivor of that obstruction; it does not by itself produce a ternary Ferrers-diagram rank-metric code of dimension \(12\).

## Assumptions and scope
Matrices are \(4\times4\) over \(\mathbb F_3\), rank means ordinary matrix rank over \(\mathbb F_3\), and kernels are right kernels. The Ferrers diagram \(E=(5,5,5,5,1,1)\) and target rank distance \(3\) are those of the recent binary counterexample. The calculation addresses only the field-spread MRD model \(U=S^\perp\) and the displayed codimension-two subspace \(K\).

For a putative \([E,12,3]\) code in the kernel-lift form, the binary argument isolates a codimension-two \(K\le U\) and forces, for every plane \(N\), a two-dimensional subspace of matrices annihilating \(N\). Over \(\mathbb F_3\), such a two-dimensional subspace has \(3^2-1=8\) nonzero matrices, so the corresponding full rank-two count is \(130\cdot8=1040\). The finding proves that the displayed \(K\) realizes exactly this profile.

## Proof
The polynomial \(x^4+x^3+x^2+1\) is irreducible over \(\mathbb F_3\), so multiplication by every nonzero element of \(\mathbb F_81\) is an invertible \(4\times4\) matrix. Hence the four multiplication matrices of the power basis span a four-dimensional spread code \(S\). The artifact constructs its twelve-dimensional orthogonal complement \(U\) explicitly and checks all \(3^{12}\) coefficient vectors. Its exact rank distribution is
\[
A_0=1,\qquad A_2=10400,\qquad A_3=220800,\qquad A_4=300240,
\]
with \(A_1=0\). Thus this particular \(U\) has minimum nonzero rank \(2\).

The two displayed rows of \(H\) are independent, so their common kernel in the twelve coefficient coordinates has dimension \(10\). Exhaustive enumeration of all \(3^{10}\) elements of \(K\) gives exactly \(1040\) matrices of rank \(2\). Every rank-two \(4\times4\) matrix has one two-dimensional right kernel. Reducing those kernels to canonical row-reduced bases partitions the \(1040\) matrices into \(130\) classes, and every class has size \(8\). Since the Gaussian binomial coefficient \({4\brack2}_3=130\), every plane occurs exactly once as a kernel class. For a fixed plane \(N\), the matrices of \(K\) annihilating \(N\) form a linear subspace; its eight nonzero members plus zero therefore give dimension \(2\). This proves the stated plane-balance property.

## Verification
`verify_ferrers_q3.py` contains the complete finite certificate. It checks irreducibility of the defining quartic, reconstructs the multiplication spread, checks that the displayed basis is exactly orthogonal to it, exhausts all \(3^{12}\) elements of \(U\), exhausts all \(3^{10}\) elements of \(K\), canonicalizes every rank-two right kernel, and verifies the \(130\)-by-\(8\) distribution. The finite enumerations are exhaustive, not samples.

The symbolic part used by the checker is elementary finite-dimensional linear algebra: a rank-two \(4\times4\) matrix has a two-dimensional right kernel, and the number of planes in \(\mathbb F_3^4\) is \({4\brack2}_3=130\).

## Relationship to prior work
Prajapati's 2026 paper proves the binary \(q=2\) counterexample for this Ferrers diagram. Its kernel-lift reduction shows that a hypothetical dimension-\(12\) binary code would require a codimension-two kernel \(K\) inside a \([4\times4,12,2]\) MRD code; its rank-distribution lemma then forces exactly \(105\) rank-two matrices, three for each of the \(35\) binary planes. The paper proceeds by classifying the binary MRD possibilities and solving the remaining finite lift problem. It does not state or construct the ternary kernel above.

Gruica and Ravagnani's 2024 rook-theoretic treatment gives general finite-field counting and probabilistic existence tools for Ferrers-diagram rank-metric codes. Its general bounds do not identify this \(q=3\) codimension-two kernel or imply the displayed \(130\)-plane incidence profile.

The present finding is therefore a boundary result for extending the new binary obstruction: the first rank-count/plane-balance filter does not eliminate the ternary field-spread model.

## Limitations
No \([E,12,3]\) code over \(\mathbb F_3\) is claimed. In particular, this finding does not construct the remaining linear lift map or prove that such a map exists. It also does not classify all codimension-two subspaces of all ternary \([4\times4,12,2]\) MRD codes, and it makes no assertion for larger fields. An unindexed computation of an equivalent ternary kernel could still exist.

## References
1. J. Prajapati, “A counterexample to the Etzion-Silberstein conjecture,” arXiv:2608.08478v1, first public 2026-08-09. See Theorem 1 and Lemmas 2–4.
2. A. Gruica and A. Ravagnani, “Rook theory of the Etzion-Silberstein Conjecture,” *Algebraic Combinatorics* (2024), especially Proposition 4.1 and the general Ferrers-diagram counting framework.
