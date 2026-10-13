# A sharp one-epoch variance-reversal threshold for two-component random reshuffling

## Finding
For scalar finite-sum minimization with **two strictly convex quadratic components**, random reshuffling (RR) can have **larger** expected last-iterate objective error than independent sampling with replacement (IID), even when each component gradient map is a strict contraction. This reversal has an exact and sharp parameter frontier.

For every \(\lambda_1,\lambda_2,c,\eta>0\), let
\[
q_1(x)=\frac{\lambda_1}{2}x^2+cx,\qquad
q_2(x)=\frac{\lambda_2}{2}x^2-cx,\qquad
F(x)=\frac{q_1(x)+q_2(x)}2=\frac{\lambda_1+\lambda_2}{4}x^2.
\]
Starting from the minimizer \(x_0=0\), after two component-gradient updates with constant step \(\eta\), the exact mean-square comparison is
\[
\boxed{\ \mathbb E_{\mathrm{RR}}[x_2^2]-\mathbb E_{\mathrm{IID}}[x_2^2]
=\eta^2c^2[\eta(\lambda_1+\lambda_2)-2].\ }
\]
The expected objective-gap comparison has the same sign, since the common objective-gap factor is \((\lambda_1+\lambda_2)/4>0\). Consequently, strict RR disadvantage occurs if and only if \(\eta(\lambda_1+\lambda_2)>2\), with equality at the exact transition. For the entire class \(0<\lambda_i\le L\), a uniform no-disadvantage conclusion at the minimizer holds exactly for \(\eta\le1/L\) in the range \(0<\eta<2/L\). Necessity is attained by setting \(\lambda_1=\lambda_2=L\).

**Stronger all-start conclusion.** In the equal-curvature subfamily \(\lambda_1=\lambda_2=L\), for every deterministic \(x_0\in\mathbb R\),
\[
\boxed{\ \mathbb E_{\mathrm{RR}}[x_2^2]-\mathbb E_{\mathrm{IID}}[x_2^2]
=2\eta^2c^2(\eta L-1).\ }
\]
Thus the reversal above \(1/L\) is independent of the starting point. This identity is part of the same one-epoch comparison, not a separate asymptotic assertion.

## Assumptions and scope
There are exactly two component functions and one real decision variable. Parameters \(\lambda_1,\lambda_2,c,\eta\) are positive real numbers; the objective is unconstrained, each component is strongly convex, and its gradient is computed without noise or arithmetic error. In each method there are **two** component-gradient evaluations: RR chooses order \((1,2)\) or \((2,1)\) with equal probability; IID draws each of the two component indices independently and uniformly at both steps. Expectations include only these sampling choices. The first identity starts from \(x_0=0\); the all-start extension requires equal component curvatures. The identities hold algebraically for every positive step; the practically salient individually stable regime is \(0<\eta\lambda_i<2\).

## Proof
Write \(t_i=\eta\lambda_i\), \(r_i=1-t_i\), and \(s_1=1,s_2=-1\). Component \(i\) induces the affine update
\[
T_i(x)=r_i x-\eta c s_i.
\]
With \(x_0=0\), the four possible two-step endpoints are computed exactly:
\[
\begin{array}{c|c}
\text{ordered indices}&x_2\\\hline
(1,2)&\eta c t_2\\
(2,1)&-\eta c t_1\\
(1,1)&-\eta c(2-t_1)\\
(2,2)&\eta c(2-t_2)
\end{array}.
\]
Therefore
\[
\mathbb E_{\mathrm{RR}}[x_2^2]
=\frac{\eta^2c^2}{2}(t_1^2+t_2^2),
\]
whereas IID gives each of the four sequences probability \(1/4\), and hence
\[
\mathbb E_{\mathrm{IID}}[x_2^2]
=\frac{\eta^2c^2}{4}\{t_1^2+t_2^2+(2-t_1)^2+(2-t_2)^2\}.
\]
Subtracting and simplifying proves
\[
\mathbb E_{\mathrm{RR}}[x_2^2]-\mathbb E_{\mathrm{IID}}[x_2^2]
=\eta^2c^2(t_1+t_2-2).
\]
Every sign and equality statement follows because \(\eta^2c^2>0\) and \(F(x)-F(0)=(\lambda_1+\lambda_2)x^2/4\). If \(\lambda_i\le L\) and \(\eta\le1/L\), then \(t_1+t_2\le2\). Conversely, whenever \(1/L<\eta<2/L\), setting \(\lambda_1=\lambda_2=L\) gives \(t_1+t_2>2\) while \(|1-\eta L|<1\), so both deterministic component-gradient maps are strict contractions. This proves the sharp uniform cutoff in the stated family.

