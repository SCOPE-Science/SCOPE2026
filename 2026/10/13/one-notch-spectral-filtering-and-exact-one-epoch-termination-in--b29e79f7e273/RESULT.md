# One-notch spectral filtering and exact one-epoch termination in MNMPSVRG
## Finding
Consider the one-component deterministic specialization of MNMPSVRG with \(h\equiv0\) on
\[
f(x)=\frac12 x^{\mathsf T}Hx,
\]
where \(H\succ0\), \(L=\lambda_{\max}(H)\), the epoch length is \(m\ge1\), and Algorithm 1 uses \(\theta\in(0,1)\) and \(0<\eta<1/(2L)\).  For a snapshot \(\widetilde x\), the inner iteration is exactly
\[
y_t=\theta x_t+(1-\theta)\widetilde x,
\qquad
x_{t+1}=x_t-\eta H y_t,
\qquad
x_0=\widetilde x.
\]
After \(m\) inner steps,
\[
x_m=P_m(\eta H;\theta)\widetilde x,
\qquad
P_m(q;\theta)=\frac{(1-\theta q)^m-(1-\theta)}{\theta}.
\]
Thus negative momentum is an exact stationary spectral filter on quadratics.

For every fixed \(\theta\in(0,1)\), the transfer polynomial has at most one zero in the algorithmic modal range \(0<q<1/2\). Any such zero must equal
\[
q_\star(\theta,m)=\frac{1-(1-\theta)^{1/m}}{\theta}.
\]
Hence a single negative-momentum parameter can annihilate at most one distinct positive eigenspace in one epoch.

For the isotropic quadratic \(H=\lambda I\), put \(q=\eta\lambda\in(0,1/2)\).  There exists a unique \(\theta\in(0,1)\) for which the first epoch sends every initial point exactly to the minimizer if and only if
\[
mq>1.
\]
Because \(q<1/2\), this is equivalent to \(m\ge3\) and \(1/m<q<1/2\).  For example, \(m=3\) and \(q=0.4\) give the unique value
\[
\theta\approx0.442810861169262,
\]
for which the snapshot is exactly zero after three inner steps.

If \(mq\le1\), exact one-epoch termination is impossible for every admissible \(\theta\), and the sharp tuning limit is
\[
\inf_{0<\theta<1}|P_m(q;\theta)|=1-mq.
\]
At \(mq=1\) the infimum is zero but is approached only as \(\theta\downarrow0\), which is outside the allowed open parameter interval.

## Assumptions and scope
The specialization uses one smooth component, so the mini-batch and variance-reduction estimator become deterministic.  With \(h\equiv0\), the proximal map in Algorithm 1 is the identity.  The source algorithm requires \(\theta\in(0,1)\) and \(0<\eta<1/(2L)\); the statement above keeps this stepsize restriction and does not rely on the paper's more conservative sufficient condition in Theorem 4.1.

The quadratic is convex and smooth, although the source algorithm is designed for a broader nonconvex composite setting.  The general SPD formula is exact for every dimension.  Exact one-epoch termination from every initial point is claimed only for the isotropic case; for a general spectrum a single \(\theta\) can cancel at most one distinct eigenvalue in the admissible range.

## Proof
At a fixed epoch, let \(r=\widetilde x\).  Because the single component equals the full objective, the variance-reduced estimator evaluated at the interpolation point is simply
\[
v_t=Hy_t=H\bigl(\theta x_t+(1-\theta)r\bigr).
\]
Hence
\[
x_{t+1}=(I-\eta\theta H)x_t-\eta(1-\theta)Hr.
\]
Set \(A=I-\eta\theta H\).  Since \(I-A=\eta\theta H\) and \(H\) commutes with \(A\), summing the affine recurrence from \(x_0=r\) gives
\[
\begin{aligned}
x_t
&=A^t r-\eta(1-\theta)\sum_{j=0}^{t-1}A^jHr\\
&=A^t r-\frac{1-\theta}{\theta}(I-A^t)r\\
&=\frac{A^t-(1-\theta)I}{\theta}r.
\end{aligned}
\]
Taking \(t=m\) proves the transfer polynomial.

For an eigenvalue \(\lambda_i\), write \(q_i=\eta\lambda_i\).  The source stepsize restriction gives \(0<q_i<1/2\), so \(1-\theta q_i>0\).  Therefore
\[
P_m(q_i;\theta)=0
\]
if and only if
\[
1-\theta q_i=(1-\theta)^{1/m},
\]
which gives the displayed \(q_\star\). There is only one positive root on the branch \(1-\theta q>0\); it is an admissible notch only when \(q_\star<1/2\). This proves the one-notch statement.

