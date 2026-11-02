# A sharp all-exponent failure of C*-like norm recovery for the Hadamard-diagonal algebra

## Finding
For each real \(1\le p<\infty\), set \(E_p=\ell_p^2(\mathbb C)\) and
\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad P_+=(I+J)/2,\quad P_-=(I-J)/2,
\qquad A_p=\{\alpha I+\beta J:\alpha,\beta\in\mathbb C\}\subset\mathcal L(E_p).
\]
For every integer \(n\ge2\), equip columns and rows over \(A_p\) with their spatial operator norms from \(E_p\) to \(\ell_p^n(E_p)\) and conversely. Their pairing is matrix multiplication. The pair is C*-like (both module norms recovered from unit-ball pairings) **if and only if** \(p=2\).

More sharply, set \(X_n=(P_+,P_-,0,\ldots,0)^T\) and \(Y_n=(P_+,P_-,0,\ldots,0)\). If \(1\le p<2\), then
\[
\|X_n\|=2^{2/p-1},\qquad
\sup_{\substack{B\in M_{1,n}^p(A_p)\\\|B\|\le1}}\|BX_n\|=2^{1/p-1/2}<\|X_n\|.
\]
If \(2<p<\infty\), then
\[
\|Y_n\|=2^{1-2/p},\qquad
\sup_{\substack{C\in M_{n,1}^p(A_p)\\\|C\|\le1}}\|Y_nC\|=2^{1/2-1/p}<\|Y_n\|.
\]
The relative pairing recovery factor of the displayed witness is exactly \(2^{-|1/p-1/2|}\). The algebra is unital and commutative for every exponent.

## Assumptions and scope
All spaces and operator matrices are complex, \(p\in[1,\infty)\), and \(n\) is any finite integer at least two. All matrix norms are induced by the standard counting-measure \(\ell_p\) norms, not entrywise matrix norms. The two C*-like equalities are those of Definition 3.1 of Calin et al., for the row-column module. Infinite-column extensions follow by zero padding for the counterexamples; the theorem's iff assertion is stated for finite \(n\).

## Proof
**1. A two-dimensional multiplier bound.** Every \(D\in A_p\) is uniquely \(D=\alpha P_++\beta P_-\). Define \(K_p=2^{|1/p-1/2|}\). We claim
\[
\|\alpha P_++\beta P_-\|_{E_p\to E_p}\le K_p\max(|\alpha|,|\beta|).
\tag{1}
\]
At \(p=1\), both columns of this matrix have absolute sum \((|\alpha+\beta|+|\alpha-\beta|)/2\le\sqrt{|\alpha|^2+|\beta|^2}\le\sqrt2\max(|\alpha|,|\beta|)\). At \(p=2\), the orthogonal spectral decomposition has norm \(\max(|\alpha|,|\beta|)\). The Riesz–Thorin theorem interpolates to \(1<p<2\), giving \(K_p=2^{1/p-1/2}\). Duality under transposition yields (1) for \(p>2\). Equality in the constant is attained by \((\alpha,\beta)=(1,i)\): the matrix \(H=P_++iP_-\) is unitary with every entry of modulus \(2^{-1/2}\), so testing the first basis vector gives \(\|H\|_p\ge2^{1/p-1/2}\) for \(p\le2\); duality gives \(2^{1/2-1/p}\) for \(p\ge2\). Hence \(\|H\|_p=K_p\).

