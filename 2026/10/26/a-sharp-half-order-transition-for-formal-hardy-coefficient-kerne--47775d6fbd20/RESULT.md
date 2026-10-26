# A sharp half-order transition for formal Hardy coefficient kernels with atomless Herglotz data

## Finding

Let \(0<\alpha<1\), choose pairwise distinct \(\lambda_j\in\mathbb T\) and strictly positive \(w_j\) with \(W:=\sum_{j\ge1}w_j<\infty\), and define
\[
\phi_\alpha(z)=\sum_{j\ge1}w_j(1-\lambda_jz)^{-\alpha},\qquad
c_n=\frac{(\alpha)_n}{n!},\qquad
\gamma_n=c_n\sum_{j\ge1}w_j\lambda_j^n.
\]
Powers use the principal holomorphic branch. On \(H^2(\mathbb D)\), define the **maximal ordinary-series coefficient transform** \(\mathcal F_\alpha\) by
\[
(\mathcal F_\alpha f)_m=\lim_{N\to\infty}\sum_{n=m}^N\overline{\gamma_{n-m}}\widehat f(n),\quad m=0,1,\ldots.
\]
Its domain consists exactly of \(f\in H^2\) for which all these ordinary limits exist and form an \(\ell^2\) sequence; no Abel summation or closed-operator extension is silently substituted.

The following dichotomy is exact:

* If \(0<\alpha<1/2\), then \(\ker\mathcal F_\alpha=\{0\}\).
* If \(1/2\le\alpha<1\), then for every polynomial \(p\), every \(\varepsilon>0\), and every integer \(N\) strictly greater than \(\deg p\), there is \(f\in\ker\mathcal F_\alpha\) with \(\widehat f(n)=\widehat p(n)\) for \(0\le n<N\) and \(\|f-p\|_{H^2}<\varepsilon\). In fact, the closure of the graph of \(\mathcal F_\alpha\) is \(H^2\oplus H^2\).

For all \(0<\alpha<1\), \(\operatorname{Re}\phi_\alpha\) is strictly positive and its Herglotz representing measure has **no atoms**. This separates the dense-kernel phenomenon from the purely atomic construction of [R2]. If \(\phi_\alpha=b_\alpha/a_\alpha\) is its Pythagorean representation, then \(\ker\mathcal F_\alpha\cap\mathcal H(b_\alpha)=\{0\}\).

## Assumptions and scope

The ambient Hilbert space is complex \(H^2(\mathbb D)\), identified isometrically with \(\ell^2(\mathbb N_0)\) by Taylor coefficients. The sequence of phases is arbitrary apart from pairwise distinctness: the phases may accumulate anywhere and may be dense in \(\mathbb T\). The positive weights are absolutely summable; no angular separation or decay rate beyond summability is assumed. The nontrivial finite-rank matrices appearing in the construction use only finitely many distinct phases at a time. The result concerns **ordinary coordinatewise series** and not the canonical closed Smirnov Toeplitz operator, whose domain and graph are different [R1,R3].

## Proof

**1. Fractional coefficients and the analytic boundary.** The binomial formula gives the stated \(\gamma_n\). For \(0<\alpha<1\), the strictly positive sequence \((c_n)\) is decreasing, since
\[
\frac{c_{n+1}}{c_n}=\frac{n+\alpha}{n+1}<1,
\]
and Stirling's formula gives \(c_n\sim n^{\alpha-1}/\Gamma(\alpha)\). Thus
\[
\sum_{n\ge0}c_n^2<\infty\iff\alpha<1/2;
\qquad\sum_{n\ge0}c_n^2=\infty\iff\alpha\ge1/2.
\]
Since \(\lvert\gamma_n\rvert\le Wc_n\), the symbol belongs to \(H^2\) in the first regime. Moreover, \(\operatorname{Re}(1-\lambda z)^{-\alpha}\ge2^{-\alpha}\cos(\pi\alpha/2)>0\) in the disk. Hence \(\phi_\alpha\) has positive real part bounded away from zero, is in the Smirnov class and is outer (alternatively use the standard positive-real-part Hardy estimates, followed by \(1/\phi_\alpha\in H^\infty\)). If \(f\in\ker\mathcal F_\alpha\) when \(\alpha<1/2\), Cauchy--Schwarz makes every defining row absolutely convergent, and
\[
0=(\mathcal F_\alpha f)_m=\langle f,z^m\phi_\alpha\rangle_{H^2}\quad\text{for all }m\ge0.
\]
Outerness implies that polynomial multiples of \(\phi_\alpha\) are dense in \(H^2\), whence \(f=0\).

