# Sharp stationary tail envelopes for Brownian motion with random proportional resets

## Finding

Consider a one-dimensional Brownian diffusion with generator \(D\partial_{xx}\), \(D>0\), interrupted at independent Poisson times of intensity \(\lambda>0\). At each such time the current position is replaced by \(RX\), where the multipliers are independent copies of a random variable supported on \([0,\rho]\), for a prescribed \(0<\rho<1\). Hold their mean fixed at \(\mathbb E R=c\), where \(0<c<\rho\). Write \(a=\sqrt{\lambda/D}\), and let \(X_\infty\) have the unique stationary law.

The exact stationary absolute-tail amplitude exists:

\[
T(R):=\lim_{x\to\infty}e^{ax}\Pr\{|X_\infty|>x\}
=\mathbb E\prod_{j=1}^{\infty}\frac{1}{1-\Pi_j^2},\qquad
\Pi_j=\prod_{i=1}^jR_i.
\]

It obeys the **sharp fixed-mean envelope**

\[
\boxed{\quad
\prod_{j=1}^{\infty}(1-c^{2j})^{-1}
\;\le\; T(R)\;\le\;
\prod_{j=1}^{\infty}(1-c\rho^{2j-1})^{-1}.
\quad}
\]

The lower endpoint is attained **only** by the deterministic rule \(R=c\) almost surely. The upper endpoint is attained **only** by the all-or-nothing rule \(\Pr(R=\rho)=c/\rho\), \(\Pr(R=0)=1-c/\rho\). Moreover, the amplitude is nondecreasing under convex order of multiplier distributions having the same mean and support bound. Thus randomness in reset severity, as measured by convex order, amplifies the leading stationary extreme tail without changing its exponential rate.

## Assumptions and scope

The Brownian motion, rate-\(\lambda\) Poisson process, and iid multipliers are mutually independent; multiplier laws may have atoms, including at zero. There is no reflecting boundary, deterministic drift, or restriction of the position to a half-line. Resetting multiplies the full pre-reset position (rather than sampling an independent restart location). The conditions \(D,\lambda>0\) and \(0<c<\rho<1\) are fixed; all infinite products are convergent. The asymptotic \(x\to\infty\) holds for each fixed admissible law, without an asserted uniform remainder over all such laws. The stationary law is symmetric; its positive one-sided tail has half the stated coefficient.

## Proof

**1. Stationary series and uniqueness.** View the independent Poisson process backwards from a stationary observation time. Its successive gap lengths are iid \(\mathrm{Exp}(\lambda)\), independent of iid reset factors. A Brownian displacement accumulated over one such gap has characteristic function
\[
\mathbb E e^{itZ}=\mathbb E e^{-Dt^2 E}=\frac{\lambda}{\lambda+Dt^2}=\frac{a^2}{a^2+t^2},
\]
so \(Z\) has the symmetric Laplace density \(a e^{-a|z|}/2\). If \((Z_j)_{j\ge0}\) is an iid sequence of such innovations, independent of the multipliers, then
\[
X_\infty\stackrel d=Z_0+W,\qquad
W=\sum_{j\ge1}\Pi_jZ_j,\quad
\Pi_0=1.
\]
This series converges absolutely almost surely because \(\Pi_j\le\rho^j\) and \(\mathbb E|Z_j|=1/a\). It defines an invariant law by the two-sided Poisson/Brownian construction. Coupling two copies with the same Brownian increments, Poisson epochs and multiplier marks makes their separation at time \(t\) equal to the initial separation times the product of all multipliers encountered by time \(t\); its magnitude is at most \(\rho^{N_t}\) times the initial separation and converges to zero almost surely. This proves uniqueness and attraction for every finite initial position (and by conditioning for arbitrary initial laws).

**2. Exact tail coefficient.** Choose \(\eta>0\) so that \((1+\eta)\rho<1\). Conditional on the multipliers, the symmetric-Laplace moment-generating formula gives
\[
\mathbb E[e^{aW}\mid(R_i)]
=\prod_{j\ge1}(1-\Pi_j^2)^{-1},
\]
which is bounded by \(\prod_{j\ge1}(1-\rho^{2j})^{-1}<\infty\). The same calculation at \(a(1+\eta)\) shows \(\mathbb E e^{a(1+\eta)|W|}<\infty\): first bound the positive and negative exponential moments, then use \(e^{s|W|}\le e^{sW}+e^{-sW}\). Thus \(\Pr(W>x)=O(e^{-a(1+\eta)x})\). Splitting the exact identity for the independent Laplace \(Z_0\) at \(W=x\),
\[
\Pr(Z_0+W>x)
=\frac12e^{-ax}\mathbb E[e^{aW};W\le x]
+\mathbb E\!\left[\left(1-\frac12e^{a(x-W)}\right);W>x\right],
\]
and using exponential integrability, yields
\[
\lim_{x\to\infty}e^{ax}\Pr(X_\infty>x)
=\frac12\mathbb E e^{aW}.
\]
Symmetry doubles this value for the absolute tail and establishes the stated formula for \(T(R)\).

**3. Multiplier moment order.** Expand the nonnegative geometric-product series. For every finitely supported sequence \((n_j)_{j\ge1}\) of nonnegative integers,
\[
\prod_{j\ge1}(1-\Pi_j^2)^{-1}
=\sum_{(n_j)}\prod_{i\ge1}R_i^{\,2\sum_{j\ge i}n_j},
\]
where factors with zero exponent are one. Tonelli's theorem and independence yield an expansion of \(T(R)\) as a sum of products of the moments \(m_k=\mathbb E R^{2k}\). Its summands are nonnegative, so \(T\) is nondecreasing in every such moment. On \([0,\rho]\), the convexity of even powers and the bound \(r^{2k}\le\rho^{2k-1}r\) give
\[
c^{2k}\le\mathbb E R^{2k}\le(c/\rho)\rho^{2k},\qquad k\ge1.
\]
The lower equality vector belongs to \(R=c\) almost surely; the upper equality vector belongs to the two-point distribution supported on \(\{0,\rho\}\) with upper-point mass \(p=c/\rho\). Applying the nonnegative series term by term proves the envelope by comparison to these two distributions. Under convex order, every even moment is nondecreasing, proving the additional monotonicity.

