# Sharp endpoint commutator norms after deleting one product rectangle

## Finding
Let \((X,\mu)\) and \((Y,\eta)\) be arbitrary probability spaces, with measurable \(A\subseteq X\), \(B\subseteq Y\) such that \(p=\mu(A)\) and \(q=\eta(B)\) satisfy \(0<p,q<1\). Normalize the product measure after deleting the rectangular event: \(S=(X\times Y)\setminus(A\times B)\) and \(\nu=\bigl((\mu\otimes\eta)|_S\bigr)/(1-pq)\). On functions on \(S\), let \(P=\mathbb E_\nu[\,\cdot\mid X]\), \(Q=\mathbb E_\nu[\,\cdot\mid Y]\), and \(C=PQ-QP\). For real or complex \(L^r(S,\nu)\), the exact sharp endpoint norms are
\[
\boxed{\|C\|_{L^1\to L^1}=\|C\|_{L^\infty\to L^\infty}=2\max\{pq,\ p(1-q),\ (1-p)q\}.}
\]
All sharp \(L^\infty\) norms are attained by blockwise sign-valued inputs. The maximizing output blocks follow a complete phase diagram: the \(A^c\times B^c\) block dominates exactly when \(p,q\ge 1/2\); the \(A^c\times B\) block dominates exactly when \(q\le1/2\) and \(p\ge q\); the \(A\times B^c\) block dominates exactly when \(p\le1/2\) and \(q\ge p\). All equalities describe genuine ties.

On \(L^2(S,\nu)\), the same operator has rank two, with nonzero eigenvalues \(\pm i\sqrt{pq(1-pq)}\), each of multiplicity one, and
\[
\boxed{\|C\|_{L^2\to L^2}=\sqrt{pq(1-pq)}.}
\]
The \(L^2\) formula is consistent with classical two-projection/maximal-correlation theory and is included as a comparison rather than claimed as a new general Hilbert-space principle. Along \(p=q\uparrow1\), the endpoint norm tends to \(2\), while the Hilbert norm tends to zero. Thus the ratio of endpoint to Hilbert commutator norms diverges, even though each conditional expectation is contractive in every \(L^r\).

## Assumptions and scope
All probability spaces are allowed, with no atom-count or regularity condition, and only the three positive-mass blocks after deleting one *entire* product rectangle are needed. Products use the completed product sigma-algebra if applicable; coordinate conditional expectations are defined in the standard almost-everywhere sense. For \(1\le r\le\infty\), both expectations act as contractions. The strict restrictions \(0<p,q<1\) ensure that all three retained blocks have positive mass; boundary cases are asserted only as limits, not as part of the theorem. The full-space scalar probabilities are \(p,q\); they are not the conditional marginals under \(\nu\).

Set \(S_0=A^c\times B^c\), \(S_1=A^c\times B\), and \(S_2=A\times B^c\). Their unnormalized masses under \(\mu\otimes\eta\) are
\[
m_0=(1-p)(1-q),\qquad m_1=(1-p)q,\qquad m_2=p(1-q).
\]
They sum to \(1-pq\). This explicit normalization is essential.

## Proof
**Block reduction.** Write \(\bar f_j=m_j^{-1}\int_{S_j}f\,d(\mu\otimes\eta)\), the product-measure average over \(S_j\). Conditional averaging first in one coordinate and then in the other depends only on the three block averages, even if the underlying spaces are nonatomic. The coordinate expectations induce the following matrices on vectors \((\bar f_0,\bar f_1,\bar f_2)\):
\[
P_0=\begin{pmatrix}1-q&q&0\\1-q&q&0\\0&0&1\end{pmatrix},\qquad
Q_0=\begin{pmatrix}1-p&0&p\\0&1&0\\1-p&0&p\end{pmatrix}.
\]
Consequently \(Cf\) is constant on every output block, with block-value matrix
\[
C_0=P_0Q_0-Q_0P_0=\begin{pmatrix}
0&pq&-pq\\ -p(1-q)&0&p(1-q)\\ (1-p)q&-(1-p)q&0
\end{pmatrix}.
\]
Equivalently, \((Cf)|_{S_i}=\sum_{j=0}^2K_{ij}\int_{S_j}f\,d(\mu\otimes\eta)\), where
\[
K=\begin{pmatrix}
0&\frac{p}{1-p}&-\frac{q}{1-q}\\
-\frac{p}{1-p}&0&1\\
\frac{q}{1-q}&-1&0
\end{pmatrix}.
\]
Thus \(K\) is skew-symmetric, as required by \(C^*=-C\) on \(L^2(\nu)\).

