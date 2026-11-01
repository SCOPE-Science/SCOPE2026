# Uniform double-scaling laws for the sharp nodal Bessel Turán constants

## Finding

Let \(J_\nu\) denote the Bessel function of the first kind, \(\nu>0\), and let \(j_{\nu,1}<j_{\nu,2}<\cdots\) be its positive zeros. On each open nodal interval define
\[
\Phi_\nu(x)=1-\frac{J_{\nu-1}(x)J_{\nu+1}(x)}{J_\nu(x)^2},\qquad
\alpha_{\nu,n}=\operatorname*{argmin}_{j_{\nu,n}<x<j_{\nu,n+1}}\Phi_\nu(x),\quad
\beta_{\nu,n}=\Phi_\nu(\alpha_{\nu,n}).
\]
The existence and uniqueness of this minimizer for every \(\nu>0\) and integer \(n\geq1\) follow from the strictly convex nodal branches established by Aktaş and Baricz [1].

For \(t>1\), put
\[
\eta(t)=\sqrt{t^2-1}-\arccos(1/t).
\]
For each \(\nu>0\) and integer \(n\geq1\), let \(t_{\nu,n}>1\) be the unique solution of
\[
\eta(t_{\nu,n})=\frac{\pi(n+1/4)}{\nu}.
\]
**Theorem.** Given any compact interval \(K\subset(0,\infty)\), as \(\nu\to\infty\) over positive real orders and \(n\geq1\) ranges over the integers with \(n/\nu\in K\), the following expansions hold uniformly:
\[
\boxed{\frac{\alpha_{\nu,n}}{\nu}
=t_{\nu,n}-\frac{t_{\nu,n}(9t_{\nu,n}^2+22)}{24\nu^2(t_{\nu,n}^2-1)^2}
+O_K(\nu^{-4})},
\]
\[
\boxed{\beta_{\nu,n}
=1-\frac1{t_{\nu,n}^2}
-\frac{9t_{\nu,n}^2+10}{12\nu^2t_{\nu,n}^2(t_{\nu,n}^2-1)^2}
+O_K(\nu^{-4})}.
\]
In particular, for any sequence \(n/\nu\to\kappa\in(0,\infty)\),
\[
\lim\beta_{\nu,n}=1-t(\kappa)^{-2},\qquad
\eta(t(\kappa))=\pi\kappa,\quad t(\kappa)>1.
\]
This nonconstant limit describes the macroscopic crossover in which the nodal index and Bessel order grow together.

## Assumptions and scope

