# Sharp weak-Schatten tails for exterior Laurent Hankel operators on Gaussian Fock space

## Finding

For an exterior reciprocal-polynomial symbol whose first nonzero inverse-power term is \(a_k z^{-k}\) with \(k\ge2\), the conjugate Hankel operator has the precise asymptotic law
\[
\lim_{n\to\infty}n^{(k+1)/2}s_n(H_{\bar f})=k|a_k|.
\]
The un-conjugated Hankel operator lies in every Schatten ideal. At the exact exponent \(p_*=2/(k+1)\), the conjugate operator is weak-Schatten but not Schatten, and
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{n=1}^{N}s_n(H_{\bar f})^{p_*}=(k|a_k|)^{p_*}.
\]
The leading spectral coefficient depends neither on the radius of the removed disk nor on higher Laurent terms. These are ordinary Hilbert-space singular values, ordered nonincreasingly with multiplicities.

## Assumptions and scope

Equip \(\mathbb C\) with \(d\mu(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\). Let \(\mathcal F^2\) be the closure of entire polynomials in \(L^2(\mu)\), with orthogonal projection \(P\) and normalized basis \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\). For each bounded measurable \(u\) define \(H_u=(I-P)M_u|_{\mathcal F^2}\). The target is \(L^2(\mu)\ominus\mathcal F^2\).

Fix a real radius \(R>0\), integers \(2\le k\le K<\infty\), and complex coefficients \(a_k\ne0\), \(a_{k+1},\ldots,a_K\). Define
\[
f(z)={\bf1}_{\{|z|\ge R\}}\sum_{j=k}^K a_jz^{-j}.
\]
The symbol is bounded on the entire plane, with any choice of boundary values on \(|z|=R\). The assertions are for every such fixed parameter tuple. For \(p>0\), \(\mathcal S_p\) means \(\sum_ns_n^p<\infty\), and \(\mathcal S_{p,\infty}\) means \(\sup_n n^{1/p}s_n<\infty\).

## Proof

**1. Exact one-mode diagonalization.** Set \(t=R^2\) and \(\Gamma(v,t)=\int_t^\infty u^{v-1}e^{-u}\,du\). For a fixed integer \(j\ge1\), write \(u_j={\bf1}_{\{|z|\ge R\}}z^{-j}\). Angular orthogonality and Gaussian radial integration show
\[
\|M_{\bar u_j}e_n\|^2=\frac{\Gamma(n-j+1,t)}{n!},\qquad
P M_{\bar u_j}e_n=\frac{\Gamma(n+1,t)}{\sqrt{n!(n+j)!}}e_{n+j}.
\]
The residuals \(H_{\bar u_j}e_n\) have distinct angular frequencies \(n+j\), hence are mutually orthogonal. Consequently the eigenvalues of \(H_{\bar u_j}^*H_{\bar u_j}\), counting multiplicity, are exactly
\[
\lambda_{n,j}(t)=\frac{\Gamma(n-j+1,t)}{n!}-\frac{\Gamma(n+1,t)^2}{n!(n+j)!},\qquad n\ge0.
\]
The first integral is finite even when \(n<j\), because \(t>0\).

For \(n\ge j\), a second angular calculation yields
\[
\|H_{u_j}e_n\|^2=\frac{\Gamma(n-j+1,t)}{n!}\left(1-\frac{\Gamma(n-j+1,t)}{(n-j)!}\right).
\]
Again, the residuals have mutually distinct angular frequencies \(n-j\); the finitely many indices \(n<j\) have no effect on any tail conclusion.

**2. Sharp one-mode tails.** For each fixed nonnegative integer \(m\),
\[
\frac{\Gamma(m+1,t)}{m!}=e^{-t}\sum_{\ell=0}^{m}\frac{t^\ell}{\ell!}
=1-O_t\left(\frac{t^{m+1}}{(m+1)!}\right)
\]
as \(m\to\infty\). The error is smaller than every inverse power of \(m\). Therefore, for fixed \(j\),
\[
\lambda_{n,j}(t)=\frac{(n-j)!}{n!}-\frac{n!}{(n+j)!}+o(n^{-L})
\]
for each fixed \(L>0\). Elementary finite products give
\[
\frac{(n-j)!}{n!}=n^{-j}\left(1+\frac{j(j-1)}{2n}+O_j(n^{-2})\right),\quad
\frac{n!}{(n+j)!}=n^{-j}\left(1-\frac{j(j+1)}{2n}+O_j(n^{-2})\right).
\]
Their subtraction gives \(\lambda_{n,j}(t)=j^2n^{-(j+1)}(1+O_j(n^{-1}))\). The decreasing rearrangement of a positive sequence asymptotic to \(j^2n^{-(j+1)}\) has the same asymptotic, by counting indices above a threshold. Thus
\[
s_n(H_{\bar u_j})\sim jn^{-(j+1)/2}.
\]
For \(H_{u_j}\), the preceding positive moment formula and the super-polynomial Poisson tail give \(\|H_{u_j}e_n\|=O_L(n^{-L})\) for every \(L\). Its orthogonal images show that all its singular values decay faster than every inverse power: \(H_{u_j}\in\mathcal S_p\) for each \(p>0\).