**Endpoint norm and equality.** For any essentially bounded input, the absolute value of the output on block \(S_i\) is at most \(\|f\|_\infty\sum_j|K_{ij}|m_j\). The three row sums are exactly \(2pq\), \(2p(1-q)\), and \(2(1-p)q\). For every row \(i\), the input equal to \(\operatorname{sgn}(K_{ij})\) on \(S_j\), with arbitrary unit phase if \(K_{ij}=0\), attains its row sum. Taking the maximum proves the \(L^\infty\) equality. Since \(C^*=-C\) and the kernel is integrable and bounded for fixed \(p,q\), the dual \(L^1\) operator has the same norm. Comparing the three positive expressions yields the stated phase regions: compare \(pq\) with \(p(1-q)\) by \(q\gtreqless1/2\), compare \(pq\) with \((1-p)q\) by \(p\gtreqless1/2\), and compare \(p(1-q)\) with \((1-p)q\) by \(p\gtreqless q\).

**Hilbert spectral calculation.** The orthonormal indicators \(e_i=\mathbf1_{S_i}/\sqrt{\nu(S_i)}\) span the range of \(C\) and are left invariant by \(C\). Their matrix is \(H_{ij}=K_{ij}\sqrt{m_i m_j}\), whose three upper off-diagonal entries are
\[
H_{01}=p\sqrt{q(1-q)},\quad
H_{02}=-q\sqrt{p(1-p)},\quad
H_{12}=\sqrt{pq(1-p)(1-q)}.
\]
A real skew-symmetric three-by-three matrix with upper entries \(a,b,c\) has spectrum \(\{0,\pm i\sqrt{a^2+b^2+c^2}\}\). Here
\[
a^2+b^2+c^2=pq\bigl[p(1-q)+q(1-p)+(1-p)(1-q)\bigr]=pq(1-pq).
\]
All three blocks have positive mass and \(H\ne0\), so the rank is exactly two. On the orthogonal complement of the block indicators, \(C=0\), proving the claimed complete nonzero spectrum and Hilbert norm.

**Separation.** For \(p=q\uparrow1\), the maximizing row is \(S_0\) and \(\|C\|_\infty=2p^2\uparrow2\), whereas \(\|C\|_2=p\sqrt{1-p^2}\downarrow0\). Since the endpoint norm is strictly below \(2\) for every admissible \(p,q\), this is a sharp unattained universal supremum.

## Verification
The standalone standard-library program `conditional_commutator_checker.py` enumerates 81 positive rational finite-product probability models with deleted nonempty proper rectangles. It reconstructs both coordinate conditional expectation matrices directly from normalized conditional weights, and checks the resulting commutator entries against the block kernel. It verifies skew-adjointness in the probability-weighted pairing, sharp \(L^1\) and \(L^\infty\) norms, trace of the squared matrix, its cubic polynomial identity, and explicit sign witnesses. The program passed 14,358 exact-rational assertions. These tests support the stated algebra but do not substitute for the proof on arbitrary probability spaces.

## Relationship to prior work
Hirschfeld–Gebelein–Rényi maximal correlation and the classical two-orthogonal-projection calculus govern Hilbert-space aspects of products of conditional expectations. Beigi's 2014 exposition gives the classical normalized joint-distribution singular-value characterization, and the corresponding binary quotient here has maximal correlation \(\sqrt{pq}\); it therefore predicts the Hilbert commutator modulus \(\sqrt{pq(1-pq)}\). No general Hilbert-space statement is claimed as new. The 2022 projection-operator discussion by Conde concerns Hilbert-space norms and commutator bounds, not maximum-coordinate norms for rectangularly truncated products. The published three-point conditional-expectation numerical-radius calculation concerns a fixed uniform three-atom real \(\ell^4\) spatial numerical radius, not endpoint norms or arbitrary hole masses. The binary conditional-expectation chain formula concerns centered products for \(1<r<\infty\), and explicitly excludes both endpoint exponents; taking norms of the two ordered products separately does not evaluate the norm of their difference. This theorem gives the new complete two-mass endpoint phase diagram and sharp separation from the Hilbert regime.

## Limitations
The theorem addresses deletion of one product rectangle from an initially independent law. More complicated missing-data patterns need not reduce to three blocks. No sharp result is asserted for intermediate \(L^r\)-norms other than the Hilbert norm, for arbitrary joint laws, or for three or more conditional expectations. The Hilbert formula follows established operator-angle principles; the originality claim is limited to the endpoint formula, phase diagram and quantitative cross-norm separation for this rectangular-deletion family. Historical priority outside examined accessible literature remains provisional, and no independent audit has been performed.

## References
1. S. Beigi, *Maximal Entanglement – A New Measure of Entanglement*, arXiv:1405.2502v1, first publicly submitted 2014-05-11. Section I gives the classical maximal-correlation and singular-value descriptions. https://arxiv.org/html/1405.2502v1 .
2. C. Conde, *A note about the norm of the sum and the anticommutator of two orthogonal projections*, Journal of Mathematical Analysis and Applications **505** (2022), article 125650. DOI:10.1016/j.jmaa.2021.125650 .
3. *Sharp numerical radius of a three-point conditional-expectation commutator*, public mathematical result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-numerical-radius-of-a-three-point-conditional-expectation--d81ced4c9642 .
4. *Exact mixing norms and time-reversal obstruction for binary conditional-expectation chains*, public mathematical result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-mixing-norms-and-time-reversal-obstruction-for-binary-cond--8cff936fbe0f .
