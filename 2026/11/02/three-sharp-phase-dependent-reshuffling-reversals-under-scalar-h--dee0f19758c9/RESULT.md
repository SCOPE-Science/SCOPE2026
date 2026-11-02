# Three sharp phase-dependent reshuffling reversals under scalar heavy-ball momentum

## Finding

Consider the stable, constant-step heavy-ball method on a two-component scalar strongly convex quadratic with opposite fixed gradient offsets, sampled either independently with replacement or by independently reshuffled two-sample epochs. The stationary expected squared error for reshuffling depends on which point of the epoch is observed. For strictly positive momentum, **the precise step-size intervals where reshuffling wins at the end of an epoch but loses after the first within-epoch update, and vice versa, have sharp algebraic boundaries**.

Write \(t=\eta\lambda\), let \(0<\beta<1\) and \(0<t<2(1+\beta)\), and define
\[
D=(1-\beta)[2(1+\beta)-t],\qquad
G=(t-1-\beta)^2+(1-\beta)^2,
\qquad U=(d/\lambda)^2.
\]
The limiting squared errors for sampling independently with replacement (\(V_{\rm I}\)), for reshuffling after the **second** step of an epoch (\(V_{\rm E}\)), and for reshuffling after the **first** step (\(V_{\rm O}\)) are exactly
\[
\begin{aligned}
V_{\rm I}&=U\,\frac{t(1+\beta)}{D},\\
V_{\rm E}&=U\left[\frac{t^2}{D}-\frac{t^2(1+\beta-t)}{(1+\beta)G}\right],\\
V_{\rm O}&=U\left[\frac{t^2}{D}+\frac{t^2(1+\beta-t)}{(1+\beta)G}\right].
\end{aligned}
\]
Introduce the three strictly ordered interior thresholds
\[
t_-=1+\beta-\sqrt{\beta(1-\beta^2)},\qquad
t_0=1+\beta,\qquad
t_+=1+\beta+\sqrt{\beta(1-\beta^2)}.
\]
Then reshuffling at the epoch end has less stationary expected squared error than independent sampling exactly for \(0<t<t_0\), and more for \(t_0<t<2(1+\beta)\). At the first step within each reshuffled epoch it has **less** error exactly for \(0<t<t_-\) and \(t_0<t<t_+\), but **more** for \(t_-<t<t_0\) and \(t_+<t<2(1+\beta)\). Equalities occur at the named interval endpoints.

In particular, for \(\lambda=d=1\), \(\beta=1/2\), and \(\eta=1\), the three limiting squared errors are
\[
V_{\rm E}=\frac13 < V_{\rm I}=\frac32 < V_{\rm O}=\frac53.
\]
Thus the same reshuffling algorithm is better at epoch boundaries and worse mid-epoch. The exact phase average obeys \((V_{\rm E}+V_{\rm O})/2=U t^2/D\); this average relation is included to distinguish the new phase-resolved result from previously studied time averages, and is not claimed as an independent discovery.

## Assumptions and scope

For \(\lambda>0\) and \(d\ne0\), use exactly two sample losses \(f_s(x)=\lambda x^2/2-sd x\) for \(s\in\{-1,+1\}\). Their uniform average is \(f(x)=\lambda x^2/2\), minimized uniquely at \(x=0\). Fix \(0<\beta<1\), \(\eta>0\), and arbitrary deterministic initial pair \((x_{-1},x_0)\). The stochastic heavy-ball recursion is
\[
x_{k+1}=(1+\beta-\eta\lambda)x_k-\beta x_{k-1}+\eta d\,s_{k+1}.
\]
Under independent sampling, the signs \(s_k\) are independent, unbiased Rademacher random variables. Under reshuffling, each epoch is an independent uniform permutation of the two signs, so \((s_{2j+1},s_{2j+2})=(\varepsilon_j,-\varepsilon_j)\) with independent unbiased \(\varepsilon_j\). Every expectation refers only to the sampling randomness, with initial conditions fixed.

All claimed stationary limits are limits as \(j\to\infty\) of the corresponding second moments, for stable stepsizes \(0<\eta\lambda<2(1+\beta)\). The limit of the mean in each phase is zero. No assertion is made about a particular finite iteration or about the full limiting probability density.

## Proof

Scale the iterate by \(d/\lambda\), which multiplies every squared error by \(U=(d/\lambda)^2\). It suffices to use the unit-offset recurrence. Let \(Y_k=(x_k,x_{k-1})^\mathsf T\),
\[
A=\begin{pmatrix}1+\beta-t&-\beta\\1&0\end{pmatrix},
\qquad g=\begin{pmatrix}t\\0\end{pmatrix}.
\]
The recurrence becomes \(Y_{k+1}=A Y_k+g s_{k+1}\). The characteristic polynomial of \(A\) is \(r^2-(1+\beta-t)r+\beta\); for \(0\le\beta<1\), its roots are strictly inside the unit disk precisely when \(0<t<2(1+\beta)\), by the second-order Schur criterion. Thus deterministic initial states decay geometrically and all phase covariance series converge. Since every innovation has mean zero, all limiting means vanish.

