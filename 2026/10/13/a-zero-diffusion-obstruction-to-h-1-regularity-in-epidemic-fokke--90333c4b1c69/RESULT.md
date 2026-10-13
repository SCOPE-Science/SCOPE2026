# A zero-diffusion obstruction to \(H^1\) regularity in epidemic Fokker–Planck control

## Finding
In equation (6) of Parkinson and Roy [1], the regularity conclusion of Proposition 2.1 is false under its explicit hypotheses. There are smooth admissible drift and diffusion coefficients, a bounded positively invariant state rectangle, a bounded zero control, and a normalized nonnegative initial density in \(L^2\), such that the unique distributional solution remains outside \(H^1(\Omega)\) at **every** positive finite time. Consequently it does not belong to \(L^2(0,T;H^1(\Omega))\) for any \(T>0\).

The obstruction is a sharp distinction between transport and diffusion: when the declared diffusion coefficients vanish, smooth deterministic characteristics propagate jumps without regularizing them. Only the unrestricted regularity assertion for the printed forward equation is disproved; mass conservation and nonnegativity continue to hold.

## Assumptions and scope
Let \(\Omega=(0,2)^2\), let \(T>0\) be arbitrary, and take the source equation (6) with parameters \(b=\delta=\gamma=1\), \(\beta=1/10\), and constant control \((\alpha,\eta,v)=(0,0,0)\). The two noise amplitudes are exactly \(\sigma_S=\sigma_I=0\). The dynamics are therefore the continuity equation
\[
\partial_t f+\nabla\cdot(Ff)=0,\qquad F(S,I)=\left(1-S-\frac{SI}{10},\left(\frac S{10}-2\right)I\right).
\]
The no-flux boundary condition in source equation (6) is imposed. Set \(Q=(1/5,2/5)^2\) and \(f_0=25\mathbf1_Q\). Since \(|Q|=1/25\), this is a nonnegative normalized probability density and belongs to \(L^2(\Omega)\), with \(\|f_0\|_2=5\). Its support lies within the physically plausible simplex \(S\ge0\), \(I\ge0\), \(S+I\le1\). All coefficient regularity, boundedness, and the explicit noise-ratio hypotheses of [1] hold, because the noise coefficients vanish identically. Zero control belongs to the source's bounded-variation admissible set.

## Proof
**1. A legitimate invariant domain.** Along the four sides of the closed square \([0,2]^2\), the outward normal components are respectively \(-1\) at \(S=0\), \(-1-I/5\le-1\) at \(S=2\), \(0\) at \(I=0\), and \(2(S/10-2)\le-18/5\) at \(I=2\). Therefore the smooth ODE preserves \([0,2]^2\) forward. The solution of \(\dot I=(S/10-2)I\) with initial \(I>0\) has \(I(t)>0\) at all finite times. Similarly \(\dot S\big|_{S=0}=1\), so a solution starting with \(S>0\) cannot meet \(S=0\) at a finite positive time; upper sides are strictly inward. Thus for each finite \(t\), the image of the compact closure \(\overline Q\) under the smooth ODE flow \(\Phi_t\) remains a compact subset of \(\Omega\). For additional physical interpretation, along \(S+I=1\), \(\dot S+\dot I=1-S-2I=-I\le0\); the epidemic simplex \(S\ge0, I\ge0, S+I\le1\) is forward invariant.

**2. The exact distributional solution.** As \(F\) is smooth, it generates a local \(C^1\) invertible characteristic flow along \(\overline Q\). Differentiation of the flow gives the Jacobian identity
\[
J_t(y)=\det D\Phi_t(y)=\exp\!\left(\int_0^t\nabla\cdot F(\Phi_s(y))\,ds\right)>0,
\qquad \nabla\cdot F(S,I)=-3+\frac{S-I}{10}.
\]
Define
\[
f(t,\Phi_t(y))=\frac{25}{J_t(y)}\quad(y\in Q),\qquad
f(t,x)=0\quad\text{for }x\notin\Phi_t(Q).
\]
It is the push-forward of \(f_0\) by \(\Phi_t\), hence solves the displayed continuity equation in distributions. Its density is compactly supported in the interior of \(\Omega\) on each bounded time interval and therefore satisfies zero boundary flux. The change-of-variables formula proves positivity and total mass one. There is no competing distributional solution: along smooth Lipschitz characteristics, pulling back the signed-measure solution and multiplying by the positive Jacobian gives a time-constant distribution, which equals \(f_0\). Equivalently, testing the weak equation against backwards transported smooth test functions proves uniqueness.

