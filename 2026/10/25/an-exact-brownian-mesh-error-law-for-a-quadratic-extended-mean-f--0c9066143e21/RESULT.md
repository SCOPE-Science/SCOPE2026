# An exact Brownian mesh-error law for a quadratic extended mean-field control problem

## Finding

Consider the scalar state equation \(dX_t=dW_t\), \(X_0=m\), on \([0,T]\), with square-integrable adapted controls taking values in \(\mathbb R\). For \(\theta\ge0\), use the time-independent running cost

\[
f(x,a,\eta)=\frac12a^2+\frac12(x+a)^2+\frac\theta2\left(\int a'\,d\eta(x',a')\right)^2,
\]

where the integral is the mean control under the joint law \(\eta\) of state and control. Let \(V\) be the minimum continuous-time cost. For a partition \(\pi=(0=t_0<t_1<\cdots<t_N=T)\), let \(V_\pi\) be the minimum cost of the left-endpoint Euler discretization with controls constant on each interval and measurable at its left endpoint. Write \(h_i=t_{i+1}-t_i\). Then

\[
\hat\alpha_t=-\frac12W_t-\frac{m}{2+\theta},\qquad
\alpha_i^\pi=-\frac12W_{t_i}-\frac{m}{2+\theta},
\]

are the respective unique optimizers, and the exact identities are

\[
\inf_{\beta\text{ adapted and constant on each }[t_i,t_{i+1})}
\|\hat\alpha-\beta\|_{\mathcal H^2}^2
=\|\hat\alpha-\alpha^\pi\|_{\mathcal H^2}^2
=V-V_\pi=\frac18\sum_{i=0}^{N-1}h_i^2.
\]

Thus, for fixed \(N\), every adapted piecewise-constant control has squared error at least \(T^2/(8N)\), and the uniform partition attains this bound. The mean-control coupling parameter \(\theta\) changes the deterministic mean of the optimizer but not the Brownian discretization floor.

## Assumptions and scope

The driving process \((W_t)_{t\in[0,T]}\) is a standard one-dimensional Brownian motion with its augmented natural filtration. The initial state \(m\in\mathbb R\) and horizon \(T>0\) are deterministic. The diffusion is uncontrolled and has constant coefficient one. The action set is the full real line, and admissible controls are progressively measurable with finite \(\mathbb E\int_0^T|\alpha_t|^2dt\). The parameter \(\theta\) is nonnegative. The cost is strongly convex in the control and convex in the lifted state-control variables and their law. The first-order condition has the Lipschitz feedback \(\hat\alpha(x,\eta)=-x/2+\theta\bar x/[2(2+\theta)]\), where \(\bar x=\int x\,d\eta\); it is independent of time and the adjoint. The discrete state uses Euler–Maruyama; because the diffusion is constant and uncontrolled, its values at grid nodes equal \(m+W_{t_i}\) exactly.

The result is an exact benchmark for this scalar quadratic model, not a convergence-rate theorem for general mean-field control problems. In particular, the action set is unbounded and the diffusion does not depend on the control.

## Proof

Let \(\bar\alpha_t=\mathbb E[\alpha_t]\). Since \(X_t=m+W_t\), the continuous running objective at time \(t\) is

\[
\frac12\mathbb E[\alpha_t^2]+\frac12\mathbb E[(X_t+\alpha_t)^2]+\frac\theta2\bar\alpha_t^2.
\]

Its first-order condition is \(2\alpha_t+X_t+\theta\bar\alpha_t=0\). Taking expectations gives \((2+\theta)\bar\alpha_t=-m\), hence \(\bar\alpha_t=-m/(2+\theta)\) and \(\hat\alpha_t=-W_t/2-m/(2+\theta)\). Strict convexity makes this optimizer unique.

At the grid node \(t_i\), the discrete state is \(X_{t_i}=m+W_{t_i}\). Minimizing the corresponding one-step quadratic cost over an \(\mathcal F_{t_i}\)-measurable control gives \(2\alpha_i+X_{t_i}+\theta\mathbb E[\alpha_i]=0\). Its mean is again \(-m/(2+\theta)\), so the unique discrete optimizer is \(\alpha_i^\pi=-W_{t_i}/2-m/(2+\theta)\).

For any \(\mathcal F_{t_i}\)-measurable value \(B_i\), conditional expectation is the orthogonal projection in \(L^2\), and

\[
\mathbb E[|\hat\alpha_t-B_i|^2]
=\mathbb E[|\hat\alpha_t-\mathbb E(\hat\alpha_t\mid\mathcal F_{t_i})|^2]
+\mathbb E[|\mathbb E(\hat\alpha_t\mid\mathcal F_{t_i})-B_i|^2].
\]

For \(t\in[t_i,t_{i+1})\), Brownian independent increments give \(\mathbb E(\hat\alpha_t\mid\mathcal F_{t_i})=\alpha_i^\pi\) and conditional variance \((t-t_i)/4\). Integrating the first term over this interval yields

\[
\int_{t_i}^{t_{i+1}}\frac{t-t_i}{4}\,dt=\frac{h_i^2}{8}.
\]

Equality holds precisely for the conditional projection \(B_i=\alpha_i^\pi\). Summing proves the exact best-approximation identity \(\inf_\beta\|\hat\alpha-\beta\|_{\mathcal H^2}^2=\|\hat\alpha-\alpha^\pi\|_{\mathcal H^2}^2=\frac18\sum_i h_i^2\).

For the value identity, substitution of the continuous optimizer gives the expected running cost \(t/4+m^2(1+\theta)/(2(2+\theta))\). The same calculation at node \(t_i\) gives the discrete expected running cost \(t_i/4+m^2(1+\theta)/(2(2+\theta))\). Therefore

\[
V=\frac{T^2}{8}+\frac{Tm^2(1+\theta)}{2(2+\theta)},\qquad
V_\pi=\frac14\sum_i h_i t_i+\frac{Tm^2(1+\theta)}{2(2+\theta)}.
\]

Since \(\int_{t_i}^{t_{i+1}}t\,dt=h_it_i+h_i^2/2\), subtracting the two values gives \(V-V_\pi=\frac18\sum_i h_i^2\). Finally, Cauchy–Schwarz gives \(\sum_i h_i^2\ge T^2/N\), with equality exactly when all interval lengths equal \(T/N\). This proves the fixed-\(N\) lower bound and its attainment by a uniform grid.

## Verification

The result follows from explicit strict-convexity first-order conditions, the orthogonal projection property of conditional expectation, and the Brownian increment variance \(\mathbb E[(W_t-W_{t_i})^2]=t-t_i\). The value-bias identity is obtained by direct integration and holds for every deterministic partition, including nonuniform partitions. No finite simulation is used to infer a universal statement.

## Relationship to prior work

Reisinger, Stockinger, Tsianni, and Zhang study time discretization in extended mean-field control and prove general regularity and convergence bounds, including a \(1/4\)-order strong control bound under their stated assumptions. Their results motivate the discretization question but do not state this exact mesh-dependent control-error/value-bias identity for this quadratic Brownian model. Jakobsen, Picarelli, and Reisinger study piecewise-constant policies for stochastic control primarily through value-function error; that is a different quantity from the strong \(\mathcal H^2\) control error here. The present claim is deliberately limited to the explicit benchmark and does not improve or contradict either general theorem.

## Limitations

The formula relies on an uncontrolled Brownian diffusion, a scalar quadratic cost, an unbounded action set, and a deterministic initial state. It does not establish a universal rate for nonlinear or control-dependent diffusions, bounded controls, nonquadratic costs, or general mean-field interactions. Brownian projection error is classical; the contribution here is the exact joint formula for the specified extended mean-field control benchmark, including the value bias and the optimal nonuniform-mesh comparison.

## References

1. C. Reisinger, W. Stockinger, M. O. Tsianni, and Y. Zhang, “Convergence Rates of Time Discretization in Extended Mean Field Control,” arXiv:2509.00904v1, first submitted 31 August 2025. https://arxiv.org/abs/2509.00904
2. E. R. Jakobsen, A. Picarelli, and C. Reisinger, “Improved order 1/4 convergence for piecewise constant policy approximation of stochastic control problems,” arXiv:1901.01193, 2019. https://arxiv.org/abs/1901.01193
