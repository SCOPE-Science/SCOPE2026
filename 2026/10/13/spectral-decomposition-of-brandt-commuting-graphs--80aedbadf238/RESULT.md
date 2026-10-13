# Spectral decomposition of Brandt commuting graphs
## Finding
Let \(n\ge 3\), and let \(B_n=([n]\times[n])\cup\{0\}\) be the aperiodic Brandt semigroup with multiplication
\[
(i,j)(k,\ell)=\begin{cases}(i,\ell),&j=k,\\0,&j\ne k.\end{cases}
\]
The center is \(\{0\}\), so the commuting graph \(\Delta(B_n)\) has vertex set \([n]^2\). Two distinct vertices \((i,j)\) and \((k,\ell)\) commute exactly when \(j\ne k\) and \(\ell\ne i\).

The adjacency characteristic polynomial is
\[
\chi_n(\lambda)=\bigl(\lambda^2-(n-1)^2\lambda+(n-1)(n-2)\bigr)
\bigl(\lambda^2+(n-1)\lambda-(n-2)\bigr)^{n-1}
\bigl(\lambda-(n-2)\bigr)^{n-1}
(\lambda+2)^{(n-1)(n-2)/2}
\lambda^{n(n-3)/2}.
\]
Equivalently, the spectrum consists of the two roots of \(\lambda^2-(n-1)^2\lambda+(n-1)(n-2)\), each once; the two roots of \(\lambda^2+(n-1)\lambda-(n-2)\), each with multiplicity \(n-1\); the eigenvalue \(n-2\) with multiplicity \(n-1\); the eigenvalue \(-2\) with multiplicity \((n-1)(n-2)/2\); and the eigenvalue \(0\) with multiplicity \(n(n-3)/2\).

Thus the adjacency matrix is nonsingular exactly at \(n=3\) among \(n\ge3\). Its graph energy is
\[
\mathcal E(\Delta(B_n))=(n-1)\left(3n-5+\sqrt{n^2+2n-7}\right).
\]

## Assumptions and scope
The result concerns the standard simple commuting graph whose vertices are the noncentral elements of the aperiodic Brandt semigroup \(B_n\), with an edge between two distinct commuting elements. The statement is for every integer \(n\ge3\). The exceptional case \(n=2\) has a different degeneracy pattern and is not included in the formula above.

The proof is over \(\mathbb R\) only because adjacency spectra are real; the semigroup itself is purely finite and combinatorial. No unproved classification theorem is used.

## Proof
Identify a real-valued function on \([n]^2\) with a matrix \(X=(x_{ij})\in M_n(\mathbb R)\). Write \(s\) for the sum of all entries, \(r_j\) for row sum \(j\), \(c_i\) for column sum \(i\), \(J\) for the all-ones matrix, and \(D(X)\) for the diagonal matrix with the same diagonal as \(X\). From the commuting criterion, the adjacency operator \(A\) is
\[
(AX)_{ij}=s-r_j-c_i+x_{ji}-(1-\delta_{ij})x_{ij},
\]
so
\[
A(X)=sJ-\mathbf 1r^{\mathsf T}-c\mathbf 1^{\mathsf T}+X^{\mathsf T}-X+D(X).
\]

Let \(W=\{u\in\mathbb R^n:\mathbf 1^{\mathsf T}u=0\}\). For \(u\in W\), put
\[
D_u=\operatorname{diag}(u),\qquad
P_u=\mathbf 1u^{\mathsf T}+u\mathbf 1^{\mathsf T},\qquad
Q_u=\mathbf 1u^{\mathsf T}-u\mathbf 1^{\mathsf T}.
\]
Direct substitution gives
\[
A(D_u)=D_u-P_u,\qquad A(P_u)=2D_u-nP_u,\qquad A(Q_u)=(n-2)Q_u.
\]
Hence each two-dimensional block \(\operatorname{span}\{D_u,P_u\}\) has characteristic polynomial \(\lambda^2+(n-1)\lambda-(n-2)\), while the \(Q_u\)-space contributes \((\lambda-(n-2))^{n-1}\).

