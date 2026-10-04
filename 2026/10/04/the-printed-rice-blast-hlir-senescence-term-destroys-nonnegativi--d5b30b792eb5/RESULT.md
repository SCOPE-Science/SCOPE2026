# The printed rice-blast HLIR senescence term destroys nonnegativity after the senescence switch

## Finding

The rice-blast HLIR model in Tabonglek, Khan, and Humphries uses
\[
\frac{\partial R(x,t)}{\partial t}
=
\frac{1}{p}I(x,t)
-h(t-t_s)r_s\bigl(H(x,t)+L(x,t)+I(x,t)\bigr)
\]
for the removed density. Here the source defines
\[
h(t-t_s)=0\quad\text{for }t\le t_s,
\qquad
h(t-t_s)=1\quad\text{for }t>t_s,
\]
and states nonnegative initial data for all five state variables.

This equation violates forward invariance of the nonnegative cone. Take spatially constant disease-free initial data
\[
H(x,0)=H_0>0,
\qquad
L(x,0)=I(x,0)=R(x,0)=u(x,0)=0.
\]
For \(0\le t\le t_s\), the infection and spore variables remain zero, the removed variable remains zero, and the healthy density satisfies
\[
\dot H
=r_GH\left(1-\frac{H}{K_G}\right).
\]
Thus \(H(t_s)>0\). At the instant after senescence activates,
\[
\left.\frac{\partial R}{\partial t}\right|_{t_s^+}
=-r_sH(t_s)<0.
\]
Hence \(R\) immediately becomes negative.

Using the source values
\[
H_0=0.015,
\quad r_G=0.209,
\quad K_G=5.524,
\quad r_s=0.103,
\quad t_s=95,
\]
the logistic solution gives
\[
H(t_s)
=
\frac{K_GH_0e^{r_Gt_s}}
{K_G+H_0(e^{r_Gt_s}-1)}
\approx5.5239951659,
\]
so
\[
\left.\frac{\partial R}{\partial t}\right|_{t_s^+}
\approx-0.5689715021.
\]

The explicit numerical scheme printed in the source reproduces the same problem. On the disease-free trajectory, \(R\) is zero until the switch. The first step evaluated with \(h=1\) has
\[
R^{n+1}=R^n-\Delta t\,r_sH^n<0.
\]
Therefore the obstruction is not caused by a stability restriction of the finite-difference method; it is already present in the differential model.

## Assumptions and scope

The claim uses exactly the host equations, Heaviside convention, and nonnegative-state interpretation printed in the source. All rates satisfy the source's positivity assumptions. The spatially constant disease-free data are admissible for the nonlocal spore equation because \(u\equiv0\) makes both dispersal and spore production vanish.

No claim is made that the particular fitted disease-outbreak trajectories plotted in the paper necessarily cross into negative \(R\). The finding is stronger at the model level: the equations do not preserve the state space they declare, so positivity cannot be guaranteed for the class of nonnegative initial conditions.

The result also does not impose one unique corrected senescence mechanism. Biological interpretation determines whether senesced tissue should move into the removed class or leave the modeled host total.

## Proof

Set
\[
L(x,0)=I(x,0)=R(x,0)=u(x,0)=0
\]
and let \(H(x,0)=H_0>0\) be spatially constant. Because the spore-production functional contains a factor \(I\), one has \(f\equiv0\). With \(u\equiv0\), the nonlocal dispersal operator also vanishes. Hence \(u\equiv0\).

The latent equation then has zero right-hand side when \(L=0\), so \(L\equiv0\). The infectious equation likewise gives \(I\equiv0\). For \(t\le t_s\), the Heaviside factor is zero, and therefore the removed equation gives \(R\equiv0\).

On that interval,
\[
N=H
\]
and the healthy equation reduces to
\[
\dot H=r_GH\left(1-\frac{H}{K_G}\right).
\]
For \(H_0>0\), its solution is
\[
H(t)=
\frac{K_GH_0e^{r_Gt}}
{K_G+H_0(e^{r_Gt}-1)},
\]
which is strictly positive for every finite \(t\).

