# Two Gaussian windows for disjoint testimony in Bernoulli threshold events

## Finding

Let \(p\in(0,1)\) be fixed. Independently sample binary configurations \(X,Y\in\{0,1\}^n\), each with independent \(\operatorname{Bernoulli}(p)\) coordinates. For a threshold \(1\le k\le n\), put \(H_{n,k}=\{x:\sum_i x_i\ge k\}\). Denote by \(\Delta_{n,k}\) the van den Berg--Kesten (BK) gap for \(H_{n,k}\) paired with itself, by \(D_{n,k}\) its product-space disjoint-testimony gap, and by \(R_{n,k}=\Delta_{n,k}-D_{n,k}\) the remaining nonnegative gap. Set

\[
 u=2p-p^2,\quad \sigma_v=\sqrt{v(1-v)},\quad \phi(z)=(2\pi)^{-1/2}e^{-z^2/2},\quad \Phi(z)=\int_{-\infty}^{z}\phi(s)\,ds.
\]

**Theorem (two-scale gap splitting and critical geometry).** The following statements hold simultaneously.

1. For any fixed \(x\in\mathbb R\), if \(k_n=\lfloor np/2+x\sqrt n\rfloor\), then

\[
 (\Delta_{n,k_n},D_{n,k_n},R_{n,k_n})\longrightarrow
 \bigl(\Phi(2x/\sigma_p),0,\Phi(2x/\sigma_p)\bigr).
\]

2. If instead \(k_n=\lfloor nu/2+x\sqrt n\rfloor\), with \(z=2x/\sigma_u\), then

\[
 (\Delta_{n,k_n},D_{n,k_n},R_{n,k_n})\longrightarrow
 (1,\Phi(z),1-\Phi(z)).
\]

Let \(\operatorname{Inf}_i\) and \(\pi_i\) be the influence and symmetric disjoint-pivot probability of coordinate \(i\) for the pair \((H_{n,k_n},H_{n,k_n})\), and put \(\rho_i=\operatorname{Inf}_i^2+\pi_i\). In the second window,

\[
 \sqrt n\,\pi_i\longrightarrow\frac{\phi(z)}{\sigma_u},\qquad
 \|\rho\|_2\longrightarrow\frac{\phi(z)}{\sigma_u}.
\]

Consequently, the symmetric-pivot lower bound of Tesio's Theorem 1.6 is of **correct constant order** in this window, whereas its influence-only lower bound (Theorem 1.4) is exponentially small. "Correct constant order" does not mean the constants in the bound and the actual gap agree.

3. Write \(J_n=\sum_{i=1}^{n}X_iY_i\), the number of shared open coordinates. In the second window, conditional on disjoint testimony failing (and both configurations meeting the threshold), the centered overlap has a nontrivial Gaussian-selection limit. More precisely, let \((G_J,G_U)\) be centered Gaussian with

\[
 \operatorname{Var}(G_J)=p^2(1-p^2),\quad
 \operatorname{Var}(G_U)=u(1-u),\quad
 \operatorname{Cov}(G_J,G_U)=p^2(1-u).
\]

Then

\[
 \mathcal L\left(\frac{J_n-np^2}{\sqrt n}\ \middle|\ X,Y\in H_{n,k_n},\ |X\cup Y|<2k_n\right)
 \Longrightarrow \mathcal L(G_J\mid G_U<2x),
\]

and the conditional expectation converges to

\[
 -\frac{p^2(1-u)}{\sigma_u}\frac{\phi(z)}{\Phi(z)}.
\]

4. On the rare-defect side, if \(k_n/n\to a\in(0,u/2)\), set \(m_n=2k_n-1\) and \(r_n=m_n/n\). Then the product-space defect has the **sharp binomial-tail equivalent**

\[
 D_{n,k_n}\sim\Pr\{\operatorname{Bin}(n,u)\le m_n\}
 \sim \frac{u(1-r_n)}{u-r_n}
 \frac{e^{-nI(r_n\|u)}}{\sqrt{2\pi n r_n(1-r_n)}},
\]

where \(I(r\|u)=r\log(r/u)+(1-r)\log((1-r)/(1-u))\). The use of \(r_n\), rather than its limit, includes the lattice rounding correction.

As an immediate phase diagram, for \(k_n/n\to a\in(0,p)\) away from the two boundaries \(p/2\) and \(u/2\), the ordered limits of \((\Delta,D,R)\) are \((0,0,0)\) when \(a<p/2\), \((1,0,1)\) when \(p/2<a<u/2\), and \((1,1,0)\) when \(u/2<a<p\). This last coarse regime was already noted in the unbiased case by Tesio and is **not** asserted as novel.

## Assumptions and scope