With independent replacement sampling, the invariant covariance \(S_{\rm I}\) of \(Y_k\) is the unique solution to
\[
S_{\rm I}=A S_{\rm I}A^\mathsf T+g g^\mathsf T.
\]
For reshuffling, the two-step update has the **independent epoch innovation**
\[
Y_{2j+2}=A^2Y_{2j}+(Ag-g)\varepsilon_j.
\]
Consequently the invariant covariance at epoch ends is the unique symmetric solution of
\[
S_{\rm E}=A^2S_{\rm E}(A^2)^\mathsf T+(Ag-g)(Ag-g)^\mathsf T.
\]
The covariance after the first step of the following epoch is
\[
S_{\rm O}=A S_{\rm E}A^\mathsf T+g g^\mathsf T.
\]
The variance at the epoch end is \((S_{\rm E})_{11}\); at the intermediate position it is \((S_{\rm O})_{11}=(S_{\rm E})_{22}\), the equality following from the shift-coordinate definition of \(Y\).

For a symmetric matrix \(S=\begin{psmallmatrix}a&z\\z&b\end{psmallmatrix}\), expanding either Lyapunov equation gives **three linear equations** in \((a,z,b)\). Solving these systems by exact rational elimination yields the three displayed variance expressions. Their consistency with both entire matrix equations, including the off-diagonal equations, is independently checked by the standalone symbolic verifier.

The sign classification is exact, rather than numerical. With \(D>0\), \(G>0\), and \(t>0\), direct algebra gives
\[
V_{\rm I}-V_{\rm E}
=U t(1+\beta-t)\left(\frac1D+\frac{t}{(1+\beta)G}\right)
\]
and
\[
V_{\rm I}-V_{\rm O}
=\frac{2 U t(1+\beta-t)
[(t-1-\beta)^2-\beta(1-\beta^2)]}{D(1+\beta)G}.
\]
The first difference has exactly the sign of \(t_0-t\), and the second has the sign of the product of \(t_0-t\) and \((t-t_-)(t-t_+)\). For \(0<\beta<1\), \(0<\sqrt{\beta(1-\beta^2)}<1+\beta\), placing all three thresholds strictly inside the stable interval. This proves the complete interval and equality classification.

For the rational witness \((\beta,t)=(1/2,1)\), substitution gives \(D=1\), \(G=1/2\), and the stated three distinct exact values. The strict comparison persists on open sets of parameters by continuity.

## Verification

Run \(\texttt{python verify_phase.py}\) with Python 3 and SymPy installed. The standalone script constructs the state-transition and innovation matrices from the definitions, independently solves both exact symbolic covariance systems, checks the resulting rational identities for both phase variances and difference factorizations, and checks the rational witness and additional admissible parameter values. Observed output:

```
VERIFY_OK symbolic=7 rational_and_boundary=111; exact stationary covariance identities and two-phase reversals
```

The exact analytical Schur and sign arguments establish the assertions for infinitely many iterations and all permitted parameters; numerical or finite checks alone would not.

## Relationship to prior work

Kühn and Rosenow (arXiv:2306.05300, especially Section 4, Appendix A and Appendix B.2) study heavy-ball SGD with epoch anti-correlation and derive variance relations **averaged over all update positions**. Appendix A explicitly defines its variance by a long time average and distinguishes that average from the variance at a fixed update step. Its framework motivates the comparison, but the phase-specific pair of stationary variances and all three sharp thresholds are not explicit consequences of its published time-averaged variance alone.

Qiu, Ma and Milzarek (arXiv:2404.18452) provide convergence analysis for random reshuffling with momentum under broader objective assumptions, with a different focus than constant-step stationary odd/even phase variance. Ying, Yuan, Vlaski and Sayed (arXiv:1803.07964) establish periodic steady-state reshuffling performance in constant-step stochastic optimization, but without the strictly positive heavy-ball memory parameter responsible for the extra reversal thresholds. De Sa (NeurIPS 2020) already provides other examples where reshuffling is not universally better; the present result does not claim priority for that general observation.

## Limitations

The results require exactly two equally weighted scalar losses of equal positive curvature and equal-and-opposite fixed gradient offsets; the momentum coefficient is strictly between zero and one, the step size is fixed, and every epoch is reshuffled independently. Comparisons are of stationary expected squared error at **specified within-epoch phases**, not transient trajectories or convergence rates. The proof does not establish comparable thresholds for heterogeneous curvature, arbitrary finite-sum datasets, nonlinear objectives, or algorithms with adaptive momentum. The time-averaged stationary formula and the mere existence of a reshuffling counterexample are already suggested by related literature; only the phase-resolved sharp classification is assessed here. Independent priority verification is not performed.

## References

1. Marcel Kühn and Bernd Rosenow, *Anti-Correlated Noise in Epoch-Based Stochastic Gradient Descent: Implications for Weight Variances in Flat Directions*, arXiv:2306.05300, initially public 2023-06-08, Sections 4, A, B.2. https://arxiv.org/abs/2306.05300
2. Junwen Qiu, Bohao Ma and Andre Milzarek, *Random Reshuffling with Momentum: Complexity Bounds and Last-iterate Convergence*, arXiv:2404.18452, initially public 2024-04-29. https://arxiv.org/abs/2404.18452
3. Bicheng Ying, Kun Yuan, Stefan Vlaski and Ali H. Sayed, *Stochastic Learning under Random Reshuffling with Constant Step-sizes*, arXiv:1803.07964, initially public 2018-03-21. https://arxiv.org/abs/1803.07964
4. Christopher M. De Sa, *Random Reshuffling is Not Always Better*, NeurIPS 2020. https://papers.neurips.cc/paper_files/paper/2020/hash/42299f06ee419aa5d9d07798b56779e2-Abstract.html
