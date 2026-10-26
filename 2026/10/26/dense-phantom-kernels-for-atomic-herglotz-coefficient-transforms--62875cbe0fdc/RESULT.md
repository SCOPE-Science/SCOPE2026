# Dense phantom kernels for atomic Herglotz coefficient transforms

## Finding

Let \(\mu\) be any Borel probability measure on the unit circle \(\mathbb T\) with infinitely many distinct atoms of positive mass. Put
\[
\phi(z)=\int_{\mathbb T}\frac{d\mu(\zeta)}{1-\zeta z},\qquad
\gamma_n=\int_{\mathbb T}\zeta^n\,d\mu(\zeta)\quad(n\geq0).
\]
The real part of \(\phi\) is at least \(1/2\); \(\phi\) is outer and belongs to \(H^p\) for every \(0<p<1\). Let \(\phi=b/a\) be its canonical Pythagorean representation, with \(a,b\) outer. Define the **formal coefficient transform** \(\mathcal T_\mu\) on the domain of \(f(z)=\sum_{n\geq0} f_nz^n\in H^2\) for which every ordinary (in increasing-index order) series below converges and the resulting coefficients belong to \(\ell^2\):
\[
(\mathcal T_\mu f)_m=\sum_{n=0}^{\infty}\overline{\gamma_n}\,f_{m+n}\quad(m\geq0).
\]
Then the following statements hold simultaneously.

**Prescribed-jet dense kernel.** For every analytic polynomial \(P\) and every \(\varepsilon>0\), a function \(f\in\ker\mathcal T_\mu\) exists whose Taylor coefficients equal those of \(P\) in all degrees up to \(\deg P\), and for which \(\|f-P\|_{H^2}<\varepsilon\). In particular, \(\ker\mathcal T_\mu\) is dense in \(H^2\), and \(\ker\mathcal T_\mu\cap\mathcal H(b)=\{0\}\).

**Maximal failure of graph closability.** The closure in \(H^2\oplus H^2\) of the graph of \(\mathcal T_\mu\) is exactly \(H^2\oplus H^2\). Equivalently, for any prescribed \(g,h\in H^2\), there are admissible \(f_k\to g\) such that \(\mathcal T_\mu f_k\to h\). Thus the coefficient transform is maximally nonclosable in the graph sense. This is a statement about the coordinatewise-series realization above, **not** about the standard closed Smirnov-class coanalytic Toeplitz operator.

## Assumptions and scope

No separation, periodicity or finite-type hypothesis is imposed on the infinitely many distinct atoms of \(\mu\). Their masses may decay arbitrarily fast; further nonatomic mass is allowed. Every sum defining \(\mathcal T_\mu\) is an ordinary increasing-index series, and its entire output must lie in \(H^2\). Zero outputs therefore automatically satisfy the range requirement. The ambient Hardy-space norm is \(\|f\|_{H^2}^2=\sum_{n\geq0}|f_n|^2\). The associated de Branges–Rovnyak space \(\mathcal H(b)\) has its standard range norm. Atoms are enumerated without repetition as \((\zeta_j,w_j)_{j\geq1}\), with \(w_j=\mu(\{\zeta_j\})>0\).

## Proof

**1. Herglotz and outer facts.** For every \(\zeta\in\mathbb T\) and \(z\in\mathbb D\),
\[
\operatorname{Re}\frac1{1-\zeta z}=
\frac12+\frac{1-|z|^2}{2|1-\zeta z|^2}\ge\frac12.
\]
Integration gives \(\operatorname{Re}\phi\ge1/2\), \(\phi(0)=\gamma_0=1\), and \(1/\phi\in H^\infty\). For \(0<p<1\), the principal analytic power obeys \(\operatorname{Re}(\phi^p)\ge\cos(\pi p/2)|\phi|^p\). Its circle mean is \(1\) by the mean-value property, so \(\phi\in H^p\subset N^+\). Membership in a Hardy class together with a bounded analytic inverse makes \(\phi\) outer. The standard Smirnov–Pythagorean factorization provides \(\phi=b/a\) with \(a\) outer; \(b=a\phi\) is also outer.