**3. No Sobolev smoothing.** For every finite \(t>0\), \(\Phi_t\) maps each open side of \(Q\) onto a smooth embedded curve strictly inside \(\Omega\). The trace from the interior of \(\Phi_t(Q)\) is \(25/J_t(y)>0\), whereas the exterior trace is zero. The distributional gradient of \(f(t,\cdot)\) therefore has a nonzero surface-measure term on the curve. For example, by integration by parts on the two sides of one transported face, its normal component equals its positive jump times one-dimensional arc length, which is singular with respect to two-dimensional Lebesgue measure. An \(H^1\) function has a distributional gradient given by an \(L^2\) function and cannot have this singular component. Therefore \(f(t)\notin H^1(\Omega)\) for every finite \(t>0\). In particular the asserted class \(L^2(0,T;H^1(\Omega))\) is impossible for every \(T>0\). This contradicts exactly the \(H^1\) portion of Proposition 2.1 under its declared assumptions.

## Verification
The standalone \(\texttt{verify.py}\) checks with exact rational arithmetic the zero-control drift, all four inward/tangent boundary inequalities, the invariant epidemic simplex, the initial total mass, the \(L^2\) squared norm, and the divergence. These checks support the hypotheses and algebra; the all-time non-\(H^1\) conclusion follows analytically from the nonzero transported jump and cannot be inferred from any finite numerical test. Run \(\texttt{python3 verify.py}\) from the extracted artifact folder and expect \(\texttt{VERIFY_OK}\).

## Relationship to prior work
Reference [1], equations (4)–(7) and Proposition 2.1, is the exact object and target: its statement assumes spatial \(C^2\) regularity of the squared noise amplitudes but contains no strict positive lower ellipticity bound. Its Section 3 uses the asserted \(L^2(0,T;H^1)\) control-to-state framework and Aubin–Lions compactness. References [2] and [3] develop characteristic/transport-flow theory: preservation of discontinuities by smooth invertible flows is standard, and is **not** claimed as a new theorem of transport theory. The new statement here is an explicit admissible epidemic-model counterexample to a specific published regularity guarantee, verified against the full public source. It does not reproduce or entail separate questions of stochastic-noise covariance or alternate divergence-form coefficient identities.

## Limitations
The counterexample uses allowed degenerate (zero) noise and deliberately discontinuous \(L^2\) initial data. It does not show failure under uniformly positive diffusion, nor assert that no distributional density exists, nor contradict numerical examples with positive noise. It also does not by itself prove that no optimal control exists; rather, the paper's unrestricted \(H^1\)-based control-to-state justification does not cover this admissible case. An additional uniform ellipticity assumption or a transport-compatible function-space theory may give a valid restricted theorem. Literature-index incompleteness remains a risk for exact-model antecedents.

## References
[1] C. Parkinson and S. Roy, *A Fokker-Planck Framework for Control of Epidemics*, arXiv:2601.20181, version 3 (1 July 2026), Sections 2–3, especially equations (4)–(7), Proposition 2.1, and Theorem 3.1; *Journal of Mathematical Biology* **93**, article 47 (16 September 2026), DOI: 10.1007/s00285-026-02462-7. First publicly submitted 28 January 2026.

[2] P. Bonicatto, G. Del Nin, and F. Rindler, *Existence and uniqueness for the transport of currents by Lipschitz vector fields*, arXiv:2303.03218 (2023); used only as background on uniqueness of Lipschitz transport flows.

[3] P.-L. Lions and B. Seeger, *Transport equations and flows with one-sided Lipschitz velocity fields*, arXiv:2306.13288 (2023); used as broader transport-theory context, not as an exact-model precedent.
