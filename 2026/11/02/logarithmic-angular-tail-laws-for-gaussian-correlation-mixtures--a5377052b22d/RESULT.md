# Logarithmic angular tail laws for Gaussian correlation mixtures

## Finding

Let \(R\) be a random correlation with \(0\le R<1\) almost surely, independent of independent standard normal variables \(X\) and \(Z\). Assume, for some constants \(a>0\) and \(c>0\),
\[
\Pr(R>1-s)\sim c s^a\qquad(s\downarrow0).
\]
Set \(Y=RX+\sqrt{1-R^2}\,Z\), and let \(C\) be the copula of \((X,Y)\), whose two margins are standard normal. Then, for every **fixed** \(w_1,w_2>0\), writing \(L=\log(1/u)\),
\[
\boxed{\lim_{u\downarrow0}\frac{L^a C(uw_1,uw_2)}{u}
=c B_a(w_1,w_2),}
\]
where the finite strictly positive angular profile is
\[
B_a(w_1,w_2)=\frac{\sqrt{w_1w_2}}{\sqrt{2\pi}}
\int_0^\infty t^{a-1/2}\exp\!\left[-\frac t2-
\frac{\{\log(w_1/w_2)\}^2}{8t}\right]dt.
\]
In particular,
\[
C(u,u)\sim c\frac{2^a\Gamma(a+1/2)}{\sqrt\pi}\,
\frac{u}{\{\log(1/u)\}^a}.
\]
The classical lower-tail copula \(\lim_{u\downarrow0}C(uw_1,uw_2)/u\) is identically zero, but the logarithmically renormalized angular profile is nonzero. For \(R\) uniform on \((0,1)\), the profile reduces to the elementary **non-product** formula
\[
\boxed{B_1(w_1,w_2)=\min(w_1,w_2)
\left(1+\frac{1}{2}|\log(w_1/w_2)|\right).}
\]
The profile is symmetric and positively homogeneous of order one. Consequently, the conditional angular tail ratios satisfy
\[
\lim_{u\downarrow0}\frac{C(uw_1,uw_2)}{C(u,u)}
=\frac{B_a(w_1,w_2)}{B_a(1,1)}.
\]

## Assumptions and scope

The distribution of \(R\) may have atoms and need not have a density. It must be supported on \([0,1)\) and have the displayed positive endpoint-tail asymptotics with fixed constants \(a,c\). The two multipliers \(w_1,w_2\) are fixed positive real numbers as \(u\downarrow0\); there is no assertion here for multipliers that diverge or vanish with \(u\), nor an assertion of uniform convergence across all such multipliers. The normal marginals and the independence of \(R,X,Z\) are essential assumptions. The statement is a theorem about a two-dimensional probability distribution and the lower tail; by normal symmetry its upper-tail analogue is identical.

## Proof

**1. Exact correlation integral.** Define \(q_i=-\Phi^{-1}(uw_i)\), where \(\Phi\) denotes the standard-normal distribution function. For all sufficiently small \(u\), \(q_i>0\). Let \(\Phi_2(x,y;r)\) be the standard bivariate normal distribution function with correlation \(r\). The Plackett differential identity is
\[
\frac{\partial}{\partial r}\Phi_2(-q_1,-q_2;r)
=\frac{1}{2\pi\sqrt{1-r^2}}
\exp\!\left[-\frac{(q_1-q_2)^2}{4(1-r)}
-\frac{(q_1+q_2)^2}{4(1+r)}\right].
\]
For completeness, this follows by checking \(\partial_r\phi_{2,r}=\partial_x\partial_y\phi_{2,r}\) for the bivariate Gaussian density and integrating twice over the lower quadrant. Denote the strictly positive right side by \(h_r(q_1,q_2)\). At \(r=0\) the two coordinates are independent, so the fundamental theorem of calculus gives
\[
\Phi_2(-q_1,-q_2;r)=u^2 w_1w_2+\int_0^r h_v(q_1,q_2)\,dv.
\]
Taking expectation over \(R\) and using Tonelli's theorem yields the **exact** identity, valid without a density assumption for \(R\),
\[
C(uw_1,uw_2)=u^2w_1w_2+
\int_0^1\Pr(R>r)h_r(q_1,q_2)\,dr.
\tag{1}
\]
There is no concern about atoms at the integration threshold, since these affect a Lebesgue-null set of \(r\)-values.

