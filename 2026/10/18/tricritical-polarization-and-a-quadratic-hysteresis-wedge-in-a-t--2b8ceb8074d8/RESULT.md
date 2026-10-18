# Tricritical polarization and a quadratic hysteresis wedge in a three-agent sigmoidal-confidence motif

## Finding
For the sigmoidal bounded-confidence dynamics of a single persuadable agent between two fixed, oppositely opinionated agents, the linear-critical polarization curve contains exactly one cubic-degenerate point. It is
\[\gamma_*=\frac{\sqrt3}{2},\qquad \delta_*=1+\frac2{\sqrt3}\log(\sqrt3-1).\]
At this point, the reduced vector field is \(\dot x=-3x^5/10+O(x^7)\); nonzero nearby solutions decay according to \(|x(t)|\sim(6t/5)^{-1/4}\). On the fixed slice \(\gamma=\gamma_*\), as the central linearization parameter \(\mu\downarrow0\) through positive values, two locally attracting polarized equilibria satisfy
\[|x_\mu|=(10\mu/3)^{1/4}(1+O(\mu^{1/2})).\]
On the opposite, cubic-positive side \(\gamma=\gamma_*+\nu\) with \(\nu>0\) small, the local saddle-node curve satisfies
\[\mu_{\mathrm{fold}}(\nu)=-\frac{10}{9}\nu^2+O(\nu^3),\qquad x_{\mathrm{fold}}^2=\frac{10\sqrt3}{9}\nu+O(\nu^2).\]
For each \(\mu_{\mathrm{fold}}(\nu)<\mu<0\) there are exactly five equilibria in a fixed sufficiently small neighborhood of zero: three attractors at zero and the two outer polarized states, separated by two repellers. This is a **local** bifurcation classification; no global bound on more distant equilibria is asserted.

## Assumptions and scope
The graph is a three-vertex path with end vertices maintaining opinions \(-1\) and \(+1\) and one persuadable central vertex with opinion \(x\in[-1,1]\). The confidence weights from the persuadable vertex to the fixed ends are
\[w_\pm(x)=\bigl[1+\exp\{\gamma((x\mp1)^2-\delta)\}\bigr]^{-1},\]
where \(\gamma>0\), \(\delta\ge0\). We use the source's normalization in which the persuadable agent changes by its confidence-weighted average discrepancy:
\[\dot x=\frac{w_+(x)(1-x)+w_-(x)(-1-x)}{w_+(x)+w_-(x)}=:F_{\gamma,\delta}(x).\]
This formula excludes any dynamics of the fixed agents. The equilibria at the endpoints are not stationary because the vector field points inward. Define the central linear parameter
\[\mu=\frac{2\gamma}{1+\exp\{\gamma(\delta-1)\}}-1.\]
Near \((\gamma_*,\delta_*)\), \((\gamma,\mu)\) are smooth local coordinates. Statements about numbers of equilibria and stability are local in \(x\), \(\gamma-\gamma_*\), and \(\mu\); asymptotics take the specified parameter to zero while satisfying these restrictions.

## Proof
**Reduction and linear-critical locus.** Cancelling the common logistic factors gives exactly
\[F_{\gamma,\delta}(x)=\frac{\sinh(2\gamma x)}{\cosh(2\gamma x)+A e^{-\gamma x^2}}-x,\qquad A=e^{\gamma(\delta-1)}.\]
This is real analytic and odd near \(x=0\). Its derivative at zero is \(2\gamma/(1+A)-1=\mu\). Thus \(\mu=0\) is equivalent to \(A=2\gamma-1\) and requires \(\gamma>1/2\). The associated critical curve is \(\delta_c(\gamma)=1+\gamma^{-1}\log(2\gamma-1)\), restricted to nonnegative \(\delta\).

**The cubic and quintic coefficients.** Direct Taylor expansion of the exact quotient on the critical curve gives
\[F_{\gamma,\delta_c(\gamma)}(x)=\frac{4\gamma^2-3}{6}x^3+C_5(\gamma)x^5+O(x^7),\]
where
\[C_5(\gamma)=\frac{8\gamma^4-20\gamma^3-50\gamma^2+15\gamma+15}{60}.\]
Since \(\gamma>0\), the cubic term vanishes uniquely at \(\gamma_*=\sqrt3/2\). The corresponding \(A=\sqrt3-1\) gives the stated positive value \(\delta_*\). Substitution yields \(C_5(\gamma_*)=-3/10\). At tricriticality \(F(x)=-3x^5/10+O(x^7)\); by dividing the differential equation by \(x^5\), \(d(x^{-4})/dt=6/5+O(x^2)\). Every sufficiently small nonzero solution tends monotonically to zero, and integration gives \(x(t)^{-4}/t\to6/5\), the stated universal relaxation law.

