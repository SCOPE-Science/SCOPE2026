# Sharp critical-density Gabor constants for causal completely monotone windows

## Finding

Let \(a>0\). Suppose \(\mu\) is a nonzero finite positive Borel measure on \((0,\infty)\) satisfying \(\int_{(0,\infty)}s^{-1}\,d\mu(s)<\infty\), and define
\[
 g(t)=\begin{cases}\displaystyle\int_{(0,\infty)}e^{-st}\,d\mu(s),&t\ge0,\\0,&t<0.\end{cases}
\]
For the **critical-density** Gabor system
\[
 \mathcal G_a(g)=\{e^{2\pi i mt/a}g(t-an):m,n\in\mathbb Z\}\subset L^2(\mathbb R),
\]
the optimal lower and upper frame bounds are, respectively,
\[
 \boxed{A_a=a\left(\sum_{k=0}^{\infty}(-1)^k g(a(k+1))\right)^2,\qquad
 B_a=a\left(\sum_{k=0}^{\infty}g(ak)\right)^2.}
\]
In particular \(0<A_a\le B_a<\infty\). The alternating sum is strictly positive and equals
\[
 \int_{(0,\infty)}\frac{e^{-as}}{1+e^{-as}}\,d\mu(s).
\]
The formula is simultaneously valid for every such measure and every \(a>0\), including mixtures with arbitrarily slow integrable decay.

For the natural power-tail family \(g_p(t)=(1+t)^{-p}\mathbf1_{[0,\infty)}(t)\) on the unit lattice, the complete Hilbert-space Bessel/frame classification is:
\[
 \begin{array}{ll}
 p>1:& \mathcal G_1(g_p)\text{ is a Riesz basis, with optimal } A=(1-\eta(p))^2,\ B=\zeta(p)^2;\\
 \tfrac12<p\le1:& \mathcal G_1(g_p)\text{ is not Bessel};\\
 0<p\le\tfrac12:&g_p\notin L^2(\mathbb R).
 \end{array}
\]
Here \(\zeta(p)=\sum_{n\ge1}n^{-p}\) for \(p>1\) and \(\eta(p)=\sum_{n\ge1}(-1)^{n-1}n^{-p}\) for \(p>0\). For instance, at \(p=2\) the **sharp** constants are
\[
 A=(1-\pi^2/12)^2,\qquad B=\pi^4/36.
\]
As \(p\downarrow1\), the optimal condition number satisfies
\[
 \frac BA\sim\frac{1}{(1-\log2)^2(p-1)^2}.
\]

## Assumptions and scope

The measure \(\mu\) is positive, finite, nonzero, and supported on \((0,\infty)\). The integrability moment \(\int s^{-1}d\mu<\infty\) is exactly \(\int_0^\infty g(t)\,dt<\infty\), by Tonelli. Thus \(g\) is bounded on the positive half-line, monotone, integrable, and square-integrable; it is assigned the value zero on the negative half-line. The jump at zero is allowed. The lattice steps are \(a\) in time and \(1/a\) in frequency, and Fourier phases are \(e^{2\pi i mt/a}\). Bounds are optimal for the frame inequality with ordinary Lebesgue \(L^2\) normalization.

The power-tail classification is for \(p>0\); the case \(p\le1/2\) is not a Gabor frame question in \(L^2\) because the proposed window does not belong to that Hilbert space.

## Proof

**1. Critical Zak diagonalization and its normalization.** For \(x\in[0,a)\), \(\theta\in[0,2\pi)\), let
\[
 Z_ag(x,\theta)=\sqrt a\sum_{k\in\mathbb Z}g(x+ak)e^{-ik\theta}.
\]
With measure \(dx/a\,d\theta/(2\pi)\), \(Z_a\) extends to a unitary map from \(L^2(\mathbb R)\) to \(L^2([0,a)\times[0,2\pi))\). Time shifts by \(an\) and modulations by \(m/a\) become multiplication by torus characters; Parseval in both torus variables gives
\[
 \sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i mt/a}g(t-an)\rangle|^2
 =\int_0^a\int_0^{2\pi}|Z_af|^2|Z_ag|^2\,\frac{d\theta}{2\pi}\frac{dx}{a}.
\]
Therefore the sharp squared frame bounds are \(\operatorname*{ess\,inf}|Z_ag|^2\) and \(\operatorname*{ess\,sup}|Z_ag|^2\).

**2. A positive-real-part lower estimate, with a sharp boundary limit.** Write \(r_s=e^{-as}\in(0,1)\). Since \(g\) vanishes on negative arguments, for \(0\le x<a\) Tonelli and absolute convergence yield
\[
 a^{-1/2}Z_ag(x,\theta)
 =\int_{(0,\infty)}\frac{e^{-sx}}{1-r_s e^{-i\theta}}\,d\mu(s).
\]
For every \(r\in(0,1)\), the elementary identity
\[
 \operatorname{Re}\frac1{1-re^{-i\theta}}-\frac1{1+r}
 =\frac{r(1-r)(1+\cos\theta)}{(1+r)(1+r^2-2r\cos\theta)}\ge0
\]
shows that
\[
 |Z_ag(x,\theta)|\ge \operatorname{Re} Z_ag(x,\theta)
 \ge\sqrt a\int\frac{e^{-sx}}{1+r_s}\,d\mu(s)
 \ge\sqrt a\int\frac{r_s}{1+r_s}\,d\mu(s).
\]
This last number is positive because \(\mu\ne0\). At \(\theta=\pi\), the integral is real and each kernel attains its real-part minimum; as \(x\uparrow a\), dominated convergence makes the last inequality an equality in the limit. The continuous interior values approach the same limit on positive-measure neighborhoods of that boundary point. Hence it is exactly the essential infimum of \(|Z_ag|\).

