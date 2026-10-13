# Reservoir spillover removes the human endemic threshold in a coupled avian-influenza model
## Finding
Ali et al. analyze a coupled bird-human SEIR system with bird-to-bird, bird-to-human, and human-to-human transmission. They state that an all-positive endemic equilibrium is biologically feasible if and only if
\[
\mathcal R_0^b>1
\quad\text{and}\quad
\mathcal R_0^h>1.
\]
For the printed model, the second inequality is not necessary.

Assume
\[
\beta_{bh}>0,\qquad \beta_h>0
\]
and all demographic and progression parameters are positive. Then the all-positive endemic equilibrium exists exactly when
\[
\mathcal R_0^b>1.
\]
If birds are endemic, their positive infectious level creates a persistent zoonotic force of infection that produces a unique positive human equilibrium even when
\[
0<\mathcal R_0^h<1.
\]

More precisely, set
\[
\kappa=\beta_{bh}I_b^*.
\]
Whenever
\[
\mathcal R_0^b>1,
\]
we have \(\kappa>0\), and the human infectious equilibrium is the unique positive root
\[
I_h^*(\kappa)=
\frac{
-\bigl[\kappa+\mu_h(1-\mathcal R_0^h)\bigr]
+
\sqrt{
\bigl[\kappa+\mu_h(1-\mathcal R_0^h)\bigr]^2
+4\mu_h\mathcal R_0^h\kappa
}
}{2\beta_h}.
\]

The limit of this forced equilibrium distinguishes three regimes:
\[
I_h^*(\kappa)\sim
\frac{\mathcal R_0^h}{\beta_h(1-\mathcal R_0^h)}\kappa
\quad\text{for }0<\mathcal R_0^h<1,
\]
\[
I_h^*(\kappa)\sim
\frac{\sqrt{\mu_h\kappa}}{\beta_h}
\quad\text{for }\mathcal R_0^h=1,
\]
and
\[
I_h^*(\kappa)\to
\frac{\mu_h(\mathcal R_0^h-1)}{\beta_h}
\quad\text{for }\mathcal R_0^h>1
\]
as \(\kappa\downarrow0\).

Thus the human reproduction threshold controls the response to removal of the reservoir, but it does not control feasibility of human infection while positive reservoir forcing remains.

## Assumptions and scope
The bird-human model is
\[
\dot S_b=\Pi_b-\beta_bI_bS_b-\mu_bS_b,
\]
\[
\dot E_b=\beta_bI_bS_b-(\sigma_b+\mu_b)E_b,
\]
\[
\dot I_b=\sigma_bE_b-(\gamma_b+\mu_b+\alpha_b)I_b,
\]
\[
\dot R_b=\gamma_bI_b-\mu_bR_b,
\]
together with
\[
\dot S_h=\Pi_h-(\beta_{bh}I_b+\beta_hI_h+\mu_h)S_h,
\]
\[
\dot E_h=(\beta_{bh}I_b+\beta_hI_h)S_h-(\sigma_h+\mu_h)E_h,
\]
\[
\dot I_h=\sigma_hE_h-(\gamma_h+\mu_h+\alpha_h)I_h,
\]
\[
\dot R_h=\gamma_hI_h-\mu_hR_h.
\]

All recruitment, mortality, progression, and recovery parameters are positive. The theorem assumes
\[
\beta_{bh}>0,\qquad \beta_h>0.
\]
The first assumption is essential: without bird-to-human transmission, endemic birds do not force human infection. The second avoids a removable singularity in the closed form written in terms of \(\mathcal R_0^h\); the case \(\beta_h=0\) can instead be solved from the resulting linear human equilibrium equation.

The finding concerns equilibrium feasibility and its small-spillover asymptotics. It does not assert global stability of the forced endemic equilibrium.

## Proof
The source defines
\[
\mathcal R_0^b=
\frac{\beta_b\Pi_b\sigma_b}
{\mu_b(\sigma_b+\mu_b)(\gamma_b+\mu_b+\alpha_b)}
\]
and
\[
\mathcal R_0^h=
\frac{\beta_h\Pi_h\sigma_h}
{\mu_h(\sigma_h+\mu_h)(\gamma_h+\mu_h+\alpha_h)}.
\]

Its bird endemic equilibrium satisfies
\[
I_b^*=
\frac{\mu_b(\mathcal R_0^b-1)}{\beta_b}.
\]
Hence the bird components can all be positive only if
\[
\mathcal R_0^b>1.
\]
Conversely, under this inequality the source's bird formulas give positive
\[
S_b^*,\ E_b^*,\ I_b^*,\ R_b^*.
\]

Now assume
\[
\mathcal R_0^b>1
\]
and define the positive spillover force
\[
\kappa=\beta_{bh}I_b^*>0.
\]
Let
\[
A_h=(\sigma_h+\mu_h)(\gamma_h+\mu_h+\alpha_h)>0.
\]
The source derives the quadratic
\[
a(I_h^*)^2+bI_h^*+c=0
\]
with
\[
a=\beta_hA_h,
\]
\[
b=(\kappa+\mu_h)A_h-\Pi_h\sigma_h\beta_h,
\]
and
\[
c=-\Pi_h\sigma_h\kappa.
\]
Because
\[
\mathcal R_0^h=
\frac{\beta_h\Pi_h\sigma_h}{\mu_hA_h},
\]
division by \(A_h\) gives
\[
\beta_h(I_h^*)^2+
\bigl[\kappa+\mu_h(1-\mathcal R_0^h)\bigr]I_h^*
-\frac{\mu_h\mathcal R_0^h}{\beta_h}\kappa=0.
\]

