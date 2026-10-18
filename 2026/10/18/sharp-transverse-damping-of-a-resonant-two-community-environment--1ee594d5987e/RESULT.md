# Sharp transverse damping of a resonant two-community environmental-feedback game

## Finding

In an admissible five-variable eco-evolutionary two-community game with balanced within- and between-community encounters, there is a one-parameter curve of fully interior coexistence equilibria. **Its transverse spectrum is strictly stable if and only if the two communities have different environmental feedback response parameters.** When the response parameters are equal, every point instead has a simple zero eigenvalue, one nonzero imaginary conjugate pair, and two eigenvalues of negative real part. In the strictly stable case, every sufficiently close trajectory converges exponentially to the unique equilibrium selected by its conserved environmental log-odds balance. The existence of resonant equilibrium continua and the log-odds conservation relation are background ingredients, not novelty claims; the sharp all-parameter transverse classification and local convergence statement are the findings.

## Assumptions and scope

Fix real parameters \(0<B<A<C\) and \(L>C+B\). For environmental condition \(n\in[0,1]\), consider the two-strategy payoff interpolation between
\[
A_0=\begin{pmatrix}L+A-B&L+A\\L&L\end{pmatrix},\qquad
A_1=\begin{pmatrix}L+A-B-C&L+A-C\\L&L\end{pmatrix}.
\]
Cooperation strictly dominates at \(n=0\) and defection strictly dominates at \(n=1\). The cooperator-minus-defector expected payoff against a fraction \(p\) of cooperators at environmental condition \(n\) is \(G(n,p)=A-Bp-Cn\).

Let \(x,y\in(0,1)\) be cooperation fractions in two equal communities, and let \(n_1,n_2,n_{12}\in(0,1)\) be their within- and cross-community environmental conditions. At encounter mixing \(\delta=1/2\), the exact five-dimensional system is
\[
\begin{aligned}
\dot x&=x(1-x)\left(A-\tfrac B2(x+y)-\tfrac C2(n_1+n_{12})\right),\\
\dot y&=y(1-y)\left(A-\tfrac B2(x+y)-\tfrac C2(n_2+n_{12})\right),\\
\dot n_1&=n_1(1-n_1)((1+\theta_1)x-1),\\
\dot n_2&=n_2(1-n_2)((1+\theta_2)y-1),\\
\dot n_{12}&=n_{12}(1-n_{12})\left((1+\theta_{12})\tfrac{x+y}{2}-1\right).
\end{aligned}
\]
Take arbitrary \(\theta_1,\theta_2>0\), put \(x_*=1/(1+\theta_1)\) and \(y_*=1/(1+\theta_2)\), and impose the environmental **resonance** \(\theta_{12}=2/(x_*+y_*)-1>0\). Define
\[
\kappa=\frac{2A-B(x_*+y_*)}{C},\qquad
I=(\max\{0,\kappa-1\},\min\{1,\kappa\}).
\]
The parameter inequalities give \(0<\kappa<2\), so \(I\) is a nonempty open interval.

Every equilibrium with all five coordinates strictly between zero and one is exactly
\[
E_s=(x_*,y_*,\kappa-s,\kappa-s,s),\qquad s\in I.
\]
At each \(E_s\), the Jacobian has a simple zero eigenvalue tangent to this equilibrium segment. If \(\theta_1\ne\theta_2\), its other four eigenvalues have strictly negative real parts. If \(\theta_1=\theta_2\), its other four eigenvalues consist of a purely imaginary conjugate pair and a pair with strictly negative real parts. The equal-response case is a sharp failure of normal exponential attraction, not a claim about nonlinear periodic orbits.