**2. Pointwise endpoint scaling.** Put \(q=-\Phi^{-1}(u)\) and \(L=\log(1/u)\). Standard normal Mills asymptotics give
\[
q^2\sim 2L,\qquad u\sim\frac{\exp(-q^2/2)}{q\sqrt{2\pi}},
\qquad q_i=q-\frac{\log w_i}{q}+o(q^{-1}).
\]
For fixed \(t>0\), let \(r=1-t/L\). Inserting these expansions into the exact Gaussian density shows that
\[
\frac{h_{1-t/L}(q_1,q_2)}{uL}\longrightarrow
\frac{\sqrt{w_1w_2}}{\sqrt{2\pi t}}
\exp\!\left[-\frac t2-\frac{\{\log(w_1/w_2)\}^2}{8t}\right].
\tag{2}
\]
Indeed, the density exponent is split exactly into the difference-square term and the sum-square term in Step 1. The former converges to \(\{\log(w_1/w_2)\}^2/(8t)\), while the latter differs from \(q^2/2\) by \(t/2-\tfrac12\log(w_1w_2)+o(1)\). The prefactor combined with Mills' formula is \(1/\sqrt{2\pi t}\). By the assumption on \(R\),
\[
L^a\Pr(R>1-t/L)\longrightarrow c t^a.
\tag{3}
\]

**3. Dominated convergence, including endpoints.** For all sufficiently large \(L\), and all \(0<t<L\), the sum-square exponent obeys
\[
\frac{(q_1+q_2)^2}{4(1+r)}-\frac{q^2}{2}
\ge\frac t4-K_{w_1,w_2},\quad r=1-t/L,
\]
for a constant depending on the fixed multipliers only. To see this, \((q_1+q_2)^2=4q^2+O_{w_1,w_2}(1)\), \(1+r\le2\), and \(q^2(1-r)/(2(1+r))\ge q^2t/(4L)\ge t/4\) for large \(L\). Discarding the nonnegative difference-square exponent, and using Mills' formula and \(\sqrt{1-r^2}\ge\sqrt{t/L}\), gives
\[
\frac{h_{1-t/L}(q_1,q_2)}{uL}
\le K'_{w_1,w_2}\,t^{-1/2}e^{-t/4}.
\tag{4}
\]
Independently, endpoint regular variation and \(\Pr(R>r)\le1\) imply the uniform bound
\[
L^a\Pr(R>1-t/L)\le K_{a,c}\,t^a
\qquad(0<t<L).
\tag{5}
\]
For (5), apply the asymptotic upper bound when \(t/L\) is small, and use \(L^a\le\delta^{-a}t^a\) when \(t/L\ge\delta\), for a fixed small \(\delta>0\). The product of (4) and (5) is bounded by \(K t^{a-1/2}e^{-t/4}\), integrable on \((0,\infty)\) for every \(a>0\). Substituting \(t=L(1-r)\) into (1), applying (2)–(5) and dominated convergence, and observing that \(L^a u^2w_1w_2/u\to0\) completes the main limit.