On \(\operatorname{span}\{I,J\}\),
\[
A(I)=I+(n-2)J,\qquad A(J)=I+n(n-2)J.
\]
The corresponding two-by-two block therefore has characteristic polynomial
\[
\lambda^2-(n-1)^2\lambda+(n-1)(n-2).
\]

There are two remaining invariant spaces. Let
\[
K_- =\{X:X^{\mathsf T}=-X,\ X\mathbf 1=0\}.
\]
Then \(D(X)=0\), all row and column sums vanish, and \(A(X)=-2X\). Its dimension is \((n-1)(n-2)/2\). Likewise let
\[
K_0=\{X:X^{\mathsf T}=X,\ D(X)=0,\ X\mathbf 1=0\}.
\]
Then \(A(X)=0\), and \(\dim K_0=n(n-3)/2\). The dimensions
\[
2+2(n-1)+(n-1)+\frac{(n-1)(n-2)}2+\frac{n(n-3)}2=n^2
\]
sum to the whole matrix space. The symmetric and skew-symmetric pieces are disjoint, and within each piece the displayed row-sum constraints separate the listed summands, so these blocks give the full characteristic polynomial.

For the energy, the first quadratic has two positive roots because its sum and product are positive for \(n\ge3\). The second quadratic has roots of opposite signs, so the sum of their absolute values is
\[
\sqrt{(n-1)^2+4(n-2)}=\sqrt{n^2+2n-7}.
\]
Adding all multiplicity-weighted absolute eigenvalues yields the stated formula.

## Verification
The accompanying `verify.py` independently builds the commuting-graph adjacency operator and checks the invariant-space identities with exact rational arithmetic for every \(3\le n\le8\). It constructs bases for the skew row-sum-zero and symmetric zero-diagonal row-sum-zero spaces, checks their predicted dimensions and eigenvalues, and verifies that all displayed invariant blocks form an exact basis of \(M_n(\mathbb Q)\). These finite checks are consistency tests; the proof above is the argument for all \(n\ge3\).

## Relationship to prior work
Gray and Ruškuc treat arbitrary finite completely \(0\)-simple semigroups, including Brandt semigroups, from the viewpoint of generating sets and rank. Their paper supplies an archive-era algebraic anchor for the family but does not study graph spectra.

Kumar, Dalal, and Pandey study exactly the commuting graphs of aperiodic Brandt semigroups. Their paper gives the neighborhood criterion used above and studies diameter, independence number, girth, clique and chromatic numbers, vertex connectivity, Hamiltonicity, planarity, Eulerian behavior, and automorphisms/endomorphisms. A full-text inspection and paper-wide searches for spectral terminology found no adjacency spectrum, characteristic-polynomial, eigenvalue, or energy formula. The present result starts from their exact adjacency description and determines the complete spectral decomposition.

Nagy later studies commuting graphs of the broader class of Rees matrix semigroups. The accessible full text was also checked for spectral and eigenvalue statements; none covering the formula above was found.

## Limitations
The result is restricted to the aperiodic Brandt semigroup \(B_n\), rather than Brandt semigroups over a nontrivial group or arbitrary Rees matrix semigroups. It concerns the ordinary adjacency spectrum, not Laplacian, signless-Laplacian, or normalized spectra. The literature search cannot logically exclude every unindexed source, so the closest exact-object and broader-object papers were inspected directly and this residual bibliographic risk remains.

## References
R. Gray and N. Ruškuc, “Generating Sets of Completely 0-Simple Semigroups,” *Communications in Algebra* 33, published online 1 February 2007, DOI 10.1080/00927870500276676.

J. Kumar, S. Dalal, and P. Pandey, “On the commuting graphs of Brandt semigroups,” arXiv:2010.05000.

A. Nagy, “Commuting graphs of Rees matrix semigroups,” *Semigroup Forum* (2025), DOI 10.1007/s00233-025-10597-0.
