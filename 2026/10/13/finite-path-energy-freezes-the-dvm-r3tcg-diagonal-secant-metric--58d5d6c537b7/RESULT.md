# Finite path energy freezes the DVM-R3TCG diagonal secant metric
## Finding

The diagonal variable-metric module of Zhang--Gao--He updates each coordinate by
\[
\widetilde u_{k+1,i}
=
\frac{s_{k,i}y_{k,i}+\omega u_{k,i}}
{s_{k,i}^2+\omega},
\qquad
u_{k+1,i}
=
\Pi_{[m_L,m_U]}(\widetilde u_{k+1,i}),
\]
with
\[
\omega>0,
\qquad
0<m_L\le1\le m_U,
\qquad
u_{0,i}=1.
\]

Suppose one coordinate receives perfectly consistent constant-curvature secant data
\[
y_{k,i}=q s_{k,i},
\qquad
q\in[m_L,m_U].
\]
Then the projection is inactive for every iteration and
\[
 u_{N,i}-q
 =
 (1-q)
 \prod_{k=0}^{N-1}
 \frac{\omega}{s_{k,i}^2+\omega}.
\]

If \(q\ne1\), exact asymptotic curvature identification occurs if and only if
\[
\sum_{k=0}^{\infty}s_{k,i}^2=\infty.
\]
Therefore every infinite trajectory with finite coordinatewise path energy has a strictly biased limiting metric:
\[
u_{\infty,i}\ne q.
\]
Moreover,
\[
|u_{\infty,i}-q|
\ge
|1-q|
\exp\!\left(
-\frac1\omega
\sum_{k=0}^{\infty}s_{k,i}^2
\right)
>0.
\]

This is not merely an abstract data sequence. With
\[
K=\mathbb R_+^2,
\qquad
\lambda^0=\frac1{\sqrt2}(1,1)^{\mathsf T},
\]
and the two identical objectives
\[
F_1(x)=F_2(x)=\frac{q}{2\sqrt2}(x-a)^2,
\]
the source scalarization satisfies
\[
g(x)=JF(x)^{\mathsf T}\lambda^0=q(x-a),
\]
so every actual step obeys
\[
y_k=q s_k.
\]
Hence the phenomenon occurs within the paper's own vector-optimization construction.

In particular, Q-linear convergence of the iterate is enough to prevent exact metric learning. If
\[
|x_{k+1}-a|
\le
r|x_k-a|,
\qquad
0<r<1,
\]
for every \(k\), then
\[
\sum_{k=0}^{\infty}s_k^2
\le
\frac{1+r}{1-r}|x_0-a|^2,
\]
and therefore
\[
|u_\infty-q|
\ge
|1-q|
\exp\!\left(
-\frac{1+r}{1-r}
\frac{|x_0-a|^2}{\omega}
\right).
\]

Thus fixed regularization creates a finite-information floor: fast convergence of the iterates can freeze the diagonal metric away from an exactly constant curvature.

## Assumptions and scope

The statement concerns the regularized diagonal secant-fitting update in Section 2.2 of the primary source. The regularization parameter \(\omega\) is fixed and positive, and the metric is projected onto the fixed interval \([m_L,m_U]\).

The exact-identification criterion is coordinatewise. It assumes that the corresponding scalarized gradient component is affine with slope \(q\), so its secant equation is exact at every iteration.

The result is independent of the particular restarted conjugate-gradient direction or Wolfe step chosen afterward: once the actual iterate differences \(s_k\) are fixed, the metric recurrence is determined by the source update.

A finite algorithmic termination is not called a failure of metric identification. The theorem concerns infinite nonterminating sequences and their asymptotic metric.

## Proof

Under the exact secant relation
\[
y_{k,i}=q s_{k,i},
\]
the unprojected update becomes
\[
\widetilde u_{k+1,i}
=
\frac{q s_{k,i}^2+\omega u_{k,i}}
{s_{k,i}^2+\omega}.
\]
This is a convex combination of \(q\) and \(u_{k,i}\). Since the source initializes \(u_{0,i}=1\) and
\[
q,1\in[m_L,m_U],
\]
induction gives
\[
\widetilde u_{k+1,i}\in[m_L,m_U].
\]
Thus projection does nothing and
\[
u_{k+1,i}=
\frac{q s_{k,i}^2+\omega u_{k,i}}
{s_{k,i}^2+\omega}.
\]
Subtracting \(q\) yields
\[
u_{k+1,i}-q
=
\frac{\omega}{s_{k,i}^2+\omega}
(u_{k,i}-q).
\]
Iteration gives
\[
u_{N,i}-q
=
(1-q)
\prod_{k=0}^{N-1}
\frac{\omega}{s_{k,i}^2+\omega}.
\]

