# A single operator tuple attains completely bounded distortion through Shalit–Shamovich radii
## Finding
Let \(\mathcal E_1\) and \(\mathcal E_2\) be operator-space structures on \(\mathbb C^d\), and set
\[
c=\|\mathrm{id}:\mathcal E_1\to\mathcal E_2\|_{\mathrm{cb}}.
\]
Then there is one bounded operator \(d\)-tuple \(T=(T_1,\ldots,T_d)\) on a separable Hilbert space for which
\[
\rho_{\mathcal E_1}(T)=\rho^{\min}_{\mathcal E_1}(T)=1,
\qquad
\rho_{\mathcal E_2}(T)=\rho^{\min}_{\mathcal E_2}(T)=c.
\]
Consequently
\[
c=
\frac{\rho_{\mathcal E_2}(T)}{\rho_{\mathcal E_1}(T)}
=
\frac{\rho^{\min}_{\mathcal E_2}(T)}{\rho^{\min}_{\mathcal E_1}(T)}.
\]
Thus completely bounded distortion is attained by a single infinite-dimensional spectral witness, even when the supremum defining the completely bounded norm need not be attained at any fixed matrix level.

## Assumptions and scope
The underlying vector space is finite-dimensional, with \(d\ge 1\). No selfadjointness, common underlying Banach norm, or finite-level attainment hypothesis is assumed. Since the spaces are finite-dimensional operator spaces, the identity map is completely bounded and \(0<c<\infty\).

For a matrix tuple \(X=(X_1,\ldots,X_d)\in M_n(\mathbb C)^d\), write \(\|X\|_{\mathcal E}\) for its matrix norm in \(M_n(\mathcal E)\). Tornes's Theorem 3.1 associates to each such \(X\) a bounded operator tuple \(T_X\) with exact power identities whose ordinary and minimal Shalit–Shamovich radii satisfy
\[
\rho_{\mathcal E}(T_X)=\rho^{\min}_{\mathcal E}(T_X)=\|X\|_{\mathcal E}
\]
for every operator-space structure \(\mathcal E\) on \(\mathbb C^d\).

## Proof
Choose matrix tuples \(X^{(r)}\in M_{n_r}(\mathbb C)^d\), for \(r\ge 1\), such that
\[
\|X^{(r)}\|_{\mathcal E_1}=1,
\qquad
\|X^{(r)}\|_{\mathcal E_2}>c-\frac1r.
\]
They exist by the definition of the completely bounded norm. For each \(r\), apply Tornes's construction to \(X^{(r)}\), obtaining \(T^{(r)}=T_{X^{(r)}}\) on a separable Hilbert space \(K_r\).

The direct sum is bounded. Indeed, for each coordinate \(j\), the scalar coordinate functional on \(\mathcal E_1\) is completely bounded, so there is a finite constant \(a_j\) with
\[
\|X_j^{(r)}\|\le a_j\|X^{(r)}\|_{\mathcal E_1}=a_j
\]
for every \(r\). In Tornes's construction the coordinate operator of \(T_{X^{(r)}}\) has norm \(\|X_j^{(r)}\|\). Hence
\[
T_j=\bigoplus_{r=1}^{\infty}T_j^{(r)}
\]
defines a bounded operator on \(K=\bigoplus_{r=1}^{\infty}K_r\), and \(K\) is separable.

Fix an operator-space structure \(\mathcal E\). The word operator appearing in the \(m\)-th power formula for either the Haagerup or minimal Shalit–Shamovich radius of \(T\) is block diagonal with \(r\)-th block equal to the corresponding word operator for \(T^{(r)}\). Tornes's exact power identities therefore give, for every integer \(m\ge1\),
\[
\left\|\text{the \(m\)-th Haagerup word operator for \(T\)}\right\|
=
\sup_r\|X^{(r)}\|_{\mathcal E}^{m},
\]
and the same equality for the minimal tensor version. Taking \(m\)-th roots yields
\[
\rho_{\mathcal E}(T)=\rho^{\min}_{\mathcal E}(T)
=
\sup_r\|X^{(r)}\|_{\mathcal E}.
\]
For \(\mathcal E=\mathcal E_1\), the right-hand side equals \(1\). For \(\mathcal E=\mathcal E_2\), every normalized tuple has norm at most \(c\), while the chosen sequence approaches \(c\); hence the supremum is exactly \(c\). This proves all asserted equalities.

## Verification
The argument is symbolic and does not rely on finite numerical experiments. The critical imported statement is the exact all-powers identity in Tornes's Theorem 3.1, not merely its limiting corollary. The remaining steps are the definition of the completely bounded norm, the standard fact that scalar-valued bounded functionals on an operator space are completely bounded with the same norm, and the norm formula for block-diagonal direct sums.

Boundary checks are immediate: \(d=1\) is allowed; the completely bounded norm is positive because the identity is injective; and failure of finite-level norm attainment causes no difficulty because a maximizing sequence is packed into the single direct-sum tuple.

## Relationship to prior work
Tornes proves that for each prescribed tuple \(X\) there is a tuple \(T_X\) satisfying \(\rho_{\mathcal E}(T_X)=\rho^{\min}_{\mathcal E}(T_X)=\|X\|_{\mathcal E}\) for every operator-space structure, and deduces the qualitative conclusion that equality of the spectral-radius functions on all operator tuples forces complete isometry. The present statement diagonalizes a completely bounded norming sequence and shows that one operator tuple attains the full quantitative distortion simultaneously for the ordinary and minimal radii.

Shalit and Shamovich introduced the operator-space spectral radius and proved its simultaneous-similarity characterization. Scherer, Shalit, and Shamovich studied dependence on the quantization and supplied the question answered by Tornes. Targeted searches for a single-tuple attainment formula for completely bounded distortion did not locate a covering statement.

## Limitations
The result is an existence-and-construction theorem for a separable infinite-dimensional witness. It does not assert that the completely bounded norm is attained at a finite matrix level, nor that a finite-dimensional operator tuple can always realize the same ratio. The direct-sum witness depends on the ordered pair \(\mathcal E_1,\mathcal E_2\) through a norming sequence.

## References
1. Maximilian Tornes, *On the Shalit–Shamovich Spectral Radius*, arXiv:2610.00816v1, 2026, especially Theorem 3.1 and the complete-isometry corollary.
2. Orr M. Shalit and Eli Shamovich, *A spectral radius for matrices over an operator space*, arXiv:2501.01325v1; *Advances in Mathematics* 479 (2025), 110449.
3. Florian Scherer, Orr Shalit, and Eli Shamovich, *On the spectral radius of operator tuples*, arXiv:2605.09354v1, 2026.
