# Exact nullspace-selection risk and a sampling transition for two-column randomized descent

## Finding

A consistent but underdetermined linear system can be solved exactly by randomized block coordinate descent (RBCD) while retaining a nonzero, sampling-dependent error relative to its minimum-Euclidean-norm solution. For the two-column rank-one system below, the entire squared selection risk and the unique optimal iid coordinate-selection probability have exact formulas. The optimum undergoes an interior-to-boundary transition at a sharp stepsize. In the equal-column, uniformly sampled case, the limiting solution is uniformly distributed along the feasible segment although every iterate is deterministically bounded; thus pathwise uniform boundedness by itself does **not** ensure minimum-norm selection.

Write \(\alpha=a^2\), \(\beta=b^2\), \(s=\alpha+\beta\), and for \(0\le p\le1\) put
\[
d(p)=p\alpha+(1-p)\beta,\qquad e(p)=p\alpha^2+(1-p)\beta^2.
\]
For the normalized nullspace coordinate
\[
T=\frac{b x_{\infty,1}-a x_{\infty,2}}{ab y},
\]
the exact moments are
\[
\mathbb ET=\frac{2p-1}{d(p)},\qquad
\operatorname{Var}(T)=\frac{\gamma p(1-p)s^2}{d(p)^2\bigl(2d(p)-\gamma e(p)\bigr)}.
\]
In particular, with \(x^\dagger=y(a,b)/s\), the exact limiting squared selection risk is
\[
\mathbb E\|x_\infty-x^\dagger\|_2^2
=\frac{\alpha\beta y^2}{s}\,q(p),\qquad
q(p)=\frac{(2p-1)^2}{d(p)^2}
+\frac{\gamma p(1-p)s^2}{d(p)^2\bigl(2d(p)-\gamma e(p)\bigr)}.
\]
For \(a>b>0\), define the critical stepsize
\[
\gamma_c=\frac{4}{3\alpha+\beta}.
\]
Among all fixed iid probabilities \(p\in[0,1]\), the **unique** risk minimizer is interior when \(0<\gamma<\gamma_c\), and is exactly \(p=1\) when \(\gamma_c\le\gamma\le 2/s\). In the interior regime, \(p_\star\) is the unique root in \((0,1)\) of \(C_2p^2+C_1p+C_0=0\), where
\[
\begin{aligned}
C_2&=(\alpha-\beta)(\gamma s-2)(3\gamma s-8),\\
C_1&=-2(\alpha-3\beta)(\gamma\beta-2)(\gamma s-2),\\
C_0&=-\beta(\gamma\beta-2)\bigl(\gamma(\alpha+3\beta)-4\bigr).
\end{aligned}
\]
The optimum satisfies \(p_\star\to\tfrac12\) as \(\gamma\downarrow0\). The boundary choice \(p=1\) means always selecting the larger column; it is allowed as a degenerate iid sampling law.

For the concrete nondegenerate system \(a=2\), \(b=1\), \(\gamma=1/5\), \(y=1\), the risk-minimizing choice is
\[
p_\star=\frac{3+2\sqrt{51}}{25}=0.6913142742\ldots,
\]
while the uniform sampler uses \(p=1/2\). Here \(q(p_\star)=-89/6+25\sqrt{51}/12\), whereas \(q(1/2)=2/33\); the minimum selection risk is about \(26.34\%\) below uniform sampling. This is **not** a claim about minimizing residual convergence time.

## Assumptions and scope

Let \(a,b>0\), \(y\in\mathbb R\setminus\{0\}\), and consider the consistent rank-one system \(a x_1+b x_2=y\), initialized at \(x_0=(0,0)\). Each iteration independently chooses coordinate \(1\) with probability \(p\) and coordinate \(2\) with probability \(1-p\), then applies the coordinate-gradient update
\[
x_{k+1}=x_k+\gamma\,a_{I_k}\,e_{I_k}\bigl(y-a x_{k,1}-b x_{k,2}\bigr),
\qquad (a_1,a_2)=(a,b).
\]
Assume \(0<\gamma\le2/(a^2+b^2)\), the source's nonexpansive stepsize range. This classification covers every \(p\in[0,1]\). The sharp optimality theorem assumes \(a>b\); interchanging coordinate labels handles \(b>a\). The equal-column case is treated separately as an exact counterexample. All probability statements concern independent draws and exact arithmetic.

