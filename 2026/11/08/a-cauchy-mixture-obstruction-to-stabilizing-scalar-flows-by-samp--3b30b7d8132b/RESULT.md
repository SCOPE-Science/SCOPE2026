# A Cauchy-mixture obstruction to stabilizing scalar flows by sampled stable-noise feedback

## Finding

Fix an observation spacing \(\tau>0\), a deterministic drift \(\theta\in\mathbb R\), a noise scale \(\sigma>0\), a feedback coefficient \(b\in\mathbb R\), and a symmetric stability index \(0<\alpha\le1\). Consider the scalar, sampled-noise-feedback stochastic differential equation defined in the next section. It has the **exact almost-sure upper logarithmic growth rate**

\[
\Lambda_\alpha=\theta+\frac{1}{2\tau}\mathbb E\log\!\left(1+b^2\sigma^2e^{-2\theta\tau}\left(\int_0^\tau e^{\alpha\theta s}\,ds\right)^{2/\alpha}V_\alpha^2\right),
\]

where the strictly positive mixing variable \(V_\alpha\) has Laplace transform \(\mathbb E e^{-sV_\alpha}=e^{-s^\alpha}\), with \(V_1=1\). In particular, if \(\theta\ge0\), **no choice of nonzero noise-feedback gain or positive sampling spacing can make the system almost surely exponentially stable**; nonzero noise feedback strictly *increases* its logarithmic growth rate relative to \(\theta\). If \(\theta<0\), the rate increases continuously and strictly with \(|b|\), crossing zero at one and only one positive critical gain.

At the Cauchy endpoint \(\alpha=1\), the critical gain is explicitly

\[
|b|_{\mathrm{crit}}=\frac{|\theta|}{\sigma}\sqrt{\coth\!\left(-\frac{\theta\tau}{2}\right)}\qquad(\theta<0).
\]

Thus the region of almost-sure exponential stability is exactly \(\theta<0\) and \(|b|<|b|_{\mathrm{crit}}\), interpreting the threshold for general \(0<\alpha<1\) through the displayed expectation. The result is **only for symmetric, centered stable noise and feedback entering the noise coefficient**, not for drift feedback or asymmetric stable innovations.

## Assumptions and scope

Let \(L\) be a real-valued symmetric strictly \(\alpha\)-stable Lévy process normalized by

\[
\mathbb E e^{iu(L_t-L_s)}=\exp\{-\sigma^\alpha(t-s)|u|^\alpha\},\qquad t\ge s\ge0.
\]

On the canonical usual filtration, take the adapted càdlàg solution of

\[
dX_t=\theta X_t\,dt+bX_{\tau\lfloor t/\tau\rfloor}\,dL_t,\qquad X_0=x_0\ne0.
\]

The stochastic integral uses the predictable, piecewise-constant sampled state. It is a well-defined semimartingale integral for every \(0<\alpha\le1\); no first or second noise moment is assumed. Write \(\log0=-\infty\). Almost-sure exponential stability means \(\limsup_{t\to\infty}t^{-1}\log|X_t|<0\).

Define \(H_\alpha(\theta,\tau)=\int_0^\tau e^{\alpha\theta s}\,ds\), always strictly positive, with \(H_\alpha(0,\tau)=\tau\). Let \(V_1=1\), and for \(0<\alpha<1\), let \(V_\alpha\) denote a positive strictly \(\alpha\)-stable variable of unit Laplace exponent. Every expectation below is finite.

## Proof

**1. Exact sampled recursion.** For \(k=0,1,\ldots\) and \(0\le s\le\tau\), variation of constants on one observation interval gives

\[
X_{k\tau+s}=X_{k\tau}\left[e^{\theta s}+b\int_0^s e^{\theta(s-u)}d(L_{k\tau+u}-L_{k\tau})\right].
\]

Consequently the sampled states \(Y_k=X_{k\tau}\) satisfy \(Y_{k+1}=Y_k M_k\), where the \(M_k\) are independent, identically distributed, and

\[
M_k\ \stackrel d=\ a+dS_\alpha,\qquad
 a=e^{\theta\tau},\quad d=b\sigma H_\alpha(\theta,\tau)^{1/\alpha},
\]

with \(\mathbb E e^{iuS_\alpha}=e^{-|u|^\alpha}\). This follows from the stable stochastic-integral characteristic function. Since \(a>0\) and the stable law is continuous when \(b\ne0\), every multiplier is nonzero almost surely (and is deterministically nonzero for \(b=0\)).

**2. Stable-as-Cauchy mixing.** For \(0<\alpha<1\), positivity and existence of \(V_\alpha\) follow from the complete monotonicity of \(e^{-s^\alpha}\), or equivalently from its positive-stable subordinator construction. Let \(C\) be an independent standard Cauchy random variable, with characteristic function \(\mathbb E e^{iuC}=e^{-|u|}\). Conditioning on \(V_\alpha\) gives

