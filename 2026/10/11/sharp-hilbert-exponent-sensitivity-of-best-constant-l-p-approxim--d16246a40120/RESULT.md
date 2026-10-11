# Sharp Hilbert-exponent sensitivity of best constant \(L^p\) approximants

## Finding

Let \(X\) be a bounded, nonconstant real random variable on an arbitrary probability space. For each \(p>1\), let \(m_p(X)\) denote the unique minimizer over real \(t\) of \(\mathbb E|X-t|^p\). Put \(\mu=\mathbb EX\) and \(\sigma=(\mathbb E|X-\mu|^2)^{1/2}>0\). Then the map \(p\mapsto m_p(X)\) is differentiable at \(p=2\), and

\[
\left.\frac{d}{dp}m_p(X)\right|_{p=2}=\mathbb E\big[(X-\mu)\log|X-\mu|\big],
\]

with the continuous convention \(0\log0=0\). There is a **sharp, distribution-independent** sensitivity bound

\[
\left|\left.\frac{d}{dp}m_p(X)\right|_{p=2}\right|\le K\sigma,
\qquad K=\frac{2a\log a}{1+a^2}=\frac{2a}{a^2-1}\approx0.662743419349182,
\]

where \(a>1\) is the unique solution of

\[
\frac{a^2-1}{a^2+1}\log a=1
\qquad(a\approx3.3190501422373).
\]

Equality holds precisely when the standardized variable \(Y=(X-\mu)/\sigma\) has the two-point law

\[
\mathbb P(Y=a)=\frac1{1+a^2},\quad
\mathbb P(Y=-1/a)=\frac{a^2}{1+a^2},
\]

or the reflection of this law. In particular, the universal constant is attained by bounded, finitely supported distributions.

For empirical measures with \(n\) equal masses, let \(S_n\) be the supremum of this derivative-to-standard-deviation ratio over nonconstant real data vectors. Then \(S_n\le K\) for every \(n\ge2\), and \(K-S_n=O(n^{-2})\) as \(n\to\infty\). The latter statement is an asymptotic proximity bound, **not** an exact formula for finite \(n\).

## Assumptions and scope

The probability measure is arbitrary and \(X\in L^\infty\) is real and nonconstant. Each minimizer is taken over constant real approximants. The exponent varies through \(p=2\) within \(p>1\); no exponent derivative at \(p=1\) or assertions for general unbounded \(X\) are made. All logarithms are natural. The numerical values are indicative only; the defining equation determines the exact constant.

## Proof

**1. Differentiation of the best constant.** Strict convexity and coercivity give a unique minimizer \(m_p\). The minimizer lies between the essential minimum and maximum of \(X\), and the optimality equation is

\[
0=\mathbb E\big[(X-m_p)|X-m_p|^{p-2}\big].
\]

Write \(p=2+\varepsilon\) and \(\psi_\varepsilon(u)=u|u|^\varepsilon\), defining \(\psi_\varepsilon(0)=0\). For \(|u|\le R\) and \(|\varepsilon|\le1/4\), Taylor's theorem yields the **uniform** expansion

\[
\psi_\varepsilon(u)=u+\varepsilon u\log|u|+O_R(\varepsilon^2).
\]

Indeed the second parameter derivative is \(u|u|^\theta(\log|u|)^2\), uniformly bounded for \(|\theta|\le1/4\), including near zero. The minimizers remain in a bounded interval and converge to \(\mu\) by uniform convergence of the strict convex objectives, or directly by their optimality equations. Substitution gives

\[
0=\mu-m_{2+\varepsilon}+\varepsilon\mathbb E\big[(X-m_{2+\varepsilon})\log|X-m_{2+\varepsilon}|\big]+O(\varepsilon^2).
\]

The signed logarithm is continuous, so division by \(\varepsilon\) and passage to the limit proves the derivative formula. Its scale dependence is legitimate: under replacing \(X\) by \(\mu+\sigma Y\), the extra \(\sigma\log\sigma\,\mathbb EY\) term vanishes, leaving \(\sigma\mathbb E[Y\log|Y|]\).

**2. A sharp scalar envelope.** Define \(g(s)=s\log|s|\) with \(g(0)=0\), and \(\phi(s)=g(s)/(1+s^2)\). A positive value of \(\phi\) is possible only for \(s>1\) or \(-1<s<0\). For \(s>1\), differentiation gives the critical-point equation

\[
\frac{s^2-1}{s^2+1}\log s=1.
\]

The left-hand side increases strictly from zero to infinity on \((1,\infty)\): its derivative is

\[
\frac{4s\log s}{(1+s^2)^2}+\frac{s^2-1}{s(1+s^2)}>0.
\]