## Proof

**1. Convergence and a nullspace series.** Set \(r_k=y-a x_{k,1}-b x_{k,2}\). A selected coordinate \(i\) gives \(r_{k+1}=(1-\gamma a_i^2)r_k\). Set \(c_1=1-\gamma\alpha\) and \(c_2=1-\gamma\beta\). As both squared column norms are strictly less than \(s\), the stated stepsize ensures \(r=\max\{|c_1|,|c_2|\}<1\). Therefore \(|r_k|\le |y|r^k\), and the coordinate increments are absolutely summable along every possible sample path. The limit \(x_\infty\) exists pathwise, satisfies \(a x_{\infty,1}+b x_{\infty,2}=y\), and obeys a deterministic finite norm bound.

Define \(\sigma_1=1\), \(\sigma_2=-1\). Multiplying the coordinate increment by the nullspace functional \((b,-a)\) yields
\[
T=\gamma\sum_{k=0}^{\infty}\sigma_{I_k}\prod_{j<k}c_{I_j}.
\]
The tail after the first draw is independent and distributed as the original series, so \(T\overset d=\gamma\sigma_I+c_I T'\), with \(T'\) independent of \(I\). This identity has bounded solutions because \(r<1\).

**2. Moments and squared distance.** Taking expectations in the fixed-point identity gives
\[
\mathbb ET=\frac{\gamma(2p-1)}{1-[pc_1+(1-p)c_2]}=\frac{2p-1}{d(p)}.
\]
For the centered variance, conditional variance of the affine first-step term yields
\[
\operatorname{Var}(T)=\mathbb E(c_I^2)\operatorname{Var}(T)
+\gamma^2\operatorname{Var}(\sigma_I-a_I^2\mathbb ET).
\]
The second variance is \(p(1-p)s^2/d(p)^2\), since the two possible values differ by \(s/d(p)\). Moreover,
\[
1-\mathbb E(c_I^2)=\gamma\bigl(2d(p)-\gamma e(p)\bigr)>0.
\]
These equations give the asserted variance. Since \(x_\infty-x^\dagger\) is orthogonal to \((a,b)\) and parallel to \((b,-a)\),
\[
\|x_\infty-x^\dagger\|_2^2=\frac{(b x_{\infty,1}-a x_{\infty,2})^2}{s}=
\frac{\alpha\beta y^2}{s}T^2.
\]
Combining its squared mean and variance proves the exact risk formula, including endpoints.

