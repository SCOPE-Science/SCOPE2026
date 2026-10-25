# Rare-displacement clocks and exact far-field calibration in Gaussian renewal-competition walks

## Finding
Consider independent positive jump and reset candidate waiting times, redrawn after every event. The shorter candidate wins: a jump adds an independent centered Gaussian displacement, whereas a reset returns the position to zero. At a stationary observation instant, let \(X\) be position, \(N\) the number of actual jumps since the most recent reset, and \(A\) elapsed physical time since that reset. These are distinct observables: observing an exceptional \(X\) does not specify how many jumps occurred or how old the excursion is.

Set \(T=\min(J,S)\), \(q=\Pr(J<S)\), \(p=1-q\), and \(m=\mathbb E T\). Define \(h_J(s)=\mathbb E[e^{-sT}\mid J<S]\) and \(b(s)=(1-\mathbb E[e^{-sT}])/(sm)\), with \(b(0)=1\). Then the **exact stationary position–reset-age transform** is
\[
\mathbb E[e^{ikX-sA}]
=\frac{p\,b(s)}{1-qh_J(s)e^{-\sigma^2 k^2/2}},\qquad k\in\mathbb R,\quad s\ge0.
\]

For \(x\ne0\), put \(r=|x|/\sigma\), \(a=-\log q\), \(\beta=\sqrt{2a}\). The stationary position law has an atom of mass \(p\) at zero, and its continuous density satisfies, for some \(c=c(a)>0\),
\[
f_X(x)=\frac{p}{\sigma\beta}e^{-\beta r}\bigl(1+O(e^{-cr})\bigr),\qquad r\to\infty.
\]
Under the regular conditional distribution given \(X=x\), the completed-jump count obeys the sharp expansions
\[
\begin{split}
\mathbb E[N\mid X=x]&=\frac r\beta+\frac1{2a}+O(re^{-cr}),\\
\operatorname{Var}(N\mid X=x)&=\frac r{\beta^3}+\frac1{2a^2}+O(r^2e^{-cr}).
\end{split}
\]
Moreover, if \(\mu=\mathbb E[T\mid J<S]\) and \(\nu=\operatorname{Var}(T\mid J<S)<\infty\), then, with independent standard normals \(G,H\),
\[
\left(\frac{N-r/\beta}{\sqrt r},\frac{A-\mu r/\beta}{\sqrt r}\right)
\ \Longrightarrow\
\left(\frac{G}{\beta^{3/2}},\frac{\mu G}{\beta^{3/2}}+\sqrt{\frac\nu\beta}\,H\right).
\]
Thus a stationary far-field displacement is overwhelmingly produced by a number of moderate Gaussian jumps *linear*, not quadratic, in distance, and the time since the last reset shares these Gaussian count fluctuations.

For independent exponential clocks of rates \(\lambda_d,\lambda_s>0\), the exact transform simplifies to
\[
\mathbb E[e^{ikX-sA}]
=\frac{\lambda_s}{s+\lambda_s+\lambda_d(1-e^{-\sigma^2k^2/2})}.
\]
Its far-field exponential decay rate \(\sqrt{2\log(1+\lambda_s/\lambda_d)}/\sigma\) is **strictly below** the diffusion-approximation rate \(\sqrt{2\lambda_s/\lambda_d}/\sigma\) for every fixed positive rate ratio; the approximation therefore misses exponentially more rare large displacements at sufficiently large distances. The marginal geometric-mixture representation and general compound-geometric tail principles themselves are not claimed as new.

## Assumptions and scope
Let \((J_j,S_j)\) be i.i.d. pairs of independent, strictly positive random variables with continuous laws, so ties have probability zero. Assume \(0<q=\Pr(J<S)<1\) and \(0<m=\mathbb E\min(J,S)<\infty\). At each event sample a fresh independent pair; a jump occurs if \(J<S\), otherwise a complete reset occurs. Jump increments \((Y_j)\) are i.i.d. \(N(0,\sigma^2)\) for fixed \(\sigma>0\), independent of all clocks. The process starts at the origin after a reset, and the theorem concerns its time-stationary regenerative version. The conditional count and density conclusions hold without additional waiting-time moment assumptions. The joint age central limit theorem assumes the finite conditional second moment \(\mathbb E[T^2\mid J<S]<\infty\). Statements conditional on \(X=x\) use the canonical density disintegration for \(x\ne0\).

