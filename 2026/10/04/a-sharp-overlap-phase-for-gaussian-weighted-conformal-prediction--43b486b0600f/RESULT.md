# A sharp overlap phase for Gaussian weighted conformal prediction
## Finding
Let \(P=N(0,1)\) be the calibration-covariate law and \(Q_n=N(\delta_n,1)\) the test-covariate law, with \(\delta_n>0\). For the exact likelihood ratio
\[
w_n(x)=\exp(\delta_n x-\delta_n^2/2),
\]
write \(W_i=w_n(X_i)\) for \(X_1,\ldots,X_n\stackrel{\mathrm{iid}}{\sim}P\), \(S_n=\sum_{i=1}^n W_i\), and \(W_*=w_n(X_*)\) for an independent \(X_*\sim Q_n\). In weighted conformal prediction under covariate shift, the published probability mass at \(+\infty\) is
\[
p_{*,n}=\frac{W_*}{S_n+W_*}.
\]
The following three-regime law holds.

If \(\delta_n^2/\log n\to\beta\in(0,2)\), then \(p_{*,n}\to0\) in probability. If \(\delta_n^2/\log n\to\beta>2\), then \(p_{*,n}\to1\) in probability. At the exact critical scaling \(\delta_n=\sqrt{2\log n}\),
\[
p_{*,n}\ \Longrightarrow\ \operatorname{Bernoulli}(1/2).
\]
Therefore, for every fixed \(\alpha\in(0,1)\), if the calibration nonconformity scores are finite almost surely, the probability that the weighted conformal \((1-\alpha)\)-quantile is \(+\infty\) tends to \(0\), \(1/2\), or \(1\) in the three regimes. Since
\[
D_{\mathrm{KL}}(Q_n\|P)=\frac{\delta_n^2}{2},
\]
the transition is exactly at \(D_{\mathrm{KL}}(Q_n\|P)=\log n\). For the usual absolute-residual score, an infinite quantile makes the prediction set all of \(\mathbb R\).

## Assumptions and scope
The source and target covariate distributions are one-dimensional Gaussians with common variance one and a positive mean shift \(\delta_n\). The likelihood ratio is assumed known exactly. The calibration covariates are iid from \(P\), the test covariate is independent from \(Q_n\), and the miscoverage level \(\alpha\) is fixed as \(n\to\infty\). The result concerns the test-point atom at \(+\infty\) in the original weighted conformal quantile. It does not require assumptions on the conditional response law beyond those needed for the covariate-shift construction, because the event studied is determined entirely by the covariate weights.

## Proof
Write \(L_n=\log n\). With independent standard normals \(Z_1,\ldots,Z_n,Z_*\), the weights have the representations
\[
W_i=\exp(-\delta_n^2/2+\delta_n Z_i),\qquad
W_*=\exp(\delta_n^2/2+\delta_n Z_*).
\]
Hence, whenever \(\delta_n^2/L_n\to\beta\in(0,\infty)\),
\[
\frac{\log W_*}{L_n}\to\frac{\beta}{2}
\]
in probability.

For the subcritical regime, let \(M_n=\max_{1\le i\le n}Z_i\). The elementary Gaussian maximum law
\[
\frac{M_n}{\sqrt{2L_n}}\to1
\]
in probability follows from a union bound and the Gaussian upper tail for the upper deviation, and from \((1-\overline\Phi(t))^n\le \exp(-n\overline\Phi(t))\) plus the Gaussian Mills lower bound for the lower deviation. Therefore
\[
\frac{\log\max_i W_i}{L_n}\to-\frac{\beta}{2}+\sqrt{2\beta}.
\]
For \(0<\beta<2\), the difference between this limit and \(\beta/2\) is \(\sqrt{2\beta}-\beta>0\). Thus \(\max_iW_i/W_*\to\infty\) in probability. Since \(S_n\ge\max_iW_i\), it follows that \(W_*/S_n\to0\), and hence \(p_{*,n}\to0\).

For the supercritical regime, fix \(\beta>2\) and set
\[
r=\sqrt{\frac{\beta-2}{2\beta}},\qquad q=1-r\in(0,1),\qquad
\varepsilon=\frac{\beta-2}{8q}.
\]
For \(0<q<1\), subadditivity gives \(S_n^q\le\sum_iW_i^q\), while Gaussian integration gives
\[
\mathbb E[W_i^q]=\exp\!\left(\frac{q^2-q}{2}\delta_n^2\right).
\]
Consequently, Markov's inequality yields
\[
\mathbb P\!\left(S_n>n^{\beta/2-\varepsilon}\right)
\le n^{1+(q^2-q)\beta/2-q(\beta/2-\varepsilon)+o(1)}.
\]
The exponent without the \(o(1)\) term equals \(- (\beta-2)/8<0\) by the displayed choice of \(q\) and \(\varepsilon\). Hence \(S_n\le n^{\beta/2-\varepsilon}\) with probability tending to one. On the other hand, the preceding limit for \(\log W_*/L_n\) gives \(W_*\ge n^{\beta/2-\varepsilon/2}\) with probability tending to one. Therefore \(S_n/W_*\to0\), and \(p_{*,n}\to1\).

