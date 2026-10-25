# Sharp whole-window boundary-layer cost of mean-speed inflow control

## Finding
Let \(\mu>0\), \(\kappa>0\), \(c\ge 0\), and \(T>2/\mu\). If \(V_\varepsilon\) is uniformly distributed on \([\mu-\varepsilon,\mu+\varepsilon]\), then the complete observation-window quadratic mismatch of the mean-speed inflow surrogate exceeds its stochastic minimum by
\[
H_\varepsilon(\bar u_\varepsilon)-H_\varepsilon(u_\varepsilon^*)
 =\frac{\kappa^2}{3\mu^6}\varepsilon^3+O(\varepsilon^4).
\]
If the mean delay is projected onto the **eligible delay interval separately at each control time**, the corresponding excess is exactly half at leading order:
\[
H_\varepsilon(\bar u_\varepsilon^{\mathrm{clip}})-H_\varepsilon(u_\varepsilon^*)
 =\frac{\kappa^2}{6\mu^6}\varepsilon^3+O(\varepsilon^4).
\]
Both coefficients are strictly positive. Because \(\operatorname{Var}(V_\varepsilon)=\varepsilon^2/3\), neither whole-window surrogate generally achieves the interior \(O(\operatorname{Var}(V_\varepsilon)^2)\) excess-cost order: the sharp full-window order is \(\operatorname{Var}(V_\varepsilon)^{3/2}\). The statement concerns this explicit affine demand and uniform velocity family, not arbitrary distributions or numerical algorithms.

## Assumptions and scope
Take \(0<\varepsilon<\mu\) sufficiently small that \(T>2b_\varepsilon-a_\varepsilon\), where
\[
a_\varepsilon=(\mu+\varepsilon)^{-1},\qquad b_\varepsilon=(\mu-\varepsilon)^{-1},\qquad r_0=\mu^{-1}.
\]
Let the deterministic demand be \(D(s)=c+\kappa s\) on \([0,T]\). The control \(u\) is measurable and square integrable on \([0,T-a_\varepsilon]\), with no amplitude cap. Starting with an empty pipe, observe the flux only on \([b_\varepsilon,T]\), when all velocities can deliver. Define the (unhalved) cost
\[
H_\varepsilon(u)=\frac1{2\varepsilon}\int_{\mu-\varepsilon}^{\mu+\varepsilon}\int_{b_\varepsilon}^T
 \{u(s-\lambda^{-1})-D(s)\}^2\,ds\,d\lambda.
\]
Only the effective control horizon \([0,T-a_\varepsilon]\) is relevant. For each \(t\) therein, the eligible delay interval is
\[
J_\varepsilon(t)=[a_\varepsilon,b_\varepsilon]\cap[b_\varepsilon-t,T-t].
\]
Its weight \(q_\varepsilon(t)\) is the probability that \(V_\varepsilon^{-1}\in J_\varepsilon(t)\), and its conditional delay mean is \(m_\varepsilon(t)=\mathbb E[V_\varepsilon^{-1}\mid V_\varepsilon^{-1}\in J_\varepsilon(t)]\) wherever \(q_\varepsilon(t)>0\). Define
\[
u_\varepsilon^*(t)=c+\kappa\{t+m_\varepsilon(t)\},\quad
 \bar u_\varepsilon(t)=c+\kappa(t+r_0),\quad
 \bar u_\varepsilon^{\mathrm{clip}}(t)=c+\kappa\{t+\Pi_{J_\varepsilon(t)}(r_0)\}.
\]
At endpoints where eligibility has zero probability, values are immaterial. The clipped surrogate here is a specifically defined delay projection; it is **not** asserted to be a scheme proposed in the cited source.

## Proof
**Conditional projection.** Substitute \(t=s-\lambda^{-1}\) in the objective and apply Fubini. At each \(t\), complete the square conditional on its eligible velocities. This yields an exact identity for every admissible control:
\[
H_\varepsilon(u)-H_\varepsilon(u_\varepsilon^*)
 =\int_0^{T-a_\varepsilon}q_\varepsilon(t)
    \{u(t)-u_\varepsilon^*(t)\}^2\,dt.
\]
In particular, the stochastic optimum is unique almost everywhere on the positive-weight set, and the losses of both proxies equal \(\kappa^2\) times the integral of the weighted squared delay bias.

**Separation into three time regions.** For the stated small \(\varepsilon\), the non-overlapping regions are \([0,b_\varepsilon-a_\varepsilon]\), \([b_\varepsilon-a_\varepsilon,T-b_\varepsilon]\), and \([T-b_\varepsilon,T-a_\varepsilon]\). In the interior the entire delay interval is eligible and \(q_\varepsilon=1\). Its mean is
\[
 m_\varepsilon^{\mathrm{int}}=\frac{1}{2\varepsilon}
  \log\frac{\mu+\varepsilon}{\mu-\varepsilon}
 =r_0+\frac{\varepsilon^2}{3\mu^3}+O(\varepsilon^4).
\]
The projection also equals \(r_0\) there, so each interior contribution is \(O(\varepsilon^4)\).