All parameters are fixed as specified above; the threshold is integral and uses the displayed floor. The claimed conditional distribution is considered only for sufficiently large \(n\), when its conditioning event has positive probability. No assumption of independence between the overlap and the union is made. All limits are as \(n\to\infty\). The results concern symmetric increasing threshold events under homogeneous independent Bernoulli coordinates, not arbitrary increasing events.

The relevant source is Pierre Tesio's arXiv:2610.32658v1 (first public 2026-10-23). Its Section 6 supplies the exact finite witness criterion and establishes the coarse obstruction regime. The claims here concern the **distinct scaling windows, their limiting gap decomposition, sharp rare-defect prefactor, and selected-overlap profile**, rather than that earlier finite criterion or coarse obstruction.

## Proof

**Finite identities.** For any support sets \(S,T\), a disjoint pair of \(k\)-element witnesses exists if and only if \(|S|\ge k\), \(|T|\ge k\), and \(|S\cup T|\ge2k\). Necessity is immediate. For sufficiency, choose the first witness from \(S\setminus T\) as far as possible, and fill its remaining places from the overlap; enough elements of \(T\) remain because \(|S\cup T|\ge2k\). This is also Section 6, equation (6.1) of the cited source. Therefore, with \(S_n=\sum_iX_i\), \(T_n=\sum_iY_i\), and \(U_n=|X\cup Y|\),

\[
 D_{n,k}=\Pr(S_n\ge k,T_n\ge k,U_n<2k).
\]

Since the coordinates of \(X\) and \(Y\) are independent, \(U_n\sim\operatorname{Bin}(n,u)\), while \(S_n,T_n\sim\operatorname{Bin}(n,p)\). The one-configuration disjoint occurrence is exactly the event of at least \(2k\) open coordinates. Writing \(h_{n,k}=\Pr\{\operatorname{Bin}(n,p)\ge k\}\),

\[
 \Delta_{n,k}=h_{n,k}^2-\Pr\{\operatorname{Bin}(n,p)\ge2k\},
\]

and the uniform comparison

\[
 \Pr(U_n<2k)-2\Pr(S_n<k)\le D_{n,k}\le\Pr(U_n<2k)
\]

holds for all \(n,k\). The remaining gap is nonnegative by the strengthened BK inequality.