**3. Unique optimum for unequal column norms.** Now \(\alpha>\beta>0\). Direct differentiation and cancellation give
\[
q'(p)=\frac{s\,[C_2p^2+C_1p+C_0]}{d(p)^2[\gamma e(p)-2d(p)]^2}.
\]
For \(0<\gamma<2/s\), the coefficients satisfy \(C_2>0\) and \(C_0<0\): both factors \(\gamma s-2\) and \(3\gamma s-8\) are negative, while \(\gamma\beta-2\) and \(\gamma(\alpha+3\beta)-4\) are also negative. Thus the numerator quadratic has exactly one positive root and one negative root. The derivative starts negative and changes sign exactly once on the positive half-line. At the right endpoint,
\[
q'(1)=\frac{s[\gamma(3\alpha+\beta)-4]}{\alpha^3(\gamma\alpha-2)}.
\]
The denominator is strictly negative, so \(q'(1)>0\) precisely for \(\gamma<\gamma_c\). Hence the unique positive stationary point lies inside \((0,1)\) exactly below \(\gamma_c\); at or above the boundary the risk decreases throughout \([0,1)\). At \(\gamma=2/s\) cancellation gives
\[
q(p)=\frac{\alpha-(\alpha-\beta)p}{\alpha\beta[\beta+(\alpha-\beta)p]},
\]
which is strictly decreasing. The limiting coefficients of the interior optimality polynomial as \(\gamma\downarrow0\) yield \(p_\star\to1/2\). This proves the complete minimizer classification and its uniqueness.

**4. Exact sampling benchmark.** Substituting \(\alpha=4\), \(\beta=1\), and \(\gamma=1/5\) yields
\[
q(p)=\frac{20p^2-23p+9}{3(3p+1)(5p+3)}.
\]
Differentiation gives the unique minimizing probability and values stated in the finding. The relative reduction is exactly \(1-q(p_\star)/q(1/2)\); no simulation enters this claim.

**5. Deterministically bounded, non-minimum-norm limit.** Set \(a=b=y=1\), \(\gamma=1/2\), and \(p=1/2\). Each residual is \(r_k=2^{-k}\), independent of the sampled coordinates. If \(B_k\) is the indicator that the first coordinate was selected at step \(k\), then
\[
x_{\infty,1}=\sum_{k=0}^{\infty}B_k2^{-(k+1)}=:U,
\qquad x_{\infty,2}=1-U.
\]
The independent fair binary digits give \(U\sim\operatorname{Uniform}[0,1]\). For every sample path and every \(k\), the coordinates are nonnegative and satisfy \(x_{k,1}+x_{k,2}=1-2^{-k}\), whence \(\|x_k\|_2\le1\). But \(x^\dagger=(1/2,1/2)\), and \(\mathbb P\{x_\infty=x^\dagger\}=0\). The exact squared selection risk is \(\mathbb E[2(U-1/2)^2]=1/6\). Thus even a deterministic uniform pathwise bound does not imply minimum-norm selection. The issue is not a lack of convergence: all trajectories converge geometrically in residual and absolutely in state.

## Verification

Execute `python verify.py` with Python 3 and SymPy installed. The standalone checker verifies the moment equations by independent symbolic reconstruction, the exact rational form and optimum for the \((2,1,1/5)\) example, the limiting risk in the fair-digit example using complete finite-prefix enumeration, and direct finite-step residual/series identities on deterministic seeded trajectories. All infinite-horizon convergence, uniform-distribution and unique-global-minimizer statements above follow analytically from the proof, not from finite tests.

## Relationship to prior work

Jin and Liu's 2024 RBCD paper supplies the underlying coordinate-gradient algorithm and proves weak convergence to a possibly random solution for general ill-posed systems. Its Remark 2.5 explicitly concludes that a uniform pathwise bound implies almost-sure minimum-norm selection. The bounded fair-digit example above violates that conclusion without violating its stated conditions. Its conditional-expectation argument uses a terminal random vector depending on the same future coordinate draws; that terminal quantity is not generally measurable with respect to the past filtration. This analysis does **not** assert that every later theorem of the source paper fails; extra hypotheses must be assessed separately.

Classical arbitrary-sampling coordinate descent and stochastic linear-system solvers analyze objective/residual rates and sampling rules; the present optimizer targets instead the Euclidean distance of the **random terminal solution** to the minimum-norm solution when the forward matrix is rank deficient. The binary-expansion uniform law is classical; the new object is its role in the bounded RBCD solution-selection claim and the complete unequal-column risk/optimizer law. Published results addressing full-column-rank least squares do not cover the rank-one underdetermined setting merely by sharing the words coordinate descent.

## Limitations

The sharp minimizer applies to two scalar columns of a rank-one consistent matrix with fixed stepsize and iid stationary sampling; it is not a universal optimal probability law for higher-rank systems, changing stepsizes, arbitrary initial states or noise. It measures terminal minimum-norm selection error, not residual convergence, finite-iteration loss, or compute time. The interior probability may differ from probabilities optimized for those objectives. The bounds and limiting laws are exact-arithmetic results; finite-precision effects were not analyzed. The original source's published minimum-norm assertion is challenged only in the scope actually refuted by the explicit example. A prior equivalent calculation under affine iterated-function systems or implicit-bias terminology remains a literature risk.

## References

1. Q. Jin and D. Liu, *Randomized block coordinate descent method for linear ill-posed problems*, arXiv:2405.13340v1, first posted 2024-05-22; especially Algorithm 1, Theorem 2.4 and Remark 2.5. https://arxiv.org/html/2405.13340v1
2. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling I: Algorithms and Complexity*, arXiv:1412.8060. https://arxiv.org/abs/1412.8060
3. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690; arXiv:1506.03296. https://arxiv.org/abs/1506.03296
4. D. Xie and Q. Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685v1, introduction and full-column-rank setting. https://arxiv.org/html/2610.04685v1
