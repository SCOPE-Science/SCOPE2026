# Infinitely divisible partial-reset equilibria with alternating self-decomposability at vanishing refractory occupation

## Finding
Consider the Brownian partial-reset model specified below. Every equilibrium positional law in this family is infinitely divisible, independently of the refractory holding-time distribution beyond its mean. Its Lévy measure is explicit. Nevertheless, the stronger property of self-decomposability oscillates along two geometrically interlaced sequences of strictly positive refractory occupancies tending to zero. In particular, self-decomposability holds at all \(w=a^{2m}\), whereas for the fixed partial-reset factor \(a=1/100\) it fails at all \(w=a^{2m+1}\), for integers \(m\ge1\).

## Assumptions and scope
Let \(D,r>0\), \(0<a<1\). During each active epoch the position evolves as \(dX_t=\sqrt{2D}\,dB_t\) for an independent time of law \(\operatorname{Exp}(r)\). On active-epoch termination, replace \(X\) instantaneously by \(aX\); freeze the resulting position for an independent nonnegative refractory time \(R\). Assume all active periods, Brownian increments, and refractory periods are mutually independent and identically distributed within their classes, and \(\tau=\mathbb E R<\infty\). The case \(\tau=0\) is allowed. The claim concerns the equilibrium observation epoch, and not a nonstationary initial distribution.

Put \(d=D/r\) and \(w=r\tau/(1+r\tau)\in[0,1)\). For \(w=0\), expressions of the form \(\exp[-t/\sqrt w]\) are interpreted as zero for \(t>0\).

The already-known equilibrium characteristic function is
\[
\phi(k)=\frac{1+w d k^2}{1+d k^2}\prod_{j=1}^{\infty}\frac1{1+d a^{2j}k^2},\qquad k\in\mathbb R.
\]
The statements below concern its distributional structure, not a new derivation of this characteristic function.

## Proof
**1. The equilibrium transform.** Let \(Z\) be the position just after partial resetting, at the start of a new active epoch. In the invariant embedded chain, \(Z\overset{d}=aZ+aB_E\), where \(B_E\) is an independent Brownian displacement over an exponential time \(E\) of rate \(r\). Direct Gaussian conditioning gives \(\mathbb E e^{ikB_E}=(1+dk^2)^{-1}\). Iterating the contractive recurrence yields
\[
\phi_Z(k)=\prod_{j=1}^{\infty}(1+da^{2j}k^2)^{-1}.
\]
At an equilibrium epoch, the refractory occupancy is \(w\), while the active occupancy is \(1-w\). Memorylessness makes the elapsed time of the active epoch exponential with rate \(r\), independently of \(Z\). The position is therefore either \(Z\), or \(Z+B_E\), with weights \(w\) and \(1-w\), respectively. This proves the displayed transform and its independence of the shape of the finite-mean refractory law.

**2. A positive Lévy measure and infinite divisibility.** For every \(b>0\), Frullani's integral, applied on the two half-lines, gives
\[
-\log(1+b^2k^2)=\int_{\mathbb R}(\cos(kx)-1)\frac{e^{-|x|/b}}{|x|}\,dx.
\]
Define
\[
K(t)=\sum_{j=0}^{\infty}e^{-t/(a^j\sqrt d)}-e^{-t/\sqrt{wd}},\qquad t>0.
\]
Because \(\sqrt w<1\), the \(j=0\) summand dominates the subtracted term and every remaining summand is positive: \(K(t)\ge0\). The sum decays exponentially at infinity; near zero it is bounded by a constant times \(1+\log(1/t)\). Consequently \(\nu(dx)=K(|x|)|x|^{-1}\,dx\) satisfies \(\int\min(1,x^2)\nu(dx)<\infty\). Applying Frullani's identity termwise, with justified convergence of the nonnegative-kernel Lévy integrals, gives
\[
\log\phi(k)=\int_{\mathbb R}(\cos(kx)-1)\frac{K(|x|)}{|x|}\,dx.
\]
This is a valid symmetric Lévy–Khintchine representation with no Gaussian component or drift. Hence the equilibrium law is infinitely divisible for every allowed \(a,w,D,r\). In particular, all odd cumulants vanish and, for every integer \(n\ge1\),
\[
\kappa_{2n}=\frac{(2n)!}{n}d^n\left(\frac1{1-a^{2n}}-w^n\right)>0.
\]
The cumulant expression follows by expanding the known characteristic function and serves as a consistency check, not as the novelty assertion.