**2. The uniform atom-extraction estimate, with no atom separation.** Fix any atom \(\zeta_j\) of mass \(w_j\). For positive integers \(L\), define
\[
\eta_j(L)=\int_{\mathbb T\setminus\{\zeta_j\}}
\min\!\left\{1,\frac{2}{L|1-\zeta/\zeta_j|}\right\}\,d\mu(\zeta).
\]
For each fixed \(\zeta\ne\zeta_j\), the integrand tends to zero as \(L\to\infty\), while it is at most one. Dominated convergence therefore gives \(\eta_j(L)\to0\), even if atoms accumulate at \(\zeta_j\) or \(\mu\) has a nonatomic component. The geometric-sum inequality \(|\sum_{n=N}^{N+t-1}q^n|\le\min\{t,2/|1-q|\}\) for \(|q|=1\), \(q\ne1\), yields for all integers \(N\ge m\ge0\) and \(0\le t\le L\):
\[
\left|\sum_{n=N}^{N+t-1}\gamma_{n-m}\zeta_j^{-n}
-tw_j\zeta_j^{-m}\right|\le L\eta_j(L).
\tag{1}
\]
This estimate is uniform in the starting point \(N\), the test index \(m\) and the partial-block position \(t\).

**3. Simultaneous cancellation with any finite initial jet.** Let \(P(z)=\sum_{n=0}^{d}p_nz^n\), with the zero polynomial treated by taking \(d=0,p_0=0\). Set \(N_0=d+1\) and \(\alpha_n=\overline{p_n}\) for \(0\le n<N_0\). We inductively create numbers \(N_M\) and coefficients \(\alpha_n\) through index \(N_M-1\), maintaining \(N_M>M\). At stage \(M\ge0\), define the finite residuals
\[
R_m=\sum_{n=m}^{N_M-1}\gamma_{n-m}\alpha_n\quad(0\le m\le M).
\]
The square Vandermonde matrix with entries \(w_j\zeta_j^{-m}\), for \(m=0,\ldots,M\) and \(j=1,\ldots,M+1\), is invertible: its nodes \(\zeta_j^{-1}\) are distinct and every column factor \(w_j\) is nonzero. Thus there is a unique solution to
\[
\sum_{j=1}^{M+1}w_j\zeta_j^{-m}d_j=-R_m
\quad (0\le m\le M).
\tag{2}
\]
Put \(D_M=\sum_{j=1}^{M+1}|d_j|\) and \(\delta_M=2^{-M-3}\). Because each of the finitely many functions \(\eta_j(L)\) tends to zero, choose an integer \(L_M\ge2\) so large that
\[
\sum_{j=1}^{M+1}|d_j|\eta_j(L_M)\le\delta_M,
\qquad \frac{D_M^2}{L_M}\le\varepsilon^2 2^{-M-1}.
\tag{3}
\]
Set \(N_{M+1}=N_M+L_M\) and fill the block by
\[
\alpha_n=\frac1{L_M}\sum_{j=1}^{M+1}d_j\zeta_j^{-n}
\quad (N_M\le n<N_{M+1}).
\tag{4}
\]
For each \(m\le M\) and \(0\le t\le L_M\), substituting (4) and using (1)–(2) gives the **entire partial-block identity and bound**
\[
\sum_{n=m}^{N_M+t-1}\gamma_{n-m}\alpha_n
=(1-t/L_M)R_m+E_{M,m,t},
\qquad |E_{M,m,t}|\le\delta_M.
\tag{5}
\]
At each stage endpoint \(t=L_M\), the entire residual for every \(m\le M\) has magnitude at most \(\delta_M\). For a fixed \(m\), once \(M>m\), the residual at the beginning of stage \(M\) is at most \(\delta_{M-1}\); hence (5) bounds the partial sum at **every** intermediate index in that stage by \(\delta_{M-1}+\delta_M\to0\). Thus, for every \(m\ge0\),
\[
\sum_{n=m}^{\infty}\gamma_{n-m}\alpha_n=0
\tag{6}
\]
with ordinary partial-sum convergence, not merely convergence along the endpoints of chosen blocks.

**4. Summability and exact jet preservation.** By (4), \(|\alpha_n|\le D_M/L_M\) on the block at stage \(M\). Therefore
\[
\sum_{n=N_M}^{N_{M+1}-1}|\alpha_n|^2
\le \frac{D_M^2}{L_M}\le\varepsilon^2 2^{-M-1}.
\]
Summing over \(M\ge0\) proves that \((\alpha_n)\in\ell^2\) and that the newly attached tail has norm at most \(\varepsilon\) (strict inequality can be obtained by replacing \(\varepsilon\) in (3) with \(\varepsilon/2\)). Define \(f(z)=\sum_{n\ge0}\overline{\alpha_n}z^n\). Its initial Taylor jet is exactly \(P\), and \(\|f-P\|_{H^2}<\varepsilon\). Taking conjugates in (6) gives \(\mathcal T_\mu f=0\). As polynomials are dense in \(H^2\), the kernel is dense.

