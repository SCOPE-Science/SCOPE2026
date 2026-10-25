# Sharp quasi-Schatten threshold for the Cesàro–Mellin square defect

## Finding
Let \(C\) be the Cesàro averaging operator on \(\ell^2(\mathbb N)\), with \(C_{nk}=n^{-1}\mathbf1_{\{k\le n\}}\), and let \(W_2\) denote the sampled Mellin convolution square of the Cesàro kernel, with \((W_2)_{nk}=n^{-1}\log(n/k)\mathbf1_{\{k\le n\}}\). Set \(D=C^2-W_2\). Then for **every real exponent** \(p>0\),
\[
D\in\mathcal S_p\quad\Longleftrightarrow\quad p>\frac12.
\]
The threshold includes the nonlocally convex quasi-Schatten range. Quantitatively, whenever \(\frac12<p\le1\),
\[
\zeta(2p)\le\|D\|_{\mathcal S_p}^{p}\le(1+2^{-p})\zeta(2p).
\]
Moreover, \(D\) is trace class and its Fredholm determinant and nonzero eigenvalues are
\[
\det(I-zD)=\prod_{n=1}^{\infty}(1-z/n^2)
=\frac{\sin(\pi\sqrt z)}{\pi\sqrt z},
\qquad \sigma(D)\setminus\{0\}=\{1/n^2:n\ge1\},
\]
with each nonzero eigenvalue algebraically simple. The trace-class inclusion and the trace \(\operatorname{Tr}D=\zeta(2)\) were obtained in earlier work; the result here is the **complete sharp \(p<1\) membership threshold**, its two-sided quantitative estimate, and the explicit spectral formulation for this same canonical defect.

## Assumptions and scope
The underlying space is the complex Hilbert space \(\ell^2(\mathbb N)\) with one-based standard basis \(e_1,e_2,\ldots\). The symbol \(\mathcal S_p\) denotes compact operators whose singular values have summable \(p\)-th powers, with the standard quasi-norm when \(0<p<1\). For \(p>0\), define \(\|T\|_{\mathcal S_p}^p=\sum_j s_j(T)^p\) whenever finite. \(\zeta\) is the Riemann zeta function. The matrix \(W_2\) arises from the multiplicative convolution \(\mathbf1_{(0,1]}\star\mathbf1_{(0,1]}(t)=\log(1/t)\mathbf1_{(0,1]}(t)\). Both constituent operators are bounded by the standard Cesàro theorem and the sampled Mellin operator theory of Bellavita–Stylogiannis. No regularity or finite-rank assumption on \(D\) is made.

## Proof
**1. Exact lattice correction and rank-one decomposition.** For all integers \(n,k\ge1\), direct matrix multiplication gives
\[
D_{nk}=\frac1n\left(H_n-H_{k-1}-\log\frac nk\right)\mathbf1_{\{k\le n\}},
\quad H_j=\sum_{r=1}^j\frac1r,\quad H_0=0.
\]
For each integer \(\ell\ge1\), introduce the positive number
\[
a_\ell=\frac1\ell-\log\left(1+\frac1\ell\right).
\]
The inequalities \(0<a_\ell\le(2\ell^2)^{-1}\) follow by writing \(a_\ell=t-\log(1+t)\) at \(t=1/\ell\) and integrating \(t/(1+t)\le t\). Splitting the harmonic sum into the last diagonal term and elementary logarithmic increments yields, for \(n\ge k\),
\[
D_{nk}=\frac1{n^2}+\frac1n\sum_{\ell=k}^{n-1}a_\ell.
\]
Define \(u_\ell=\sum_{n>\ell}n^{-1}e_n\), \(v_\ell=\sum_{k\le\ell}e_k\), and \(Q=\operatorname{diag}(1,2^{-2},3^{-2},\dots)\). The matrix identity is equivalent to the **exact trace-norm convergent decomposition**
\[
D=Q+\sum_{\ell=1}^{\infty}a_\ell\,u_\ell\otimes v_\ell^*.
\]
Indeed, \(\|v_\ell\|_2=\sqrt\ell\) and \(\|u_\ell\|_2^2=\sum_{n>\ell}n^{-2}\le1/\ell\), so \(\|u_\ell\otimes v_\ell^*\|_{\mathcal S_p}=\|u_\ell\|_2\|v_\ell\|_2\le1\) for every \(p>0\). Absolute trace-norm convergence follows from \(\sum_\ell a_\ell<\infty\), while \(Q\in\mathcal S_1\). Equality of the trace-norm sum with the matrix of \(D\) follows by checking every matrix coefficient. This also independently proves trace class without relying on the previously published result.

