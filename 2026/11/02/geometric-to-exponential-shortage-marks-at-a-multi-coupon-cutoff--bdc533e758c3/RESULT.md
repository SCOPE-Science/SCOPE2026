# Geometric-to-exponential shortage marks at a multi-coupon cutoff

## Finding

Consider the usual uniform coupon collector with \(n\) coupon types and a common required multiplicity \(m_n\). At the critical completion window, the *number* of types still short of their quota is asymptotically Poisson, as is implicit in the existing terminal-defect calculation. The new assertion is a joint, quantitative classification of *how far short* each of those types remains.

Let \(m_n\to\infty\), \(m_n/\log n\to\alpha\in[0,\infty]\). Write
\[
Q_m(u)=e^{-u}\sum_{k=0}^{m-1}\frac{u^k}{k!},\quad
Q_{m_n}(b_n)=\frac1n,\quad
q_n=\frac{m_n-1}{b_n},\quad h_n=1-q_n,
\]
and set \(N_n(x)=\lfloor n(b_n+x/h_n)\rfloor\) for any fixed \(x\in\mathbb R\). If \(K_{n,i}(x)\) is the count of coupon type \(i\) in those draws, define the missing-copy depth
\[
D_{n,i}(x)=(m_n-K_{n,i}(x))_+,
\quad Z_n(x)=\#\{i:D_{n,i}(x)>0\},\quad
S_n(x)=\sum_i D_{n,i}(x).
\]
For all three regimes, \(Z_n(x)\Rightarrow\operatorname{Poisson}(e^{-x})\). More precisely:

1. If \(\alpha=0\), with probability tending to one every deficient type is missing exactly one copy; \(S_n(x)\Rightarrow\operatorname{Poisson}(e^{-x})\).
2. If \(0<\alpha<\infty\), let \(r_\alpha>1\) be the unique solution of \(r_\alpha-1-\log r_\alpha=1/\alpha\) and set \(q_\alpha=1/r_\alpha\). The counts of types missing exactly \(j\) copies, for any finite collection of positive integers \(j\), converge jointly to independent Poisson variables with means \(e^{-x}(1-q_\alpha)q_\alpha^{j-1}\). Equivalently the finite multiset of positive shortage depths converges to a Poisson number of independent geometric marks, with \(\Pr(J=j)=(1-q_\alpha)q_\alpha^{j-1}\), and
\[
\lim_{n\to\infty}\mathbb E[z^{S_n(x)}]
=\exp\!\left[e^{-x}\left(\frac{(1-q_\alpha)z}{1-q_\alpha z}-1\right)\right],\qquad 0\le z\le1.
\]
3. If \(\alpha=\infty\), the positive marks \(h_nD_{n,i}(x)\) converge as a finite marked point process on \((0,\infty)\) to a Poisson number \(\operatorname{Poisson}(e^{-x})\) of independent unit-exponential marks. Consequently
\[
\lim_{n\to\infty}\mathbb E[e^{-t h_nS_n(x)}]
=\exp\!\left(-e^{-x}\frac{t}{1+t}\right),\qquad t\ge0.
\]
The limits are at each **fixed** \(x\); no temporal process-level convergence is claimed.

## Assumptions and scope

The draws are iid and uniformly distributed on \(\{1,\dots,n\}\), the quotas are deterministic positive integers tending to infinity, and the ratio \(m_n/\log n\) converges in the extended interval \([0,\infty]\). The quantile equation has one positive solution because \(Q_m\) is continuous and strictly decreasing from one to zero. Eventually \(b_n>m_n-1\), so \(0<h_n<1\). The geometric law is supported on \(\{1,2,\ldots\}\). The compound-Poisson limits allow an empty collection of shortage marks.

## Proof