## Proof
**1. Stationary regenerative decomposition.** A reset-to-reset cycle has finite mean length \(m/p\): before its terminal reset there are geometrically many independent jump-labelled events, and the unconditional event waiting time has mean \(m\). At a stationary observation the currently occupied inter-event interval is sampled by duration bias. Its elapsed part \(B\) has density \(\Pr(T>b)/m\) on \(b\ge0\), and is independent of all preceding event labels, Gaussian jumps, and labelled durations. The probability that exactly \(n\) jumps occurred since the last reset is \(p q^n\), for every integer \(n\ge0\), because every reached state has the same expected next holding time \(m\). Conditional on that count, its \(n\) preceding jump-event durations are independent draws of \(T\mid J<S\). Consequently,
\[
X=\sum_{j=1}^{N}Y_j,\qquad A=B+\sum_{j=1}^{N}U_j,
\]
where \(N\) is geometric with \(\Pr(N=n)=p q^n\), the \(U_j\) are i.i.d. copies of \(T\mid J<S\), and these variables and \(B\) are mutually independent. The equilibrium inspection formula gives \(\mathbb E[e^{-sB}]=b(s)\). Summing the geometric series proves the exact transform. Setting \(s=0\) retrieves the previously known stationary position marginal.

**2. Exact conditional count weights.** For \(x\ne0\), Gaussian convolution implies
\[
\Pr(N=n\mid X=x)=\frac{n^{-1/2}e^{-an-r^2/(2n)}}{Z_a(r)},\quad
Z_a(r)=\sum_{j=1}^{\infty}j^{-1/2}e^{-aj-r^2/(2j)},\quad n\ge1.
\]
The continuous position density is \(pZ_a(r)/(\sigma\sqrt{2\pi})\). In particular, these posterior weights depend on the candidate waiting-time laws **only through** \(q\), independently of their temporal shapes.

**3. Sharp summation and constants.** For \(r>0\), extend \(t^{-1/2}\exp(-at-r^2/(2t))\) to be zero for \(t\le0\). Its smoothness and exponential decrease justify Poisson summation. The elementary Gaussian–inverse-Gaussian integral yields the absolutely convergent identity
\[
Z_a(r)=\sqrt\pi\sum_{j\in\mathbb Z}(a+2\pi i j)^{-1/2}
\exp\!\left[-r\sqrt{2(a+2\pi i j)}\right],
\]
with principal square roots. The term \(j=0\) equals \(\sqrt{\pi/a}\,e^{-\beta r}\). Every other term has strictly faster real exponential rate, since \(\Re\sqrt{2(a+2\pi i j)}>\beta\) for \(j\ne0\); the sum of these terms and its first two derivatives in \(a\) is exponentially smaller, with at most polynomial factors in \(r\). This establishes the density asymptotic. From
\[
\mathbb E[N\mid X=x]=-\partial_a\log Z_a(r),\qquad
\operatorname{Var}(N\mid X=x)=\partial_a^2\log Z_a(r),
\]
the two count expansions follow with some sufficiently small \(c(a)>0\). This step also specifies the normalization and prefactor, not merely the exponential rate.

**4. Conditional joint central limit law.** For fixed real \(t\), the conditional moment-generating function of \((N-r/\beta)/\sqrt r\) is \(\exp(-tr^{1/2}/\beta)Z_{a-t/\sqrt r}(r)/Z_a(r)\). Taylor expansion of the leading Poisson-summation term gives the Gaussian limiting log-transform \(t^2/(2\beta^3)\); the nonzero Fourier modes are exponentially negligible. Hence the first coordinate converges to \(G/\beta^{3/2}\), while \(N/r\to1/\beta\) conditionally. Conditional on \(N\), the centered duration sum \(\sum_{j=1}^N(U_j-\mu)\), divided by \(\sqrt r\), obeys the independent random-index central limit theorem with limit \(\sqrt{\nu/\beta}\,H\). Its conditional characteristic function converges uniformly on the typical window \(N/r\to1/\beta\), giving asymptotic independence from the count fluctuation. The independent, proper inspection age \(B\) divided by \(\sqrt r\) converges to zero in probability. Combining these facts gives the stated bivariate limit. No limit theorem for a simultaneously varying reset probability is asserted.