**Two normal windows.** In both windows, \(k_n/n\) tends to a number strictly less than \(p\); thus \(1-h_{n,k_n}=O(e^{-cn})\) for a constant \(c>0\) by a binomial Chernoff bound. In the first window, \(2k_n=np+2x\sqrt n+O(1)\); the binomial central limit theorem shows \(\Pr(S_n<2k_n)\to\Phi(2x/\sigma_p)\). Meanwhile \(u>p\), so \(\Pr(U_n<2k_n)=O(e^{-c'n})\). The first limit follows. In the second window, \(2k_n=nu+2x\sqrt n+O(1)\), with \(u>p\). Hence \(\Pr(S_n\ge2k_n)=O(e^{-c''n})\), \(\Delta_{n,k_n}\to1\), and the comparison above plus the binomial CLT gives \(D_{n,k_n}\to\Phi(2x/\sigma_u)\). Subtraction yields the residual profiles. Fixed-ratio laws follow from the law of large numbers and the same comparison.

**Pivot normalization.** The cited source's Section 6, equations (6.2)--(6.3), gives

\[
 \operatorname{Inf}_i=\Pr\{\operatorname{Bin}(n-1,p)=k-1\},
\]

and \(\pi_i=\Pr(U_{n-1}=2k-1, S_{n-1}\ge k,T_{n-1}\ge k)\), with the restricted supports obtained by omitting coordinate \(i\). Conditional on \(U_{n-1}=m\), each of the \(m\) union-occupied coordinates belongs to \(X\) with independent conditional probability \(1/(2-p)\). In the second window its conditional mean is \(m/(2-p)=np+O(\sqrt n)\), a linear distance above \(k=nu/2+O(\sqrt n)\). Chernoff bounds show that either support-size constraint fails with conditional probability \(O(e^{-cn})\). Consequently \(\pi_i\sim\Pr\{\operatorname{Bin}(n-1,u)=2k-1\}\). The local binomial CLT gives \(\sqrt n\pi_i\to\phi(z)/\sigma_u\). The influence is exponentially small, so \(\|\rho\|_2=\sqrt n(\operatorname{Inf}_i^2+\pi_i)\to\phi(z)/\sigma_u\). In Tesio's Theorem 1.6 this produces a strictly positive limiting lower bound for each fixed \(p,x\); its influence-only bound vanishes exponentially.

**Conditional overlap.** A single coordinate has the four joint outcomes \((0,0),(1,0),(0,1),(1,1)\), so direct calculation gives the covariance matrix displayed in the theorem for the pair \((X_iY_i,X_i\vee Y_i)\). The bivariate central limit theorem implies

\[
 ((J_n-np^2)/\sqrt n,(U_n-nu)/\sqrt n)\Longrightarrow(G_J,G_U).
\]

The difference between \(\{U_n<2k_n\}\) and the conditioning event in the theorem has exponentially small probability because \(k_n/n<p\). The limiting truncation event has probability \(\Phi(z)>0\), and its Gaussian boundary has zero measure, so conditioning is stable under joint weak convergence. Uniform integrability of the centered overlap follows from its uniformly bounded second moments together with the conditioning probability bounded away from zero. Gaussian linear regression then yields the displayed expectation: \(\mathbb E(G_J\mid G_U<2x)=-(p^2(1-u)/\sigma_u)\phi(z)/\Phi(z)\).

**Sharp rare-defect equivalent.** Suppose \(k_n/n\to a\in(0,u/2)\) and write \(K_n=2k_n\). Conditional on \(U_n=m\), each restricted support count is marginally \(\operatorname{Bin}(m,1/(2-p))\). Choose a constant \(\delta\in(0,p/2)\). When \((1-\delta)K_n\le m<K_n\), the conditional mean of either support count exceeds \(k_n\) by a fixed positive fraction of \(n\), and a Chernoff bound makes failure exponentially unlikely. When \(m<(1-\delta)K_n\), the binomial large-deviation rate is strictly greater than at \(m=K_n-1\), so its probability is exponentially negligible relative to \(\Pr(U_n<K_n)\). These two estimates prove \(D_{n,k_n}/\Pr(U_n<K_n)\to1\). Finally, Stirling's formula at \(m_n=K_n-1\) gives the point mass \(e^{-nI(r_n\|u)}/\sqrt{2\pi nr_n(1-r_n)}\) up to a relative \(1+o(1)\) error. Successive lower point-mass ratios converge to \(r(1-u)/(u(1-r))<1\), with \(r=2a\). Summing the asymptotically geometric tail gives the factor \(u(1-r_n)/(u-r_n)\), proving the sharp equivalent. No numerical extrapolation is used in this proof.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic. It independently enumerates pairs of binary configurations through seven coordinates at three biases, checks the finite disjoint-testimony probabilities and binomial comparison, tests the symmetric disjoint-pivot criterion against its original three-modification definition through six coordinates, and checks the overlap/union covariance and binomial likelihood ratios. It passed 178630 assertions; `verify_output.txt` records the actual output. Run `python3 verify.py` from the same directory. These finite tests check proof inputs and normalizations; the asymptotic conclusions are established analytically above.

## Relationship to prior work

Pierre Tesio, *How much do increasing events occur disjointly?* (arXiv:2610.32658v1, first public 2026-10-23), proves two general quantitative bounds and gives the crucial finite threshold witness condition (6.1) and pivot characterization (6.2). Section 6 also proves a coarse product-gap obstruction for unbiased thresholds strictly above the union threshold \(3/8\) and strictly below \(1/2\). We make no claim to those prior facts. The present theorem resolves the two \(\sqrt n\)-windows of the full BK-gap decomposition, the local asymptotic pivot norm at the union window, the overlap selection law, and the rare-phase sharp prefactor. The first paper does not state these limits or constants, although its finite identities are the starting point. Cerf and Tesio's *The case of equality in BK* (arXiv:2607.02272, first public 2026-07-02) establishes the strengthened inequality and equality classification, not the present critical scaling profiles. The central/local binomial limit theorems and Stirling asymptotics are standard tools, not claimed as new.

## Limitations

This is a model-specific sharp asymptotic, not a strengthening of the general BK inequality for arbitrary events. The Gaussian windows assume fixed \(p\), fixed real window parameter, and thresholds with the stated floor. The sharp tail equivalent assumes a fixed strictly positive limiting threshold fraction below \(u/2\), and is not claimed to hold uniformly as that fraction approaches either endpoint. The law of the overlap is conditional on the specific failure of disjoint testimony; it is not a general law for all BK-defect configurations. The critical pivot lower bound is correct only in order, not in exact constant. Standard finite identities in the motivating paper and classical normal-limit results could make related corollaries discoverable; complete historical priority has not been independently established. No independent validation has been performed.

## References

1. P. Tesio, *How much do increasing events occur disjointly?*, arXiv:2610.32658v1 (first public 2026-10-23), https://arxiv.org/html/2610.32658v1 . Particularly equations (6.1)--(6.3), Section 6 and Theorems 1.4 and 1.6.
2. R. Cerf and P. Tesio, *The case of equality in BK*, arXiv:2607.02272v2 (first public 2026-07-02), https://arxiv.org/html/2607.02272v2 . Particularly Theorems 1.3 and 1.6.
3. J. van den Berg and H. Kesten, *Inequalities with applications to percolation and reliability*, Journal of Applied Probability 22 (1985), 556--569. (Foundational inequality.)