Put
\[
t_k=\frac{s_{k,i}^2}{\omega}\ge0.
\]
The infinite product vanishes exactly when
\[
\sum_{k=0}^{\infty}\log(1+t_k)=\infty.
\]
If \(\sum_k t_k<\infty\), then
\[
\log(1+t_k)\le t_k
\]
shows that the logarithmic sum is finite. Conversely, if \(\sum_k t_k=\infty\), either \(t_k\ge1\) infinitely often, in which case infinitely many logarithmic terms are at least \(\log2\), or eventually \(t_k<1\), in which case
\[
\log(1+t_k)\ge\frac{t_k}{2}.
\]
Thus the logarithmic sum diverges. This proves
\[
\prod_{k=0}^{\infty}(1+t_k)^{-1}=0
\quad\Longleftrightarrow\quad
\sum_{k=0}^{\infty}s_{k,i}^2=\infty.
\]
When \(q\ne1\), the exact-identification criterion follows immediately.

For finite path energy, use
\[
\log(1+t)\le t
\]
to obtain
\[
\prod_{k=0}^{\infty}(1+t_k)^{-1}
=
\exp\!\left(-\sum_k\log(1+t_k)\right)
\ge
\exp\!\left(-\sum_k t_k\right).
\]
Therefore
\[
|u_{\infty,i}-q|
\ge
|1-q|
\exp\!\left(
-\frac1\omega\sum_k s_{k,i}^2
\right).
\]

For the source-compatible biobjective quadratic, each component derivative is
\[
F_j'(x)=\frac{q}{\sqrt2}(x-a),
\]
so
\[
JF(x)^{\mathsf T}\lambda^0
=
\frac{F_1'(x)+F_2'(x)}{\sqrt2}
=q(x-a).
\]
Thus \(y_k=q s_k\) exactly.

Finally let
\[
e_k=x_k-a
\]
and suppose
\[
|e_{k+1}|\le r|e_k|
\]
for all \(k\). Then
\[
|s_k|
=|e_{k+1}-e_k|
\le
|e_{k+1}|+|e_k|
\le
(1+r)r^k|e_0|.
\]
Hence
\[
\sum_{k=0}^{\infty}s_k^2
\le
(1+r)^2|e_0|^2
\sum_{k=0}^{\infty}r^{2k}
=
\frac{1+r}{1-r}|e_0|^2.
\]
Substitution into the preceding bias inequality gives the stated Q-linear bound.

## Verification

The standalone script `artifacts/verify_metric_freeze.py` checks the exact product recurrence with rational arithmetic, verifies that projection remains inactive on representative admissible parameters, and compares the computed limiting bias against the analytic exponential lower bound on a geometrically convergent trajectory.

The infinite-product equivalence and the Q-linear energy estimate are proved analytically above; finite computation is not used as a substitute for those quantified arguments.

## Relationship to prior work

The primary paper introduces the regularized diagonal variable metric as one of the main algorithmic novelties of DVM-R3TCG. Its metric subproblem combines diagonal secant fitting with a fixed regularization term that suppresses abrupt changes, and its ablation study reports improved computational performance when the metric module is enabled.

The source proves a useful bound of order \(\|s_k\|^2\) on successive metric changes. It does not state the complementary consequence established here: because the learning strength itself is proportional to the squared coordinate displacement, finite path energy can leave a permanent bias even when every observed secant is exactly consistent with one constant curvature.

Earlier nonlinear and spectral conjugate-gradient methods for vector optimization establish descent and global convergence for different scalar or spectral parameter constructions. The inspected papers do not use this fixed-regularization coordinatewise secant-fitting recursion and therefore do not imply the product law or the finite-energy identification criterion.

Targeted searches using the primary DOI, diagonal secant fitting, regularized diagonal Barzilai--Borwein terminology, finite path energy, curvature identification, and the exact update formula did not locate an equivalent published statement.

## Limitations

The result characterizes asymptotic learning of the diagonal metric, not convergence of the full DVM-R3TCG algorithm. A biased metric can still be useful as a preconditioner and can improve transient performance.

The exact criterion assumes a coordinate with constant scalarized curvature inside \([m_L,m_U]\). If the true curvature lies outside the projection interval, exact identification is excluded for the simpler reason that the projection clips it.

The result does not prescribe an optimal time-varying regularization schedule. It only shows that fixed positive regularization needs infinite cumulative squared excitation in a coordinate to identify an initially missed exact curvature.

## References

1. Y. Zhang, J. Gao, C. He, *A restarted three-term vector conjugate gradient method with a diagonal variable metric for nonconvex unconstrained vector optimization*, AIMS Mathematics 11(9), 2026, 30904--30943. DOI: 10.3934/math.20261224.
2. Q.-R. He, C.-R. Chen, S.-J. Li, *Spectral conjugate gradient methods for vector optimization problems*, Computational Optimization and Applications 86(2), 2023, 457--489. DOI: 10.1007/s10589-023-00508-w.
3. L. R. Lucambio Pérez, L. F. Prudente, *Nonlinear Conjugate Gradient Methods for Vector Optimization*, SIAM Journal on Optimization 28(3), 2018, 2690--2720. DOI: 10.1137/17M1126588.
