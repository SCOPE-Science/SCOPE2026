# A sharp coupling-reversal frontier for stochastic extragradient on a bilinear game

## Finding

Consider stochastic extragradient for the scalar zero-sum bilinear game \(\min_x\max_y \mathbb E[S]xy\), where \(S\) takes two positive values. Two oracle calls within each iteration need not be independent or identical, even if each individually has the prescribed unbiased distribution. The optimal **within-iteration coupling reverses at an exact step-size threshold**.

Let \(0<a<b\), \(0<p<1\), \(d=\min(p,1-p)\), and let the oracle strengths in the predictor and corrector be \(X\) and \(Y\), each taking value \(b\) with probability \(p\), and value \(a\) otherwise. Every joint law with these marginals has a unique parameter \(t\in[0,d]\):

\[
\begin{aligned}
\mathbb P(X=a,Y=a)&=1-p-t,\\
\mathbb P(X=a,Y=b)&=t,\\
\mathbb P(X=b,Y=a)&=t,\\
\mathbb P(X=b,Y=b)&=p-t.
\end{aligned}
\]

Define \(u=\eta^2>0\), \(M_2=(1-p)a^2+pb^2\), and \(M_4=(1-p)a^4+pb^4\). For every nonzero deterministic initial vector \(z_0\in\mathbb R^2\), the **exact** mean-square factor is

\[
\boxed{\rho(u,t)=1-uM_2+u^2M_4+tu(b-a)^2\bigl[2-u(a+b)^2\bigr]}
\]

and \(\mathbb E\|z_n\|_2^2=\rho(u,t)^n\|z_0\|_2^2\) for every integer \(n\geq0\).

For every fixed \(u>0\), the coupling that minimizes the mean-square factor across **all** joint laws with the given marginals is uniquely \(t=0\) (identical samples) when \(u<2/(a+b)^2\), uniquely \(t=d\) (maximal discordance, or antithetic coupling) when \(u>2/(a+b)^2\), and every coupling is tied at equality.

For a fixed \(t\), geometric mean-square convergence occurs if and only if \(M_2>2t(b-a)^2\) and

\[
0<u<u_*(t):=\frac{M_2-2t(b-a)^2}{M_4-t(b^2-a^2)^2}.
\]

If the numerator is nonpositive, no positive step yields mean-square convergence. At the positive boundary \(u=u_*(t)\), the mean-square error is constant for every iteration; above it the expected squared error grows exponentially. Maximal discordance increases the largest stable squared step compared with identical sampling **if and only if**

\[
\boxed{(a+b)^2M_2>2M_4.}
\]

For example, taking \(a=1\), \(b=2\), \(p=1/2\), \(u=1/3\), the factors for \(t=0\), independent stages \(t=1/4\), and fully anticorrelated stages \(t=1/2\) are exactly \(10/9\), \(37/36\), and \(17/18\). The first two diverge in mean square and the third converges geometrically. Their exact squared-step stability ceilings are respectively \(5/17\), \(8/25\), and \(3/8\).

## Assumptions and scope

The iterates are unconstrained real vectors \(z=(x,y)^\top\), and the stochastic operator is \(F_s(z)=sJz\), with \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\). Since \(\mathbb E[S]>0\), the unique saddle point is \(z_*=0\). There is no additive noise; the operator noise vanishes at the saddle point. Each iteration makes exactly two oracle evaluations with a common positive step \(\eta\). The joint pair \((X,Y)\) may be dependent within an iteration, but pairs are independently resampled across iterations with the **same** joint law. Fixed one-call marginals are essential for the comparison; runtime and coupling-construction costs are not included in the metric.

## Proof

The predictor and corrector are \(\widetilde z=z-\eta XJz\) and \(z^+=z-\eta YJ\widetilde z\). As \(J^2=-I\),

\[
z^+=\bigl[(1-\eta^2XY)I-\eta YJ\bigr]z.
\]

Because \(J^\top=-J\), the transpose-times-itself of the bracketed matrix equals \(\bigl[(1-\eta^2XY)^2+\eta^2Y^2\bigr]I\). Thus the squared norm is multiplied exactly by \(R(X,Y)=(1-uXY)^2+uY^2\), independently of the input direction. Conditioning on the past, outer-iteration independence gives \(\mathbb E[\|z_{n+1}\|_2^2\mid z_n]=\rho(u,t)\|z_n\|_2^2\), proving the stated power identity by induction.

Both marginals force the off-diagonal joint masses to equal \(t\), and nonnegativity forces \(0\leq t\leq d\). Directly from the displayed probability table,