**2. Upper quasi-Schatten estimate.** For \(0<p\le1\), the Schatten quasi-norm obeys the \(p\)-power triangle inequality (the standard Rotfel'd inequality):
\[
\|A+B\|_{\mathcal S_p}^p\le\|A\|_{\mathcal S_p}^p+\|B\|_{\mathcal S_p}^p.
\]
For \(\frac12<p\le1\), apply it to finite partial sums of the decomposition and pass to the \(\mathcal S_p\) limit, obtaining
\[
\|D\|_{\mathcal S_p}^p\le\|Q\|_{\mathcal S_p}^p+\sum_{\ell\ge1}a_\ell^p
\le\zeta(2p)+2^{-p}\zeta(2p).
\]
The \(\mathcal S_p\) limit coincides with the \(\mathcal S_1\) limit because both imply convergence in operator norm. For \(p>1\), the already established inclusion \(D\in\mathcal S_1\subset\mathcal S_p\) suffices.

**3. Lower bound and sharp nonmembership.** Let \(P_N\) project onto \(\operatorname{span}\{e_1,\dots,e_N\}\), and let \(D_N=P_NDP_N\) be viewed as an \(N\)-by-\(N\) matrix. It is lower triangular with diagonal entries \(1,2^{-2},\dots,N^{-2}\); its eigenvalues are therefore precisely those numbers. In any finite-dimensional complex matrix, Weyl's eigenvalue–singular-value majorization gives, for every \(p>0\),
\[
\sum_{n=1}^N|\lambda_n(D_N)|^p\le\sum_{j=1}^Ns_j(D_N)^p.
\]
This follows from multiplicative log-majorization and convexity of the exponential, so is valid even for \(p<1\). Compression is contractive for every Schatten quasi-norm. Therefore, **if** \(D\in\mathcal S_p\),
\[
\sum_{n=1}^Nn^{-2p}\le\|D_N\|_{\mathcal S_p}^p\le\|D\|_{\mathcal S_p}^p.
\]
For \(p\le\frac12\), the left side diverges as \(N\to\infty\), proving nonmembership. For \(p>\frac12\), the same comparison and passage to the limit gives the asserted lower quantitative bound \(\zeta(2p)\le\|D\|_{\mathcal S_p}^p\). Together with Step 2, this proves the exact threshold.

**4. Fredholm determinant.** Because \(D\in\mathcal S_1\), its finite compressions \(D_N\) converge to \(D\) in trace norm. The determinants \(\det(I-zD_N)=\prod_{n=1}^N(1-z/n^2)\) converge locally uniformly in \(z\) to the Fredholm determinant. The classical Euler sine product gives \(\det(I-zD)=\sin(\pi\sqrt z)/(\pi\sqrt z)\), interpreted at \(z=0\) by its entire extension. The zeros of this determinant give the nonzero eigenvalues of \(D\) with their algebraic multiplicities. Thus they are exactly \(n^{-2}\) and are simple, as claimed. This step sharpens the spectral description of this one operator but is **not** needed for the \(p\)-threshold argument.

## Verification
The standalone file `verify_mellin_defect.py` uses only the Python standard library for rational harmonic-sum identities, coefficient bounds and finite lower-triangular identities; when NumPy is installed, it also compares finite singular values against eigenvalue power sums. Run `python3 verify_mellin_defect.py`. The supplementary computations checked 4,095 matrix-entry identities, 4,005 coefficient bounds, four finite compressions and 16 finite singular-value comparisons. These are checks of algebraic and numerical instances, **not** a proof for infinite-dimensional operators or all real exponents. The universal conclusions follow from the four analytical steps above.

## Relationship to prior work
Bellavita and Stylogiannis (2026, arXiv:2609.09453v1) introduced sampled Mellin operators and proved a general Hilbert–Schmidt multiplicativity defect, identifying Schatten improvements as a natural direction. The publicly available finding *Trace-class Mellin semigroup defects and zeta traces for Cesàro powers* (September 2026) already proves \(D\in\mathcal S_1\), \(\operatorname{Tr}D=\zeta(2)\) and trace-class results for the entire integer Mellin semigroup. The present finding **does not reclaim those earlier results**: it determines, for the canonical square defect, the exact critical exponent \(1/2\) within the quasi-Schatten scale, including both directions and quantitative \(\mathcal S_p\) bounds. That earlier account explicitly did not assert quasi-Schatten membership criteria below \(p=1\). Results on Schatten membership of Rhaly matrices (Bellavita–Dellepiane–Stylogiannis 2025, 2026) concern related triangular operators but not this cancellation defect. For comparison, the published cubic Schatten decay of the *Cesàro self-commutator* concerns the distinct operator \(C^*C-CC^*\), not the lattice Mellin square defect \(C^2-W_2\).

## Limitations
The threshold is established only for this specific square defect, not every convolution pair in the sampled Mellin algebra and not arbitrary Cesàro power defects. The proof determines class membership and a uniform norm bracket, **not** a leading coefficient for individual singular values or the full singular-value distribution. The eigenvalue formula follows from the triangular diagonal and trace-class approximation, and by itself does not determine singular values. A residual possibility of equivalent older or unindexed triangular-matrix/quasi-Schatten results remains; no independent publication-priority or scientific audit has been performed.

## References
1. C. Bellavita and G. Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453v1, first posted 2026-09-08, https://arxiv.org/abs/2609.09453.
2. *Trace-class Mellin semigroup defects and zeta traces for Cesàro powers*, public mathematical research finding (2026), https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-zeta-trace-cesaro-mellin-defects--b8e60639c683. The \(\mathcal S_1\) and zeta-trace result is prior art.
3. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930v1, https://arxiv.org/abs/2503.21930.
4. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875v1, https://arxiv.org/abs/2606.15875.
5. *Cubic spectral decay of the classical Cesàro self-commutator*, public mathematical research finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-cubic-spectral-decay-of-the-classical-ces-ro-self-commutator--1d9ae52b1d38.
