# Sharp one-step Pareto-capture threshold and full-set overshoot for MO-Adagrad on symmetric quadratics
## Finding
Consider MO-Adagrad on the two scalar convex objectives
\[
f_-(x)=\frac{\lambda}{2}(x+c)^2,
\qquad
f_+(x)=\frac{\lambda}{2}(x-c)^2,
\]
with \(\lambda>0\), \(c>0\), and startup parameter \(\varsigma\in(0,1)\). The exact Pareto-critical set is \([-c,c]\).

Put
\[
r=\frac{\varsigma}{\lambda^2}.
\]
For a right-side start \(x_0=c+y\) with \(y>0\), the first MO-Adagrad step is
\[
x_1=c+y\left(1-\frac{1}{\sqrt{r+y^2}}\right).
\]
Thus the step crosses the near endpoint \(c\) exactly when \(r+y^2<1\). In this crossing regime define the depth
\[
\delta_r(y)=c-x_1
=y\left(\frac{1}{\sqrt{r+y^2}}-1\right).
\]
For \(0<r<1\), its exact maximum is
\[
\max_{0<y<\sqrt{1-r}}\delta_r(y)
=(1-r^{1/3})^{3/2},
\]
attained uniquely at
\[
y_*=r^{1/3}\sqrt{1-r^{1/3}}.
\]
Consequently, every first-step crossing from either side lands somewhere in the entire Pareto interval if and only if
\[
2c\ge (1-r^{1/3})^{3/2}.
\]
When the reverse strict inequality holds, the start \(x_0=c+y_*\) jumps in one step from the right of \(c\) to the left of \(-c\), skipping the whole Pareto interval. The left-side statement is symmetric.

There is also an exact noncrossing alternative. If \(r+y^2=1\), the nearest endpoint is reached in one step. If \(r+y^2>1\), all subsequent iterates remain on the starting side and converge monotonically to the nearest endpoint. Hence for \(r\ge1\), every outside start converges to the nearest endpoint without crossing it.

## Assumptions and scope
MO-Adagrad initializes \(w_{-1}=\sqrt{\varsigma}\), computes the minimum-Euclidean-norm vector \(g_k^s\) in the convex hull of the objective gradients, updates
\[
w_k=\sqrt{w_{k-1}^2+\|g_k^s\|_2^2},
\]
and takes
\[
x_{k+1}=x_k-\frac{g_k^s}{w_k}.
\]
The source fixes \(\varsigma\in(0,1)\). The finding uses its deterministic, exact-gradient algorithm exactly as stated, with no line search or dominance acceptance test.

For the symmetric quadratic pair, the two gradients are
\[
\lambda(x+c),\qquad \lambda(x-c).
\]
Their convex hull contains zero exactly for \(x\in[-c,c]\). Therefore \(g^s(x)=0\) on that interval. Outside it, both gradients have the same sign and the smaller magnitude is attained at the nearer endpoint, so
\[
g^s(x)=
\begin{cases}
\lambda(x-c),&x>c,\\
\lambda(x+c),&x<-c.
\end{cases}
\]
This also proves that \([-c,c]\) is exactly the Pareto-critical set for this family.

## Proof
Take \(x_0=c+y\), \(y>0\). Since \(g_0^s=\lambda y\),
\[
w_0=\sqrt{\varsigma+\lambda^2y^2}
=\lambda\sqrt{r+y^2},
\]
and therefore
\[
x_1=c+y-\frac{\lambda y}{\lambda\sqrt{r+y^2}}
=c+y\left(1-\frac{1}{\sqrt{r+y^2}}\right).
\]
The first step crosses \(c\) precisely when \(r+y^2<1\). In that regime,
\[
\delta_r(y)=y\left((r+y^2)^{-1/2}-1\right)>0.
\]
Differentiation gives
\[
\delta_r'(y)=\frac{r}{(r+y^2)^{3/2}}-1.
\]
For \(0<r<1\), this derivative is positive near zero, negative near \(\sqrt{1-r}\), and has the unique zero determined by
\[
r+y^2=r^{2/3}.
\]
Thus
\[
y_*=r^{1/3}\sqrt{1-r^{1/3}},
\]
and substitution yields
\[
\delta_r(y_*)=(1-r^{1/3})^{3/2}.
\]
A right-side crossing lands in \([-c,c]\) exactly when \(\delta_r(y)\le2c\). Taking the maximum over the entire crossing basin gives the stated if-and-only-if width threshold. If the threshold fails strictly, \(y_*\) gives \(x_1=c-\delta_r(y_*)<-c\), so the first step skips the full Pareto interval. If a crossing lands inside \([-c,c]\), the next common descent vector is zero, so the method stays there exactly.

