# Exact critical relaxation and logarithmic signatures in a payoff-reversal evolutionary game

## Finding

Consider the one-dimensional feedback-replicator dynamics introduced by Chen, Zhang, and Li [1], in the exact deterministic well-mixed form
\[
\dot x=x(1-x)(2x-1)\bigl[a+(b-a)x\bigr],\qquad a=S-P,\quad b=R-T,
\]
where \(x\in[0,1]\) is the cooperation fraction and \(R,S,T,P\in\mathbb R\) are constant payoff entries. The entire nonhyperbolic locus in the two effective payoff differences consists of the three lines \(a=0\), \(b=0\), and \(a+b=0\). Except at their common intersection \(a=b=0\), each line has exactly one coalescing double equilibrium. On precisely the attracting sides specified below, the solutions have exact critical relaxation laws.

**Endpoint collisions.** If \(a=0,b>0\), every initial \(x_0\in(0,1/2)\) approaches \(0\). If \(b=0,a>0\), every initial \(x_0\in(1/2,1)\) approaches \(1\). In either case let \(u(t)\) be the distance from the attracting endpoint (respectively \(x(t)\) or \(1-x(t)\)), let \(c=b\) or \(c=a\), and set \(z(t)=1/u(t)>2\). Then the *exact* time law is
\[
 F(z(t))=ct+F(z_0),\qquad F(z)=z-\log(z-1)+4\log(z-2),
\]
and the sharp two-term asymptotic is
\[
 \frac{1}{u(t)}=ct-3\log(ct)+F(z_0)+o(1).
\]
In particular \(t\,u(t)\to1/c\); the reciprocal distance has a universal nonzero logarithmic correction.

**Interior collision.** Suppose \(a+b=0\) and \(a\ne0\). When \(a>0\), every initial \(x_0\in(1/2,1)\) approaches \(1/2\); when \(a<0\), every initial \(x_0\in(0,1/2)\) approaches \(1/2\). Define \(u(t)=|x(t)-1/2|\), \(c=|a|\), and \(z(t)=1/u(t)>2\). Then
\[
 G(z(t))=ct+G(z_0),\qquad G(z)=z+\log\!\left(\frac{z-2}{z+2}\right),
\]
and
\[
 \frac{1}{u(t)}=ct+G(z_0)+o(1).
\]
Again \(t\,u(t)\to1/c\), but **the logarithmic correction is absent**. At \(a=b=0\), the vector field vanishes identically and every cooperation fraction is a stationary state.

## Assumptions and scope

The stated conclusions concern the deterministic autonomous scalar replicator equation above, not finite-population randomness, spatial lattice simulations, delayed environmental dynamics, or strategies outside \([0,1]\). The payoff entries are real constants; no positivity or payoff ordering is needed for the mathematics. The displayed asymptotic statements apply **only** to strictly interior initial data in the indicated one-sided basins, with the corresponding nonzero critical payoff difference. Values at the fixed points remain stationary, and trajectories on the opposite side of a double equilibrium have a different limiting equilibrium. No claim of exponential critical attraction is made.

The source [1] defines the time-varying payoff matrix and derives this exact scalar equation (its Eqs. (1), (4), and (7)); its critical stability analysis identifies two payoff-driven collisions, with \(S=P\) mentioned as a degenerate condition. The new claim is the complete critical one-sided *time law*, its logarithmic dichotomy, and the simultaneous-degeneracy behavior, rather than discovery of the original model or its equilibrium locations.

## Proof

**1. Recovery of the equation from the payoffs.** The source matrix is
\[
 U(x)=(1-x)\begin{pmatrix}T&P\\R&S\end{pmatrix}
      +x\begin{pmatrix}R&S\\T&P\end{pmatrix}.
\]
Writing the expected cooperation and defection payoffs as \(\Pi_C=xU_{CC}+(1-x)U_{CD}\) and \(\Pi_D=xU_{DC}+(1-x)U_{DD}\), direct subtraction gives
\[
 \Pi_C-\Pi_D=(2x-1)\bigl[(S-P)+x(R-T-S+P)\bigr].
\]
Multiplication by \(x(1-x)\) recovers the asserted drift exactly.

**2. Exhaustive nonhyperbolic locus.** The equilibria \(0\), \(1\), and \(1/2\) exist for all parameters. Their derivatives are, respectively,
\[
 f'(0)=-a,\qquad f'(1)=-b,\qquad f'(1/2)=\frac{a+b}{4}.
\]
Any fourth equilibrium must be a zero of the affine bracket \(a+(b-a)x\). Away from \(a=b=0\) it is simple unless it coincides with one of these three equilibria, which occurs precisely on the corresponding lines. Thus there are no other nonhyperbolic cases in \([0,1]\). If \(a=b=0\), every factor from the payoff bracket vanishes and \(f\equiv0\).

