# Zero-insertive matrices are exactly the half-rank locus
## Finding
Let \(D\) be a division ring and let \(n\ge 2\). Following the recent zero-insertive terminology, put
\[
Z_i(M_n(D))=\{X\in M_n(D):X=ARB\text{ for some }A,B,R\in M_n(D)\text{ with }AB=0\}.
\]
Then
\[
Z_i(M_n(D))=\{X\in M_n(D):\operatorname{rank}_D(X)\le \lfloor n/2\rfloor\}.
\]
Thus the complete zero-insertive locus in a full matrix algebra over a division ring is the determinantal locus of rank at most half the matrix size.

For a finite field \(\mathbb F_q\), this gives the exact enumeration
\[
|Z_i(M_n(\mathbb F_q))|
=
\sum_{r=0}^{\lfloor n/2\rfloor}
\frac{\prod_{j=0}^{r-1}(q^n-q^j)^2}{\prod_{j=0}^{r-1}(q^r-q^j)}.
\]
In particular, when \(n=2\), the theorem recovers the fact that every singular matrix is zero-insertive. When \(n\ge3\), singularity is no longer sufficient: every singular matrix of rank greater than \(\lfloor n/2\rfloor\) lies outside \(Z_i(M_n(D))\).

## Assumptions and scope
Matrices act on the right \(D\)-vector space \(D^n\), and \(\operatorname{rank}_D(X)\) means the right-\(D\)-dimension of the image. The proof uses only rank-nullity over a division ring and elementary row/column equivalence. The finite-field count is a consequence for commutative finite fields; the structural rank theorem itself is valid for every division ring.

The definition of zero-insertive is exactly the factorization condition \(X=ARB\) with \(AB=0\). No nil-cleanness assumption is used.

## Proof
Suppose first that \(X=ARB\) with \(AB=0\). The equality \(AB=0\) gives
\[
\operatorname{im}(B)\subseteq \ker(A).
\]
Hence rank-nullity yields
\[
\operatorname{rank}(A)+\operatorname{rank}(B)\le n.
\]
Also
\[
\operatorname{rank}(ARB)\le \min\{\operatorname{rank}(A),\operatorname{rank}(B)\}.
\]
Therefore
\[
\operatorname{rank}(X)\le \lfloor n/2\rfloor.
\]

Conversely, let \(X\in M_n(D)\) have rank \(r\le\lfloor n/2\rfloor\). Elementary row and column reduction over a division ring gives invertible \(U,V\in GL_n(D)\) with
\[
X=U J_r V,
\qquad
J_r=\sum_{i=1}^r E_{ii}.
\]
Because \(2r\le n\), define
\[
A_r=\sum_{i=1}^r E_{i,r+i},
\qquad
R_r=\sum_{i=1}^r E_{r+i,i},
\qquad
B_r=J_r.
\]
Matrix-unit multiplication gives
\[
A_rB_r=0,
\qquad
A_rR_rB_r=J_r.
\]
Consequently
\[
X=(UA_r)R_r(B_rV)
\]
and
\[
(UA_r)(B_rV)=U(A_rB_r)V=0.
\]
Thus \(X\) is zero-insertive. This proves the classification.

For \(D=\mathbb F_q\), the number of rank-\(r\) matrices in \(M_n(\mathbb F_q)\) is
\[
\frac{\prod_{j=0}^{r-1}(q^n-q^j)^2}{\prod_{j=0}^{r-1}(q^r-q^j)}.
\]
Summing this over \(0\le r\le\lfloor n/2\rfloor\) gives the stated finite-field count.

## Verification
The obstruction direction was checked directly at the level of images and kernels: \(AB=0\) forces \(\operatorname{im}(B)\subseteq\ker(A)\), so no product \(ARB\) can have rank exceeding half of \(n\).

The constructive direction was checked symbolically from the matrix-unit identities \(E_{ij}E_{kl}=\delta_{jk}E_{il}\). They give \(A_rB_r=0\) and \(A_rR_rB_r=J_r\) for every \(2r\le n\), after which invertible left and right changes of basis recover every rank-\(r\) matrix.

Boundary checks agree with the theorem: for \(n=2\), the allowed ranks are \(0,1\), precisely the singular matrices; for \(n=3\), only ranks \(0,1\) occur, so rank-\(2\) singular matrices are excluded.

## Relationship to prior work
Subba and Subedi introduced the elementwise zero-insertive set and, in their 2026 paper, proved that every non-unit of \(M_2(K)\) is zero-insertive for a field \(K\), via the Leavitt path algebra model \(L_K(A_2)\cong M_2(K)\). The same paper provides a special family of zero-insertive elements for general \(n\), but its inspected matrix discussion does not state an intrinsic rank classification of \(Z_i(M_n(K))\).

Their 2025 precursor studies ZINC rings and proves, among other statements, that \(M_n(K)\) is ZINC for a division ring \(K\) exactly when \(K\cong\mathbb F_2\). That ring-level nil-clean property does not identify which matrices are zero-insertive. The theorem here instead determines the zero-insertive subset itself for every division ring and every size.

Targeted searches for the zero-insertive matrix locus, rank formulations, and equivalent \(ARB\) factorizations did not locate a published statement equivalent to the half-rank classification. The residual literature risk is an equivalent elementary factorization result under older terminology such as zero-product sandwich factorizations.

## Limitations
The theorem is specific to full matrix algebras over division rings. It does not classify zero-insertive elements of \(M_n(R)\) for a general coefficient ring, where a single rank invariant need not exist. The finite-field formula counts matrices but does not classify their similarity orbits inside the zero-insertive locus.

Originality is supported by the inspected sources and targeted searches, not by an exhaustive proof that no equivalent statement exists anywhere under unrelated terminology.

## References
1. S. Subba and T. Subedi, *Zero Insertive Nil Clean Rings*, arXiv:2508.01333v1, 2025.
2. S. Subba and T. Subedi, *Semicommutativity via Zero-Insertive Elements: Insights from Path and Leavitt Path Algebras*, arXiv:2609.24439v1, 2026.