**Fourth-root branch on the degenerate slice.** Holding \(\gamma=\gamma_*\), the analytic odd field admits \(F=xG(y,\mu,0)\) with \(y=x^2\). Because the local change from \(\delta\) to \(\mu\) is analytic, its Taylor expansion reads \(G(y,\mu,0)=\mu-(3/10)y^2+O(|\mu|y+ y^3)\). On a fixed small interval \(0\le y\le\epsilon\), strict concavity \(G_{yy}<0\) and the signs \(G(0)=\mu>0\), \(G(\epsilon)<0\) ensure a unique positive zero, even if \(G_y(0)\) is positive. At the root scale \(y\asymp\sqrt\mu\), one has \(G_y=-(3/5)y+O(|\mu|+y^2)<0\). The implicit-function theorem after scaling \(y=\sqrt\mu z\) proves the unique small positive root \(y=\sqrt{10\mu/3}(1+O(\sqrt\mu))\). At each nonzero root, \(F'(x)=2y\partial_yG<0\).

**Quadratic fold and five-state wedge.** Write \(\gamma=\gamma_*+\nu\) and solve the definition of \(\mu\) for \(\delta\):
\[\delta=1+\gamma^{-1}\log\!\left(\frac{2\gamma}{1+\mu}-1\right).\]
The analytic function \(G(y,\mu,\nu)\) now has expansion
\[G=\mu+b\nu y-c y^2+O(|\mu|y+\nu^2y+(|\mu|+|\nu|)y^2+y^3),\quad b=\frac{2\sqrt3}{3},\quad c=\frac3{10}.\]
In particular \(G_{yy}(0,0,0)=-3/5<0\). Scale \(y=\nu z\), \(\mu=\nu^2s\). The equations \(G=0\) and \(G_y=0\), divided by \(\nu^2\) and \(\nu\) respectively, extend analytically to \(\nu=0\) as
\[s+bz-cz^2=0,\qquad b-2cz=0.\]
The Jacobian with respect to \((s,z)\) is nonsingular. The implicit-function theorem produces a unique nearby fold with
\[z=\frac{b}{2c}=\frac{10\sqrt3}{9},\qquad s=-\frac{b^2}{4c}=-\frac{10}{9}\]
at leading order. Shrink a common fixed neighborhood \(0\le y<\epsilon\) so that \(G_{yy}<0\) throughout, and \(G(\epsilon,\mu,\nu)<0\). For every \(\mu\) strictly between the local fold and zero, \(G(0)=\mu<0\) while its unique positive maximum is positive: there are exactly two positive roots in the neighborhood, the first with \(G_y>0\), the second with \(G_y<0\). Oddness gives the four nonzero equilibria and the central zero. At zero \(F'(0)=\mu<0\); at the nonzero points \(F'=2yG_y\), establishing the announced alternating stability types. For \(\nu<0\) on the critical curve, the cubic is negative (continuous onset); for \(\nu>0\), it is positive (the subcritical side).

## Verification
The standalone file `verify.py` uses symbolic Taylor coefficients and arbitrary-precision root solving to check the exact cubic coefficient, cancellation of the cubic term, quintic coefficient \(-3/10\), unfolding coefficient \(2\sqrt3/3\), and numerical approach of fold ratios to \(10\sqrt3/9\) and \(-10/9\). Execute `python verify.py` with SymPy and mpmath installed. Computation corroborates the explicitly proved local expansions; it does not certify them independently or extend the local theorem globally.

## Relationship to prior work
Brooks, Chodrow and Porter (arXiv:2209.07004) introduced the logistic, or sigmoidal, bounded-confidence model and established the **linear** stability boundary of the central equilibrium for a fixed-zealot motif. The present work retains that model and known boundary, but resolves the nonlinear degeneracy on it: the uniquely vanishing cubic, the exact quintic coefficient, fourth-root polarization onset, quartic-time critical relaxation, and the quadratic-width local bistable wedge. These detailed coefficients are not implied by the linear boundary alone. Generic pitchfork/cusp arguments motivate the analysis but do not specify these constants for this confidence kernel.

## Limitations
This result concerns a single persuadable agent between two fixed zealots, not arbitrary opinion networks. The five-equilibrium statement counts only states in a fixed small neighborhood of the central zero, not any distant solutions; the asymptotic fold law holds only close to its degenerate point. Critical relaxation is deterministic and asymptotic, not a mixing-time or stochastic-noise result. The already-known linear stability curve is not claimed as new. Publication priority for specialized identical derivations remains subject to independent literature assessment.

## References
1. Brooks, H. Z., Chodrow, P. S. and Porter, M. A. *Emergence of polarization in a sigmoidal bounded-confidence model of opinion dynamics*. arXiv:2209.07004 (first posted 2022-09-15), https://arxiv.org/abs/2209.07004. In particular, original model equations and the symmetric competing-zealot linear stability theorem.
2. Franci, A., Srivastava, V. and Leonard, N. E. *A model-independent theory of consensus and dissensus decision making*. arXiv:1909.05765. Related general bifurcation viewpoint; distinct dynamical response equations.
3. Bizyaeva, A. et al. *Nonlinear Opinion Dynamics with Tunable Sensitivity*. arXiv:2009.04332. Related nonlinear-opinion mechanism; distinct equation family.
