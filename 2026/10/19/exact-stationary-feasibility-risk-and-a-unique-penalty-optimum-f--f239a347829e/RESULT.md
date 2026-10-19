# Exact stationary feasibility risk and a unique penalty optimum for stochastic momentum augmented Lagrangian

## Finding

Consider the constant-parameter scalar stochastic momentum augmented-Lagrangian (MALM) recurrence specified below. Its mean-square stability threshold is exactly \(0<\beta/\eta<4/3\). In that stable interval, the limiting squared feasibility error is
\[
\lim_{r\to\infty}\mathbb E[x_r^2]=\frac{\sigma^2}{\eta^2}\frac{2\alpha^2[2-\alpha-(1-\alpha)t]}{t(2-\alpha)(4-3t)[\alpha^2+(1-\alpha^2)t]},\qquad t=\beta/\eta.
\]
For each fixed \(0<\alpha<1\), this expression has exactly one minimizing penalty ratio, characterized as the unique zero in \((2/3,1)\) of
\[
-\frac{1-\alpha}{2-\alpha-(1-\alpha)t}-\frac1t+\frac3{4-3t}-\frac{1-\alpha^2}{\alpha^2+(1-\alpha^2)t}=0.
\]
The sharp stability boundary is a unit-circle eigenvalue crossing. At and beyond the boundary, nondegenerate gradient noise produces unbounded second-moment feasibility risk. The optimizer tends to \(1\) as \(\alpha\downarrow0\), and to \(2/3\) as \(\alpha\uparrow1\).

## Assumptions and scope

The optimization problem is \(\min_{x\in\mathbb R}f(x)=0\) subject to \(x=0\). Its stochastic gradient oracle supplies independent identically distributed \(\xi_r\), independent of the finite-second-moment initial state, with \(\mathbb E\xi_r=0\) and \(\mathbb E\xi_r^2=\sigma^2\in(0,\infty)\). Gaussianity is unnecessary. All arithmetic and constraint residuals are exact. Parameters are constant: primal parameter \(\eta>0\), constraint penalty \(\beta>0\), and momentum refresh \(0<\alpha<1\). The iterates are
\[
\begin{split}
x_{r+1}&=x_r-\eta^{-1}(m_r+\lambda_r+\beta x_r),\\
\lambda_{r+1}&=\lambda_r+\beta x_{r+1},\\
m_{r+1}&=(1-\alpha)m_r+\alpha\xi_{r+1}.
\end{split}
\]
This is a constant-parameter specialization of the stochastic MALM method of Qiu, Maithripala and Lin, not their diminishing-parameter convergence regime. The theorem concerns the mean-square feasibility measure \(\mathbb E[x_r^2]\), not general nonconvex KKT complexity.

## Proof

Put \(t=\beta/\eta\), \(u_r=\lambda_r/\eta\), \(v_r=m_r/\eta\), and \(z_r=(x_r,u_r,v_r)^{\mathsf T}\). Then \(z_{r+1}=Mz_r+\alpha\eta^{-1}\xi_{r+1}e_3\) with
\[
M=\begin{pmatrix}1-t&-1&-1\\t(1-t)&1-t&-t\\0&0&1-\alpha\end{pmatrix}.
\]
The characteristic polynomial factors as
\[
(z-1+\alpha)\,[z^2-2(1-t)z+(1-t)].
\]
For the quadratic factor, the three strict real Schur conditions are \(t>0\), \(4-3t>0\), and \(|1-t|<1\). In conjunction with \(0<\alpha<1\) this gives exactly \(0<t<4/3\). For this interval the stationary covariance is the unique solution to the discrete Lyapunov equation \(C=MCM^{\mathsf T}+(\alpha^2\sigma^2/\eta^2)e_3e_3^{\mathsf T}\), and all finite-second-moment initial distributions converge to it in second moments.

