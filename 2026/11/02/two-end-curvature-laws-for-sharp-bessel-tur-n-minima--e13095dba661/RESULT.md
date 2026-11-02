# Two-end curvature laws for sharp Bessel Turán minima

## Finding
Fix an integer \(n\ge1\). Denote by \(j_{\mu,k}\) the \(k\)-th positive zero of the Bessel function \(J_\mu\), and put
\[
\Phi_\mu(x)=1-\frac{J_{\mu-1}(x)J_{\mu+1}(x)}{J_\mu(x)^2},\qquad
\beta_n(\mu)=\min_{j_{\mu,n}<x<j_{\mu,n+1}}\Phi_\mu(x),\quad \mu>0.
\]
The minimum is unique. Write \(r_n=j_{1,n}\). As \(\mu\downarrow0\),
\[
\boxed{\beta_n(\mu)=1-\frac{\mu^2}{r_n^2}+\frac{2\mu^3}{r_n^4J_0(r_n)^2}+O_n(\mu^4)},\qquad
\boxed{\beta_n''(\mu)=-\frac{2}{r_n^2}+\frac{12\mu}{r_n^4J_0(r_n)^2}+O_n(\mu^2)}.
\]
For the opposite endpoint let \(a_1>a_2>\cdots\) be the negative real zeros of \(\operatorname{Ai}\), let \(s_k=-a_k/2^{1/3}\), and define
\[
U(s)=\operatorname{Ai}(-2^{1/3}s),\quad Q(s)=\frac{U'(s)}{U(s)},\quad
F(s)=2s+Q(s)^2,\quad c_n=\min_{s_n<s<s_{n+1}}F(s).
\]
The positive constant \(c_n\) has a unique minimizing argument. As \(\mu\to\infty\),
\[
\boxed{\beta_n(\mu)=c_n\mu^{-2/3}+O_n(\mu^{-4/3})},\qquad
\boxed{\beta_n''(\mu)=\frac{10c_n}{9}\mu^{-8/3}+O_n(\mu^{-10/3})}.
\]
Consequently the order curvature is strictly negative near zero and strictly positive for sufficiently large order, for **every fixed nodal index**. In particular it changes sign at least once. No uniqueness of the sign change is asserted.

## Assumptions and scope
All parameters \(\mu\) are real and positive, and \(n\) is fixed as \(\mu\) tends to either endpoint. The Bessel functions and zeros have their standard normalization. The stated limits are not uniform as \(n\) grows. Derivatives of \(\beta_n\) are derivatives with respect to the order \(\mu\), not with respect to the spatial argument.

## Proof
**1. The smooth minimizer.** Put \(y_\mu(x)=xJ_\mu'(x)/J_\mu(x)\). Standard recurrences and the Bessel equation give
\[
\Phi_\mu(x)=1+\frac{y_\mu(x)^2-\mu^2}{x^2},\quad
y_\mu'(x)=-x\Phi_\mu(x),\quad
\frac{x\Phi_\mu'(x)}2=1-(1+y_\mu(x))\Phi_\mu(x).
\]
At every stationary point \(x\) of \(\Phi_\mu\), differentiation of the last identity gives \(\Phi_\mu''(x)=2\Phi_\mu(x)^2>0\). At the simple neighboring zeros of \(J_\mu\), the quotient diverges to \(+\infty\). Therefore there is exactly one stationary point in each nodal interval: two distinct strict minima would require an intervening stationary point that is not a strict minimum. Denote it by \(\alpha_n(\mu)\). Nondegeneracy and the analytic dependence of \(J_\mu(x)\) on \((\mu,x)\) make \(\alpha_n\) and \(\beta_n\) real-analytic locally in the order.

**2. Small-order expansion.** At \(\mu=0\), \(J_0'=-J_1\) and
\(\Phi_0(x)=1+(J_0'(x)/J_0(x))^2\). Its minimum on the interval bounded by the \(n\)-th and \((n+1)\)-st positive zeros of \(J_0\) is exactly at \(x=r_n=j_{1,n}\), with \(\Phi_0(r_n)=1\) and \(\Phi_0''(r_n)=2\). Thus \(\alpha_n(0)=r_n\).

The Bessel order derivative identity \(\left.\partial_\mu J_\mu(x)\right|_{\mu=0}=\pi Y_0(x)/2\) and the Wronskian \(J_1(r_n)Y_0(r_n)-J_0(r_n)Y_1(r_n)=2/(\pi r_n)\) show that
\[
\left.\partial_\mu\frac{J_\mu'}{J_\mu}\right|_{(0,r_n)}
=-\frac{\pi Y_1(r_n)}{2J_0(r_n)}=\frac{1}{r_nJ_0(r_n)^2},\quad
\left.\partial_x\frac{J_0'}{J_0}\right|_{r_n}=-1.
\]
At a stationary point the identity \(\Phi_\mu=1/(1+y_\mu)\), combined with the first formula of step 1, gives \(y_\mu(\alpha_n(\mu))=O_n(\mu^2)\). In particular \(J_\mu'(\alpha_n(\mu))/J_\mu(\alpha_n(\mu))=O_n(\mu^2)\). Implicit differentiation at order zero then yields
\[
\alpha_n(\mu)=r_n+\frac{\mu}{r_nJ_0(r_n)^2}+O_n(\mu^2).
\]
The exact expression \(\beta_n=1+(y_\mu(\alpha_n)^2-\mu^2)/\alpha_n^2\) now gives \(\beta_n=1-\mu^2/\alpha_n^2+O_n(\mu^4)\), and substitution yields the displayed cubic expansion. Since this is an analytic expansion in \(\mu\) near zero, it can be differentiated twice, giving the claimed small-order curvature formula.

**3. Large-order turning-point reduction.** Put \(t=\mu^{-2/3}\) and \(x=\mu+\mu^{1/3}s\). On compact \(s\)-intervals let
\[
R_\mu(s)=\frac{J_\mu(\mu+\mu^{1/3}s)}{J_\mu(\mu)}.
\]
The denominator is nonzero for large positive \(\mu\). The rescaled Bessel equation is exactly
\[
(1+ts)^2R_\mu''+t(1+ts)R_\mu'+(2s+ts^2)R_\mu=0.
\]
The classical uniform large-order turning-point expansions for both \(J_\mu\) and \(J_\mu'\) (DLMF §§10.20(i),(ii), including the Olver 1954 complex-order extension cited there) give \(R_\mu(s)=U(s)/U(0)+O_n(t)\), locally with all required spatial derivatives. For the stated **order-curvature remainder**, the requisite stronger form is important: these expansions have complete expansions in integral powers of \(t\), uniformly in a fixed complex-order sector about the positive axis. Their error bounds, Cauchy's estimates in complex order, and the analytic-coefficient rescaled ODE give
\[
R_\mu(s)=R_0(s)+tR_1(s)+t^2R_2(s)+O_n(t^3),
\quad R_0(s)=U(s)/U(0),
\]
locally with two order derivatives satisfying \(\partial_\mu^j O_n(t^3)=O_n(t^3\mu^{-j})\) for \(j=0,1,2\). One may equivalently start with the complete complex-uniform series for \(R_\mu'(0)\), fix \(R_\mu(0)=1\), and propagate its successive coefficients through the displayed regular differential equation. This identifies which asymptotic error may legitimately be differentiated; a mere pointwise Airy limit would not suffice.

The exact Turán identity becomes, wherever \(R_\mu\ne0\),
\[
\frac{\Phi_\mu(\mu+\mu^{1/3}s)}{t}
=\frac{1-(1+ts)^{-2}}{t}
+\left(\frac{R_\mu'(s)}{R_\mu(s)}\right)^2
=F(s)+t F_1(s)+t^2F_2(s)+O_n(t^3).
\]
This expansion holds locally with two order derivatives away from the zeros of \(U\). The rescaled consecutive Bessel zeros approach \(s_n,s_{n+1}\). On their intervening interval, \(Q'(s)=-F(s)\) by the Airy equation; thus
\[
F'(s)=2-2Q(s)F(s),\qquad F''(s)=2F(s)^2>0\quad\text{whenever }F'(s)=0.
\]
As \(s\) approaches either Airy zero, \(F(s)\to+\infty\). There is therefore exactly one stationary point \(s_n^*\in(s_n,s_{n+1})\), it is a nondegenerate global minimum, and \(c_n=F(s_n^*)>0\). Uniform convergence away from the endpoints, plus the strict-minimum property of the exact Bessel profile, places the Bessel minimizer at \(s_n^*+O_n(t)\). To see that it cannot escape to the ends, note that the derivative vanishing condition and \(\Phi_\mu\ll t\) at a fixed interior test point force the scaled logarithmic derivative to stay bounded, whereas it diverges at each zero; use the zero convergence and the uniform Airy expansion in a fixed neighborhood of each endpoint. The nondegenerate implicit equation then gives a complete differentiable expansion of the minimizing \(s\)-coordinate in \(t\).

Consequently
\[
\beta_n(\mu)=c_nt+t^2d_n+O_n(t^3)
\]
with the remainder carrying two order derivatives of the expected sizes. Substituting \(t=\mu^{-2/3}\), and differentiating this **complete uniform expansion**, yields
\[
\beta_n''(\mu)=\frac{10c_n}{9}\mu^{-8/3}+O_n(\mu^{-10/3}).
\]
Since \(c_n>0\), the large-order curvature is eventually positive. The small-order formula is eventually negative; continuity produces a sign change.

## Verification
A standalone numerical checker `CHECK.py` evaluates the exact normalized Turán expression, independently reconstructs first nodal minimizers, compares the cubic small-order expansion for three indices, computes the Airy minimum, and checks the large-order scaled convergence. It is supplementary only: numerical samples do not certify the infinite-parameter claims. The decisive checks are the analytic Bessel identities, nondegeneracy, and the complex-uniform differentiable Airy expansion used above.

## Relationship to prior work
Aktaş and Baricz (2026) prove uniqueness and order monotonicity of the nodal minima, then explicitly ask about the second derivative with respect to the order (their Question 1). Their theorem does not provide the two endpoint curvature laws. Baricz and Pogány (2014) discuss classical unnormalized Turán extrema and bounds, but not these order-curvature asymptotics. Uniform Bessel turning-point expansions and order differentiation are classical tools; the new claim is their application to the sharp nodal minima, with both explicit endpoint coefficients. A published result on the inverse-square **nodal-index** limit treats fixed order and the different limit \(n\to\infty\); its implication does not cover the fixed-index order-curvature laws.

## Limitations
The proof does not establish exactly one inflection point, its location, a bound on the number of inflection points, or uniformity as the nodal index grows. The complex-uniform turning-point expansion is used as a standard external theorem and not reproved here. Earlier unindexed work on Bessel parameter derivatives could potentially contain equivalent endpoint formulas.

## References
1. I. Aktaş and Á. Baricz, *Turán type inequalities for oscillatory special functions* (first public 2026-09-30), arXiv:2609.39008v1, especially §§2 and 8, Question 1. https://arxiv.org/abs/2609.39008
2. Á. Baricz and T. K. Pogány, *Turán determinants of Bessel functions*, arXiv:1101.4624 (first public 2011-01-24); Forum Mathematicum 26 (2014), 295–322. https://arxiv.org/abs/1101.4624
3. NIST Digital Library of Mathematical Functions, §§10.5 (Wronskians), 10.15 (order derivatives), 10.20(i)–(ii) (uniform large-order Airy expansions), 10.21 (zeros). https://dlmf.nist.gov/10.20
4. T. M. Dunster, *Uniform asymptotic expansions for the zeros of Bessel functions*, arXiv:2310.16016, 2023. https://arxiv.org/abs/2310.16016