All orders \(\nu\) are **positive real numbers**, and all indices \(n\) are positive integers. Uniformity is claimed only for ratios \(n/\nu\) in a *fixed compact subset* of \((0,\infty)\), so the turning-point layer \(n=o(\nu)\) and the far-tail layer \(n/\nu\to\infty\) are excluded. \(O_K(\nu^{-4})\) means an absolute bound uniform in the specified indices, with a constant depending on \(K\) alone. The function \(\eta\) is strictly increasing because \(\eta'(t)=\sqrt{t^2-1}/t>0\), tends to zero at \(t\downarrow1\), and diverges as \(t\to\infty\); thus \(t_{\nu,n}\) is well defined.

## Proof

**1. Nodal phase coordinates.** Set \(u(t)=\sqrt{t^2-1}\), \(k(t)=u(t)/t\), and \(\theta_\nu(t)=\nu\eta(t)-\pi/4\). On any compact subinterval of \((1,\infty)\), the classical differentiated Debye expansions for Bessel functions [2, §10.19(ii), especially 10.19.5–10.19.7; 3] give, with uniform differentiable remainders,
\[
J_\nu(\nu t)=\left(\frac{2}{\pi\nu u(t)}\right)^{1/2}
\left[\left(1+O_K(\nu^{-2})\right)\cos\theta_\nu(t)
+\left(\frac{B(t)}\nu+O_K(\nu^{-3})\right)\sin\theta_\nu(t)\right],
\]
\[
B(t)=\frac{1}{8u(t)}+\frac{5}{24u(t)^3}.
\]
The even powers of \(\nu^{-1}\) multiply the cosine and the odd powers multiply the sine; one may differentiate these expansions to the required finite order. In particular, the zeros at the ends of the \(n\)-th nodal interval have phase \((n-1/2)\pi+O_K(\nu^{-1})\) and \((n+1/2)\pi+O_K(\nu^{-1})\). These zero estimates follow uniformly from the same Debye expansion and the simplicity of the limiting cosine zeros. The central phase \(\theta_\nu(t_{\nu,n})=n\pi\) lies in that nodal interval for all sufficiently large \(\nu\), uniformly with \(n/\nu\in K\).

**2. Localization at the phase center.** The Bessel recurrences and differential equation give the exact identities
\[
\Phi_\nu(x)=1-\frac{\nu^2}{x^2}+\left(\frac{J_\nu'(x)}{J_\nu(x)}\right)^2,
\qquad
\frac{x}{2}\Phi_\nu'(x)=1-\left(1+x\frac{J_\nu'(x)}{J_\nu(x)}\right)\Phi_\nu(x).
\]
These are also equations (2.4)–(2.5) of [1]. The two zeros bracketing the minimum have \(x/\nu\) in a fixed compact subinterval of \((1,\infty)\); therefore \(1-\nu^2/x^2\) has a uniform strictly positive lower bound. At the minimum, \(\Phi_\nu=\beta_{\nu,n}\), while evaluating at the phase center gives \(\beta_{\nu,n}\leq1-t_{\nu,n}^{-2}+O_K(\nu^{-2})\). Hence \(\beta_{\nu,n}\) is uniformly bounded away from zero and infinity. The stationarity identity yields
\[
\alpha_{\nu,n}\frac{J_\nu'(\alpha_{\nu,n})}{J_\nu(\alpha_{\nu,n})}=\frac1{\beta_{\nu,n}}-1=O_K(1).
\]
Writing \(\alpha_{\nu,n}=\nu s\) implies the logarithmic derivative is \(O_K(\nu^{-1})\). After multiplying the differentiated Debye quotient by its denominator, the leading terms give \(k(s)\sin\theta_\nu(s)=O_K(\nu^{-1})|\cos\theta_\nu(s)|+O_K(\nu^{-2})|\sin\theta_\nu(s)|\), because the quotient itself is \(O_K(\nu^{-1})\). The uniform positivity of \(k\) then implies \(\tan\theta_\nu(s)=O_K(\nu^{-1})\) (including the exclusion of neighborhoods of poles). Since the phase runs only once between the two adjacent zeros, necessarily
\[
\theta_\nu(s)=n\pi+O_K(\nu^{-1}),\qquad s=t_{\nu,n}+O_K(\nu^{-2}).
\]

**3. Coefficient of the minimizer.** Write \(t=t_{\nu,n}\) temporarily, and \(\theta_\nu(s)=n\pi+\delta/\nu\). The preceding estimate gives \(\delta=O_K(1)\). Differentiate the Debye expansion and divide by the expansion itself; since \(s=t+O_K(\nu^{-2})\), this yields
\[
\frac{J_\nu'(\nu s)}{J_\nu(\nu s)}
=\frac1\nu\biggl[D_0(t)+k(t)(B(t)-\delta)\biggr]+O_K(\nu^{-3}),
\qquad D_0(t)=-\frac{t}{2(t^2-1)}.
\]
Because \(s=t+O_K(\nu^{-2})\) and the logarithmic derivative is \(O_K(\nu^{-1})\), the exact quotient formula now gives \(\beta_{\nu,n}=1-t^{-2}+O_K(\nu^{-2})\). From the minimum identity one also gets
\[
\frac{J_\nu'(\nu s)}{J_\nu(\nu s)}
=\frac{1}{\nu t(t^2-1)}+O_K(\nu^{-3}).
\]
Consequently,
\[
\delta=B(t)+\frac{D_0(t)-1/[t(t^2-1)]}{k(t)}+O_K(\nu^{-2})
=-\frac{9t^2+22}{24(t^2-1)^{3/2}}+O_K(\nu^{-2}).
\]
Taylor expansion of \(\eta\) in \(\theta_\nu(s)-\theta_\nu(t)=\nu(\eta(s)-\eta(t))\), using \(\eta'(t)=k(t)\), gives
\[
s=t+\frac\delta{\nu^2k(t)}+O_K(\nu^{-4})
=t-\frac{t(9t^2+22)}{24\nu^2(t^2-1)^2}+O_K(\nu^{-4}).
\]
The displayed error order uses the Debye even/odd structure: the next possible error in \(\delta\) is \(O_K(\nu^{-2})\), not \(O_K(\nu^{-1})\).

**4. Minimum value.** At the minimum, the logarithmic derivative squared is
\[
\left(\frac{J_\nu'(\alpha_{\nu,n})}{J_\nu(\alpha_{\nu,n})}\right)^2
=\frac{1}{\nu^2t^2(t^2-1)^2}+O_K(\nu^{-4}).
\]
Substitute the location expansion into the exact formula in Step 2, obtaining
\[
\beta_{\nu,n}
=1-t^{-2}+\frac1{\nu^2}\left[-\frac{9t^2+22}{12t^2(t^2-1)^2}+\frac{1}{t^2(t^2-1)^2}\right]+O_K(\nu^{-4})
=1-t^{-2}-\frac{9t^2+10}{12\nu^2t^2(t^2-1)^2}+O_K(\nu^{-4}).
\]
Finally, if \(n/\nu\to\kappa>0\), then \(t_{\nu,n}\to t(\kappa)\) by continuity and monotonicity of \(\eta^{-1}\), proving the limit.

## Verification

The supplement `CHECK.py` independently evaluates the unique stationary point through the exact Bessel differential equation and checks the predicted scaled location and deficit for integer and noninteger orders. It also checks the key coefficient identity at an exact rational point. These finite numerical tests are supplementary, not a substitute for the uniform Debye and stationary-phase proof. The two input identities, the Debye coefficient, index convention and error parity are explicitly identified above so that the calculation can be reproduced.

## Relationship to prior work

Aktaş and Baricz [1, §2] prove strict convexity, uniqueness, monotonicity and qualitative convergence of successive nodal minima for fixed Bessel order; their open questions in §8 concern order variation rather than the simultaneous growth regime. The previously published result *Inverse-square convergence of sharp cylinder-function Turán minima* [4] gives \(1-\beta_{\mu,n}=\mu^2/(\pi^2n^2)+O_{\mu,\alpha}(n^{-3})\) for **fixed order** and \(n\to\infty\), and explicitly excludes simultaneous large-order/large-index asymptotics. It cannot imply this theorem, because its error constant depends on the fixed order and it controls only the far-tail endpoint, not the nonconstant ratio-dependent interior profile or its two correction laws. The earlier survey by Baricz and Pogány [5, §2.8] formulated the nodal-minimum conjecture and bounds, while Baricz, Ponnusamy and Singh [6, Theorems 1–3] analyze inequalities and extrema of the *unnormalized* cylinder Turánian; neither supplies an interior joint-order/index asymptotic of the sharp nodal normalized minimum. Classical Debye expansions [2,3] supply local asymptotics for \(J_\nu\), but do not themselves identify the sharp normalized Turán minima across nodal intervals; the nontrivial stationarity equation and uniform localization produce the displayed rational coefficients.

## Limitations

The theorem is restricted to the Bessel function \(J_\nu\) and the range \(n/\nu\in K\Subset(0,\infty)\). It does not address the turning-point transition \(n=o(\nu)\), the far tail \(n/\nu\to\infty\), general cylinder phases, or optimal error constants. Independent mathematical review has not been performed. As with any literature-based originality assessment, earlier unindexed equivalent asymptotic computations remain possible.

## References

1. I. Aktaş and Á. Baricz, *Turán type inequalities for oscillatory special functions*, arXiv:2609.39008v1 (first posted 2026-09-30), especially §2 and §8. https://arxiv.org/abs/2609.39008
2. NIST Digital Library of Mathematical Functions, §10.19(ii), formulas 10.19.5–10.19.7, and §10.41(ii), Debye polynomials. https://dlmf.nist.gov/10.19 and https://dlmf.nist.gov/10.41
3. G. N. Watson, *A Treatise on the Theory of Bessel Functions*, 2nd ed., Cambridge University Press, 1944, pp. 241–245.
4. *Inverse-square convergence of sharp cylinder-function Turán minima*, public research note, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-inverse-square-convergence-of-sharp-cylinder-function-tur-n-mini--7a66df847375
5. Á. Baricz and T. K. Pogány, *Turán determinants of Bessel functions*, arXiv:1101.4624, §2.8. https://arxiv.org/abs/1101.4624
6. Á. Baricz, S. Ponnusamy, and S. Singh, *Turán type inequalities for general Bessel functions*, arXiv:1502.02877v1, especially Theorems 1–3. https://arxiv.org/html/1502.02877v1