At the exact critical scaling, put \(\delta_n=\sqrt{2L_n}\), so \(n=\exp(\delta_n^2/2)\). Define \(A_i=W_i\mathbf 1\{W_i\le n\}=W_i\mathbf 1\{Z_i\le\delta_n\}\). Exponential tilting gives the exact identities
\[
\mathbb E[A_i]=\frac12,
\qquad
\mathbb E[A_i^2]=n^2\overline\Phi(\delta_n).
\]
Thus
\[
\operatorname{Var}\!\left(\frac1n\sum_{i=1}^n A_i\right)
\le n\overline\Phi(\delta_n)\to0.
\]
Also
\[
\mathbb P\!\left(\max_iW_i>n\right)
\le n\overline\Phi(\delta_n)\to0.
\]
It follows that \(S_n/n\to1/2\) in probability. Meanwhile \(W_*/n=\exp(\delta_nZ_*)\). Hence this ratio tends to zero when \(Z_*<0\) and to infinity when \(Z_*>0\); the event \(Z_*=0\) has probability zero. Slutsky's theorem therefore gives \(p_{*,n}\Longrightarrow\mathbf 1\{Z_*>0\}\), which is \(\operatorname{Bernoulli}(1/2)\).

Finally, the weighted conformal quantile places mass \(p_{*,n}\) at \(+\infty\). With all calibration scores finite, its \((1-\alpha)\)-quantile equals \(+\infty\) exactly when \(p_{*,n}>\alpha\). The three probability limits follow immediately.

## Verification
The proof is analytic. The accompanying `verify.py` checks the algebraic sign of the subcritical exponent gap, verifies an explicit fractional-moment choice making the supercritical Markov exponent negative for representative values of \(\beta>2\), and numerically checks the critical Gaussian-tail quantities entering the variance and union bounds. These computations are consistency checks, not substitutes for the asymptotic proof.

## Relationship to prior work
Tibshirani, Barber, Candès and Ramdas introduced weighted conformal prediction under covariate shift. Their weight formula assigns the test point a normalized likelihood-ratio mass at \(+\infty\), and their empirical example explicitly uses exponential tilting. Those ingredients define the object analyzed here, but the inspected paper does not give a growing-Gaussian-shift overlap threshold or the critical \(1/2\) law.

Chatterjee and Diaconis proved that importance sampling has a logarithmic sample-size cutoff governed by \(D_{\mathrm{KL}}(Q\|P)\), and they study the maximum source weight divided by the sum of source weights as a degeneracy diagnostic. That broader theory predicts that \(D_{\mathrm{KL}}\) is the relevant overlap scale. It does not state the weighted-conformal event involving an independent target draw, nor the exact critical limit in which the conformal test-point atom converges to a two-point law and the infinite-quantile probability tends to \(1/2\).

A later training-conditional analysis of weighted split conformal prediction studies finite-sample coverage through chi-squared divergence and tail averages of the likelihood ratio. Its inspected statements address conditional coverage and clipping, rather than the test-point \(+\infty\) atom or this Gaussian triangular-array phase law.

## Limitations
The exact critical result is proved for the exact scaling \(\delta_n=\sqrt{2\log n}\). Second-order critical windows, such as shifts differing from this boundary by smaller deterministic terms, are not classified. The theorem is one-dimensional and assumes a known likelihood ratio; it does not analyze estimated or clipped weights. It characterizes when the weighted quantile is infinite, not the finite-width distribution in the subcritical regime. Generic importance-sampling theory already identifies the KL scale, so the new content is the conformal test-point atom law and its exact Gaussian critical behavior rather than discovery of KL as an overlap measure.

## References
1. Ryan J. Tibshirani, Rina Foygel Barber, Emmanuel J. Candès, and Aaditya Ramdas. “Conformal Prediction Under Covariate Shift.” arXiv:1904.06019, first version 2019-04-12; NeurIPS 2019.
2. Sourav Chatterjee and Persi Diaconis. “The Sample Size Required in Importance Sampling.” arXiv:1511.01437; Annals of Applied Probability 28(2), 2018, 1099–1135.
3. Mehrdad Pournaderi. “Sharp training-conditional coverage for conformal prediction under covariate shift.” arXiv:2609.33456, 2026.
