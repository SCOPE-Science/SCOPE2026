# A lattice Weyl constant for power-decaying Rhaly matrices

## Finding

For every real \(\gamma>1\), let \(R_\gamma:\ell^2(\mathbb N;\mathbb C)\to\ell^2(\mathbb N;\mathbb C)\) be the positive-coefficient Rhaly (terraced) matrix
\[
(R_\gamma x)_j=j^{-\gamma}\sum_{k=1}^{j}x_k,\qquad j\ge1.
\]
Write \(s_1(R_\gamma)\ge s_2(R_\gamma)\ge\cdots>0\) for its singular values, with multiplicities, and put
\[
\mathsf C_\gamma
=\frac1\pi\int_0^\pi\bigl(2\sin(\theta/2)\bigr)^{-1/\gamma}\,d\theta
=\frac{2^{-1/\gamma}}{\sqrt\pi}
\frac{\Gamma((\gamma-1)/(2\gamma))}{\Gamma(1-1/(2\gamma))}.
\]
Then the **sharp singular-value Weyl law** is
\[
\boxed{\lim_{n\to\infty}n^\gamma s_n(R_\gamma)=\mathsf C_\gamma^\gamma.}
\]
Consequently \(R_\gamma\in\mathcal S_p\) exactly when \(p>1/\gamma\), for every \(0<p<\infty\); at the critical exponent
\[
\lim_{N\to\infty}\frac1{\log N}
\sum_{n=1}^{N}s_n(R_\gamma)^{1/\gamma}=\mathsf C_\gamma.
\]
In particular, the positive weak-trace-class operator \(|R_\gamma|^{1/\gamma}\) has a unique normalized logarithmic spectral residue \(\mathsf C_\gamma\). For example, when \(\gamma=2\), the singular-value coefficient is \(\mathsf C_2^2\approx1.393203929685678\).

## Assumptions and scope

The underlying scalar field is \(\mathbb C\), and index \(j\) starts at one. The exponent is fixed and strictly greater than one. Singular values are the eigenvalues of \(|R_\gamma|=(R_\gamma^*R_\gamma)^{1/2}\) arranged nonincreasingly. Schatten membership for \(p<1\) refers to the usual quasi-ideal. No assertion is made at \(\gamma=1\), where the classical discrete Cesàro operator is not compact. The result is specifically for *discrete* summation and is not a continuous Volterra singular-value formula.

## Proof