For \(\theta_1\ne\theta_2\), every compact subsegment of the equilibrium curve has a neighborhood in which trajectories starting sufficiently close to its interior are attracted exponentially to a **single** equilibrium. The limiting point is uniquely determined by the initial value of
\[
H=\operatorname{logit}(n_{12})-\frac{x_*}{x_*+y_*}\operatorname{logit}(n_1)-\frac{y_*}{x_*+y_*}\operatorname{logit}(n_2),
\]
where \(\operatorname{logit}(z)=\log(z/(1-z))\). This local statement does not assert global attraction from the open cube.

## Proof

**All interior equilibria.** Because none of the environmental logistic factors vanishes in the open cube, the three environmental equations force \(x=x_*\), \(y=y_*\), and the given resonance. The first two strategy equations then respectively force \(n_1+n_{12}=\kappa\) and \(n_2+n_{12}=\kappa\). Writing \(s=n_{12}\) yields the stated segment and its exact admissible interval. Conversely, direct substitution makes all five derivatives zero.

**Exact spectrum.** Fix \(s\in I\), and abbreviate the positive quantities
\[
\begin{gathered}
p=x_*(1-x_*),\quad q=y_*(1-y_*),\quad
w=(\kappa-s)(1-\kappa+s),\quad v=s(1-s),\\
\alpha=B/2,\quad\beta=C/2,\quad
u=w/x_*,\quad r=w/y_*,\quad t=v/(x_*+y_*).
\end{gathered}
\]
Linearization in coordinate order \((x,y,n_1,n_2,n_{12})\) gives
\[
J_s=\begin{pmatrix}
-\alpha p&-\alpha p&-\beta p&0&-\beta p\\
-\alpha q&-\alpha q&0&-\beta q&-\beta q\\
 u&0&0&0&0\\0&r&0&0&0\\ t&t&0&0&0
\end{pmatrix}.
\]
Eliminating the three environmental perturbations at nonzero spectral parameter, or computing the determinant directly, yields \(\det(\lambda I-J_s)=\lambda P_4(\lambda)\), where
\[
\begin{aligned}
P_4(\lambda)&=\lambda^4+a_3\lambda^3+a_2\lambda^2+a_1\lambda+a_0,\\
a_3&=\alpha(p+q),\\
a_2&=\beta[p(u+t)+q(r+t)],\\
a_1&=\alpha\beta pq(u+r),\\
a_0&=\beta^2pq[ur+t(u+r)].
\end{aligned}
\]
All four coefficients are positive. The two nontrivial quartic Routh–Hurwitz differences are exactly
\[
a_3a_2-a_1=\alpha\beta\big[p^2u+q^2r+(p+q)^2t\big]>0
\]
and
\[
\begin{aligned}
a_3a_2a_1-a_1^2-a_3^2a_0
&=\alpha^2\beta^2pq(pu-qr)^2\\
&=\alpha^2\beta^2pq\,w^2(x_*-y_*)^2.
\end{aligned}
\]
The quartic Routh–Hurwitz theorem now says that all four roots lie in the open left half-plane **if and only if** \(x_*\ne y_*\), equivalently \(\theta_1\ne\theta_2\). Because \(a_0>0\), the fifth eigenvalue \(0\) is simple.

**Sharp equality case.** If \(x_*=y_*\), then \(p=q\) and \(u=r\), and the quartic factors exactly as
\[
P_4(\lambda)=
\left(\lambda^2+2\alpha p\lambda+\beta p(u+2t)\right)
\left(\lambda^2+\beta pu\right).
\]
The first factor is strictly Hurwitz and the second gives the nonzero imaginary pair \(\lambda=\pm i\sqrt{\beta pu}\).

