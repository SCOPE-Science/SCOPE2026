# Exact population conservation and the sharp pointwise-closure boundary in spatial SIR
## Finding
For the spatial SIR systems in Wang and Echkina, take the displayed normalization \(\tau_S=\tau_I=\tau_R=1\), a rectangular domain \(\Omega=(0,L_x)\times(0,L_y)\), classical solutions, positive \(I\) for the unregularized chemotactic flux, and homogeneous Neumann data. Then the spatially integrated population
\[
M(t)=\int_\Omega (S+I+R)\,dx
\]
is conserved. By contrast,
\[
\frac{d}{dt}\int_\Omega S\,dx=-\int_\Omega \frac{\beta SI}{N}\,dx,
\]
so susceptible mass decreases strictly whenever \(SI\) is positive on a set of positive measure.

There is also a sharp distinction between integrated conservation and the stronger pointwise closure \(S+I+R\equiv N_0\). For the reaction-diffusion system without chemotaxis, that constant-sum manifold is invariant for every smooth positive initial triple having the sum \(N_0\) if and only if
\[
D_S=D_I=D_R.
\]
For the chemotactic system, the corresponding universal invariance holds if and only if
\[
D_S=D_I=D_R\quad\text{and}\quad\chi=0.
\]
Thus unequal compartment diffusion or a nonzero fear/avoidance flux generically destroys the ODE-style pointwise constant-population closure even though total integrated population is still conserved.

## Assumptions and scope
The claim concerns exactly the PDE forms printed in arXiv:2608.15164v1 after the paper sets \(\tau_(\cdot)=1\). The domain is rectangular and boundary conditions are homogeneous Neumann. For the chemotactic identity, \(I>0\) is assumed so that \(\nabla\log I\) is classical; the same integrated-flux conclusion applies to a conservative regularization when its boundary normal flux vanishes. The result is about the continuous PDE, not the paper's time-discrete IMEX implementation.

The universal pointwise-invariance statement quantifies over all smooth positive initial triples satisfying \(S_0+I_0+R_0=N_0\) pointwise and the Neumann compatibility conditions. It does not claim that no special nonconstant solution can preserve the sum when the coefficient criterion fails.

## Proof
Write \(n=S+I+R\). In the reaction-diffusion system, the infection and recovery reactions cancel exactly after summing the three equations, leaving
\[
n_t=D_S\Delta S+D_I\Delta I+D_R\Delta R.
\]
In the chemotactic system the same cancellation gives
\[
n_t=D_S\Delta S+D_I\Delta I+D_R\Delta R+\chi\,\nabla\!\cdot(S\nabla\log I).
\]
Integrating either identity over \(\Omega\), the three Laplacians have zero integral by the Neumann conditions. In the chemotactic term, the boundary flux is \(S\,\partial_n I/I\), which also vanishes. Hence \(M'(t)=0\).

Integrating the susceptible equation alone instead gives
\[
\frac{d}{dt}\int_\Omega S\,dx=-\int_\Omega \frac{\beta SI}{N}\,dx,
\]
because the diffusive and chemotactic divergences integrate to zero. This derivative is strictly negative whenever \(\beta>0\), \(N>0\), and \(SI>0\) on a set of positive measure.

For sufficiency of the pointwise criterion without chemotaxis, if \(D_S=D_I=D_R=D\), then \(n_t=D\Delta n\). Constant initial data \(n(0,\cdot)=N_0\) with Neumann boundary conditions therefore remain constant.

For necessity, let \(k=\pi/L_x\) and choose, for sufficiently small \(0<\varepsilon<1\),
\[
S_0=1+\varepsilon\cos(kx),\qquad I_0=1-\varepsilon\cos(kx),\qquad R_0=1.
\]
The sum is identically \(3\), all components are positive, and the Neumann conditions hold. At time zero,
\[
n_t=\varepsilon k^2(D_I-D_S)\cos(kx).
\]
Universal invariance therefore forces \(D_I=D_S\). Cycling the same zero-sum perturbation through the compartment pairs forces all three diffusion coefficients to agree.

For the chemotactic model, universal invariance first forces \(D_S=D_R\) by taking \(I_0\) constant and opposite cosine perturbations in \(S_0\) and \(R_0\), so that the chemotactic term vanishes. Next choose
\[
S_0=1,\qquad I_0=1+\varepsilon\cos(kx),\qquad R_0=1-\varepsilon\cos(kx).
\]
At the midpoint \(x=L_x/2\), the diffusion contribution proportional to \(\Delta I_0\) vanishes, whereas
\[
\partial_x^2\log I_0=-\varepsilon^2k^2.
\]
Thus universal invariance forces \(\chi=0\). With \(\chi=0\), the preceding pairwise cosine argument forces \(D_I=D_R\), hence all three diffusion coefficients are equal. The converse follows from \(n_t=D\Delta n\).

## Verification
The accompanying `verify.py` symbolically checks reaction cancellation, the two witness calculations, and the midpoint chemotactic obstruction. Running it with Python 3 prints `VERIFY_OK`.

The primary full text explicitly prints unequal coefficients \(D_S,D_I,D_R\), the relation \(S+I+R=N>0\), homogeneous Neumann conditions, and—later—the conservative chemotactic flux. It also labels \(\iint S\,dx\,dy\) as "Total" when discussing population conservation. The exact PDE identities above distinguish that susceptible integral from conserved integrated total population.

## Relationship to prior work
Wang and Echkina formulate both the reaction-diffusion and fear/avoidance chemotactic SIR systems and use population conservation as a numerical correctness check. Their displayed equations supply the object to which the identities here apply.

Mosleh, Panico, and Efendiyev analyze a diffusive SIR model under Neumann conditions and formulate population accounting through the spatial integral of the compartment sum. Naz, Naheed, and Afzal study a diffusive SIR system with equal diffusion, a setting consistent with the sufficiency half of the pointwise constant-sum criterion. In the inspected material, neither source gives the source-specific susceptible-mass correction together with the sharp universal if-and-only-if criterion for unequal diffusion and chemotaxis.

## Limitations
This result does not establish existence, uniqueness, positivity, stability, or convergence for the PDE. It does not assess whether a particular numerical trajectory happens to have nearly constant susceptible mass over a finite plotted window. It also does not analyze unequal time-scale factors \(\tau_S,\tau_I,\tau_R\), for which reaction cancellation in the unweighted sum must be reconsidered. The originality comparison is limited by the literature actually inspected; the conservation calculation itself is elementary, while the value lies in the sharp closure criterion and its direct consequence for the stated spatial epidemic model.

## References
1. Y. Wang and E. Echkina, *From the SIR/SEIR/SVEIR Model to a Chemotactic System: Analysis of Spatiotemporal Mechanisms of Infection Spread within the Einstein Paradigm*, arXiv:2608.15164v1, 15 August 2026.
2. R. Mosleh, C. Panico, and M. Efendiyev, *Numerical Investigation of a Diffusive SIR Model: Focus on Positivity Preservation*, Mathematical Methods in the Applied Sciences, 2026, DOI: 10.1002/mma.70610.
3. R. Naz, S. Naheed, and A. Afzal, *The Exact Solutions of a Diffusive SIR Model via Symmetry Groups*, 2024, DOI: 10.1155/2024/4598831.