\[
\mathbb E e^{iuV_\alpha C}=\mathbb E e^{-|u|V_\alpha}=e^{-|u|^\alpha},
\]

so \(S_\alpha\stackrel d=V_\alpha C\). The same identity holds at \(\alpha=1\) with \(V_1=1\).

**3. Logarithmic potential identity.** For real \(a\ne0\) and real \(w\), the Poisson integral formula on the upper half-plane yields

\[
\int_{\mathbb R}\frac{\log|a+wc|}{\pi(1+c^2)}\,dc
 =\frac12\log(a^2+w^2).
\]

The formula at \(w=0\) is immediate. For \(w\ne0\), it is the harmonic extension of the integrable boundary function \(c\mapsto\log|a+wc|\), evaluated at \(i\); the sole logarithmic singularity lies on the boundary and is integrable. Conditioning on \(V_\alpha\) gives

\[
\mathbb E\log|M_k|
=\frac12\mathbb E\log(a^2+d^2V_\alpha^2)
=\theta\tau+\frac12\mathbb E\log\left(1+\frac{d^2}{a^2}V_\alpha^2\right).
\]

To justify finite integrability, for every \(0<\varepsilon<\alpha\) one has \(\mathbb E V_\alpha^\varepsilon<\infty\); negative moments are finite as well by the gamma-integral representation of \(\mathbb E V_\alpha^{-\varepsilon}\). The conditional Cauchy logarithm has integrable absolute value, bounded by a constant plus \(|\log V_\alpha|\) and \(\log(1+V_\alpha)\) for fixed \(a,d\). An alternative argument uses the bounded stable density near the unique root of \(a+dx\) and polynomial stable tails. Therefore \(\mathbb E|\log|M_k||<\infty\).

**4. Continuous-time upper exponent.** The strong law of large numbers yields

\[
\lim_{k\to\infty}\frac{\log|Y_k|}{k\tau}=\Lambda_\alpha\quad\text{almost surely}.
\]

For each interval define the independent envelope

\[
R_k=\log^+\sup_{0\le s\le\tau}\left|e^{\theta s}+b\int_0^s e^{\theta(s-u)}d(L_{k\tau+u}-L_{k\tau})\right|.
\]

Integration by parts with the deterministic \(C^1\) kernel implies that the supremum of the integral is at most a constant depending on \(\theta,\tau\) times \(\sup_{s\le\tau}|L_{k\tau+s}-L_{k\tau}|\). For any \(0<p<\alpha\), the latter has finite \(p\)-th moment: for \(\alpha<1\) this follows from finite-variation jump estimates, and for \(\alpha=1\) from standard symmetric-stable maximal estimates. Thus \(\mathbb E R_k<\infty\). Since the envelopes are identically distributed, \(\sum_k\Pr(R_k>\varepsilon k)<\infty\) for each \(\varepsilon>0\), so \(R_k/k\to0\) almost surely. Combining the sampled growth limit and the within-interval envelope shows

\[
\boxed{\ \limsup_{t\to\infty}\frac1t\log|X_t|=\Lambda_\alpha\quad\text{almost surely}.\ }
\]

The reverse inequality uses the subsequence \(t=k\tau\). We do not assert a full continuous-time limit, since an interpolated path may approach or hit zero within intervals.

**5. Signs and unique threshold.** The expectation in the boxed rate is nonnegative, and is strictly positive for \(b\ne0\) because \(V_\alpha>0\) almost surely. Hence \(\Lambda_\alpha\ge\theta\), strictly when noise feedback is nonzero. At fixed negative \(\theta\), dominated convergence on bounded \(b\)-intervals and strict positivity of \(V_\alpha\) imply continuity and strict increase in \(|b|\). The value at zero is \(\theta<0\). As \(|b|\to\infty\), restricting to an event \(\{V_\alpha\ge\delta\}\) of positive probability makes the expectation diverge, so the rate crosses zero exactly once.

At \(\alpha=1\), use \(V_1=1\) and, when \(\theta\ne0\), the explicit expression

\[
\Lambda_1=\theta+\frac{1}{2\tau}\log\left(1+\frac{b^2\sigma^2}{\theta^2}(1-e^{-\theta\tau})^2\right).
\]

Solving \(\Lambda_1=0\) gives the stated hyperbolic-cotangent threshold. For \(\theta=0\), the rate reduces to

\[
\Lambda_1=\frac1{2\tau}\log(1+b^2\sigma^2\tau^2),
\]

strictly positive for \(b\ne0\), completing the boundary check.

## Verification

The standalone `verify.py` compares the Cauchy potential identity against direct quadrature, checks the Cauchy critical-gain formula and strict rate monotonicity across signed drifts and observation spacings, verifies the \(\alpha=1/2\) mixing integral through its explicit positive-stable representation \(V_{1/2}=1/(2Z^2)\) for a standard normal \(Z\), and compares three cases with seeded independent Monte Carlo samples. It performed 253 grouped assertions. These finite and numerical checks do **not** certify the infinite-horizon law; the argument above does.