**2. Uniform weighted block averaging.** Fix \(\alpha\ge1/2\), integers \(N\ge m\ge0\), and one index \(j\). Write \(B_L=\sum_{n=N}^{N+L-1}c_n^2\), so \(B_L\to\infty\), and \(B_t=\sum_{n=N}^{N+t-1}c_n^2\) for \(0\le t\le L\). We claim
\[
\sup_{0\le t\le L}\left|\frac{1}{B_L}
\sum_{n=N}^{N+t-1}\gamma_{n-m}c_n\lambda_j^{-n}
- w_j\lambda_j^{-m}\frac{B_t}{B_L}\right|\longrightarrow0.
\tag{1}
\]
For the diagonal frequency \(\lambda_j\), compare \(c_{n-m}c_n\) to \(c_n^2\). Monotonicity and telescoping show, uniformly in \(t\),
\[
0\le\sum_{n=N}^{N+t-1}c_n(c_{n-m}-c_n)
\le c_N\sum_{r=N-m}^{N-1}c_r=:D_{N,m}<\infty.
\]
The normalized discrepancy vanishes. For \(\ell\ne j\), let \(\rho=\lambda_\ell/\lambda_j\ne1\), and put \(q_n=c_{n-m}c_n\), a positive decreasing sequence. Abel summation of the geometric progression gives
\[
\left|\sum_{n=N}^{N+t-1}q_n\rho^n\right|
\le\min\left\{\sum_{n=N}^{N+t-1}q_n,\;\frac{2q_N}{|1-\rho|}\right\}.
\]
Dividing by \(B_L\), the second bound tends to zero for any fixed \(\ell\ne j\); the first is at most \(1+D_{N,m}/B_L\), uniformly in \(t\). Summability of the \(w_\ell\) and dominated convergence therefore make the sum of **all** off-diagonal frequencies \(o(B_L)\), even if the phases have arbitrarily close pairs or dense accumulation. Together these prove (1). The convergence is uniform over any preassigned finite set of \(m,j\).

**3. Prescribing a finite Taylor jet with vanishing output.** Start with an arbitrary polynomial \(p\), \(\varepsilon>0\), and \(N_0>\deg p\); increase \(N_0\) to at least \(1\). We construct coefficients \(u_n\in\ell^2\) whose first \(N_0\) entries are \(u_n=\overline{\widehat p(n)}\), and for which \(\sum_{n=m}^\infty\gamma_{n-m}u_n=0\) for each \(m\ge0\). The desired function is then \(f(z)=\sum_{n\ge0}\overline{u_n}z^n\).

Inductively suppose \(u_n\) is defined for \(n<N_M\), where \(N_M\ge M+1\). Put
\[
R_m=\sum_{n=m}^{N_M-1}\gamma_{n-m}u_n\quad(0\le m\le M).
\]
Distinctness of \(\lambda_1,\ldots,\lambda_{M+1}\) makes the weighted Vandermonde system
\[
\sum_{j=1}^{M+1}w_j\lambda_j^{-m}d_j=-R_m,
\quad m=0,\ldots,M,
\tag{2}
\]
uniquely solvable. Let \(C_M=\sum_{j=1}^{M+1}|d_j|\). With \(N=N_M\) fixed, use (1) and \(B_L\to\infty\) to choose one finite integer \(L_M\ge2\) so large that, simultaneously for \(0\le m\le M\), \(1\le j\le M+1\), and \(0\le t\le L_M\), the error in (1) is at most \(2^{-M-4}/(1+C_M)\), and
\[
C_M^2/B_{L_M}<\varepsilon^2 2^{-2M-4}.
\tag{3}
\]
For \(N_M\le n<N_M+L_M\) put
\[
u_n=\frac{c_n}{B_{L_M}}\sum_{j=1}^{M+1}d_j\lambda_j^{-n},
\qquad N_{M+1}=N_M+L_M.
\]
Using (1),(2), the row partial sum at every point inside this entire block equals
\[
\sum_{n=m}^{N_M+t-1}\gamma_{n-m}u_n
=\left(1-\frac{B_t}{B_{L_M}}\right)R_m+E_{M,m}(t),
\qquad |E_{M,m}(t)|\le2^{-M-4}.
\tag{4}
\]
At the block endpoint, each of the first \(M+1\) residuals has modulus at most \(2^{-M-4}\). For fixed \(m\), the residual at the start of every sufficiently late block was controlled by the preceding block, and (4) bounds every intermediate partial sum by a quantity tending to zero. Thus all the **ordinary** coefficient series converge to zero, not just a selected subsequence.