At \(t=t_s^+\), the source convention changes the Heaviside factor from zero to one. Since \(I=L=R=0\) and \(H(t_s)>0\),
\[
\left.\frac{\partial R}{\partial t}\right|_{t_s^+}
=
-r_sH(t_s)<0.
\]
Standard one-sided differentiability then gives \(R(t)<0\) for all sufficiently small \(t>t_s\). Thus the nonnegative cone is not forward invariant.

The printed forward-Euler update has the same component
\[
R_i^{n+1}
=
R_i^n
+\Delta t\left[
\frac{1}{p}I_i^n
-h^nr_s(H_i^n+L_i^n+I_i^n)
\right].
\]
On the same disease-free trajectory, at the first index with \(h^n=1\),
\[
R_i^n=I_i^n=L_i^n=0,
\qquad H_i^n>0,
\]
so
\[
R_i^{n+1}=-\Delta t\,r_sH_i^n<0.
\]

Finally, summing the source equations for \(H,L,I,R\) cancels infection, latency, and disease-removal transfers and yields
\[
\frac{\partial N}{\partial t}
=
r_GN\left(1-\frac{N}{K_G}\right)
-2h(t-t_s)r_s(H+L+I),
\]
which is exactly the total-density equation printed earlier in the paper. The extra loss is therefore internally propagated through the model rather than being a transcription confined to the numerical formula.

## Verification

The bundled checker evaluates the closed-form disease-free trajectory at the source's parameter values and verifies
\[
H(95)\approx5.5239951659
\]
and
\[
-r_sH(95)\approx-0.5689715021.
\]
It also symbolically verifies the sum of the four host equations and the negative first finite-difference update after the senescence switch.

No finite experiment is used to prove the sign obstruction. The counterexample is exact for every \(H_0>0\), \(r_s>0\), and finite \(t_s\).

## Relationship to prior work

Tabonglek, Khan, and Humphries (2022), DOI 10.3934/math.2023125, introduce the HLIR extension considered here. Their primary full text explicitly declares nonnegative initial conditions, defines the senescence switch, prints the negative \(H+L+I\) term in the removed equation, and repeats it in the finite-difference method.

The immediate predecessor by Tabonglek, Humphries, and Khan (2022), DOI 10.3390/sym14061131, contains only healthy-host and spore variables and explicitly recommends separating the host population into HLIR classes as future work. It therefore does not contain the removed-compartment senescence equation or this positivity issue.

Rimbaud et al. (2018), DOI 10.1111/eva.12681, use an HLIR architecture for plant epidemics in which infectious hosts become epidemiologically inactive in the removed class. That literature supports the standard compartmental interpretation of \(R\), but it does not analyze the rice-blast senescence term or imply this source-specific counterexample.

Searches by exact title, DOI, the phrases “removed density,” “senescence,” “nonnegative,” and “positivity,” and by equivalent HLIR compartment terminology found no published correction or prior statement of this model-specific sign obstruction.

## Limitations

The result diagnoses the printed mathematical model. It does not reconstruct the authors' implementation code, which was not part of the inspected article, and it does not claim that every plotted fitted trajectory necessarily has negative \(R\).

There is more than one biologically plausible repair. If senescence transfers tissue into the removed class, the corresponding transfer into \(R\) must be nonnegative. If senescence removes tissue from the modeled host population, then a loss term should act on the compartment being depleted rather than force a boundary value \(R=0\) negative. Selecting between those interpretations requires biological modeling choices beyond the mathematical obstruction proved here.

## References

1. S. Tabonglek, A. Khan, U. W. Humphries, “An extension of mathematical model for severity of rice blast disease,” AIMS Mathematics 8 (2023), 2419–2434. DOI: 10.3934/math.2023125. First published 2 November 2022.
2. S. Tabonglek, U. W. Humphries, A. Khan, “Mathematical Model for Rice Blast Disease Caused by Spore Dispersion Affected from Climate Factors,” Symmetry 14 (2022), 1131. DOI: 10.3390/sym14061131.
3. L. Rimbaud et al., “Mosaics, mixtures, rotations or pyramiding: What is the optimal strategy to deploy major gene resistance?”, Evolutionary Applications 11 (2018), 1791–1810. DOI: 10.1111/eva.12681.