**5. Exponential-clocks calibration.** If the two candidate clocks are exponential, the event type and event waiting time are independent. Then \(T\sim\operatorname{Exp}(\lambda_d+\lambda_s)\), \(\mu=(\lambda_d+\lambda_s)^{-1}\), \(\nu=(\lambda_d+\lambda_s)^{-2}\), and \(q=\lambda_d/(\lambda_d+\lambda_s)\). Substitution yields the explicit age-position transform. The claimed strict comparison follows from \(\log(1+u)<u\) for every \(u>0\).

## Verification
The standalone file `checks/verify.py` executes 186 deterministic standard-library comparisons across four reset probabilities, several rare-distance regimes, posterior conditional moments, the central-limit profile, exponential-clock bivariate transforms, and a non-exponential competing-clock example. In the exponential case it also checks the conditional age mean and variance via the exact gamma-mixture law. The analytic proof, especially the stationary length-bias decomposition and nonzero Fourier-mode bounds, is not replaced by those finite comparisons. Run from the package root using `python checks/verify.py`.

## Relationship to prior work
Li, Zhang and Liu (2026, arXiv:2609.09738v1) introduce the competing-clock intermittent CTRW and derive the stationary **position** characteristic function in their Section 2.5, equation (63); their Gaussian-jump analysis uses a diffusion approximation to obtain the large-distance exponential profile (Section 3.2). The existing marginal geometric transform is used here, not claimed as a discovery. The new assessed result concerns the exact *joint* reset-age transform, sharp conditional depth of a rare excursion (including two constant corrections), and its bivariate Gaussian rare-event clock.

Colantoni and Pagnini (2025, arXiv:2507.07590v1) describe general reset CTRW counting processes, but the inspected representation does not determine the above competing-clock stationary age conditional on a far-field Gaussian displacement. Asmussen, Hashorva, Laub and Taimre (2017, arXiv:1712.04070v1) study light-tailed sums, including compound **Poisson** sums; their work is important general tail precedent but does not present this geometric-clock conditional joint theorem. Classical Cramér–Lundberg compound-geometric asymptotics provide broad precedent for exponential tails; the marginal tail exponent by itself is not an originality claim.

## Limitations
The theorem fixes \(p,q\) and \(\sigma\) while taking \(|x|\to\infty\); it does not treat simultaneous weak-reset scaling, heavy-tailed spatial jumps, or jumps whose lengths depend on their waiting times. The age limit needs finite conditional jump-duration variance. The count law is conditional on an exact nonzero position using a regular conditional density, not on first hitting or exceeding a threshold. Independent scientific priority assessment has not been performed, and broad renewal large-deviation theorems may imply portions of the conditional law; the novelty claim is deliberately restricted to the explicit combined physical calibration.

## References
- G. Li, H. Zhang, and Y. Liu, *Intermittent continuous-time random walks under renewal reset mechanism*, arXiv:2609.09738v1 (first public September 9, 2026), https://arxiv.org/html/2609.09738.
- F. Colantoni and G. Pagnini, *Master equations for continuous-time random walks with stochastic resetting*, arXiv:2507.07590v1 (2025), https://arxiv.org/html/2507.07590.
- S. Asmussen, E. Hashorva, P. J. Laub, and T. Taimre, *Tail asymptotics of light-tailed Weibull-like sums*, arXiv:1712.04070v1 (2017), https://arxiv.org/abs/1712.04070.
- J. Cai, *Cramér–Lundberg Asymptotics*, Wiley StatsRef (2014), https://doi.org/10.1002/9781118445112.stat04304.