For an explicit algebraic certificate, write \(a=\alpha\), \(D=a^2+(1-a^2)t\), \(d=2-a\), and \(e=1-a\). Scale out \(\sigma^2/\eta^2\). A direct solution of the six independent Lyapunov equations gives \(X=C_{11}\) equal to
\[
X=\frac{2a^2(d-et)}{td(4-3t)D},
\]
and the remaining independent entries
\[
C_{12}=\frac{tX}{2},\quad C_{13}=-\frac{a^2e}{dD},\quad C_{23}=-\frac{ate}{dD},\quad C_{33}=\frac a d,
\]
\[
C_{22}=t(3-2t)X-C_{33}+2(1-t)C_{13}-2C_{23}.
\]
In these formulas the notation \(C\) denotes the normalized covariance; multiply each entry by \(\sigma^2/\eta^2\) for the physical covariance. Substituting this symmetric matrix into the displayed Lyapunov identity verifies all six entries. In particular, its \((1,1)\) entry is the asserted risk. The coefficient block is noise controllable because \(\det[e_3,Me_3,M^2e_3]=t\), and the first-coordinate output is observable because \(\det[e_1^{\mathsf T};e_1^{\mathsf T}M;e_1^{\mathsf T}M^2]=-\alpha\). Thus at or beyond the spectral stability frontier, no unstable or unit-modulus mode is hidden from either the forcing or feasibility output; the accumulated nonzero forcing variance rules out a finite limiting feasibility second moment.

For fixed \(a\), let \(V_a(t)=X\). Logarithmic differentiation gives
\[
(\log V_a)'=-\frac{e}{d-et}-\frac1t+\frac3{4-3t}-\frac{1-a^2}{D}.
\]
Its derivative is
\[
(\log V_a)''=-\frac{e^2}{(d-et)^2}+\frac1{t^2}+\frac9{(4-3t)^2}+\frac{(1-a^2)^2}{D^2}>0.
\]
Indeed \(3/(4-3t)>e/(d-et)\), since \(3d-4e=2+a>0\); hence even the difference of the first and third terms is positive. Also \(V_a(t)\to\infty\) at both stable endpoints. Strict convexity therefore gives a unique minimum. At \(t=2/3\), the log derivative is \(-9(1-a)(a+2)/[(4-a)(a^2+2)]<0\); at \(t=1\), it is \(a(a+1)>0\). These signs give \(2/3<t_*(a)<1\). On compact interior subintervals, the derivative tends continuously to the appropriate endpoint-parameter equation as \(a\to0\) or \(a\to1\); the unique roots approach \(1\) and \(2/3\), respectively.

## Verification

Run `python verify.py` with Python 3 standard library. The script independently constructs and solves the six Lyapunov equations over exact rational numbers for multiple values of \(\alpha\) and \(t\), verifies the proposed covariance and derivative identities, brackets the optimal ratio, and cross-checks four stationary-risk points using a seeded stochastic simulation. It reports 1716 passing exact-rational or seeded numerical comparisons. Finite computation corroborates the identities, but the universal theorem relies on the preceding algebra and spectral proof.

## Relationship to prior work

Qiu, Maithripala and Lin (2026, arXiv:2604.13272, first public April 14, 2026) define the momentum-based constrained stochastic method and establish finite-horizon approximate KKT guarantees under their parameter assumptions. The contribution here is a constant-parameter noise-floor classification, a sharp stability boundary, and a unique penalty choice in a solvable constrained oracle model, not a rederivation of the source's nonconvex complexity theorem. Related available work treats deterministic proximal augmented-Lagrangian stability, deterministic linearized ADMM, and unconstrained STORM stationary noise covariance. Those models do not directly imply this specific three-state MALM covariance or penalty optimum. A previous equivalent specialization in broader stochastic primal-dual literature cannot be excluded.

## Limitations

The constraint and objective are scalar and affine/constant, respectively; the oracle has additive state-independent noise with finite nonzero variance. Exact expected feasibility, not iteration complexity or wall-clock performance, is measured. Constant parameters differ materially from diminishing-parameter regimes. The near-boundary instability statement does not imply failure of every decreasing-stepsize MALM implementation. The comparison with earlier literature is not an independent exhaustive review.

## References

Qiu, C., Maithripala, M., and Lin, Z., *A Momentum-based Stochastic Algorithm for Linearly Constrained Nonconvex Optimization*, arXiv:2604.13272v1 (first public 2026-04-14), https://arxiv.org/abs/2604.13272.

Relevant comparison records: *Exact stationary covariance and stability factorization for constant-template STORM* (2026, research record identifier `fd5004e04a73`); *Exact stabilization phase diagram for scalar linearized ADMM* (`9ae77a2e1a30`); *Sharp local stability frontier for fixed-parameter proximal augmented Lagrangian dynamics* (`b8117b8b15ed`). These concern different updates and cannot alone establish either novelty or coverage of the present MALM specialization.