For the noncrossing regime write \(y_k=x_k-c>0\). As long as the iterates remain to the right,
\[
w_k^2=\varsigma+\lambda^2\sum_{j=0}^k y_j^2,
\qquad
y_{k+1}=y_k\left(1-\frac{\lambda}{w_k}\right).
\]
If \(w_0=\lambda\), then \(y_1=0\). If \(w_0>\lambda\), monotonicity of \(w_k\) gives \(0<1-\lambda/w_k<1\), so \(y_k\) stays positive and decreases. Moreover
\[
w_k^2\le \varsigma+\lambda^2(k+1)y_0^2,
\]
so \(\sum_k\lambda/w_k\) diverges. Using \(\log(1-t)\le-t\) for \(0<t<1\),
\[
\log\frac{y_{k+1}}{y_k}
\le-\frac{\lambda}{w_k},
\]
and hence \(y_k\to0\). Thus \(x_k\downarrow c\). Reflection through the origin proves the left-side statements.

## Verification
The bundled script `artifacts/verify_pareto_capture.py` replays the exact MO-Adagrad recurrence for the symmetric quadratic family, checks the analytic maximizer of \(\delta_r\) over a dense collection of parameter values, tests both sides of the sharp width threshold, and verifies monotone endpoint convergence in the noncrossing regime.

These finite computations are consistency checks. The if-and-only-if threshold and convergence statements are proved analytically above; no finite sampling is used as an infinite proof.

## Relationship to prior work
De Santis, Eichfelder, and Porcelli define MO-Adagrad using the minimum-norm point in the convex hull of the gradients, cumulative squared common-gradient norm, and unconditional line-search-free steps. Their analysis gives a global rate for the common-descent criticality measure and reports convergence to Pareto-critical points. It does not state the symmetric-quadratic phase diagram, the exact capture-width threshold, or a full-Pareto-set one-step overshoot example.

Gonçalves, Grapiglia, and Melo independently introduced a closely related adaptive line-search-free multiobjective gradient method. Its conservative variant uses the same cumulative-norm mechanism up to its explicit master stepsize and initialization parameters. Its paper develops complexity bounds and does not state the exact two-quadratic capture/overshoot threshold derived here.

Classical multiobjective steepest-descent literature establishes convergence to Pareto-critical or weakly Pareto-optimal points under line-search or related safeguards. Those results do not imply this unconditional adaptive-step selection law, whose threshold depends jointly on the startup accumulator and the width of a nontrivial Pareto set.

## Limitations
The exact formula is for a scalar, deterministic, equal-curvature, symmetric two-objective quadratic family. It does not classify unequal curvatures, higher-dimensional Pareto manifolds, stochastic gradients, or the dynamics after a full-set overshoot. The result concerns the actual MO-Adagrad iterate, not a line-search variant.

The originality assessment is based on direct inspection of the two 2026 adaptive multiobjective papers, the foundational steepest-descent context, current published-result searches, and the available prior research ledger. An equivalent calculation under different notation remains a residual literature risk.

## References
1. M. De Santis, G. Eichfelder, and M. Porcelli, *Objective-Function Free Multi-Objective Optimization: Rate of Convergence and Performance of an Adagrad-like algorithm*, arXiv:2602.05893v1, 2026; later published in *Computational Optimization and Applications* 95 (2026).
2. M. L. N. Gonçalves, G. N. Grapiglia, and J. G. Melo, *An adaptive line-search-free multiobjective gradient method and its iteration-complexity analysis*, Optimization Online, 2026-01-30.
3. J. Fliege and B. F. Svaiter, *Steepest descent methods for multicriteria optimization*, *Mathematical Methods of Operations Research* 51 (2000), 479--494.
4. G. Cocchi, G. Liuzzi, S. Lucidi, and M. Sciandrone, *On the convergence of steepest descent methods for multiobjective optimization*, *Computational Optimization and Applications* 77 (2020), 1--27.
