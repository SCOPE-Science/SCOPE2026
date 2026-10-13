# Strict Gaussian negentropy monotonicity for symmetric beta laws

## Finding

For every real shape parameter \(a>0\), let \(X_a\) have the symmetric beta law \(\operatorname{Beta}(a,a)\), and let \(G_a\) be its moment-matched Gaussian law. Define the forward Gaussian negentropy
\[
J(a)=D_{\mathrm{KL}}\bigl(\mathcal L(X_a)\,\|\,\mathcal L(G_a)\bigr).
\]
Then \(J(a)>0\), \(J'(a)<0\) for all \(a>0\), and
\[
\lim_{a\to\infty}a^2J(a)=\frac{3}{16}.
\]
In particular, as \(a\) increases through the U-shaped, uniform and unimodal beta regimes, the standardized distribution becomes *strictly closer to Gaussian in forward relative entropy* despite its bounded support.

If \(M_n\) is the sample median of \(n\) independent \(\operatorname{Uniform}(0,1)\) observations with \(n\ge1\) odd, and
\[
K_n=\inf_{\mu\in\mathbb R,\,s^2>0}
D_{\mathrm{KL}}\bigl(\mathcal L(M_n)\,\|\,N(\mu,s^2)\bigr),
\]
then \(K_{n+2}<K_n\) for every positive odd \(n\), the unique optimizing Gaussian is \(N(1/2,1/[4(n+2)])\), and
\[
\lim_{\substack{n\to\infty\\n\ \mathrm{odd}}}n^2K_n=\frac34.
\]

## Assumptions and scope

All parameters \(a\) are strictly positive real numbers; integer or asymptotically large shape is not assumed. The beta density is
\[
f_a(x)=\frac{x^{a-1}(1-x)^{a-1}}{B(a,a)},\qquad 0<x<1,
\]
with mean \(1/2\) and variance \(v_a=1/[4(2a+1)]\). Here \(B\) denotes Euler's beta function, \(\psi\) the digamma function and \(\psi_1\) its derivative. Thus \(G_a=N(1/2,v_a)\). Relative entropy is always taken in the order beta law to Gaussian law, not the reverse order. The positive real-line scale parameter and the odd sample-size parameter in the two statements are explicitly related below.

## Proof

**1. Optimal Gaussian and exact negentropy.** For any real random variable \(X\) with positive finite variance \(v\) and finite differential entropy \(h(X)\), direct integration of the Gaussian log density gives
\[
D_{\mathrm{KL}}(\mathcal L(X)\|N(\mu,s^2))
=\frac12\log(2\pi s^2)+\frac{v+(\mathbb EX-\mu)^2}{2s^2}-h(X).
\]
Minimizing first in \(\mu\), then in positive \(s^2\), shows that the unique minimizer has \(\mu=\mathbb EX\) and \(s^2=v\); the minimum is \(\frac12\log(2\pi ev)-h(X)\).

The beta logarithmic moments satisfy \(\mathbb E\log X_a=\mathbb E\log(1-X_a)=\psi(a)-\psi(2a)\). Consequently
\[
h(X_a)=\log B(a,a)-2(a-1)[\psi(a)-\psi(2a)]
\]
and the sought quantity is exactly
\[
J(a)=\frac12\log\left(\frac{2\pi e}{4(2a+1)}\right)
-\log B(a,a)+2(a-1)[\psi(a)-\psi(2a)]. \tag{1}
\]
Because \(X_a\) has bounded support and no nondegenerate Gaussian does, equality in the Gaussian maximum-entropy inequality is impossible, so \(J(a)>0\).

**2. Strict derivative sign on the entire parameter range.** Differentiate (1), using \(\frac{d}{da}\log B(a,a)=2[\psi(a)-\psi(2a)]\) and the trigamma duplication identity \(4\psi_1(2a)=\psi_1(a)+\psi_1(a+1/2)\). Cancellation leaves the exact formula
\[
J'(a)=-\frac1{2a+1}+(a-1)\bigl[\psi_1(a)-\psi_1(a+1/2)\bigr]. \tag{2}
\]
The trigamma function is strictly decreasing on positive arguments; therefore, for \(0<a\le1\), the second term of (2) is nonpositive and \(J'(a)<0\).

For \(a>1\), the standard trigamma integral and a change of variable yield
\[
\begin{aligned}
\psi_1(a)-\psi_1(a+1/2)
&=\int_0^\infty\frac{t e^{-at}}{1+e^{-t/2}}\,dt\\
&=4\int_0^\infty\frac{s e^{-2as}}{1+e^{-s}}\,ds.
\end{aligned}
\]
For every \(s>0\), strict AM–GM gives \(1+e^{-s}>2e^{-s/2}\), and hence
\[
0<\psi_1(a)-\psi_1(a+1/2)<\frac{2}{(2a-1/2)^2}.
\]
The bound is sufficient *without any numerical inequality*: for all \(a>1\),
\[
(2a-1/2)^2-2(a-1)(2a+1)=\frac94>0.
\]
It follows that \((a-1)[\psi_1(a)-\psi_1(a+1/2)]<1/(2a+1)\), so (2) is strictly negative. This proves the global monotonicity, including both sides of the transition at \(a=1\).

**3. Sharp limit.** Standard Stirling expansion of \(\Gamma\) in (1) implies \(J(a)\to0\) as \(a\to\infty\). The trigamma asymptotic expansion gives
\[
\psi_1(a)-\psi_1(a+1/2)=\frac1{2a^2}+\frac1{4a^3}+O(a^{-5}),
\]
which substituted into (2) yields
\[
J'(a)=-\frac{3}{8a^3}+O(a^{-4}).
\]
Integrating from \(a\) to infinity (using \(J(\infty)=0\)) proves
\[
J(a)=\frac{3}{16a^2}+O(a^{-3}).
\]
This is an asymptotic statement for every continuously increasing real \(a\), not merely integers.

**4. Median specialization.** For odd \(n=2m-1\), the sample median has exactly the law \(\operatorname{Beta}(m,m)\). Its variance is \(1/[4(n+2)]\), and the first step identifies its unique Gaussian KL projection. Thus \(K_n=J((n+1)/2)\), so strict decrease follows from the all-real monotonicity. Finally, \(n^2J((n+1)/2)\to4(3/16)=3/4\).

## Verification

Run `python verify.py` after installing the version of `mpmath` specified in `requirements.txt`. The program evaluates exact beta-entropy and trigamma formulas at 15 positive shapes, compares analytical and numerical derivatives at high precision, checks positivity and sample Gaussian optimality at selected parameters, checks the explicit upper trigamma bound, tests three large-shape values against the leading asymptotic coefficient, and reproduces six odd-sample median identities. All listed checks pass on the supplied script. They are diagnostics only: the proof of universal monotonicity is the integral inequality and the polynomial identity above; the infinite asymptotic follows from special-function expansions.

## Relationship to prior work

The exact entropy of uniform order statistics and an entropic central limit theorem are already established by Cardone, Dytso and Rush (arXiv:2205.04621v1, 2022), especially their Lemma 2, equation (15), and the observation after equation (17) that the symmetric entropy approximation has second-order convergence. These known inputs are not claimed as new. Their preprint uses a Gaussian based on the asymptotic quantile variance and does not establish the strict inequality in (2) for every positive real shape or the sharp constant for optimal finite-sample Gaussian approximation.

Skorski (arXiv:2101.02094, first posted 2021; version 5, 2023) gives sharp beta concentration bounds and a central-moment recurrence, motivated in part by beta order-statistic applications; it does not compare the beta distribution's Gaussian negentropy across its entire symmetric shape family. Classical beta moments, maximum-entropy projection and trigamma integral identities are invoked as known facts.

The later journal article by Cardone, Dytso and Rush (IEEE Transactions on Information Theory 69, 2023, pages 2193–2205, DOI 10.1109/TIT.2022.3219344) has an abstract referring to discussion of monotonicity of relative entropy. A full updated journal text was not available for direct comparison; it remains a relevant bibliographic priority risk, distinct from the fully inspected preprint. No independent priority determination is asserted.

## Limitations

The theorem concerns one symmetric beta family and forward KL divergence to an unrestricted Gaussian family; it does not imply the analogous monotonicity for asymmetric beta laws, reverse KL divergence, or arbitrary parent distributions of sample medians. Exact entropy and asymptotic variance are available in the prior literature, so the asserted contribution is the *global strict shape-monotonicity* together with its precise optimal-Gaussian consequence, not the general beta entropy formula. The published journal treatment of order-statistic entropy has not been fully compared, and independent mathematical and priority validation has not been performed.

## References

1. M. Skorski, *Bernstein-Type Bounds for Beta Distribution*, arXiv:2101.02094, first public 2021-01-06, v5 2023-02-06, https://arxiv.org/abs/2101.02094. Primary MSC 60E05 in the source record.
2. M. Cardone, A. Dytso and C. Rush, *Entropic CLT for Order Statistics*, arXiv:2205.04621v1, first public 2022-05-10, https://arxiv.org/abs/2205.04621. See Lemma 2 and Appendix A.
3. M. Cardone, A. Dytso and C. Rush, *Entropic Central Limit Theorem for Order Statistics*, IEEE Transactions on Information Theory 69 (2023), 2193–2205, https://doi.org/10.1109/TIT.2022.3219344 (later version; abstract checked but complete journal text unavailable).
