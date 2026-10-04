# A closed-form remainder for the unweighted rank-two LIL boundary law
## Finding
For the unweighted Hermite-rank-two law of the iterated logarithm, put \(\varepsilon=1-2\alpha\in(0,1)\) and
\[
R(\varepsilon)=\frac{\Lambda_2((1-\varepsilon)/2,0)}{\sqrt{\varepsilon}}.
\]
Let \(K_\alpha\) be the integral operator
\[
(K_\alpha f)(x)=\int_0^1 |x-y|^{-\alpha}f(y)\,dy,
\]
let \(K_*=K_{1/2}\), and write \(\lambda_*=\lambda_{\max}(K_*)\). Define
\[
\delta(\varepsilon)=2\sqrt{2}\left(1-\frac{2^{-\varepsilon/2}}{1+\varepsilon}\right).
\]
Then, for every \(0<\varepsilon<1\),
\[
\frac{\sqrt{1+\varepsilon}}2\max\{0,\lambda_*-\delta(\varepsilon)\}
\le R(\varepsilon)\le
\frac{\sqrt{1+\varepsilon}}2\lambda_*.
\]
Consequently,
\[
\left|R(\varepsilon)-\frac{\lambda_*}2\right|
\le \frac12\left[\lambda_*\bigl(\sqrt{1+\varepsilon}-1\bigr)+\sqrt{1+\varepsilon}\,\delta(\varepsilon)\right].
\]
This replaces the previously unspecified first-order remainder at the unweighted memory boundary by an explicit nonasymptotic modulus.

## Assumptions and scope
The statement concerns only the unweighted rank-two family \(d=0\) and \(0<\alpha<1/2\). The endpoint operator \(K_*\) is an auxiliary bounded compact operator; the statement does not assert an LIL at \(\alpha=1/2\). The stochastic LIL theorem and the exact normalization are taken from the cited source; the new step is a closed-form operator perturbation bound.

## Proof
Moldavskaya's exact normalization, with \(\varepsilon=1-2\alpha\), is
\[
R(\varepsilon)=\frac12\sqrt{1+\varepsilon}\,\lambda_\varepsilon,
\qquad
\lambda_\varepsilon=\lambda_{\max}(K_{(1-\varepsilon)/2}).
\]
Because \(0<(1-\varepsilon)/2<1/2\), the kernel difference \(D_\varepsilon=K_*-K_{(1-\varepsilon)/2}\) is pointwise nonnegative. Let \(g_\varepsilon\) and \(g_*\) be normalized nonnegative leading eigenfunctions of \(K_{(1-\varepsilon)/2}\) and \(K_*\), respectively. Pointwise kernel comparison on \(g_\varepsilon\ge0\) gives \(\lambda_\varepsilon\le\langle g_\varepsilon,K_*g_\varepsilon\rangle\le\lambda_*\). Conversely, the Rayleigh quotient at \(g_*\) gives \(\lambda_\varepsilon\ge\lambda_*-\langle g_*,D_\varepsilon g_*\rangle\ge\lambda_*-\|D_\varepsilon\|\). Thus \(0\le\lambda_*-\lambda_\varepsilon\le\|D_\varepsilon\|\) without requiring \(D_\varepsilon\) to be positive semidefinite as an operator.

For \(0\le t\le1\), set
\[
H_\varepsilon(t)=\int_0^t\left(r^{-1/2}-r^{-1/2+\varepsilon/2}\right)dr
=2\sqrt t-\frac{2}{1+\varepsilon}t^{(1+\varepsilon)/2}.
\]
The row integral of the nonnegative kernel of \(D_\varepsilon\) at \(x\) is
\[
H_\varepsilon(x)+H_\varepsilon(1-x).
\]
Moreover,
\[
H_\varepsilon''(t)=\frac12t^{-3/2}\left((1-\varepsilon)t^{\varepsilon/2}-1\right)<0
\]
for \(0<t\le1\). Thus \(H_\varepsilon\) is strictly concave, and the symmetric row-sum function is maximized at \(x=1/2\). Its maximum is exactly
\[
2H_\varepsilon(1/2)
=2\sqrt2\left(1-\frac{2^{-\varepsilon/2}}{1+\varepsilon}\right)
=\delta(\varepsilon).
\]
Schur's test therefore yields \(\|D_\varepsilon\|\le\delta(\varepsilon)\). Combining this with the two Rayleigh-quotient comparisons gives
\[
\max\{0,\lambda_* -\delta(\varepsilon)\}\le\lambda_\varepsilon\le\lambda_*.
\]
Multiplication by \(\sqrt{1+\varepsilon}/2\) proves the two-sided enclosure. Subtracting \(\lambda_*/2\) and using the triangle inequality proves the displayed explicit error modulus.

Finally, \(\delta(\varepsilon)=\sqrt2(2+\log2)\varepsilon+O(\varepsilon^2)\), so the bound has the correct first-order scale required by the source asymptotic.

## Verification
The source certifies
\[
2.682918382150264832337066716763<\lambda_*<2.682918382150264832337066725454.
\]
Substitution makes the enclosure numerical without requiring a new eigenvalue computation. At \(\varepsilon=0.02\), direct high-precision evaluation gives
\[
\delta(0.02)=0.0746136429069799366\ldots,
\]
followed by
\[
1.3171293297370383<R(0.02)<1.3548073724874499.
\]
The standalone `verify.py` reproduces these numbers and checks the derivative signs on a diagnostic grid. The proof of the operator inequality is analytic and does not depend on that finite grid.

## Relationship to prior work
Moldavskaya proves \(\Lambda_2(\alpha,0)=C_{2,0}\sqrt{1-2\alpha}[1+O(1-2\alpha)]\), identifies \(C_{2,0}=\lambda_*/2\), and gives a certified 25-decimal enclosure for \(\lambda_*\). The same paper explicitly identifies an explicit remainder for the unweighted boundary asymptotic as a useful open quantitative refinement. Its proof records only a local \(O(|\alpha-1/2|)\) Schur estimate. The formula above computes a global row-sum bound exactly and turns it into a usable interior-parameter enclosure.

The cited companion manuscript on global bounds and parameter expansions is listed by the source as unpublished and was not publicly available in the searches used here. That inaccessible manuscript is therefore a residual originality risk, not evidence of coverage.

## Limitations
The enclosure is not claimed sharp, and no second-order asymptotic coefficient is identified. It controls only the unweighted rank-two memory-boundary path. The numerical example illustrates the certified enclosure rather than an optimal error bar. The result also does not alter the stochastic assumptions of the underlying LIL theorem.

## References
1. E. Moldavskaya, *Constants in the Weighted Law of the Iterated Logarithm under Long-Range Dependence: Hermite Rank Two*, arXiv:2609.30331v1, 2026.
2. E. Moldavskaya, *Law of the Iterated Logarithm for Weighted Sums of Functionals of Long-Memory Gaussian Sequences*, arXiv:2606.21006, 2026.
3. M. S. Veillette and M. S. Taqqu, *Properties and numerical evaluation of the Rosenblatt distribution*, Bernoulli 19(3), 2013.