**3. Exact self-decomposability criterion.** A standard one-dimensional characterization of self-decomposable infinitely divisible laws (Sato, Theorem 15.10) states that a symmetric Lévy density of the form \(K(|x|)/|x|\) represents a self-decomposable law if and only if \(K\) is nonincreasing. Here \(K\) is continuously differentiable on \((0,\infty)\). Set \(s=t/\sqrt d\); direct differentiation yields
\[
-\sqrt d\,K'(t)=\sum_{j=0}^{\infty}a^{-j}e^{-s/a^j}-w^{-1/2}e^{-s/\sqrt w}.
\]
Thus the stated pointwise inequality, for every \(s>0\), is necessary and sufficient. When \(w=0\), \(K\) is a positive sum of decreasing exponentials, so self-decomposability holds.

**4. A universal resonant sequence.** Choose any \(0<a<1\) and integer \(m\ge1\). At \(w=a^{2m}\), the subtracted exponential in \(K\) cancels precisely its positive \(j=m\) summand:
\[
K(t)=\sum_{\substack{j\ge0\\j\ne m}}e^{-t/(a^j\sqrt d)}.
\]
This is strictly decreasing, so the law is self-decomposable.

**5. A non-self-decomposable sequence.** Fix \(a=1/100\), choose any integer \(m\ge1\), and set \(w=a^{2m+1}\). In the derivative criterion evaluate \(s=a^m/10\). Multiplying both sides by \(a^m\), the negative term becomes \(10/e\), whereas the positive sum equals
\[
S_m=\sum_{k=-m}^{\infty}100^k e^{-100^k/10}.
\]
The terms with \(k\le0\) sum to at most \(\sum_{k=-\infty}^{0}100^k=100/99\). For \(k\ge1\), successive positive summands have ratio at most \(100e^{-990}<1/2\); their sum is therefore less than \(200e^{-10}\). Hence
\[
S_m<\frac{100}{99}+200e^{-10}<2<\frac{10}{e}.
\]
Therefore \(K'(a^m\sqrt d/10)>0\), contradicting self-decomposability. This strict inequality holds for every integer \(m\ge1\), regardless of \(d\).

Finally \(a^{2m}>a^{2m+1}>a^{2m+2}>0\), and both sequences converge to zero. Every prescribed positive neighborhood of zero refractory occupancy thus contains interlaced self-decomposable and non-self-decomposable stationary distributions, while all remain infinitely divisible. Each occupancy is physically attained by any refractory time distribution of mean \(\tau=w/[r(1-w)]\), including deterministic durations.

## Verification
The standalone `verify.py` checks the characteristic exponent by an independent real-space Lévy integral at nine parameter values, exact moment-to-cumulant relations through order sixteen, six strictly positive derivative witnesses, and twenty-five resonant exponential cancellations. All checks passed on the embedded program. These finite tests support, but do not replace, the analytic inequalities proved above. Reproduce with `python3 verify.py` using only the Python standard library.

## Relationship to prior work
Olsen and Löwen (2024), Section IV and Appendix B, obtain the stationary active/refractory mixture and its infinite-product transform, and develop all-order moments and kurtosis; these formulas are explicitly taken as the starting point. Tal-Friedman, Roichman and Reuveni (2022), Section II, identify the infinite convolution of Laplace laws for partial resetting **without** refractory periods. Di Bello and coauthors (2023), Section 3, develop corresponding stationary transforms for partial resetting. Grzywny and coauthors (2024), Appendix B, analyze Lévy/AR representations in the nonrefractory setting. All may imply the \(w=0\) self-decomposable case; no novelty is asserted for that case.

The present result concerns the explicit **positive** Lévy measure for the *refractory mixture*, an exact self-decomposability test, and the two interlaced sequences exhibiting loss and recovery under arbitrarily small positive refractory occupancy. These are structural properties not inferred from the prior work's stated cumulant and convolution formulas without additional arguments.

## Limitations
This theorem treats one spatial dimension, driftless Brownian exploration, a deterministic contraction \(0<a<1\) at each reset, independent exponential active intervals, and independent refractory intervals of finite mean. It does not address arbitrary Lévy driving noise, nonexponential active intervals, infinite-mean refractory times, or a complete classification of all intermediate \(w\) values. The established sequences are explicit witnesses, not a claim that self-decomposability alternates on whole intervals between them. The literature comparison is not a certification of publication priority; independent external review has not been performed.

## References
1. K. Stølevik Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1 (first posted 2024-06-14), https://arxiv.org/html/2406.10039v1.
2. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363, https://arxiv.org/pdf/2205.03363.
3. C. Di Bello et al., *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722, https://arxiv.org/pdf/2305.13722.
4. T. Grzywny et al., *Stationary states for stable processes with partial resetting*, arXiv:2412.15626v1, https://arxiv.org/pdf/2412.15626.
5. K.-I. Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge University Press (1999), Theorem 15.10.
