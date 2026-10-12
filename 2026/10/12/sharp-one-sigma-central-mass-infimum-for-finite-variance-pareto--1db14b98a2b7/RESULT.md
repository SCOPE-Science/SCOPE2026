# Sharp one-sigma central-mass infimum for finite-variance Pareto laws
## Finding
Let \(X_{a,\alpha}\) have the Pareto type-I law with scale \(a>0\), shape \(\alpha>2\), and survival function
\[
\Pr\{X_{a,\alpha}>x\}=\left(\frac{a}{x}\right)^\alpha,\qquad x\ge a.
\]
Write \(\mu=\mathbb E X_{a,\alpha}\) and \(\sigma^2=\operatorname{Var}(X_{a,\alpha})\). Then
\[
\Pr\{|X_{a,\alpha}-\mu|\le\sigma\}
=1-\left(\frac{\alpha-1}{\alpha+\sqrt{\alpha/(\alpha-2)}}\right)^\alpha.
\]
For every finite \(\alpha>2\), this probability is strictly larger than \(1-e^{-2}\), and
\[
\Pr\{|X_{a,\alpha}-\mu|\le\sigma\}
=1-e^{-2}+\frac{e^{-2}}{\alpha}+O(\alpha^{-2})
\qquad(\alpha\to\infty).
\]
Hence
\[
\inf_{a>0,\,\alpha>2}
\Pr\{|X_{a,\alpha}-\mathbb E X_{a,\alpha}|\le
\sqrt{\operatorname{Var}(X_{a,\alpha})}\}
=1-e^{-2},
\]
and the infimum is not attained.

## Assumptions and scope
The result concerns the ordinary Pareto type-I family and exactly the finite-variance regime \(\alpha>2\). The scale \(a\) is arbitrary and cancels from the standardized probability. The statement is an infimum over the Pareto family only; it does not assert a distribution-free one-standard-deviation bound. It also does not claim that the same endpoint controls central windows of every standardized radius.

## Proof
For \(\alpha>2\), the standard Pareto moments are
\[
\mu=\frac{\alpha a}{\alpha-1},\qquad
\sigma=\frac{a\sqrt{\alpha}}{(\alpha-1)\sqrt{\alpha-2}}.
\]
The lower endpoint of the one-standard-deviation interval lies below the support edge:
\[
\mu-\sigma<a
\iff
1<\sqrt{\frac{\alpha}{\alpha-2}},
\]
which is strict for every \(\alpha>2\). Thus only the upper tail can leave the interval, and exact Pareto tail summation gives
\[
\Pr\{|X_{a,\alpha}-\mu|\le\sigma\}
=\Pr\{X_{a,\alpha}\le\mu+\sigma\}
=1-\left(\frac{a}{\mu+\sigma}\right)^\alpha
=1-A_\alpha^{-\alpha},
\]
where
\[
A_\alpha
=\frac{\alpha+\sqrt{\alpha/(\alpha-2)}}{\alpha-1}
=\frac{\alpha}{\alpha-1}
\left(1+\frac{1}{\sqrt{\alpha(\alpha-2)}}\right).
\]
It remains to prove \(\alpha\log A_\alpha>2\). For every \(x>0\),
\[
\log(1+x)>\frac{x}{1+x}.
\]
Apply this first with \(x=1/(\alpha-1)\):
\[
\alpha\log\left(1+\frac{1}{\alpha-1}\right)>1.
\]
Apply it again with \(y=1/\sqrt{\alpha(\alpha-2)}\). Since
\[
(\alpha-1)^2=\alpha(\alpha-2)+1,
\]
we have \((\alpha-1)y>1\), and hence
\[
\alpha\log(1+y)>\frac{\alpha y}{1+y}>1.
\]
Adding the two strict inequalities yields \(\alpha\log A_\alpha>2\), so \(A_\alpha^{-\alpha}<e^{-2}\) and the central mass is strictly greater than \(1-e^{-2}\).

For sharpness, put \(u=1/\alpha\). Direct Taylor expansion at \(u=0\) gives
\[
\log A_\alpha
=2u+u^2+\frac{7}{6}u^3+O(u^4),
\]
so
\[
\alpha\log A_\alpha
=2+\frac{1}{\alpha}+\frac{7}{6\alpha^2}+O(\alpha^{-3}).
\]
Exponentiating,
\[
1-A_\alpha^{-\alpha}
=1-e^{-2}+\frac{e^{-2}}{\alpha}+\frac{2e^{-2}}{3\alpha^2}+O(\alpha^{-3}),
\]
which proves both the stated first correction and the unattained sharp infimum.

## Verification
The argument is analytic for the full parameter range \(\alpha>2\). A supplementary checker evaluates the exact closed form at representative shapes from just above \(2\) through \(10^6\), verifies the strict lower bound numerically, and checks the first-order asymptotic regression. Those finite checks are not used to prove the infinite statement.

## Relationship to prior work
Li, Hu, and Zhou study the Pareto family through the different functional \(\Pr\{X\le\kappa\mathbb E X\}\) with fixed \(\kappa\), including its exact shape optimization. Their Pareto section does not study a variance-scaled central interval. Hu, Song, and Tan later study the complementary anti-concentration extremum \(\inf\Pr\{|X-\mathbb EX|\ge y\sigma\}\) and show that it is zero for Pareto laws by sending the shape down to \(2\). That result is an infimum of the tail probability, equivalently a supremum-type statement for central mass, and therefore does not determine the infimum of central one-sigma mass proved here. The Gamma literature explicitly treats the infimum of one-standard-deviation central mass, making the Pareto analogue a natural missing member of the same variation-comparison program.

## Limitations
No monotonicity of the one-sigma probability in \(\alpha\) is asserted or needed. The theorem does not identify the infimum for arbitrary radii \(y\sigma\), where the extremal shape can behave differently. Literature searches and direct comparison with the most relevant Pareto papers did not locate the displayed sharp infimum, but an equivalent elementary observation under different terminology remains possible.

## References
1. C. Li, Z.-C. Hu, and Q.-Q. Zhou, *A study on the Weibull and Pareto distributions motivated by Chvátal's theorem*, arXiv:2305.02114v1, first public version 2023-05-03.
2. Z.-C. Hu, R. Song, and Y. Tan, *On the anti-concentration functions of some familiar families of distributions*, arXiv:2401.09998v1, first public version 2024-01-18.
3. P. Sun, Z.-C. Hu, and W. Sun, *The infimum values of two probability functions for the Gamma distribution*, Journal of Inequalities and Applications 2024, Article 5, DOI 10.1186/s13660-024-03081-w.