## Relationship to prior work

Mao's 2016 article treats the **same sampled-state diffusion-feedback architecture** with Brownian, not stable, noise and proves that sufficiently strong Brownian noise can stabilize a positive drift for sufficiently small sampling gaps [1]. The present result establishes the opposite sign phenomenon under **symmetric stable indices at most one**, giving a sharp tail-index boundary to the Brownian intuition; the 2016 result does not entail a conclusion for stable noises with infinite first moments.

Wang, Gao and Yuan's G-Lévy feedback paper, first publicly available online March 17, 2025 [2], studies mean-square and quasi-sure exponential stabilization via discrete observation under sublinear expectations. Its published abstract gives sufficient stability results, rather than an exact classical stable-Lévy sample-multiplier exponent at indices at most one; full text was not accessible for a definitive inclusion test, which is an explicit historical-priority risk. The primary mathematical subject classification of that paper includes 60H10. Its sampled Lévy stabilization setting motivates testing the limiting heavy-tail case and distinguishing moment stability from almost-sure logarithmic growth.

Li and coauthors' June 2025 paper [4] instead applies discretely observed drift feedback to nonlinear Lévy-driven hybrid models under mean-square jump assumptions. It likewise does not directly imply the sampled noise-feedback classification, although its general stabilizing interpretation must not be extrapolated to the infinite-moment endpoint.

A separate preprint of November 3, 2026 [3] analyzes the same linear sampled-noise architecture under general stable Lévy processes and gives sufficient stabilization conditions for stable index strictly above one. Its explicitly written sampled recurrence is consistent with step 1 here. Its displayed sufficient results use a positive moment-order parameter strictly below the index minus one, so they do not cover the regime \(0<\alpha\le1\). It supplies a closely matched comparison without covering the boundary \(0<\alpha\le1\).

The use of stable subordinators, Cauchy Poisson kernels, and the scalar product strong law is classical. Neither the mixture representation nor the Cauchy potential identity is claimed to be invented here. The claimed contribution is their joint application to an **exact, all-gain, all-sampling-gap stability classification and pathwise rate for sampled symmetric heavy-tail noise feedback**.

## Limitations

Only centered symmetric stable drivers, a scalar linear drift, fixed positive deterministic sampling gap, constant noise-feedback gain, and nonzero deterministic initial state are covered. Asymmetric or noncentered stable noises, Brownian noise, nonlinear state dynamics, delayed drift feedback, vector-valued systems and random sampling intervals are not addressed. The result is not a moment-stability assertion; for \(\alpha\le1\), standard first/second-moment techniques generally fail. The endpoint \(\Lambda_\alpha=0\) is nonnegative exponential rate and **not** a claim about boundedness or recurrence. The novelty comparison is best-knowledge rather than a certification that no equivalent historical theorem exists; the classical Cauchy-potential/subordination literature is a particular residual priority risk.

## References

[1] X. Mao, *Almost Sure Exponential Stabilization by Discrete-time Stochastic Feedback Control*, IEEE Transactions on Automatic Control **61** (2016), 1619–1624. https://doi.org/10.1109/TAC.2015.2471696. Open manuscript: https://strathprints.strath.ac.uk/54009/1/Mao_etal_IEEE_TOAC_2016_Almost_sure_exponential_stabilization_by_discrete_time_stochastic.pdf.

[2] B. Wang, H. Gao, M. Yuan, *Quasi-sure exponential stabilization of stochastic systems driven by G-Lévy Process with discrete time feedback control*, Mathematical Control and Related Fields **16** (2026), 315–328; first published online March 17, 2025. https://doi.org/10.3934/mcrf.2025020. Publisher abstract: https://www.aimsciences.org/article/doi/10.3934/mcrf.2025020. Full text inaccessible through the available lawful sources at review.

[3] X. Zhang, *Almost sure exponential stabilization of linear stochastic systems driven by a general \(\alpha\)-stable process via discrete-time state feedback*, preprint first posted November 3, 2026, arXiv:2611.04340v1. https://arxiv.org/html/2611.04340v1.

[4] W. Li, H. Xu, F. Chen, X. Mao, W. Fei, *Aperiodically Delay Intermittent Control for Lévy Noise Driven Highly Nonlinear Stochastic Hybrid Systems Based on Discrete-Time Observations*, IEEE Transactions on Automatic Control **70** (2025), 7939–7954; published online June 4, 2025. https://doi.org/10.1109/TAC.2025.3576694. Open manuscript: https://pure.strath.ac.uk/ws/portalfiles/portal/287446498/Li-etal-2025-Aperiodically-delay-intermittent-control-for-Levy-noise.pdf.

[5] D. Applebaum, M. Siakalli, *Asymptotic stability of stochastic differential equations driven by Lévy noise*, Journal of Applied Probability **46** (2009), 1116–1129. https://doi.org/10.1239/jap/1261670692.