The leading coefficient is positive and the constant term is strictly negative. The product of the two roots is therefore negative. The discriminant is strictly positive, so there are exactly two real roots of opposite sign. Hence there is exactly one positive human infectious equilibrium, namely
\[
I_h^*(\kappa)=
\frac{
-\bigl[\kappa+\mu_h(1-\mathcal R_0^h)\bigr]
+
\sqrt{
\bigl[\kappa+\mu_h(1-\mathcal R_0^h)\bigr]^2
+4\mu_h\mathcal R_0^h\kappa
}
}{2\beta_h}.
\]
The source's remaining equilibrium formulas then give
\[
E_h^*=
\frac{\gamma_h+\mu_h+\alpha_h}{\sigma_h}I_h^*>0,
\qquad
R_h^*=\frac{\gamma_h}{\mu_h}I_h^*>0,
\]
and
\[
S_h^*=
\frac{A_h}{\sigma_h(\kappa+\beta_hI_h^*)}I_h^*>0.
\]
Thus every component of the bird-human equilibrium is positive whenever
\[
\mathcal R_0^b>1.
\]
Since positivity of the bird infectious component already requires that inequality, it is also necessary.

For the small-spillover limits, write
\[
B(\kappa)=\kappa+\mu_h(1-\mathcal R_0^h).
\]
If
\[
0<\mathcal R_0^h<1,
\]
then \(B(0)>0\). Expanding the square root at \(\kappa=0\) gives
\[
I_h^*(\kappa)=
\frac{\mathcal R_0^h}{\beta_h(1-\mathcal R_0^h)}\kappa
+O(\kappa^2).
\]
If
\[
\mathcal R_0^h=1,
\]
the exact root becomes
\[
I_h^*(\kappa)=
\frac{-\kappa+\sqrt{\kappa^2+4\mu_h\kappa}}{2\beta_h},
\]
so
\[
I_h^*(\kappa)\sim
\frac{\sqrt{\mu_h\kappa}}{\beta_h}.
\]
Finally, if
\[
\mathcal R_0^h>1,
\]
then \(B(0)<0\), and direct passage to the limit gives
\[
I_h^*(\kappa)\to
\frac{\mu_h(\mathcal R_0^h-1)}{\beta_h}.
\]

## Verification
The bundled script `verification/verify.py` checks the coefficient reduction from the source's quadratic, the opposite-sign root property, the closed positive-root formula, positivity of the reconstructed human compartments, and the three small-spillover limits for representative exact or high-precision parameter values.

The decisive existence argument is analytic: when the bird reservoir is endemic and
\[
\beta_{bh}>0,
\]
the source's own human quadratic has negative constant term. No finite simulation or numerical root search is used to infer existence.

## Relationship to prior work
The motivating article derives a lower-triangular next-generation matrix and obtains
\[
\mathcal R_0=\max\{\mathcal R_0^b,\mathcal R_0^h\}.
\]
It also derives the human endemic quadratic used here, but its biological-feasibility summary says that the all-positive endemic equilibrium exists if and only if both component reproduction numbers exceed one. The sign of the same quadratic shows that the human condition is unnecessary once endemic birds provide positive spillover forcing.

The general phenomenon is not claimed as new. Singh, Schneider, and Myers showed in a stochastic coupled animal-human model that animal-human coupling can generate large human outbreaks even when human-to-human transmission is subcritical. Voinson et al. likewise studied recurrent infection from an endemic reservoir and showed explicitly that spillover can repeatedly sustain infection in a subcritical incidental host.

Those papers establish the broader reservoir-forcing mechanism. They do not contain the deterministic eight-compartment equilibrium quadratic of the 2026 avian-influenza model, its exact unique positive root, or the linear-versus-square-root small-spillover crossover derived above.

## Limitations
The result is an equilibrium-feasibility correction, not a global-stability theorem for the positive equilibrium.

For
\[
\mathcal R_0^b\le1,
\]
the bird subsystem cannot supply a positive endemic reservoir equilibrium. If instead
\[
\mathcal R_0^h>1,
\]
a human-only endemic equilibrium can still exist with disease-free birds; this boundary equilibrium is distinct from the all-positive equilibrium analyzed here.

At
\[
\beta_{bh}=0,
\]
the forcing mechanism disappears and the usual human threshold is recovered. The result therefore does not say that a subcritical human infection can persist autonomously.

## References
1. A. Ali, A. Grine, M. Arfan, J. Ullah, M. A. Cengiz, M. Asif, “Mathematical Modeling of Avian Influenza Transmission with Neural Network-Based Simulation,” Mathematics 14 (2026), 1693. DOI: 10.3390/math14101693.
2. S. Singh, D. J. Schneider, C. R. Myers, “Using multitype branching processes to quantify statistics of disease outbreaks in zoonotic epidemics,” Physical Review E 89 (2014), 032702. DOI: 10.1103/PhysRevE.89.032702.
3. M. Voinson, A. Alvergne, S. Billiard, C. Smadi, “Stochastic dynamics of an epidemic with recurrent spillovers from an endemic reservoir,” Journal of Theoretical Biology 457 (2018), 37–50. DOI: 10.1016/j.jtbi.2018.08.017.