**3. Exact endpoint normal form.** On \(a=0,b=c>0\), set \(u=x\) for an initial point below \(1/2\). On \(b=0,a=c>0\), instead set \(u=1-x\) for an initial point above \(1/2\). In both cases substitution gives the *same* positive-distance differential equation
\[
 \dot u=-c\,u^2(1-u)(1-2u),\qquad 0<u<1/2.
\]
Its right side is strictly negative. Uniqueness and boundedness of scalar solutions imply global existence, no crossing of the endpoints, and monotone convergence to \(u=0\) (the only equilibrium in \([0,u_0]\)). For \(z=1/u>2\),
\[
 \dot z=c\left(1-\frac1z\right)\left(1-\frac2z\right),
 \qquad F'(z)=\frac{z^2}{(z-1)(z-2)}.
\]
Consequently \(\frac{d}{dt}F(z(t))=c\), proving the exact time identity. As \(z\to\infty\),
\[
 F(z)=z+3\log z+O(z^{-1}).
\]
The exact relation implies \(z/(ct)\to1\). Therefore replacing \(\log z\) by \(\log(ct)+o(1)\) yields
\[
 z-ct+3\log(ct)\longrightarrow F(z_0).
\]
This proves both the endpoint coefficient and the nonvanishing logarithmic term.

**4. Exact interior normal form.** On \(b=-a\ne0\), the drift reduces to
\[
 f(x)=-a\,x(1-x)(2x-1)^2.
\]
If \(a>0\) the drift is negative and every point above \(1/2\) decreases to it; if \(a<0\) the drift is positive and every point below \(1/2\) increases to it. With \(u=|x-1/2|\) the equation in either attracting basin is
\[
 \dot u=-c\,u^2(1-4u^2),\qquad 0<u<1/2,
\]
where \(c=|a|\). Hence
\[
 \dot z=c\left(1-\frac4{z^2}\right),\qquad G'(z)=\frac{z^2}{z^2-4}.
\]
Integration gives the exact \(G\)-identity. Since
\[
 G(z)=z-\frac4z+O(z^{-3}),
\]
we have \(z-ct\to G(z_0)\), with no possible logarithmic term. The positivity of the transformed derivative proves global convergence and excludes finite-time arrival at the equilibrium.

**5. Other one-sided data.** Each nonzero critical-line drift has a fixed sign on each connected component of the complement of the three permanent fixed points, so trajectories on the opposite side of the double root proceed monotonically toward the next fixed point. They do not exhibit the stated double-root attraction. This completes the exhaustive critical classification, including the simultaneous intersection.

## Verification

The complete standalone file `check_critical.py` uses only the Python standard library. Run `python3 check_critical.py`. It reconstructs the drift from the original payoff matrix for thousands of rational parameter choices, checks the three critical substitutions and the two antiderivative identities over exact rational values, compares the resulting implicit solutions with independent fourth-order Runge–Kutta integration, and checks quantitative asymptotic residuals over increasing times. The program reported **12,859 passing checks**. The infinite-time conclusions are proved in the preceding exact argument; finite computations alone would not establish them.

The asymptotic logarithm is taken of the dimensionless positive quantity \(ct\). No universal finite-time error estimate is asserted for initial conditions approaching a repelling equilibrium or for parameters approaching the codimension-two frozen state.

## Relationship to prior work

Chen, Zhang, and Li [1], first publicly posted 2026-10-15, introduce the payoff-reversal model, its scalar replicator and equilibrium/bifurcation diagrams. Their discussion through the conclusions treats fixed-point positions, signs of linearization, and transcritical thresholds, without the exact critical-time identities or the endpoint-versus-interior logarithmic distinction above. It also does not supply the complete one-sided time law on the special \(S=P\) line. Thus the new analysis is an additional model-specific quantitative result, **not** a new general transcritical-bifurcation method.

Ito and Yamamichi [2] classify a different environmental-feedback game in which an independent environmental-resource coordinate evolves. Their two-dimensional system is not the instantaneous payoff-reversal scalar equation here and neither specifies nor implies these particular time constants. General one-dimensional separable-ODE techniques explain *how* the present proof works, but do not themselves state the model's triple critical locus and its two different sharp corrections.

## Limitations

The result gives deterministic critical one-sided asymptotics for the specified payoff-reversal model only. It does not extend to stochastic imitation, networked play, dynamically lagged environmental resources, or finite-size deviations from mean field. Its leading \(t^{-1}\) decay is consistent with generic one-dimensional nonhyperbolic behavior; the model-specific contribution is the exhaustive critical-line classification, exact quadratures, and distinct subleading logarithmic terms. No independent scientific audit has yet been performed. Possible overlap with unindexed work on scalar payoff-feedback normal forms remains a publication-priority risk.

## References

[1] Y. Chen, J.-Q. Zhang, B.-Q. Li, *Cooperation Dynamics with Environmental Feedback: Steady States and Transitions*, arXiv:2610.21575, version 1 publicly posted 2026-10-15. https://arxiv.org/abs/2610.21575

[2] H. Ito and M. Yamamichi, *A complete classification of evolutionary games with environmental feedback*, PNAS Nexus 3 (2024), pgae455, DOI:10.1093/pnasnexus/pgae455. https://doi.org/10.1093/pnasnexus/pgae455