Strictness is not lost through the infinite sum: the term with \(n_1=1\) and all other entries zero is precisely \(\mathbb ER^2\). Jensen's inequality is strict for a nonconstant \(R\), so the lower endpoint is unique. The upper second-moment inequality is strict whenever \(\Pr(0<R<\rho)>0\); the fixed-mean condition then forces the stated two-point law as the sole upper extremizer.

**4. Explicit upper endpoint.** For the two-point law, let \(N\) be the number of consecutive multipliers equal to \(\rho\) before the first zero, so \(\Pr(N=n)=(1-p)p^n\), \(n\ge0\). With \(q=\rho^2\) and \((q;q)_n=\prod_{j=1}^n(1-q^j)\),
\[
T(\{0,\rho\})=(1-p)\sum_{n=0}^\infty\frac{p^n}{(q;q)_n}.
\]
The identity \(\sum_{n\ge0}p^n/(q;q)_n=\prod_{k\ge0}(1-pq^k)^{-1}\) follows without external special-function theory: writing the series as \(S(p)\), subtract \(S(qp)\), obtaining \(S(p)-S(qp)=pS(p)\), then iterate \((1-p)S(p)=S(qp)\) and use \(S(q^mp)\to1\). Hence
\[
T(\{0,\rho\})=\prod_{j\ge1}(1-p\rho^{2j})^{-1}
=\prod_{j\ge1}(1-c\rho^{2j-1})^{-1}.
\]
The deterministic lower product follows directly from \(\Pi_j=c^j\).

## Verification

Run `python3 verify_tail.py` using only the Python standard library. The program verifies 319 finite assertions: agreement of the geometric-mixture sum with its infinite-product expression (truncated at 250 terms), finite-tree tests for interior two-point reset laws, quantitative truncation bounds and exact finite signed-exponential tail mixtures. For \(\rho=0.7\), \(c=0.35\), it gives lower amplitude \(1.159391053821\) and upper amplitude \(1.693211347383\). These finite checks are corroboration, not a replacement for convergence, the \(x\to\infty\) passage, or uniqueness proofs above.

## Relationship to prior work

Assefa, Keller-Ressel and Palmowski (2026) establish polynomial-moment and cross-moment formulas for general affine-reset Markov processes, including random proportional marks; this paper provides the recent random-affine-reset model but does not supply extreme-tail prefactor optimization. Di Bello et al. (2023), Grzywny et al. (2024), and Di Bello et al. (2025) analyze fixed proportional reset factors and give stationary density/large-position or transition asymptotics; the deterministic lower prefactor is already available or immediately implied by those fixed-factor formulas. Dahlenburg et al. (2021) explicitly consider random-amplitude resetting but their developed examples concern ballistic displacement and reset-time moment profiles, not this Brownian rare-tail envelope. Buraczewski et al. (2017), Proposition 1, already provides a general exponential-tail transfer mechanism for perpetuities under assumptions excluding reset multipliers equal to zero; the isolated-Laplace-innovation tail argument here is elementary, and **novelty is not claimed for generic perpetuity tail transfer**. The assessed additional claim is the **exact sharp two-endpoint fixed-mean extremal envelope, its unique reset laws, and convex-order comparison for the stationary Brownian extreme-tail prefactor**.

## Limitations

The upper bound needs a strict essential support cap \(\rho<1\); allowing multipliers arbitrarily close to one requires different estimates and can change asymptotic regimes. Neither the result nor its strict equality characterization extends as written to signed multipliers, dependent reset marks, nonlinear resets, general Lévy drivers, or time-dependent resetting rates. The asymptotic amplitude is not a finite-threshold stochastic ordering. Exact historical priority of the specialized endpoint optimization is subject to external review; broad perpetuity and convex-order principles could furnish alternate proofs or implicit coverage.

## References

- J. Assefa, M. Keller-Ressel, Z. Palmowski, *Moments of polynomial processes under affine resetting* (2026), arXiv:2610.01363v1, https://arxiv.org/html/2610.01363v1 (first public October 1, 2026).
- C. Di Bello, A. Chechkin, A. Hartmann, Z. Palmowski, R. Metzler, *Time-dependent probability density function for partial resetting dynamics* (2023), arXiv:2305.13722v2, https://arxiv.org/html/2305.13722v2.
- T. Grzywny, Z. Palmowski, K. Szczypkowski, B. Trojan, *Stationary states for stable processes with partial resetting* (2024), arXiv:2412.15626v1, https://arxiv.org/html/2412.15626v1.
- C. Di Bello et al., *Partial versus total resetting for Lévy flights in d dimensions: similarities and discrepancies* (2025), arXiv:2501.01139v1, https://arxiv.org/html/2501.01139v1.
- M. Dahlenburg, A. Chechkin, R. Schumer, R. Metzler, *Stochastic resetting by a random amplitude* (2021), arXiv:2104.14866v1, https://arxiv.org/pdf/2104.14866.
- D. Buraczewski, P. Dyszewski, A. Iksanov, A. Marynych, *On perpetuities with gamma-like tails* (2017), arXiv:1703.02330, https://arxiv.org/abs/1703.02330.
