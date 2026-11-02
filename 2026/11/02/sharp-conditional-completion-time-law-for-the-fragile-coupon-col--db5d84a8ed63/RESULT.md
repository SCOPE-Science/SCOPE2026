# Sharp conditional completion-time law for the fragile coupon collector

## Finding

Consider the uniform fragile coupon collector with \(n\ge 2\) types and fixed per-round survival probability \(s\in(0,1)\) for each *unseen* type. Let \(T_n\) be the number of draws needed to discover all types, on the successful-collection event, and define \(K_n=T_n-n\), the number of repeated-type draws. For each \(m\in\{1,\ldots,n\}\), put
\[
 r_{m,n}=\left(1-\frac mn\right)s^m.
\]
Conditional on success,
\[
 K_n\ \overset{d}=\sum_{m=1}^{n}G_{m,n},\qquad
 \Pr(G_{m,n}=j)=(1-r_{m,n})r_{m,n}^{j},\quad j=0,1,\ldots,
\]
with the \(G_{m,n}\) independent. Write \(G_m\) for independent geometric-failure variables with \(\Pr(G_m=j)=(1-s^m)s^{mj}\) and put \(K_s=\sum_{m\ge1}G_m\), which is finite almost surely. Then \(K_n\) converges to \(K_s\) in total variation. The limiting distribution is the number of parts in an ordinary Boltzmann integer partition: with \((s;s)_k=\prod_{j=1}^{k}(1-s^j)\), \((s;s)_0=1\),
\[
 p_k:=\Pr(K_s=k)=(s;s)_\infty\frac{s^k}{(s;s)_k},\qquad k\ge0.
\]
Define the finite positive quantities
\[
 \alpha_s=\sum_{m=1}^{\infty}\frac{m s^m}{1-s^m},\qquad
 h_k=k+\sum_{j=1}^{k}\frac{j s^j}{1-s^j}.
\]
The sharp first-order approximation is
\[
 \boxed{\lim_{n\to\infty} n\,d_{\rm TV}(\mathcal L(K_n),\mathcal L(K_s))
 = C_s:=\frac12\sum_{k=0}^{\infty}p_k\lvert\alpha_s-h_k\rvert\in(0,\infty).}
\]
In fact, the stronger signed \(\ell^1\) expansion holds:
\[
 \lim_{n\to\infty}\sum_{k=0}^{\infty}
 \bigl\lvert n[\Pr(K_n=k)-p_k]-p_k(\alpha_s-h_k)\bigr\rvert=0.
\]
The coefficient is not merely an upper bound. For example \(C_{1/2}=1.00731244900266\ldots\). The exact conditional mean and variance are respectively
\[
 \mathbb E[K_n]=\sum_{m=1}^{n}\frac{r_{m,n}}{1-r_{m,n}},\qquad
 \operatorname{Var}(K_n)=\sum_{m=1}^{n}\frac{r_{m,n}}{(1-r_{m,n})^2},
\]
and their limiting means satisfy
\[
 \lim_{n\to\infty}n(\mathbb E[K_s]-\mathbb E[K_n])
 =\sum_{m=1}^{\infty}\frac{m s^m}{(1-s^m)^2}.
\]

## Assumptions and scope

Draws are independent and uniform on exactly \(n\) distinguishable types. Immediately after each draw, all types still unseen independently survive with fixed probability \(s\in(0,1)\); if any disappears the run fails. Once discovered, a type is permanently safe. The result describes the law *conditioned on successful collection*, which always has strictly positive probability. The number \(n\) tends to infinity with \(s\) fixed; the asymptotic statements are not claimed uniformly as \(s\) tends to zero or one. We use \(\operatorname{Geom}_0(1-r)\) to mean a nonnegative integer with mass \((1-r)r^j\).

## Proof

**1. Exact conditional stage decomposition.** With \(m\) unseen types, the number \(F_m\) of repeated draws until the next new coupon has independent laws \(\Pr(F_m=j)=(m/n)(1-m/n)^j\). A trajectory with these waiting counts has exactly
\[
 A_n=\frac{n(n-1)}2+\sum_{m=1}^{n}mF_m
\]
post-draw exposures of unseen types. Given the trajectory, all its unseen types survive with probability \(s^{A_n}\). Conditioning the joint stage law on success therefore exponentially tilts the independent \(F_m\) distributions by \(s^{mF_m}\). The normalizing factors separate by stage, yielding the displayed independent geometric variables with continuation parameters \(r_{m,n}\). The finite mean and variance follow immediately from geometric moments.

**2. Coupling and limiting partition law.** Couple each \(G_{m,n}\) with \(G_m\) using the same independent uniforms to generate geometric-failure variables. Since \(0\le r_{m,n}\le s^m\), the coupling gives \(G_{m,n}\le G_m\) almost surely, with \(G_{m,n}=0\) for \(m>n\). In particular \(K_n\le K_s\) under this coupling. Summing the one-coordinate mismatch bounds gives the explicit estimate
\[
 d_{\rm TV}(\mathcal L(K_n),\mathcal L(K_s))
 \le\frac1n\sum_{m=1}^{n}\frac{m s^m}{1-s^m}
 +\sum_{m>n}s^m
 \le\frac{\alpha_s}{n}+\frac{s^{n+1}}{1-s}.
\]
Since \(\sum_{m\ge1}s^m<\infty\), almost surely only finitely many \(G_m\) are nonzero. The product partition function is
\[
 Z(z,s)=\prod_{m\ge1}\frac1{1-zs^m}
 =\sum_{k\ge0}\frac{s^k z^k}{(s;s)_k},
\]
using Euler's \(q\)-binomial identity (or its elementary generating-function recurrence). Normalization at \(z=1\) gives \(p_k\). The corresponding random integer partition has \(G_m\) parts of size \(m\), and \(K_s\) is its part count.