**1. Compact embedding and the inverse difference form.** The squared Hilbert--Schmidt norm is
\[
\sum_{j=1}^\infty\sum_{k=1}^{j}j^{-2\gamma}
=\sum_{j=1}^\infty j^{1-2\gamma}
=\zeta(2\gamma-1)<\infty.
\]
Hence \(R_\gamma\) is compact. Let \(\mathcal H\) be the completion of finitely supported sequences \(w=(w_j)_{j\ge1}\), with \(w_0=0\), for the energy
\[
q(w)=\sum_{j\ge1}|w_j-w_{j-1}|^2.
\]
Its elements are precisely the prefix sums \(w_j=\sum_{k\le j}x_k\) of \(x\in\ell^2\): finite sequences with total sum zero are dense in \(\ell^2\) (a finite vector's total sum can be cancelled by distributing an arbitrarily small \(\ell^2\)-norm correction over a distant long block). Thus \(x\mapsto w\) is a unitary map from \(\ell^2\) to \(\mathcal H\). Define
\[
m_\gamma(w)=\sum_{j\ge1}j^{-2\gamma}|w_j|^2.
\]
The operator \(R_\gamma\) is this weighted embedding, in the unitary coordinates. Cauchy--Schwarz gives \(|w_j|^2\le j q(w)\); therefore \(m_\gamma(w)\le\zeta(2\gamma-1)q(w)\). Its weighted tail is bounded by \(q(w)\sum_{j>M}j^{1-2\gamma}\to0\), proving compactness directly and showing that the generalized Rayleigh spectrum \(q(w)/m_\gamma(w)\) has eigenvalues \(0<\lambda_1\le\lambda_2\le\cdots\uparrow\infty\) with \(\lambda_n=s_n(R_\gamma)^{-2}\).

**2. Reduction to a long finite string.** For \(\Lambda>0\), denote by \(\mathcal N_\gamma(\Lambda)\) the number of those generalized eigenvalues not exceeding \(\Lambda\), counting multiplicity. Write \(R=\Lambda^{1/(2\gamma)}\). Choose any \(\kappa>\gamma/(\gamma-1)\) and integer \(M=\lceil R^\kappa\rceil\). On the first \(M\) sites consider the free-right quadratic form
\[
q_M^N(w)=\sum_{j=1}^{M}|w_j-w_{j-1}|^2
\]
with weighted denominator \(\sum_{j=1}^{M}j^{-2\gamma}|w_j|^2\), and let \(\mathcal N_M^N(\Lambda)\) be its counting function. Deleting the one edge between sites \(M\) and \(M+1\) makes the full form the orthogonal direct sum of this finite form and a free-left tail form
\[
q_{>M}^N(w)=\sum_{j=M+2}^\infty |w_j-w_{j-1}|^2.
\]
The latter has at most one eigenvalue below \(\Lambda\): indeed on its codimension-one subspace \(w_{M+1}=0\), Cauchy--Schwarz yields
\[
\sum_{j>M}j^{-2\gamma}|w_j|^2
\le q_{>M}^N(w)\sum_{j>M+1}(j-M-1)j^{-2\gamma}
\le C_\gamma M^{2-2\gamma}q_{>M}^N(w),
\]
where \(C_\gamma<\infty\) is independent of \(M\). By the choice of \(\kappa\), \(\Lambda C_\gamma M^{2-2\gamma}\to0\); min--max and the codimension-one condition prove the assertion. For the opposite comparison, extend vectors on the first \(M\) sites by zero: only the boundary term \(|w_M|^2\) is added to \(q_M^N\), a rank-one change. Edge deletion and rank-one interlacing therefore give, for large \(\Lambda\),
\[
\mathcal N_M^N(\Lambda)-1
\le\mathcal N_\gamma(\Lambda)
\le\mathcal N_M^N(\Lambda)+1.
\]
Here \(C_\gamma\) is an auxiliary inequality constant, distinct from \(\mathsf C_\gamma\).

**3. Elementary path dispersion on geometric blocks.** Fix \(\varepsilon>0\) and \(\delta>0\). Set aside the first \(\lfloor\varepsilon R\rfloor\) sites and partition the remaining indices up to \(M\) into consecutive intervals whose endpoint ratios are at most \(1+\delta+o(1)\). A geometric partition has \(O_{\varepsilon,\delta}(\log R)\) intervals because \(M\) is a fixed polynomial in \(R\). Deleting their joining edges changes the number of eigenvalues below \(\Lambda\) by at most one per deleted edge (finite-dimensional min--max for a rank-one positive form). The initial discarded block contributes at most \(\varepsilon R+1\) eigenvalues.

On a block \(I=[a,b]\) of length \(h=b-a+1\), the weight in the denominator lies between \(b^{-2\gamma}\) and \(a^{-2\gamma}\). The unweighted Neumann path Laplacian, whose form is \(\sum_{j=a+1}^b|w_j-w_{j-1}|^2\), has eigenvalues
\[
4\sin^2\!\left(\frac{\pi k}{2h}\right),\qquad 0\le k<h.
\]
Define the continuous nondecreasing function
\[
F(u)=\begin{cases}(2/\pi)\arcsin(u/2),&0\le u\le2,\\1,&u\ge2.\end{cases}
\]
The number of its eigenvalues not exceeding \(u^2\) is \(hF(u)+O(1)\), with an absolute error at most two. Comparison of denominators sandwiches the block counting function between
\[
hF((R/b)^\gamma)-2
\quad\text{and}\quad
hF((R/a)^\gamma)+2.
\]
Summing these bounds, then sending \(R\to\infty\), \(\delta\downarrow0\), and \(\varepsilon\downarrow0\), gives
\[
\lim_{\Lambda\to\infty}
\frac{\mathcal N_\gamma(\Lambda)}{\Lambda^{1/(2\gamma)}}
=\int_0^\infty F(x^{-\gamma})\,dx.
\]
Here the Riemann-sum passage is justified on compact positive \(x\)-intervals by continuity of \(F\). The small-\(x\) piece contributes at most its length; the large-\(x\) tail is uniformly bounded by a constant multiple of \(\int_L^\infty x^{-\gamma}dx\), since \(F(u)\le u/2\) for \(u\le2\). Both vanish on taking the corresponding endpoints to zero and infinity. The \(O(\log R)\) joining-edge and individual-block counting errors are \(o(R)\).

**4. Exact constant and inversion.** The path phase formula is
\[
F(u)=\frac1\pi\bigl|\{\theta\in[0,\pi]:2\sin(\theta/2)\le u\}\bigr|.
\]
Tonelli's theorem therefore gives
\[
\int_0^\infty F(x^{-\gamma})dx
=\frac1\pi\int_0^\pi\int_0^{(2\sin(\theta/2))^{-1/\gamma}}dx\,d\theta
=\mathsf C_\gamma.
\]
The beta integral evaluates this as the gamma quotient in the finding. Since \(\mathcal N_\gamma(\Lambda)\sim\mathsf C_\gamma\Lambda^{1/(2\gamma)}\) and the spectrum is discrete, its monotone inverse satisfies \(\lambda_n\sim(n/\mathsf C_\gamma)^{2\gamma}\), hence \(s_n(R_\gamma)=\lambda_n^{-1/2}\sim\mathsf C_\gamma^\gamma n^{-\gamma}\). A comparison with the power series \(\sum n^{-\gamma p}\) proves the Schatten criterion; the harmonic-series asymptotic proves the logarithmic residue.

## Verification

The embedded standalone program `check_rhaly_weyl.py` evaluates the gamma-integral identity and counts finite generalized eigenvalues by a tridiagonal Sturm recurrence, for several exponents and cutoffs. It checks the predicted phase-space constant against finite-string counts and separately checks finite matrix Hilbert--Schmidt identities. These tests are finite diagnostics only. The theorem and exact constant follow from the complete infinite-dimensional variational and bracketing argument above.

## Relationship to prior work

Bellavita, Dellepiane, and Stylogiannis developed compactness, approximation-number comparisons, and Schatten-class membership criteria for Rhaly matrices, including results on weighted Hardy spaces. Their quantified comparison of approximation numbers with dyadic weight blocks does not provide the sharp individual \(n^{-\gamma}\) singular-value coefficient calculated here. The discrete dispersion \(2\sin(\theta/2)\) is essential: continuous weighted Volterra asymptotics do not supply this lattice coefficient. Published work on unbounded Jacobi matrices offers neighboring spectral methods, but no identified inspected theorem settles this particular critical weighted-difference string's coefficient. The claim is the power-weighted discrete Rhaly limit above, not those pre-existing general boundedness, compactness, or ideal-membership criteria.

## Limitations

The asymptotic is for each fixed \(\gamma>1\), not uniform as \(\gamma\downarrow1\); it gives no finite-rank error bound or eigenvector asymptotic and does not classify arbitrary Rhaly weights. The June 2026 related paper and some general unbounded-Jacobi literature could not be compared in complete text; unindexed or more general spectral results remain a priority risk.

## References

1. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875 (first submitted 14 June 2026).
2. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930v3; J. London Math. Soc. 112 (2025), e70304.
3. W. D. Evans, D. J. Harris, J. Lang, *The Approximation Numbers of Hardy-Type Operators on Trees*, Proc. London Math. Soc. 83 (2001), 390--418.
4. J. Janas, S. Naboko, *Infinite Jacobi Matrices with Unbounded Entries: Asymptotics of Eigenvalues and the Transformation Operator Approach*, SIAM J. Math. Anal. 36 (2004), 643--658.