**Left boundary.** Write \(t=\varepsilon y/\mu^2\). Then the left strip corresponds to \(0\le y\le 2+O(\varepsilon^2)\). Parametrize velocity by \(V_\varepsilon=\mu+\varepsilon v\), with \(v\) uniform on \([-1,1]\). Uniformly on the strip, the eligible normalized velocities are \(v\le y-1+O(\varepsilon)\) (with the interval naturally clipped at its endpoints). Hence
\[
q_\varepsilon=\frac y2+O(\varepsilon),\qquad
m_\varepsilon-r_0=\frac\varepsilon{\mu^2}\left(1-\frac y2\right)+O(\varepsilon^2).
\]
All estimates are uniform: conditional means are means of a smooth function over intervals in a bounded normalized velocity variable, including when that interval shrinks to a point. The raw proxy contributes, after division by \(\kappa^2\varepsilon^3/\mu^6\),
\[
 C_{L,\mathrm{raw}}=\int_0^2\frac y2\left(1-\frac y2\right)^2dy=\frac16.
\]
The clipped proxy has delay \(b_\varepsilon-t\) for \(0\le y<1\) and delay \(r_0\) for \(1<y\le2\), up to shifts of size \(O(\varepsilon)\). Its limit coefficient is
\[
 C_{L,\mathrm{clip}}=\int_0^1\frac{y^3}{8}\,dy
 +\int_1^2\frac y2\left(1-\frac y2\right)^2dy=\frac1{12}.
\]
The bounded integrands and uniform first-order parameter expansions show that replacing these limit profiles by the finite-width integrands incurs \(O(\varepsilon)\) error after normalization, hence \(O(\varepsilon^4)\) in the unnormalized cost.

**Right boundary.** Put \(t=T-b_\varepsilon+\varepsilon y/\mu^2\). Eligibility now requires \(v\ge y-1+O(\varepsilon)\), so
\[
 q_\varepsilon=1-\frac y2+O(\varepsilon),\qquad
 m_\varepsilon-r_0=-\frac{\varepsilon y}{2\mu^2}+O(\varepsilon^2).
\]
The corresponding raw integral is \(\int_0^2 (1-y/2)y^2/4\,dy=1/6\). For the clipped delay, the first half of the strip retains \(r_0\) and the second projects it to \(T-t\), giving
\[
 C_{R,\mathrm{clip}}=
 \int_0^1\left(1-\frac y2\right)\frac{y^2}{4}\,dy
 +\int_1^2\left(1-\frac y2\right)^3dy=\frac1{12}.
\]
The same uniform error control applies. Summing both strips with the interior \(O(\varepsilon^4)\) contribution gives the two displayed asymptotics. The nonzero leading coefficients establish sharpness.

## Verification
The accompanying `verify_boundary.py` independently evaluates the rational boundary integrals exactly using fractions and computes the entire finite-width conditional-projection integral by midpoint quadrature for two distinct mean velocities. `verification_output.txt` records exact fractions and convergence of the normalized raw and clipped costs to \(1/3\) and \(1/6\), respectively. Run `python3 verify_boundary.py` with Python 3; no third-party packages or source files are required. The analytic projection argument and uniform rescaling, not the finite quadrature, prove the asymptotic statement.

## Relationship to prior work
Göttlich and Schillinger [1] derive conditional-expectation optimal inflow controls under random velocities, discuss mean-velocity proxy controls, and bound interior approximation errors in terms of squared velocity variance. Their full-text discussion of finite-horizon boundaries does not provide the two sharp whole-observation-window asymptotic constants above. Here the smooth affine demand isolates a boundary effect even when the interior bound is stronger. The earlier uncertain-demand transport study [2] treats a different stochastic input, so it does not imply this random-flight-time truncation law. Neither absence of a matching search result nor specialization of the velocity law proves global novelty; the claimed distinction is the new quantified full-window cost asymptotic.

## Limitations
The result assumes uniform positive velocities, one constant-velocity route of unit length, zero initial transported mass, affine demand, square cost, and no control amplitude limits; other settings may yield different orders. In particular, the mean-speed and clipped proxies here are explicit whole-control-horizon extensions, and the result does not undermine the published guarantee on its narrower interior interval. A source-associated code repository was not materially read; unindexed classical boundary-layer literature may contain an equivalent formulation. Self-review is not an independent audit.

## References
[1] S. Göttlich and J. Schillinger, *Optimal Inflow Control for Transport Equations with Uncertain Velocities and Demand*, arXiv:2609.01291, first publicly submitted 2026-09-01; Sections 3–4 and 6.4. https://arxiv.org/abs/2609.01291

[2] S. Göttlich and J. Schillinger, *Control Strategies for Transport Networks under Demand Uncertainty*, arXiv:2111.09674 (2021). https://arxiv.org/abs/2111.09674

[3] S. Göttlich, O. Kolb and K. Lux, *Chance-constrained optimal inflow control in hyperbolic supply systems with uncertain demand* (2020), https://doi.org/10.1002/oca.2689