**4. Constants and elementary special case.** On the diagonal the remaining integral is a Gamma integral:
\[
B_a(1,1)=\frac{1}{\sqrt{2\pi}}\int_0^\infty
 t^{a-1/2}e^{-t/2}dt
=\frac{2^a\Gamma(a+1/2)}{\sqrt\pi}.
\]
For \(a=1\), set \(d=|\log(w_1/w_2)|\). Differentiate in \(\beta>0\) the classical elementary Gaussian integral
\[
\int_0^\infty t^{-1/2}e^{-\beta t-\gamma/t}dt
=\sqrt{\frac\pi\beta}\,e^{-2\sqrt{\beta\gamma}},
\]
at \(\beta=1/2\), \(\gamma=d^2/8\), obtaining
\[
\frac1{\sqrt{2\pi}}\int_0^\infty t^{1/2}e^{-t/2-d^2/(8t)}dt
=e^{-d/2}(1+d/2).
\]
Multiplication by \(\sqrt{w_1w_2}\) gives the displayed \(B_1\) formula. All equal-weight cases follow continuously at \(d=0\). Symmetry and degree-one homogeneity are immediate from the integral. Since \(L^{-a}\to0\), the classical first-order tail copula is zero; the ratio statement follows because \(B_a(1,1)>0\).

## Verification

The standalone accompanying `verify.py` uses independent numerical evaluation of the Gamma/Bessel representation and the defining integral, finite-threshold evaluation of the **exact** Plackett correlation integral for several endpoint power laws, and finite-difference checks of the Plackett identity at interior correlations. Execute `python verify.py` with SciPy installed. The packaged output records **100 passed numerical assertions**, including an off-diagonal comparison for the uniform-correlation case. These finite computations are cross-checks only; the infinite-limit and endpoint-uniformity claims are established by Steps 1–4.

## Relationship to prior work

Koike, Hofert and Tsunekawa (2026, arXiv:2604.05985v1, first posted April 7, 2026) study path-based maximal tail dependence and non-degenerate **first-order** tail copulas. Their Theorem 1 explicitly assumes a non-degenerate tail copula, whereas every model here has a degenerate one. The present logarithmic normalization supplies an explicit finer-scale profile in a natural family outside that hypothesis. No claim is made here to prove their maximal-path existence theorem for this degenerate family.

Manner and Segers (2009 preprint; 2011 journal article, arXiv:0912.3516v1), Section 3.2 and Proposition 4, study the *same Gaussian correlation-mixture object*. They establish zero first-order tail dependence and near-asymptotic dependence with Ledford–Tawn coefficient one when the correlation upper endpoint is one. Those results neither state the power of the logarithmic correction nor an exact off-diagonal angular profile. This theorem refines, rather than replaces, their near-dependence classification; the conclusion about their statements is based on inspection of the actual text of Section 3.2 and its proof.

Fung and Seneta (2011) analyze regular variation of a **fixed-correlation** bivariate normal copula, not random correlation distributions approaching one; the accessible abstract does not provide sufficient basis to exclude all potential implicit corollaries. Existing tail-order/Hüsler–Reiss theory may allow an alternative proof by integrating a near-perfect-correlation scaling limit. As usual, independent historical-priority review remains outstanding.

## Limitations

The precise coefficient relies on the endpoint-tail assumption \(\Pr(R>1-s)\sim c s^a\); other endpoint regimes require separate analysis. The theorem does not cover positive mass at \(R=1\), negative correlation support beyond the stated assumptions, moving angular multipliers, finite-threshold relative-error bounds or uniqueness/existence of globally maximizing nonlinear tail paths. It describes a two-variable probabilistic law rather than a general high-dimensional result. The numerical checker cannot establish novelty or infinite asymptotics.

## References

- T. Koike, M. Hofert and H. Tsunekawa (2026), *Tail copula representation of path-based maximal tail dependence*, arXiv:2604.05985v1, https://arxiv.org/html/2604.05985v1 (first public April 7, 2026; MSC 60E05).
- H. Manner and J. Segers (2009), *Tails of correlation mixtures of elliptical copulas*, arXiv:0912.3516v1, https://arxiv.org/html/0912.3516v1; published in *Insurance: Mathematics and Economics* 48 (2011), 153–160.
- T. Fung and E. Seneta (2011), *The bivariate normal copula function is regularly varying*, *Statistics & Probability Letters* 81, 1670–1676, https://doi.org/10.1016/j.spl.2011.06.003.