**3. Finite Laurent combinations.** Linearity gives
\[
H_{\bar f}=\overline{a_k}H_{\bar u_k}+B,\qquad B=\sum_{j=k+1}^K\overline{a_j}H_{\bar u_j}.
\]
The singular-value inequality \(s_{m+n-1}(A+B)\le s_m(A)+s_n(B)\) and finiteness of the sum imply \(s_n(B)=O(n^{-(k+2)/2})\). The same inequality applied in both directions, assigning an \(\varepsilon\)-fraction of indices to \(B\), shows that if \(s_n(A)\sim cn^{-a}\) and \(s_n(B)=o(n^{-a})\), then \(s_n(A+B)\sim cn^{-a}\). Explicitly, the upper and lower bounds have leading coefficients at most \(c(1-\varepsilon)^{-a}\) and at least \(c(1+\varepsilon)^{-a}\), respectively; then let \(\varepsilon\downarrow0\). Taking \(A=\overline{a_k}H_{\bar u_k}\) proves the stated coefficient \(k|a_k|\). Finite sums preserve membership in every \(\mathcal S_p\), including the quasi-Banach range \(0<p<1\), so \(H_f\) belongs to every such ideal.

**4. Exact critical ideal and residue.** Set \(p_*=2/(k+1)\). The established asymptotic gives \(s_n(H_{\bar f})^{p_*}\sim (k|a_k|)^{p_*}/n\). Comparing this positive sequence to the harmonic series proves divergence at \(p_*\), convergence for all \(p>p_*\), the weak-class upper bound, and the claimed normalized logarithmic sum. The equivalent distribution-function statement is \(\#\{n:s_n(H_{\bar f})>x\}\sim (k|a_k|/x)^{p_*}\) as \(x\downarrow0\).

## Verification

The attached `checker.py` verifies exact symbolic factorial-product limits for eight inverse powers, checks the one-mode incomplete-gamma formula and positivity at multiple radii and degrees, and tests finite asymptotic ratios. It reports 179 supplementary assertions. The infinite-rank, Schatten, and perturbation steps are proved analytically above; finite numerical checks are not substitutes for those proofs. Run with `python checker.py` after installing `sympy` and `mpmath`.

## Relationship to prior work

Xia's 2023 counterexample uses the bounded exterior reciprocal symbol of order one to disprove trace-class Berger–Coburn symmetry. The theorem here addresses exterior Laurent symbols whose first order is at least two, determining their exact singular-value constant, every critical quasi-Schatten exponent, and the weak endpoint residue; it does not claim the order-one counterexample is new. Hu and Virtanen (2023) establish generalized-Fock Schatten membership obstructions using Xia's example, without these exact Laurent-class asymptotic coefficients in their examined preprint. Fan, Wang and Zeng (2024) develop general rearrangement and weak-Schatten criteria; their theorem-level conclusions are estimates or equivalences, not the exact coefficient shown here. Zerouali and coauthors (2015) diagonalize anti-meromorphic Hankel operators on an essentially different punctured Fock space with a two-sided singular weight; their moment asymptotics and Hilbert spaces do not imply this Gaussian entire-space cutoff formula.

## Limitations

The result is for one complex dimension, the standard Gaussian weight, fixed cutoff radius, and a finite exterior Laurent sum with first order at least two. It does not assert operator-norm equality, uniformity as the cutoff radius grows with degree, a converse characterization for arbitrary symbols, or the exact lower-order coefficient of the singular-value expansion. Xia's complete publisher text was not accessible at the time of the literature comparison; prior appearances of a related exact special-case formula therefore remain a historical-priority risk. The self-review is not an independent mathematical audit.

## References

1. Jingbo Xia, *The Berger–Coburn Phenomenon for Hankel Operators on the Fock Space*, Complex Analysis and Operator Theory 17 (2023), article 35. DOI: https://doi.org/10.1007/s11785-023-01338-8 (published online 2023-02-25; publisher abstract and first-page preview inspected; complete text inaccessible).
2. Zhangjian Hu and Jani A. Virtanen, *On the Berger–Coburn phenomenon*, arXiv:2304.09716v1 (2023-04-19), https://arxiv.org/abs/2304.09716 (full preprint examined).
3. Zhijie Fan, Xiaofeng Wang and Zhicheng Zeng, *IDA function and asymptotic behavior of singular values of Hankel operators on weighted Bergman spaces*, arXiv:2410.20082v1 (2024-10-26), https://arxiv.org/abs/2410.20082 (full preprint examined; supporting comparison).
4. E. H. Zerouali, W. Alhomsi, H. Hachadi and E. H. Youssfi, *Hankel operators with anti-meromorphic symbols*, Annals of Functional Analysis 6 (2015), 143–161. DOI: https://doi.org/10.15352/afa/06-2-13 (full text examined).
