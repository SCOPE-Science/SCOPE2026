# Exact fold and multistationarity phase diagram for a three-species mass-action example
## Finding
Consider
\[
X\to Y,\qquad Y\to Z,\qquad 2X\to2Z,\qquad Y+Z\to2X.
\]
For the positive reparameterization \(\theta_1,\theta_2,\theta_3>0\) used for this network, positive equilibria on the class \(x+y+z=K\) are in one-to-one correspondence with \(\alpha\in(0,1)\) satisfying
\[
K=K(\alpha):=\frac{\theta_1}{2}(1-\alpha)+\frac{\theta_2}{4}\alpha(1-\alpha)+\theta_3\frac{2-\alpha}{\alpha}.
\]
When \(\theta_2>2\theta_1\), define
\[
T:=\frac{(\theta_2-2\theta_1)^3}{216\theta_2^2}.
\]
If \(\theta_2\le2\theta_1\), or if \(\theta_2>2\theta_1\) and \(\theta_3>T\), then \(K(\alpha)\) is strictly decreasing from \(+\infty\) to \(\theta_3\), so every \(K>\theta_3\) has exactly one positive equilibrium and every \(K\le\theta_3\) has none.

If \(\theta_2>2\theta_1\) and \(\theta_3=T\), the curve is still one-to-one but has the unique cusp
\[
\alpha_*=\frac{\theta_2-2\theta_1}{3\theta_2},
\qquad
K_*=\frac{8\theta_1^3+60\theta_1^2\theta_2+42\theta_1\theta_2^2+17\theta_2^3}{216\theta_2^2}.
\]

If \(\theta_2>2\theta_1\) and \(0<\theta_3<T\), the equation
\[
\theta_3=\frac{\alpha^2}{8}\bigl((1-2\alpha)\theta_2-2\theta_1\bigr)
\]
has exactly two roots \(\alpha_-<\alpha_+\). Set \(K_-=K(\alpha_-)\) and \(K_+=K(\alpha_+)\). Then exactly three positive equilibria occur for \(K_-<K<K_+\); exactly two distinct positive equilibria occur at \(K=K_-\) and \(K=K_+\), one of them double; and exactly one positive equilibrium occurs for every other \(K>\theta_3\). The two endpoint degeneracies are transverse nondegenerate folds.

## Assumptions and scope
The parameters \(\theta_1,\theta_2,\theta_3\) and the conserved total \(K\) are positive. The cited primary sources establish the smooth one-to-one reduction from positive equilibria of this network to roots \(\alpha\in(0,1)\), and establish that the fold/cusp tests may be performed on the alternative scalar equation. The result is global in \(K\) for fixed positive \(\theta\). It does not classify equilibrium stability away from the local fold/cusp type or global trajectories.

## Proof
The scalar equation is
\[
f(\alpha;\theta_1,\theta_2,\theta_3,K)
=
2\theta_1\alpha(1-\alpha)
+\theta_2\alpha^2(1-\alpha)
+4\theta_3(2-\alpha)-4K\alpha.
\]
Solving \(f=0\) for \(K\) gives the displayed \(K(\alpha)\). Moreover,
\[
\lim_{\alpha\downarrow0}K(\alpha)=+\infty,
\qquad
\lim_{\alpha\uparrow1}K(\alpha)=\theta_3,
\]
and \(K(\alpha)>\theta_3\) for every \(\alpha\in(0,1)\).