**Selection of the attracting equilibrium.** Differentiation using the three environmental equations shows \(dH/dt=0\) exactly. On the equilibrium segment,
\[
H(E_s)=\operatorname{logit}(s)-\operatorname{logit}(\kappa-s),
\quad \frac{dH(E_s)}{ds}=\frac1{s(1-s)}+\frac1{(\kappa-s)(1-\kappa+s)}>0.
\]
The function \(H(E_s)\) maps \(I\) onto \(\mathbb R\). For distinct feedback responses, compact portions of the equilibrium segment are normally hyperbolic attracting one-dimensional manifolds, by the simple tangent eigenvalue and four strictly stable transverse eigenvalues. The standard local stable-foliation theorem for a compact normally attracting segment (or its local extension inside the full smooth equilibrium curve) gives exponential convergence to a point of that segment for all sufficiently nearby initial conditions. Conservation of \(H\) and its strict monotonicity there identify the point uniquely.

**Admissible example.** Take \(A=2\), \(B=1\), \(C=3\), \(L=5\), \(\theta_1=1\), \(\theta_2=3\), and \(\theta_{12}=5/3\). Then \(x_*=1/2\), \(y_*=1/4\), \(\kappa=13/12\), and \(s=1/2\) gives the full-interior equilibrium \((1/2,1/4,7/12,7/12,1/2)\). Its nonzero characteristic factor is exactly
\[
P_4(\lambda)=\frac{24576\lambda^4+5376\lambda^3+16576\lambda^2+1260\lambda+2485}{24576},
\]
whose roots are strictly stable by the inequalities above. Both endpoint matrices have strictly positive entries and satisfy the source model's dominance assumptions.

## Verification

The standalone file `verification.py` uses Python, SymPy, and NumPy. Running `python verification.py` checks the five equilibrium equations; the log-odds derivative; each of the 25 Jacobian entries; the independent reduced characteristic determinant; the two exact quartic Routh–Hurwitz factorizations; and the equal-response spectral factorization. It also constructs 27 independent finite rational five-dimensional Jacobians and compares their directly computed characteristic polynomials to the general formula, with numerical eigenvalue-sign checks in the asymmetric cases. These checks passed when run against the supplied source file. The argument above, not this finite sample, proves the unrestricted parameter result.

## Relationship to prior work

Betz, Fu, and Masuda [1] introduce the five-variable two-community edge-environment model, develop analytical stability classifications for lower-dimensional symmetry reductions, and numerically investigate its general dynamics. Their inspected five-dimensional section and Appendix G do not give the resonant affine-payoff quartic Routh–Hurwitz identity or its sharp feedback-asymmetry criterion. Resonant environmental invariants and equilibrium continua are not claimed as novel here. Wang, Zheng, and Fu [2] study stable manifold segments in a *different* environmental-feedback public-goods game with lower-dimensional state and nonlinear selection; its assertions do not imply this particular five-variable spectral threshold. General two-dimensional environmental-feedback game results in [3] likewise do not directly give the mixed-edge transverse polynomial. Existing general normal-hyperbolicity theory is used as an implication, not claimed as original.

## Limitations

Only interior equilibria of the displayed affine-payoff, balanced-mixing, resonant subfamily are classified. Parameter conditions exclude zero feedback slopes and corner states. The exponential convergence result is local, not global, and does not establish attractivity of the whole open equilibrium segment from arbitrary initial states. At equal community feedback parameters the linearization has an imaginary pair; whether nonlinear nearby solutions are periodic or attracted requires separate analysis. Publication priority remains subject to independent literature assessment, including possible implications of more general spectral theorems.

## References

[1] K. Betz, F. Fu, N. Masuda, *Evolutionary game dynamics with environmental feedback in a network with two communities*, arXiv:2404.17082 (first publicly posted April 25, 2024), Bulletin of Mathematical Biology 86, 84 (2024). https://arxiv.org/html/2404.17082v2

[2] X. Wang, Z. Zheng, F. Fu, *Steering Eco-Evolutionary Games Dynamics with Manifold Control*, arXiv:1906.07161 (2019). https://arxiv.org/abs/1906.07161

[3] A. R. Tilman et al., *Evolutionary games with environmental feedbacks*, Nature Communications 11 (2020). https://doi.org/10.1038/s41467-020-14531-6
