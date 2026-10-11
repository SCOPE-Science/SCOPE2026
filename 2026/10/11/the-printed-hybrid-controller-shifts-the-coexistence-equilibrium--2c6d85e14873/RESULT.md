# The printed hybrid controller shifts the coexistence equilibrium and reverses the reported Hopf-threshold effect
## Finding
For the controlled predator–prey delay system printed as equations (4.1) and (7.2) by Ou et al., the parameter perturbation \(\alpha_1\neq1\) does not preserve the positive equilibrium of the uncontrolled model because the delayed state-feedback term vanishes at every constant state while \(\alpha_1\) rescales the prey-growth balance. At the paper's Example 7.2 parameters \(h_1=h_2=0.5\), \(a_1=a_2=2\), \(d_1=0.4\), \(b=0.1\), \(d=0.45\), \(\alpha_1=0.6\), and \(k=0.5\), the printed controlled system has the unique positive equilibrium \(E_c=(0.163263531322406646\ldots,0.264457676684001822\ldots)\), not the reported \(E=(0.1975,0.2674)\). Linearizing the printed system at \(E_c\) gives a first imaginary-axis crossing at \(\delta_c=2.96355390887214958\ldots\) with positive crossing speed, whereas the printed uncontrolled system has first crossing \(\delta_0=2.92415281225183456\ldots\). Thus the paper's reported controlled threshold \(\delta_\ast\approx2.85\) and its claim that this controller reduces the stability-delay interval do not describe the printed equations; for those equations the controller instead slightly enlarges the first linear-stability interval by \(0.0394010966203150\ldots\).

## Assumptions and scope
The calculation takes the differential-delay equations exactly as printed in Ou et al., equations (4.1) and (7.2), with all numerical parameters from Example 7.2. The claim concerns the positive coexistence equilibrium and the first **linear** characteristic-root crossing of those printed equations. It does not assess nonlinear Hopf direction, orbital stability of a bifurcating branch, or alternative controller formulas that were not printed.

For the controlled system, constant states make the feedback term \(k[u_1(t-\delta)-u_1(t)]\) vanish. Hence a positive equilibrium \(E_c=(x_c,y_c)\) satisfies
\[
\alpha_1(h_1-a_1x_c)=\frac{d_1y_c}{1+bx_c},\qquad
h_2-a_2y_c+\frac{dd_1x_c}{1+bx_c}=0.
\]

## Proof
The uncontrolled positive equilibrium \(E_0=(x_0,y_0)\) satisfies the same two equations with \(\alpha_1=1\). If a positive equilibrium were shared by the controlled and uncontrolled systems while \(\alpha_1\neq1\), subtraction of their first equilibrium equations would give \((\alpha_1-1)(h_1-a_1x_0)=0\). Thus \(h_1-a_1x_0=0\), and the uncontrolled first balance would then force \(y_0=0\), contradicting positivity. Therefore the assertion in Section 4 that the parameter-perturbed controlled system has the same positive equilibrium is false whenever \(\alpha_1\neq1\).

At the Example 7.2 parameters, eliminating \(y_c\) yields
\[
12x_c^3+237x_c^2+1186x_c-200=0,
\]
with
\[
y_c=\frac14+\frac{9x_c}{10(10+x_c)}.
\]
The cubic is negative at \(x_c=0\), positive at \(x_c=1\), and has strictly positive derivative for \(x_c>0\), so it has exactly one positive root. Numerically,
\[
E_c=(0.163263531322406646\ldots,0.264457676684001822\ldots).
\]
By contrast, the uncontrolled positive equilibrium is
\[
E_0=(0.197549162365241034\ldots,0.267434997693845779\ldots).
\]
Substitution of \(E_0\) into the first controlled equation gives residual \(-0.00828929523208151522\ldots\), while the second residual is zero, so the reported point is not even a constant solution of the printed controlled system.