Exact differentiation gives
\[
K'(\alpha)=\frac{2}{\alpha^2}\bigl(g(\alpha)-\theta_3\bigr),
\qquad
g(\alpha)=\frac{\alpha^2}{8}\bigl((1-2\alpha)\theta_2-2\theta_1\bigr).
\]
If \(\theta_2\le2\theta_1\), then \(g(\alpha)<0\), hence \(K'(\alpha)<0\).

Assume \(\theta_2>2\theta_1\), and put
\[
c=1-\frac{2\theta_1}{\theta_2}>0.
\]
Then
\[
g(\alpha)=\frac{\theta_2}{8}\alpha^2(c-2\alpha),
\qquad
g'(\alpha)=\frac{\theta_2}{4}\alpha(c-3\alpha).
\]
Thus \(g\) is positive precisely for \(0<\alpha<c/2\), has a unique positive maximum at \(\alpha_*=c/3\), and
\[
g(\alpha_*)=\frac{\theta_2c^3}{216}
=\frac{(\theta_2-2\theta_1)^3}{216\theta_2^2}=T.
\]
Therefore \(K\) has zero, one, or two critical points according as \(\theta_3>T\), \(\theta_3=T\), or \(0<\theta_3<T\). In the two-critical-point case \(K'\) has signs negative, positive, negative, so \(K_-\) is a strict local minimum and \(K_+\) a strict local maximum. The endpoint limits then give the stated global equilibrium counts.

At a critical point, \(f=f_\alpha=0\). Solving these equations gives
\[
\theta_3=\frac{\alpha^2}{8}\bigl((1-2\alpha)\theta_2-2\theta_1\bigr)
\]
and
\[
K=\frac{\theta_1}{4}(\alpha^2-4\alpha+2)
+\frac{\theta_2}{8}\alpha(2\alpha^2-7\alpha+4).
\]
Along this locus,
\[
f_{\alpha\alpha}=-2(3\alpha\theta_2+2\theta_1-\theta_2).
\]
It vanishes exactly at \(\alpha_*\), while
\[
f_{\alpha\alpha\alpha}=-6\theta_2\ne0.
\]
Substitution yields the formulas for \(T\) and \(K_*\). The cusp unfolding matrix in parameters \((K,\theta_3)\),
\[
\begin{pmatrix}
f_K & f_{\theta_3}\\
f_{\alpha K} & f_{\alpha\theta_3}
\end{pmatrix}
=
\begin{pmatrix}
-4\alpha & 4(2-\alpha)\\
-4 & -4
\end{pmatrix},
\]
has determinant \(32\). At either ordinary critical point \(\alpha_\pm\ne\alpha_*\), one has \(f_{\alpha\alpha}\ne0\) and \(f_K=-4\alpha_\pm\ne0\), so both are transverse nondegenerate folds. The cited dual-equation theorem transfers these classifications to the original mass-action system.

## Verification
All identities above were checked by exact symbolic simplification. The global root count uses only the derivative factorization, the unique maximum of \(g\), continuity, and the two endpoint limits. No finite sampling or numerical root census is used as an infinite proof.

## Relationship to prior work
Banaji and Feliu introduced this exact network and scalar cubic, proved the positive-equilibrium reduction, showed that three positive equilibria can occur, and stated that Sturm theory can produce a semialgebraic parameter description, while explicitly omitting the resulting lengthy expressions. Banaji's later dual-equation paper develops the fold/cusp transfer theorem and gives an explicit cusp parametrization for the same example. The result here instead gives the complete fixed-\(\theta\) phase diagram as the conserved total \(K\) varies: the sharp threshold \(T\), the one-versus-three-equilibrium regimes, the exact two-fold window, and the cusp where the folds coalesce. The 2024 Banaji--Boros--Hofbauer classification concerns different small-network classes and does not cover this three-species rank-two example.

## Limitations
The result is specific to this network and parameterization. It does not determine stability away from the local bifurcation type or global dynamics. An equivalent derivation under a different parameterization may exist in unindexed literature; that is the main residual originality risk.

## References
1. M. Banaji, *On the computation of fold and cusp bifurcations in mass action networks via dual equations*, arXiv:2609.07265v1 (2026).
2. M. Banaji and E. Feliu, *Positive equilibria in mass action networks: geometry and bounds*, arXiv:2409.06877v3; Journal of Mathematical Biology 93, 37 (2026), DOI 10.1007/s00285-026-02429-8.
3. M. Banaji, B. Boros, and J. Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity*, Nonlinear Dynamics 112 (2024), DOI 10.1007/s11071-024-10068-1.
