# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof was checked term by term against the recent source argument.

For a normalized univalent function
\[
\phi(\zeta)=\zeta+a_2\zeta^2+a_3\zeta^3+\cdots,
\]
the logarithmic derivative satisfies
\[
(\log\phi')''(0)=6a_3-4a_2^2
=6\left(a_3-\frac23a_2^2\right).
\]
The classical sharp Fekete–Szegő estimate at \(\mu=2/3\) therefore gives
\[
|(\log\phi')''(0)|\le 6(1+2e^{-4}),
\]
which applies at every real point of the strip after unit-disk normalization. This justifies the improved global real-axis bound on \(B''\).

The Gaussian convolution is centered with
\[
B(t-s)-B(t)+sB'(t),
\]
the sign dictated by the Taylor expansion of \(B(t-s)\). Its Gaussian second moment is \(\sigma^2\), so the real-axis phase error is
\[
E_\sigma=3(1+2e^{-4})\sigma^2.
\]

For the imaginary part, the exact Gaussian phase reduces the estimate to
\[
4\sigma e^{r^2/2}
\mathbb E[|Z||\sin(rZ)|].
\]
Cauchy–Schwarz and
\[
\mathbb E\sin^2(rZ)=\frac{1-e^{-2r^2}}2
\]
give
\[
|\operatorname{Im}G|
\le4\sigma\sqrt{\sinh(r^2)}
\le4\sigma\sqrt{\sinh(\sigma^{-2})}.
\]
The final straightening factor therefore has derivative modulus at most one on the whole strip, while its real-axis argument lies in a cone of half-angle \(E_\sigma\).

At \(\sigma=9/14\), direct evaluation gives
\[
E_\sigma\approx1.2852112270<\pi/2,\qquad
\lambda_\sigma\approx6.0726394941,
\]
and
\[
c_0\approx0.0006493848651>6.49\times10^{-4}.
\]
The verification script reproduces these values.

The source proof's two local displayed slips were also checked. After \(x=t-s\), the first-order Taylor term is \(-sB'(t)\), so the centered remainder uses \(+sB'(t)\). Also, \(8\int s^2k_\sigma(s)\,ds=8\sigma^2\). With the source's \(\sigma=1/3\), the corrected value \(8/9\) remains below \(\pi/3\), so the source theorem and its stated constant survive the correction.

## Originality

**PASS, to the best of our knowledge.**

MacMahon's arXiv:2609.20607v1 was read at the statement and full proof of the analytic-Lipschitz/inner-metric comparison. It proves existence of a universal lower constant and records the explicit value about \(1.29\times10^{-42}\) from its Gaussian construction. It does not invoke the Fekete–Szegő functional or state a substantially larger quantitative constant.

The classical Fekete–Szegő inequality itself is old and no novelty is claimed for it. A standard modern source recording the exact inequality is Choi–Kim–Sugawa (2007), whose introduction states
\[
|a_3-\mu a_2^2|
\le1+2\exp(-2\mu/(1-\mu)),
\quad 0\le\mu\le1.
\]

Searches combining the new source title or arXiv identifier with Fekete–Szegő, pre-Schwarzian derivative bounds, analytic Lipschitz metrics, inner/path metrics, and bounded-derivative holomorphic functions found no matching quantitative refinement. The current SCOPE archive was also searched by source identifier, object, and synonymous terminology, with no overlap located.

No specifically identified inaccessible paper produced concrete evidence of prior coverage. The principal residual risk is that the source preprint is extremely recent, so a parallel or not-yet-indexed quantitative observation could exist.

## Value

**PASS.**

The refinement turns an existence-scale constant of about \(10^{-42}\) into an explicit constant of order \(10^{-4}\), a gain exceeding \(5\times10^{38}\), without changing the theorem's hypotheses. The mechanism is structural rather than numerical tuning alone: the second derivative of the pre-Schwarzian logarithm is exactly a Fekete–Szegő functional, so a classical sharp coefficient theorem replaces a coarse Cauchy estimate; the Gaussian imaginary-part estimate is then sharpened by its exact oscillatory factor and Cauchy–Schwarz.

The result also supplies a corrected quantitative version of the newly introduced metric comparison, while explicitly preserving the source theorem because its local slips are repairable.

## Literature checked

- C. MacMahon, arXiv:2609.20607v1, especially Theorem 1.2 and its Gaussian-convolution proof.
- J. H. Choi, Y. C. Kim, T. Sugawa, *A general approach to the Fekete–Szegő problem*, J. Math. Soc. Japan 59 (2007), 707–727, doi:10.2969/jmsj/05930707, for the classical sharp Fekete–Szegő inequality.
- Searches for quantitative analytic-Lipschitz/inner-metric comparisons, pre-Schwarzian/Fekete–Szegő refinements, and bounded-derivative holomorphic metric constants.
- The current SCOPE archive, by arXiv identifier, mathematical object, and equivalent terminology.

## Scope of the claim

Novelty is claimed only for the quantitative synthesis yielding the displayed \(c_0\), including the improved pre-Schwarzian second-derivative estimate, the sharper Gaussian strip estimate, and their use in the recent analytic-Lipschitz metric theorem.

No novelty is claimed for the qualitative metric comparison, the Riemann-map reduction, the Gaussian-straightening idea itself, the Bieberbach coefficient bound, or the classical Fekete–Szegő theorem. No optimality claim is made for \(c_0\).