For the all-start identity, put \(\lambda_1=\lambda_2=L\), \(t=\eta L\), and \(r=1-t\). Both methods then have the same deterministic part \(r^2x_0\) in the final iterate, and the random part has mean zero. Under RR the two signs are opposite, so the random part is \(\pm\eta ct\) and has variance \(\eta^2c^2t^2\). Under IID the signs are independent, so the random part has variance \(\eta^2c^2(1+r^2)\). Their expected squares differ by
\[
\eta^2c^2[t^2-1-(1-t)^2]=2\eta^2c^2(t-1),
\]
regardless of \(x_0\). This proves the extension.

A rational witness takes \(\lambda_1=\lambda_2=3/2\), \(\eta=c=1\). The two RR endpoints are \(\pm3/2\), whereas IID has endpoints of magnitudes \(3/2\) and \(1/2\), each with total probability \(1/2\). Hence its expected squared errors are \(9/4\) (RR) and \(5/4\) (IID); both component maps have contraction factor \(1/2\) in absolute value. The same difference holds for any deterministic \(x_0\).

## Verification
The included standalone `verify.py` exhaustively enumerates the four possible two-step index sequences using rational arithmetic; it checks the displayed identity over a fixed, reproducible grid of positive rational curvatures, step lengths, and nonzero gradient offsets. It separately checks the equal-curvature identity over arbitrary rational starting points. The analytic proof, not the finite checks, establishes the results for all parameters in the stated domains. Run `python verify.py` with the Python standard library; the successful script prints `VERIFY_OK` with check counts.

## Relationship to prior work
Liu's 2026 work on random reshuffling proves bounds that dominate corresponding SGD **worst-case averaged-iterate convergence rates** for smooth convex finite sums. Its analysis and two-component appendix address those rate bounds, not the exact instancewise **last iterate after a single epoch** in this two-quadratic family. The present reversal therefore does **not** contradict that theorem. De Sa (2020) previously gave non-dominance examples, notably in higher-dimensional/noiseless asymptotic settings; the general idea that RR can be worse is **not new**. The contribution here is the complete one-dimensional, two-component, one-epoch parameter frontier and its all-start equal-curvature strengthening. Domingo-Enrich (2022) studies chiefly stationary variances through a spectral-noise model, with small-step asymptotics, rather than this finite-horizon reversal threshold. These comparisons do not establish exhaustiveness of all possible synonymous earlier observations.

## Limitations
This is an exact finite-horizon comparison of a deliberately minimal class, not a theorem asserting that RR is generally inferior. It compares **last iterates** after exactly two updates with the same constant step and the same sampling budget, not ergodic averages, long-run stationary errors, or minimax convergence rates. The general-curvature identity needs the initial point to be the common finite-sum minimizer; the robust all-start version needs equal curvatures. Finite rational tests are consistency checks rather than proofs of parameter-uniform claims. Other older formulations of variance comparisons may contain equivalent observations; independent audit has not been performed.

## References
1. Z. Liu, *Random Reshuffling Dominates Stochastic Gradient Descent*, COLT 2026, Proceedings of Machine Learning Research 336, 4859–4882, https://proceedings.mlr.press/v336/liu26d.html ; first arXiv version 2026-06-30, https://arxiv.org/abs/2606.32005 .
2. Z. Liu, *Random Reshuffling for Smooth Convex Optimization: Dominates Stochastic Gradient Descent*, extended version, 2026, https://optimization-online.org/wp-content/uploads/2026/09/Random-Reshuffling-for-Smooth-Convex-Optimization.pdf .
3. C. De Sa, *Random Reshuffling is Not Always Better*, NeurIPS 2020, https://proceedings.neurips.cc/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Paper.pdf .
4. C. Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, 2022, https://arxiv.org/abs/2206.00632 .