**2. Exact column and row norms.** At \(p=1\), the four-by-two matrix \(X_2\) has column absolute sums \(2\), so \(\|X_2\|_1=2\). At \(p=2\), \(X_2^*X_2=P_++P_-=I\), so \(\|X_2\|_2=1\). Interpolation gives \(\|X_2\|_p\le2^{2/p-1}\) for \(1\le p\le2\). The first unit coordinate vector maps to four entries each of modulus \(1/2\), which gives equality. Its Banach adjoint is the row \(Y_2\); therefore for \(p>2\), \(\|Y_2\|_p=\|X_2\|_{p'}=2^{1-2/p}\), with \(p'=p/(p-1)\). Zero padding preserves all these norms.

**3. Exact strict deficit for \(p<2\).** For any algebra row \(B=(b_1,\ldots,b_n)\), let \(\alpha\) be the scalar by which \(b_1\) acts on the \(+\) eigenspace of \(J\), and \(\beta\) the scalar by which \(b_2\) acts on the \(-\) eigenspace. Unit eigenvectors inserted into the first and second input blocks show \(\|B\|_p\ge\max(|\alpha|,|\beta|)\). Moreover, \(BX_n=\alpha P_++\beta P_-\). Thus (1) gives \(\|BX_n\|_p\le K_p\|B\|_p\). This bound is attained by \(B_0=(P_+,iP_-,0,\ldots)\): its norm equals one because its \(p=1\) norm and its \(p=2\) norm are both one, interpolation gives an upper bound of one, and a \(+\) eigenvector gives a lower bound of one. Its product with \(X_n\) equals \(H\), whose norm equals \(K_p\). Since \(2^{1/p-1/2}<2^{2/p-1}\) when \(p<2\), the column norm is not recovered.

**4. Exact strict deficit for \(p>2\).** For any algebra column \(C=(c_1,\ldots,c_n)^T\), define \(\alpha\) as the \(+\)-eigenvalue of \(c_1\) and \(\beta\) as the \(-\)-eigenvalue of \(c_2\). Input eigenvectors show \(\|C\|_p\ge\max(|\alpha|,|\beta|)\); and \(Y_nC=\alpha P_++\beta P_-\). Equation (1) yields \(\|Y_nC\|_p\le K_p\|C\|_p\). For \(C_0=(P_+,iP_-,0,\ldots)^T\), interpolation between \(p=2\) and \(p=\infty\) proves \(\|C_0\|_p=1\) (the endpoint norms equal one, and a \(+\) eigenvector provides the lower bound). Again \(Y_nC_0=H\), so the supremum is exactly \(K_p\), strictly below \(\|Y_n\|_p=2^{1-2/p}\).

**5. The Hilbert point.** At \(p=2\), \(A_2\) is a concrete unital commutative C*-algebra and the usual Hilbert C*-module norm recovery applies to its finite direct sums (also directly from the spectral decomposition). Thus the two norm-recovery conditions hold. This completes the iff proof.

## Verification
Every calculation is finite-dimensional, but the proof covers the continuum of all real exponents in its scope because the interpolation and duality arguments are analytic. A reproducible standard-library Python checker accompanies the statement. It verifies the projection identities and selected exact test-vector norms without using finite sampling to certify the universal statement. In particular the constants for \(p=3/2\) are \(\|X\|=2^{1/3}\) and pairing supremum \(2^{1/6}\), while at \(p=3\) the row has the same sharp pair of values.

## Relationship to prior work
Calin, Cartwright, Coffman, Delfín, Girard, Goldrick, Nerella and Wu (2025 preprint; 2026 journal), Sections 3–5, define C*-like row-column modules, prove the block-diagonal theorem, and exhibit the same unital Hadamard-diagonal algebra failing at \(p=1\) through a different column with eigenvalues \((2,1)\) and \((1,2)\). They explicitly leave their Example 5.2 unresolved at non-Hilbert interior exponents. Here the **underlying algebra** is classified at every exponent, using complementary projections rather than asserting that their particular original column remains a witness. The matrix norm interpolation is standard; the strict all-exponent module-pairing comparison is the additional conclusion. Delfín's \(L^p\)-modules framework gives the general definition but not this classification.

## Limitations
This is a classification for one explicit two-dimensional unital commutative algebra and its finite row-column modules. It does not classify arbitrary unital matrix \(L^p\)-operator algebras and does not decide the fate of the specific, differently weighted column in Example 5.2 of the cited article. Source-priority checks cannot exclude unindexed or unpublished equivalent arguments. No independent audit has been performed.

## References
1. A. Calin, I. Cartwright, L. Coffman, A. Delfín, C. Girard, J. Goldrick, A. Nerella, W. Wu, *C*-like modules and matrix p-operator norms*, arXiv:2505.19471 (initially public 2025-05-26); *Annals of Functional Analysis* 17, article 30 (2026), doi:10.1007/s43034-025-00492-8. Full open-access text: https://link.springer.com/article/10.1007/s43034-025-00492-8.
2. A. Delfín, *L^p-modules and L^p-correspondences*, *Banach Journal of Mathematical Analysis* 20, article 13 (2026), doi:10.1007/s43037-025-00469-8.
3. Riesz–Thorin interpolation and Banach-space adjoint duality (standard results used explicitly in the proof).