**1. Quantile scale and hazard.** Put \(m=m_n\), \(b=b_n\), \(h=h_n\). The quantile asymptotics from the growing-multiplicity coupon-collector theory, or equivalently Stirling's formula and the Poisson large-deviation rate \(I(r)=r-1-\log r\), give:
\[
\begin{array}{c|c|c}
\alpha& q_n=(m-1)/b_n & b_nh_n^2\\\hline
0& q_n\to0&\sim\log n\\
(0,\infty)&q_n\to1/r_\alpha&\asymp\log n\\
\infty&q_n\to1&\sim2\log n.
\end{array}
\]
For completeness, when \(0<\alpha<\infty\), the Poisson lower-tail exponential rate gives \(m I(b/m)\sim\log n\), hence \(b/m\to r_\alpha\). If \(m=o(\log n)\), bounded \(b/m\) would make the logarithm of the lower-tail probability \(o(\log n)\), contradicting \(Q_m(b)=1/n\); the same rate comparison gives \(b\sim\log n\). If \(\log n=o(m)\), the upper Gamma quantile satisfies \(b/m=1+\delta_n\), \(\delta_n\to0\), and \(m\delta_n^2\sim2\log n\); its prefactor contributes only \(O(\log\log n)\) in the logarithmic tail estimate. Since \(h_n=\delta_n/(1+\delta_n)+O(1/m)\), the third displayed scale follows. In particular \(mh_n^2\to\infty\) in the \(\alpha=\infty\) regime and \(b_nh_n^2=O(\log n)=o(n)\) in all regimes.