Expanding \(r_s/(1+r_s)=\sum_{k\ge0}(-1)^kr_s^{k+1}\) and using the integrable decreasing tail, or the monotone alternating-series identity followed by dominated convergence, identifies this boundary value as \(\sum_{k\ge0}(-1)^kg(a(k+1))\). Its positivity also follows from the integral expression.

**3. Sharp upper estimate.** The triangle inequality and monotonicity give
\[
 |Z_ag(x,\theta)|\le\sqrt a\sum_{k\ge0}g(x+ak)
 \le\sqrt a\sum_{k\ge0}g(ak).
\]
The series converges because \(\sum_{k\ge1}g(ak)\le a^{-1}\int_0^\infty g(t)\,dt\). The upper value is approached at \(x\downarrow0\), \(\theta\to0\), so it is the exact essential supremum. Combining this step with the preceding one proves both stated sharp constants, without relying on finite truncation.

**4. Power tails and the threshold.** For \(p>1\), the gamma-mixture identity
\[
 (1+t)^{-p}=\frac1{\Gamma(p)}\int_0^\infty e^{-(1+t)s}s^{p-1}\,ds
\]
meets the measure hypothesis (the inverse moment is \(1/(p-1)\)). At \(a=1\), \(\sum_{k\ge0}g_p(k)=\zeta(p)\), while \(\sum_{k\ge0}(-1)^kg_p(k+1)=\sum_{n\ge2}(-1)^n/n^p=1-\eta(p)\). Since the frame is at critical density, its nonvanishing Zak multiplier also makes it a Riesz basis. At \(p=2\), \(\zeta(2)=\pi^2/6\), \(\eta(2)=\pi^2/12\). The condition-number asymptotic follows from \(\zeta(p)\sim1/(p-1)\) and \(\eta(p)\to\log2\).

Now suppose \(1/2<p\le1\). The same causal window lies in \(L^2\), and for every fixed \(x\in(0,1)\) its Zak transform has nonnegative Fourier coefficients \(c_k(x)=(1+x+k)^{-p}\), indexed by \(k\ge0\). If the Gabor system had a Bessel bound, the Zak function would be essentially bounded, say by \(M\), in its two variables. On almost every fiber \(x\), convolution in \(\theta\) with the normalized nonnegative Fejér kernel would keep absolute value below \(M\). Its value at \(\theta=0\), however, is
\[
 \sum_{k=0}^{N}\left(1-\frac{k}{N+1}\right)c_k(x),
\]
which diverges with \(N\) (already the first half has terms bounded below by \(\tfrac12 c_k(x)\) and divergent sum). This contradicts uniform essential boundedness. Finally, \(\int_0^\infty(1+t)^{-2p}dt\) is finite exactly for \(p>1/2\). This proves the complete classification.

## Verification

The identity in Step 2 can be verified by clearing the positive denominator. No estimate is based on numerical grids: both global extrema are proved analytically and approached through interior Zak coordinates. The accompanying `CHECK.py` checks the rational-kernel inequality numerically over a broad grid for finite exponential mixtures, checks the boundary extremizers, and reproduces the explicit \(p=2\) values; it is a reproducibility supplement, not the proof of any infinite statement. The Fejér argument proves genuine unboundedness rather than merely divergence at a single frequency point.

## Relationship to prior work

Belov and Kulikov, *Gabor frames for functions supported on a semi-axis* (first public 20 May 2025, arXiv:2505.14207), prove frame-set criteria for **stably decreasing** causal windows, a condition that forces exponential decay; their full accessible 2025 revised article does not state the sharp two-sided frame constants for the present Laplace-mixture class. Polynomial tails do not satisfy their stable-decrease hypothesis. Coarse sufficient estimates for integrable decreasing convex causal windows do not imply these optimal constants or the non-Bessel side of the transition. The present result supplies both a universal exact-optimum formula for completely monotone windows and a complete natural power-tail Bessel threshold.

Janssen's 1996 *Some Weyl–Heisenberg frame bound calculations* is a close historical source for exact bounds in certain specific windows. Its publicly accessible description does not establish coverage of arbitrary positive Laplace mixtures or the zeta/eta power-tail phase diagram; the full text was not accessible during this comparison, so complete priority verification against that work remains a limitation. General Zak-frame equivalence is standard and is not claimed as new.

## Limitations

Only rectangular critical-density lattices and nonnegative Laplace mixtures are covered by the general exact-constant theorem; no claims are made for arbitrary convex windows, signed mixtures, or oversampled lattices. The non-Bessel side is shown for the stated power tails, not every nonintegrable mixture. The argument does not assert that the associated sharp numerical values were never independently observed. The comparison with Janssen (1996) is limited by full-text access. No independent audit has been performed.

## References

1. Y. Belov and A. Kulikov, *Gabor frames for functions supported on a semi-axis*, arXiv:2505.14207 (first posted 20 May 2025; revised 19 Aug 2025). https://arxiv.org/html/2505.14207v2
2. A. J. E. M. Janssen, *Some Weyl–Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, doi:10.1016/0019-3577(96)85088-9.
3. M. Faulhuber and S. Steinerberger, *Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions*, J. Math. Anal. Appl. 445 (2017), 407–422, doi:10.1016/j.jmaa.2016.07.074 (Gaussian-window comparison, not the present window family).