\[
\mathbb E[XY]=M_2-t(b-a)^2,\qquad
\mathbb E[X^2Y^2]=M_4-t(b^2-a^2)^2,\qquad
\mathbb E[Y^2]=M_2.
\]

Substituting into \(\rho=1-2u\mathbb E[XY]+u\mathbb E[Y^2]+u^2\mathbb E[X^2Y^2]\) yields the claimed closed form. Its derivative with respect to \(t\) is \(u(b-a)^2[2-u(a+b)^2]\). Since \(u>0\) and \(b>a\), the derivative is strictly positive or negative on the two sides of \(u=2/(a+b)^2\), and is zero exactly at the boundary. This establishes the **global** coupling optimum over the entire set of feasible joint distributions, not merely over three named sampling schemes.

For stability, \(\rho(u,t)-1=u\{-M_2+2t(b-a)^2+u[M_4-t(b^2-a^2)^2]\}\). The final coefficient is \(\mathbb E[X^2Y^2]>0\), so the sign is negative precisely under the two stated strict inequalities. This proves the convergence, neutral and divergence cases without an unproved spectral approximation.

Finally, wherever the stability ceiling is positive, differentiation gives

\[
\frac{d}{dt}u_*(t)=
\frac{(b-a)^2\bigl[(a+b)^2M_2-2M_4\bigr]}
{\bigl[M_4-t(b^2-a^2)^2\bigr]^2}.
\]

Consequently its direction is constant throughout the feasible coupling interval. If the numerator of the ceiling becomes nonpositive, the usable positive-step ceiling is zero. This completes the exact criterion for which extremal coupling maximizes the admissible stable step. Substitution of the rational example into the probability-table formula yields \(10/9,37/36,17/18\) and the corresponding three ceilings.

## Verification

The standalone `verify.py` uses only the Python standard library and completes **2,467 exact-rational checks**, including probability-table normalization, the moment identity at many positive parameters, the globally optimal endpoint for the two step-size regimes, the strict mean-square convergence classification, derivative-sign comparisons, the crossover equality, and the explicit rational witness. Run `python3 verify.py` alongside this file. The proof above, not the finite tests, establishes the all-parameter claims.

## Relationship to prior work

Chavdarova et al. (2019) show how stochastic noise can destabilize extragradient on a bilinear game; Mishchenko et al. (2020) advocate reusing the same stochastic sample. Li et al. (2021, original preprint) analyze same-sample extragradient on bilinear games, especially with averaging and restarting. Gorbunov et al. (2021, original preprint) analyze same-sample and independent-sample methods and arbitrary marginal sampling. Yoon and Loizou (2026) study those two conventional variants in monotone variational inequalities. The specific contribution here is an **exact if-and-only-if optimal joint coupling frontier with fixed stage marginals**, including an antithetic regime and strict reverse-stability example; it is not a claim that antithetic variates, stochastic extragradient, or bilinear games themselves are new. The papers examined do not state the within-iteration two-point joint-coupling optimization or imply its closed-form critical boundary via their published convergence bounds.

## Limitations

The theorem concerns a two-dimensional, one-mode, zero-sum bilinear game; two-point positive multiplicative oracle strengths; identical marginal laws; iid pairs across iterations; and fixed equal predictor/corrector step sizes. It establishes exact mean-square behavior, not almost-sure rates, the behavior of averaged iterates, general nonlinear convergence, higher-dimensional games, or an implementation-level speedup. An equivalent specialized derivation outside the inspected literature remains a priority risk.

## References

1. Chavdarova, Gidel, Fleuret, and Lacoste-Julien, *Reducing Noise in GAN Training with Variance Reduced Extragradient*, first public arXiv preprint 2019-04-18. https://arxiv.org/abs/1904.08598
2. Mishchenko, Kovalev, Shulgin, Richtárik, and Malitsky, *Revisiting Stochastic Extragradient*, 2020. https://proceedings.mlr.press/v108/mishchenko20a/mishchenko20a.pdf
3. Li, Yu, Loizou, Gidel, Ma, Le Roux, and Jordan, *On the Convergence of Stochastic Extragradient for Bilinear Games using Restarted Iteration Averaging*, first public 2021-06-30. https://arxiv.org/abs/2107.00464
4. Gorbunov, Berard, Gidel, and Loizou, *Stochastic Extragradient: General Analysis and Improved Rates*, first public 2021-11-16. https://proceedings.mlr.press/v151/gorbunov22b/gorbunov22b.pdf
5. Yoon and Loizou, *On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities*, 2026. https://arxiv.org/pdf/2608.06182