**5. Separation from \(\mathcal H(b)\).** Ransford's positive-real-part coefficient theorem [1, Theorem 2.1] says that if \(f\in\mathcal H(b)\), the above ordinary coefficient series are the coefficients of its canonical companion, and
\[
\|f\|_{\mathcal H(b)}^2=\|f\|_{H^2}^2+\|\mathcal T_\mu f\|_{H^2}^2.
\]
As \(b\) is outer, the strict-norm lemma [1, Lemma 3.2] gives \(\|f\|_{\mathcal H(b)}>\|f\|_{H^2}\) whenever \(f\ne0\) lies in \(\mathcal H(b)\). It follows that \(\ker\mathcal T_\mu\cap\mathcal H(b)=\{0\}\).

**6. Closure of the graph.** On polynomials of degree at most \(d\), \(\mathcal T_\mu\) is represented in the ordered monomial basis by an upper-triangular matrix whose diagonal entries are \(\overline{\gamma_0}=1\). Hence this finite-dimensional restriction is invertible and \(\mathcal T_\mu\) maps polynomials onto polynomials. Given \(g,h\in H^2\), select polynomials \(h_k\to h\) and polynomial preimages \(p_k\) with \(\mathcal T_\mu p_k=h_k\). Kernel density supplies \(q_k\in\ker\mathcal T_\mu\) such that \(\|q_k-(g-p_k)\|_{H^2}<1/k\). Then \(f_k=p_k+q_k\to g\) while \(\mathcal T_\mu f_k=h_k\to h\), proving \(\overline{\operatorname{graph}(\mathcal T_\mu)}=H^2\oplus H^2\).

## Verification

The crucial new estimate is (1), whose proof is the finite geometric-sum bound plus dominated convergence on the complement of the selected atom. The partial-block control (5), not just cancellation at stage endpoints, is what establishes ordinary convergence in (6). The weighted Vandermonde determinant is \((\prod_{j=1}^{M+1}w_j)\prod_{i<j}(\zeta_j^{-1}-\zeta_i^{-1})\ne0\). Every newly created block is square summable with the explicit bound (3). The graph conclusion uses only exact finite-dimensional triangular invertibility and the proved dense-kernel property. These are analytic arguments valid for all infinitely atomic probability measures, not a finite computation or a claim of independent certification.

As an additional boundary check, these symbols are outside the earlier \(H^2\) regime: the Cesàro means of \(|\gamma_n|^2\) tend to \(\sum_{j\ge1}w_j^2>0\), by expanding the double integral and applying dominated convergence to the averaged geometric kernel. Thus \(\phi\notin H^2\). This observation does not classify measures with finitely many or no atoms.

## Relationship to prior work

Ransford [1, Theorem 3.1] constructed one zero-output, nonzero \(H^2\) vector for a specific dyadic atomic measure; [1, Theorem 2.1 and Lemma 3.2] supply the positive-real norm identity and the strict inequality used above. The result here makes the phenomenon **dense with arbitrary finite prescribed jets**, shows that the formal transform has **the entire product space as its graph closure**, and removes every atom-spacing and weight specification while allowing extra nonatomic mass. None of these three strengthened conclusions is stated in [1]. Ransford [2] establishes positive coefficient formulas in the \(H^2\)-symbol or rational-symbol settings; the symbols here fail the \(H^2\) hypothesis and are not rational when the infinitely many atoms have nonzero masses. Earlier conventional Toeplitz-kernel work [3] concerns properly defined Toeplitz operators, not the unrestricted coordinatewise-series realization here.

## Limitations

No assertion is made about purely nonatomic measures, about full necessity of the infinite-atom condition, or about the spectrum of the formal transform (which is not closable). The constructed approximants can require extraordinarily long blocks; no useful quantitative bound in terms of the given measure is claimed. Dense kernel is a statement in the ambient \(H^2\) norm, not in the \(\mathcal H(b)\) norm. The operator studied here is the maximal coordinatewise-series realization; identifying it with a closed Smirnov-class Toeplitz operator would be incorrect. Historical priority under alternative terminology remains an open verification risk.

## References

[1] T. Ransford, *A counterexample concerning the coefficient formula for de Branges–Rovnyak norms*, arXiv:2610.15019v1 (first public 10 October 2026), especially Theorems 2.1 and 3.1, Lemma 3.2 and the proof on pp. 5–7. https://arxiv.org/abs/2610.15019

[2] T. Ransford, *On the coefficient formula for de Branges–Rovnyak norms*, arXiv:2605.30114 (first public 28 May 2026). https://arxiv.org/abs/2605.30114

[3] M. T. Nowak, P. Sobolewski, A. Sołtysiak and M. Wołoszkiewicz-Cyll, *On kernels of Toeplitz operators*, Analysis and Mathematical Physics 10 (2020), article 85, DOI:10.1007/s13324-020-00436-6.