At \(E_c\), write
\[
\Delta(\lambda,\delta)=(\lambda-c_1-kE)(\lambda+c_5E)+c_2c_3,
\qquad E=e^{-\lambda\delta},
\]
where
\[
 c_1=\alpha_1h_1-2\alpha_1a_1x_c-\frac{d_1y_c}{(1+bx_c)^2}-k,
\]
\[
 c_2=\frac{d_1x_c}{1+bx_c},\qquad
 c_3=\frac{dd_1y_c}{(1+bx_c)^2},\qquad
 c_5=a_2y_c.
\]
At \(\delta=0\), the two characteristic roots are approximately \(-0.20333972\) and \(-0.51981986\), so the corrected equilibrium is initially linearly stable.

For an imaginary root \(\lambda=i\omega\), set \(z=\omega^2\) and \(\theta=\omega\delta\). Multiplication by \(e^{i\theta}\) makes the real and imaginary parts linear in \(\cos\theta\) and \(\sin\theta\). Eliminating those two trigonometric quantities and imposing \(\cos^2\theta+\sin^2\theta=1\) gives
\[
H(z)=-z^4-0.951268908236266024\ldots z^3+0.048905671702565674\ldots z^2
+0.0673068448228945203\ldots z+0.00475223555969860554\ldots.
\]
Its descending coefficient signs are \(-,-,+,+,+\), so Descartes' rule gives at most one positive root. Since \(H(0)>0\) and \(H(1)<0\), there is exactly one positive root,
\[
z_c=0.281841752700586256\ldots,
\qquad \omega_c=0.530887702532829667\ldots.
\]
Recovering the phase gives the least positive crossing delay
\[
\delta_c=2.96355390887214958\ldots.
\]
Implicit differentiation of \(\Delta(\lambda,\delta)=0\) gives
\[
\operatorname{Re}\left(\frac{d\lambda}{d\delta}\right)
=0.0808341228563103542\ldots>0
\]
at this crossing. Because there is no earlier positive imaginary frequency and \(\lambda=0\) is not a root, this is the first loss of linear stability of the corrected controlled equilibrium.

Repeating the same characteristic calculation for the printed uncontrolled system gives its first crossing
\[
\delta_0=2.92415281225183456\ldots.
\]
Therefore \(\delta_c-\delta_0=0.0394010966203150\ldots>0\): the printed controller enlarges, rather than reduces, the first stability-delay interval.

## Verification
`VERIFY.py` reconstructs both positive equilibria from the printed parameters, checks that the controlled equilibrium cubic has a unique positive root, evaluates the controlled residual at the paper's reported point, reconstructs the controlled characteristic equation, derives the quartic frequency condition, checks its coefficient-sign pattern and positive-root bracket, recovers the first phase-compatible delay, verifies transversality, and independently recomputes the uncontrolled first crossing. Running the script prints `VERIFY_OK` only after all assertions pass.

## Relationship to prior work
Ou et al. explicitly state that system (4.1) has the same equilibrium as system (1.2), and Example 7.2 again states that system (7.2) has the positive equilibrium \(E(0.1975,0.2674)\), reports \(\delta_\ast\approx2.85\), and interprets the controller as reducing the stability region. The correction above follows from the printed controller itself: the state-feedback difference vanishes at equilibrium, but the multiplicative factor \(\alpha_1\) does not. Searches for the DOI, title, numerical equilibrium, and threshold found the original article and mirrors but no published correction or erratum containing the corrected equilibrium or crossing value.

## Limitations
The first-crossing calculation concerns linear local stability of the corrected positive equilibrium. It does not establish the direction or nonlinear stability of any Hopf branch. The numerical values are high-precision evaluations of algebraic and transcendental equations derived from the printed coefficients; the equilibrium non-preservation argument itself is exact. A non-indexed correction or later author note could exist and would supersede the literature-status assessment, but none was found in the sources checked.

## References
1. W. Ou, C. Xu, Q. Cui, Y. Pang, Z. Liu, J. Shen, M. Z. Baber, M. Farman, S. Ahmad, “Hopf bifurcation exploration and control technique in a predator-prey system incorporating delay,” *AIMS Mathematics* 9(1), 1622–1651, DOI 10.3934/math.2024080. Published 13 December 2023. Equations (4.1), (7.2), and Example 7.2.