To classify the isotropic tuning, write
\[
u=(1-\theta)^{1/m}\in(0,1).
\]
At a zero,
\[
q=\frac{1-u}{1-u^m}=\frac{1}{1+u+\cdots+u^{m-1}}.
\]
As \(\theta\) increases from zero to one, \(u\) decreases from one to zero, so this zero location increases strictly from \(1/m\) to \(1\).  Thus for a fixed \(q\in(0,1/2)\), an admissible zero exists uniquely exactly when \(q>1/m\), equivalently \(mq>1\).

Finally, for fixed \(q>0\), let \(g(\theta)=(1-q\theta)^m\).  For \(m\ge2\), \(g\) is strictly convex on \((0,1)\), so its secant slope \([g(\theta)-g(0)]/\theta\) is strictly increasing.  Since
\[
P_m(q;\theta)=1+\frac{g(\theta)-g(0)}{\theta},
\]
\(P_m(q;\theta)\) is strictly increasing in \(\theta\), with
\[
\lim_{\theta\downarrow0}P_m(q;\theta)=1-mq.
\]
If \(mq\le1\), it is therefore positive for every \(\theta>0\) and has the stated sharp infimum.  The case \(m=1\) is immediate from \(P_1(q;\theta)=1-q\).

## Verification
The bundled script `artifacts/verify_mnmpsvrg_filter.py` replays the inner recurrence against the closed form for random admissible parameters, verifies the exact notch formula, checks the displayed \(m=3\), \(q=0.4\) annihilation, tests the no-zero regime \(mq\le1\), and checks a diagonal SPD instance mode by mode.  It prints `VERIFY_OK`.

These finite computations are consistency checks only.  The transfer identity, uniqueness of the admissible zero, and tuning classification are proved analytically above.

## Relationship to prior work
Cui, He, Cao, and Yang define MNMPSVRG with exactly the snapshot interpolation \(y_t=\theta x_t+(1-\theta)\widetilde x\), a variance-reduced gradient evaluated at \(y_t\), and a proximal update.  Their paper proves a general sublinear stationarity bound and experimentally reports substantial sensitivity to \(\theta\), while listing adaptive parameter tuning as a future direction.  It does not state the quadratic epoch-transfer polynomial, its admissible spectral zero, or the exact finite-termination criterion above.

Allen-Zhu's Katyusha paper explains negative momentum as attraction toward a snapshot and proves accelerated convergence for a different multi-sequence scheme.  Its relevant full-text discussion does not give this MNMPSVRG transfer polynomial or a one-epoch annihilation rule.

He, Ye, and E introduced NMSVRG, the direct convex predecessor cited by the MNMPSVRG paper.  The accessible publisher preview and abstract describe its one-parameter negative-momentum SVRG framework and linear convergence theory, but the full article text was not lawfully accessible during this check.  No accessible statement establishes the exact filter or finite-termination classification here; this inaccessible close predecessor remains the main residual originality risk.

Driggs, Ehrhardt, and Schönlieb analyze negative momentum as one acceleration mechanism for variance-reduced methods and develop an alternative universal acceleration framework.  Their comparison is at the convergence-rate/framework level and does not imply the present exact epoch polynomial.

## Limitations
The exact spectral-filter identity is for the deterministic one-component quadratic specialization with \(h\equiv0\).  It does not claim one-epoch termination for stochastic mini-batches, nonsmooth regularizers, nonlinear objectives, or a general anisotropic quadratic with several active eigenvalues.

The finite-termination tuning may lie outside the sufficient stepsize condition used in the source paper's general Theorem 4.1 even though it remains inside Algorithm 1's stated \(0<\eta<1/(2L)\) requirement.  Therefore it should be read as an exact property of the published iteration, not as a strengthening of that theorem without further analysis.

The closest NMSVRG predecessor could not be inspected in full text, so an equivalent unpublished-in-this-search scalar calculation cannot be excluded.

## References
1. W. Cui, C. He, M. Cao, and Y. Yang, *A new mini-batch negative momentum proximal stochastic variance reduction method for nonconvex optimization*, AIMS Mathematics 11(2), 4759--4786, 2026. DOI: 10.3934/math.2026194.
2. Z. Allen-Zhu, *Katyusha: The First Direct Acceleration of Stochastic Gradient Methods*, Journal of Machine Learning Research 18(221), 1--51, 2018.
3. L. He, J. Ye, and J. E, *Accelerated Stochastic Variance Reduction for a Class of Convex Optimization Problems*, Journal of Optimization Theory and Applications 196, 810--828, 2023. DOI: 10.1007/s10957-022-02157-1.
4. D. Driggs, M. J. Ehrhardt, and C.-B. Schönlieb, *Accelerating Variance-Reduced Stochastic Gradient Methods*, Mathematical Programming 191, 615--650, 2022. DOI: 10.1007/s10107-020-01566-2.