Thus its unique critical point \(a\) is the unique global maximum on \((1,\infty)\), since \(\phi\) vanishes at both endpoints. The involution \(s\mapsto-1/s\) preserves \(\phi\) on positive \(s\), so \(-1/a\) is the only other positive maximum and there are no additional equality points. Consequently for every real \(s\),

\[
 g(s)\le\frac K2(1+s^2),
\]

with equality only at \(s=a\) and \(s=-1/a\). The critical equation also yields \(K=2a/(a^2-1)\).

**3. Universal sharpness and equality.** For any centered unit-variance real \(Y\), the scalar inequality gives

\[
\mathbb E[Y\log|Y|]\le\frac K2(1+\mathbb EY^2)=K.
\]

Apply it to \(-Y\) to bound the absolute value. If equality holds, nonnegativity of the scalar slack forces \(Y\in\{a,-1/a\}\) almost surely, or its reflection. The mean-zero requirement uniquely forces masses \(1/(1+a^2)\) and \(a^2/(1+a^2)\); direct evaluation confirms their variance is one and the signed logarithmic moment equals \(K\). Conversely those two laws attain equality. This proves the complete equality characterization and optimality.

**4. Equally weighted samples.** Let \(t_*=1/(1+a^2)\). For sufficiently large \(n\), choose an integer \(k_n\) nearest to \(nt_*\). Take \(k_n\) sample values \(\sqrt{(n-k_n)/k_n}\) and the remaining \(n-k_n\) values \(-\sqrt{k_n/(n-k_n)}\). The sample is centered and has variance one; its signed logarithmic moment equals

\[
F(t_n)=\sqrt{t_n(1-t_n)}\log\frac{1-t_n}{t_n},\qquad t_n=k_n/n.
\]

The constructed equality law gives \(F(t_*)=K\), while the universal bound makes \(t_*\) an interior maximizer of \(F\). Hence \(F'(t_*)=0\). As \(F\) has bounded second derivative near this interior point and \(|t_n-t_*|\le1/(2n)\), Taylor's theorem gives \(0\le K-S_n\le K-F(t_n)=O(n^{-2})\). No finite-dimensional optimizer classification is required.

## Verification

Run `python3 verify.py` with Python 3's standard library. The script bisects the defining equation, checks both two-point moments and equivalent exact expressions for \(K\), scans finite scalar-envelope samples, checks the explicit two-atom \(p\)-mean at nearby exponents, and tests the empirical-rate construction. It prints `EXPONENT_SENSITIVITY_CHECK_OK` when those finite numerical checks pass. The all-distribution inequality, equality cases, differentiability, and asymptotic bound rest on the analytic proof above, **not** on the numerical scans.

## Relationship to prior work

Arnaudon and Miclo, *A stochastic algorithm finding \(p\)-means on the circle* (arXiv:1301.7156, first public 2013-01-30), define generalized \(p\)-means by minimizing expected powered distance and analyze a stochastic convergence algorithm on the circle. Their statements do not supply a sharp derivative with respect to the power at the Hilbert exponent in real constant approximation. Aldaz, *Sharp bounds for the difference between the arithmetic and geometric means* (arXiv:1203.4454, first public 2012-03-20), proves distinct variance-controlled inequalities for nonnegative arithmetic/geometric means, not the signed sharp log-moment envelope here. Generalized Fréchet mean convergence-rate results, including Schötz (arXiv:1812.08037), address sample-size variation rather than exponent differentiation. A previous sharp data-Lipschitz estimate for best constant approximants controls variation in the **input**, a different quantity from derivative in the **exponent** and does not imply this optimal constant. Searches for signed-log-moment aliases and two-atom best constants did not produce an equivalent source, but this is not a proof of novelty.

## Limitations

The theorem is for bounded real random variables and exponent response at \(p=2\). It does not provide a uniform second-order Taylor remainder over all bounded distributions, nor a sharp finite-sample value \(S_n\) for each fixed \(n\). An equivalent historical moment inequality or parameter-sensitivity theorem may be unindexed; bibliographic distinctness is not an independent validation. The numerical verifier makes only finite consistency checks.

## References

- J. M. Aldaz, *Sharp bounds for the difference between the arithmetic and geometric means*, arXiv:1203.4454v1 (2012-03-20), https://arxiv.org/abs/1203.4454; full text https://arxiv.org/html/1203.4454v1.
- M. Arnaudon and L. Miclo, *A stochastic algorithm finding \(p\)-means on the circle*, arXiv:1301.7156v1 (2013-01-30), https://arxiv.org/abs/1301.7156; accessible revised full text https://arxiv.org/html/1301.7156v2.
- C. Schötz, *Convergence Rates for the Generalized Fréchet Mean via the Quadruple Inequality*, arXiv:1812.08037v1 (2018-12-19), https://arxiv.org/abs/1812.08037 (abstract and publication metadata checked).