**3. First-order variation in total variation.** Work on the complete multiplicity-vector space under the product law \(\mu_s\) of the \(G_m\). Let \(M=\sum_{m\ge1}mG_m\) be the partition size; it is integrable with \(\mathbb E M=\alpha_s\). The finite-collector law, extended by zero multiplicities above \(n\), has density \(L_n=A_n^{*}B_n\) relative to \(\mu_s\), where
\[
 A_n^{*}=\prod_{m=1}^{n}\left(1+\frac{m s^m}{n(1-s^m)}\right)
 \prod_{m>n}(1-s^m)^{-1},\quad
 B_n=\boldsymbol1_{\{G_m=0\ \forall m>n\}}
 \prod_{m=1}^{n}(1-m/n)^{G_m}.
\]
The convention \(0^0=1\) applies. By summability of \(m s^m/(1-s^m)\),
\[
 n(A_n^{*}-1)\longrightarrow\alpha_s.
\]
The corresponding sequence is bounded. Furthermore \(B_n\to1\) almost surely and \(n(1-B_n)\to M\) almost surely, because a partition has only finitely many nonzero multiplicities. For every sample and every \(n\),
\[
 0\le n(1-B_n)\le M.
\]
This follows by expanding the probability of at least one failure in the product of factors, and if any part has size greater than \(n\), then \(M\ge n+1\). Dominated convergence yields the *integrable signed density limit*
\[
 n(L_n-1)\longrightarrow\alpha_s-M\quad\text{in }L^1(\mu_s).
\]
Projection from multiplicity vectors to total part count is an \(L^1\) contraction. Consequently the signed discrete distributions satisfy
\[
 \sum_{k\ge0}\left| n[\Pr(K_n=k)-p_k]
 -p_k(\alpha_s-\mathbb E[M\mid K_s=k])\right|\to0.
\]
Differentiating the coefficient \(s^k/(s;s)_k\) in \(Z(z,s)\) gives
\[
 \mathbb E[M\mid K_s=k]=s\frac{\partial}{\partial s}
 \log\frac{s^k}{(s;s)_k}=h_k.
\]
Taking one-half the discrete \(\ell^1\) norm proves the sharp total-variation constant. Finiteness follows from \(\mathbb E M<\infty\), and strict positivity follows already from the atom \(k=0\), where \(h_0=0\), \(p_0>0\), and \(\alpha_s>0\).

**4. Mean correction.** Because \(r_{m,n}=s^m(1-m/n)\), direct subtraction gives
\[
 n\left[\frac{s^m}{1-s^m}-\frac{r_{m,n}}{1-r_{m,n}}\right]
 =\frac{m s^m}{(1-s^m)(1-r_{m,n})},\qquad m\le n.
\]
Each term tends to \(m s^m/(1-s^m)^2\), bounded by the same summable sequence. The missing terms \(m>n\), after multiplication by \(n\), vanish because their geometric tail is exponentially small. Dominated convergence proves the stated mean correction.

## Verification

The standalone `verify.py` independently evolves all seen-subset states with exact rational arithmetic and weights every round's new unseen-type survival. For \(n\in\{2,\ldots,7\}\), \(s\in\{1/2,2/3,4/5\}\), and completion times from \(n\) through \(n+10\), it matches the direct probabilities to the conditional geometric convolution times the exact success probability. Additional exact checks test coupling inequalities and finite-stage moments. Controlled numerical computations test the first-order total-variation coefficient and the signed single-atom expansion at three values of \(s\). Running `python verify.py` produces `verification_output.txt`, containing 462 successful exact or numerically tolerance-controlled assertions. These experiments do not prove any infinite statement; the signed \(L^1\) argument above does.

## Relationship to prior work

Igor Kleiner, *The Fragile Coupon Collector: Random Deadlines, Critical Fragility, and Optimal Sampling* (2026), derives the exposure transform, the independent waiting-stage representation, and the success probability, and explicitly identifies the conditional completion-time distribution as an open direction (Section 8). The present first-order total-variation constant requires a different analysis of conditioned stage variables, Boltzmann partition limits, and the signed \(L^1\) perturbation. Classical Euler \(q\)-series already supplies the partition coefficient identity; it is not claimed as new. The novelty claim is narrowly the *sharp first-order conditional-collector approximation* and its exact positive coefficient, rather than the underlying stage factorization or partition identities.

## Limitations

Fixed \(s\in(0,1)\) only; no estimates uniform at fragility endpoints. The result requires uniform independent sampling, independent memoryless pre-discovery hazards, and conditioning on the potentially rare event that all coupons survive. The conditional distribution is not a statement about typical failed runs. The reference's underlying waiting-stage decomposition is prior work, as are Euler partition identities. Historical priority for a same-parameter sharp signed perturbation in older conditioned-renewal or partition literature remains open; a mathematical literature search cannot certify novelty. No independent mathematical audit has been performed.

## References

1. I. Kleiner, “The Fragile Coupon Collector: Random Deadlines, Critical Fragility, and Optimal Sampling,” *Mathematics* **14** (2026), 3729. DOI: https://doi.org/10.3390/math14203729 (first published 14 October 2026).
2. E. W. Weisstein, “q-Binomial Theorem,” *MathWorld*, https://mathworld.wolfram.com/q-BinomialTheorem.html (classical generating-function identity).
3. J. C. Peyen, L. V. Bogachev, P. P. Martin, “Boltzmann Distribution on ‘Short’ Integer Partitions with Power Parts: Limit Laws and Sampling,” arXiv:2303.16960 (2023), https://arxiv.org/abs/2303.16960 (related but distinct partition setting).