For any \(u>0\), write \(p_{m-1}(u)=e^{-u}u^{m-1}/(m-1)!\), and introduce the exact ratio
\[
R_m(u)=\frac{Q_m(u)}{p_{m-1}(u)}
=\sum_{j=0}^{m-1}\frac{(m-1)_{\underline j}}{u^j},
\]
where the falling factorial includes the \(j=0\) term one. At \(u=b_n+x/h_n\), the ratio of successive terms is at most \((m-1)/u\). When \(q_n\to q<1\), geometric domination gives \(R_m(u)\to(1-q)^{-1}\). When \(q_n\to1\), the falling-factorial correction is \(1+o(1)\) uniformly on indices \(j=O(1/h_n)\), because \(j^2/m=O(1/(mh_n^2))\to0\). The upper bound by the geometric series and a lower bound from those indices give \(h_nR_m(u)\to1\). Thus, in every regime,
\[
\frac{p_{m-1}(b_n+x/h_n)}{Q_m(b_n+x/h_n)}\sim h_n
\quad\text{for each fixed }x.
\]
The replacement of \(b_n\) by \(b_n+x/h_n\) is negligible on this relative scale since \(b_nh_n^2\to\infty\). Integrating the exact logarithmic derivative \((\log Q_m)'=-p_{m-1}/Q_m\) over this interval yields
\[
nQ_m(b_n+x/h_n)\longrightarrow e^{-x}.
\tag{1}
\]

**2. Conditional shortage depth.** At Poissonized time \(t=n(b_n+x/h_n)\), the \(n\) type counts are independent Poisson variables of mean \(u=b_n+x/h_n\). Conditional on a type being short, its depth \(J_n\in\{1,\ldots,m\}\) has
\[
\Pr(J_n=j\mid J_n>0)=\frac{p_{m-j}(u)}{Q_m(u)},\qquad
\frac{p_{m-j}(u)}{p_{m-1}(u)}
=\frac{(m-1)_{\underline{j-1}}}{u^{j-1}}.
\tag{2}
\]
For \(q_n\to q<1\), termwise convergence and a geometric bound show that the normalized probabilities in (2) tend to \((1-q)q^{j-1}\). If \(q=0\) the limit is concentrated at one. For \(q_n\to1\), the same uniform factorial estimate for \(j=O(1/h_n)\), together with \((1-h_n)^{\lfloor y/h_n\rfloor}\to e^{-y}\) and geometric domination, gives \(h_nJ_n\Rightarrow\operatorname{Exp}(1)\). These estimates also establish tightness of the entire conditional mark law.

**3. Rare independently marked types.** By (1), a given type is short with probability \(Q_m(u)\sim e^{-x}/n\). The independence in the Poissonized model implies that for every bounded nonnegative test function \(g\) on the mark space, the marked Laplace functional equals
\[
\Bigl(1-Q_m(u)+Q_m(u)\,\mathbb E[e^{-g(J_n)}\mid J_n>0]\Bigr)^n.
\]
In the infinite-ratio case use \(g(h_nJ_n)\). By (1) and step 2 it converges to \(\exp\{e^{-x}(\mathbb E[e^{-g(J)}]-1)\}\), the functional of a finite Poisson random measure with the asserted mark law. This proves Poisson count limits, joint exact-depth counts, and the stated compound-Poisson transforms in continuous time. Since the total number of positive marks is tight, there is no missing mass at infinity.

**4. Return to a deterministic number of draws.** Couple the iid coupon stream to an independent rate-one total Poisson clock. For each fixed \(\varepsilon>0\), the Poisson counts at times \(n(b_n+(x\pm\varepsilon)/h_n)\) bracket \(N_n(x)\) with probability \(1-o(1)\), since the difference in their expectations is of order \(n/h_n\), whereas their standard deviations are \(O(\sqrt{nb_n})\), and \(b_nh_n^2/n\to0\). For each threshold \(d\), the number of types missing at least \(d\) copies decreases with each draw. Apply this pathwise sandwich simultaneously to finitely many thresholds: fixed positive integer thresholds in the first two regimes, and \(\lceil y/h_n\rceil\) for each fixed \(y>0\) in the third. The upper and lower Poissonized limits are continuous in \(x\); taking \(\varepsilon\downarrow0\) transfers all finite-dimensional tail-count laws. Difference of tail counts gives exact-depth counts. Tightness follows by bracketing the total number of deficient types, followed by the conditional mark-tail bounds. The finite marked point-process laws and compound-Poisson limits therefore hold for \(N_n(x)\) discrete draws. \(\square\)

## Verification

Run `python verify.py` with Python 3, NumPy, and SciPy. The code checks exact finite Poisson/Gamma formulas, selected exact multinomial occupancy probabilities, numerical quantiles, window approximations, and conditional mark identities. The saved output is `verification_output.txt`. These finite computations illustrate the exact formulas; the limiting assertions follow from the analytical argument above, not from the test count.

## Relationship to prior work

Castro and Marinho (2026) and Long (2026) independently establish growing-multiplicity coupon-collection Gumbel scaling and Gamma-tail estimates. Long explicitly identifies the terminal-defect *count*, obtaining a binomial variable after Poissonization, but his inspected section 3.1 does not classify the conditional *number of missing copies per deficient type*. The present added assertion is the marked-depth phase diagram and its explicit geometric and exponential compound-Poisson total-shortfall laws. Ilienko (2020/2026) proves process-level occupancy limits for fixed collection indices; Gnedin, Janson, and Malinovsky (2025) study maximal occupancies in stopped schemes while explicitly fixing the occupancy threshold. Thus their inspected regimes do not directly state the growing-quota deficit-depth law. Classical thinning and marked rare-event methods are used as proof tools, not claimed as new.

## Limitations

The assumptions require iid uniform coupons and quota \(m_n\to\infty\) with a convergent ratio to \(\log n\). The result concerns deterministic near-cutoff times \(N_n(x)\), not the random stopping configuration, not simultaneous trajectories over all \(x\), and not unequal coupon weights. Historical priority outside the inspected papers remains subject to independent review, especially older general occupancy point-process theory; neither numerical testing nor a search establishes uniqueness of a mathematical claim.

## References

- M. E. Castro and R. Marinho, *Cutoff profile for the coupon collector with many collections*, arXiv:2610.33199v1 (first public October 23, 2026), https://arxiv.org/html/2610.33199v1.
- C. D. Long, *Terminal Defects, Growing Multiplicity, and Variance Extremality in the Double Dixie Cup Problem*, arXiv:2604.25108v2 (v1 first public April 28, 2026), https://arxiv.org/html/2604.25108v2.
- A. Ilienko, *Limit theorems in the extended coupon collector's problem*, arXiv:2002.00650 (2020), https://vmsta.org/journal/VMSTA/article/358/text.
- A. Gnedin, S. Janson and Y. Malinovsky, *Maximal Counts in the Stopped Occupancy Problem*, arXiv:2506.20411 (2025), https://arxiv.org/abs/2506.20411.
- P. Neal, *The generalised coupon collector problem*, *Journal of Applied Probability* 45 (2008), 621–629, https://doi.org/10.1239/JAP/1222441818.