The square norm contributed by the \(M\)-th block satisfies, by the triangle inequality,
\[
\sum_{n=N_M}^{N_{M+1}-1}|u_n|^2
\le\frac{C_M^2}{B_{L_M}}<\varepsilon^2 2^{-2M-4}.
\]
Summing over \(M\ge0\) proves \(\|f-p\|_{H^2}<\varepsilon\). Every prescribed initial coefficient is unchanged, and \(\mathcal F_\alpha f=0\). Since polynomials are dense in \(H^2\), the kernel is dense.

**4. Full graph closure and atomless representation.** On polynomials of degree at most \(d\), the transform is triangular with nonzero diagonal \(\overline{\gamma_0}=W\), so it maps that finite-dimensional polynomial space bijectively onto itself. For any polynomial output \(h\), choose polynomial input \(p\) with \(\mathcal F_\alpha p=h\), and approximate \(p\) in \(H^2\) by zero-output inputs \(f_k\). Then \(p-f_k\to0\) but \(\mathcal F_\alpha(p-f_k)=h\). The closed graph therefore contains \(\{0\}\oplus H^2\); density of the kernel supplies \(H^2\oplus\{0\}\). Their sum is the entire product.

The positive harmonic function \(\operatorname{Re}\phi_\alpha\) has a finite Herglotz representing measure \(\nu_\alpha\). For each \(\zeta\in\mathbb T\),
\[
|\phi_\alpha(r\zeta)|\le W(1-r)^{-\alpha},\qquad
(1-r)\operatorname{Re}\phi_\alpha(r\zeta)\longrightarrow0.
\]
The atomic recovery formula for the Poisson integral therefore gives \(\nu_\alpha(\{\zeta\})=0\) at every boundary point: the entire representing measure is atomless. Finally, \(\phi_\alpha=b_\alpha/a_\alpha\) has a Pythagorean pair with outer \(b_\alpha\). By the positive-real-part coefficient identity in [R2, Theorem 2.1], if a kernel vector \(f\) belonged to \(\mathcal H(b_\alpha)\), its associated \(H^2\)-partner would vanish. Then \(T_{\overline{b_\alpha}}f=0\), which forces \(f=0\) because \(b_\alpha\) is outer.

## Verification

All critical steps are explicit analytic estimates: the gamma-ratio square-summability threshold, the finite weighted Vandermonde determinant, the Abel/geometric bound, dominated convergence with summable weights, uniform-in-block residual convergence, and the convergent sum of tail \(H^2\) norms. The series are ordinary partial sums; no finite computation is used as a substitute for infinite convergence. A numerical illustration with four distinct phases and \(\alpha=1/2\) showed normalized off-diagonal block errors decreasing when the block length increased from \(10^3\) to \(1.5\times10^5\); at \(\alpha=3/4\) the same normalized errors decreased more rapidly. Such finite illustrations do not establish (1), which is proved above.

## Relationship to prior work

Ransford [R2, Theorem 3.1] gives a single coefficient-kernel counterexample whose positive-real symbol is a sum of **ordinary simple poles** with explicitly separated dyadic phases. The present theorem concerns instead an entire fractional-power family, arbitrary distinct phases with possible dense accumulation, a sharp threshold including the half-order endpoint, and **atomless** Herglotz measures. The distinction is not a renaming of the atomic theorem: its measure-atom hypothesis is false here. The proof adapts the finite Vandermonde cancellation principle but replaces bounded angular separation by weighted Abel summation and square-sum divergence. Ransford [R1, Theorem 3.1] covers the injective \(H^2\)-symbol regime, but not the dense-kernel half. Łanucha and Nowak [R3] analyze individual fractional symbols and canonical closed operators, not the arbitrary infinite-mode ordinary-series graph described here. No claim is made about uniqueness of this conclusion in unindexed historical sources.

## Limitations

The dense-kernel assertion requires infinitely many distinct nonzero phases and positive summable weights. The theorem does not classify finite-mode fractional sums, arbitrary non-pure-point phase distributions, exponents outside \((0,1)\), or the domain of the canonical closed Smirnov Toeplitz operator. Its graph-closure assertion refers only to the explicitly specified maximal coordinatewise ordinary-series transform. Historical-priority searches cannot exclude every alternative formulation, especially older unbounded Toeplitz literature.

## References

[R1] T. Ransford, *On the coefficient formula for de Branges–Rovnyak norms*, arXiv:2605.30114v1 (first public 2026-05-28), https://arxiv.org/abs/2605.30114.

[R2] T. Ransford, *A counterexample concerning the coefficient formula for de Branges–Rovnyak norms*, arXiv:2610.15019v1 (first public 2026-10-10), https://arxiv.org/abs/2610.15019.

[R3] B. Łanucha and M. T. Nowak, *Examples of de Branges–Rovnyak spaces generated by nonextreme functions*, Ann. Acad. Sci. Fenn. Math. 44 (2019), 449–457, doi:10.5186/aasfm.2019.4427.
