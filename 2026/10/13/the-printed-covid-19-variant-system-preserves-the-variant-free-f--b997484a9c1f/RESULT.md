# The printed COVID-19 variant system preserves the variant-free face

## Finding

In the published system (12), collect all compartments assigned to the new variant as
\[
Z(t)=\bigl(f_5^{j,k}(t)\bigr)_{2\le j\le m-1,\,1\le k\le m}.
\]
Then the coordinate face
\[
Z=0
\]
is forward invariant.

Therefore, if the model starts with no variant,
\[
f_5^{j,k}(0)=0
\quad\text{for every }2\le j\le m-1,\ 1\le k\le m,
\]
then
\[
f_5^{j,k}(t)=0
\quad\text{for every }t\ge0.
\]

Consequently, system (12) as printed cannot endogenously generate the new variant from the primary-virus population. It can describe the subsequent spread and competition of a variant that is already seeded.

## Assumptions and scope

The claim concerns the finite-dimensional normalized system (12) exactly as printed in the source. The state indices satisfy
\[
2\le j\le m-1,
\qquad
1\le k\le m.
\]
The transmission modulation \(\alpha(t)\) may be the piecewise-constant locking/de-locking function used in the simulations. All model parameters retain the source's nonnegative biological interpretation.

The statement is about the mathematical creation of the variant state. It does not dispute the biological fact that real viruses mutate, and it does not invalidate simulations whose scientific question begins after a variant has already been introduced.

## Proof

Equation (12) gives the variant equations by replacing the primary-virus variables and proliferation rate with the corresponding variant variables and rate. Explicitly,
\[
\begin{aligned}
\partial_t f_5^{j,k}
={}&\alpha(t)f_1^{1,k}\,\delta_{2j}
\sum_{s=1}^{m}\sum_{r=2}^{m-1}u_r f_5^{r,s}
+\beta(1+\lambda)u_{j-1}f_5^{j-1,k}\\
&+\gamma_k w_k f_5^{j+1,k}
-\beta(1+\lambda)u_jf_5^{j,k}
-\gamma_k w_k f_5^{j,k}.
\end{aligned}
\]
At boundary indices, the source's terminal-state convention removes the out-of-range infected state; this does not change the argument.

Set every component of \(Z\) equal to zero. The infection term contains the sum of variant components, the progression and regression terms contain neighboring variant components, and both loss terms contain the current variant component. Hence
\[
\left.\partial_t f_5^{j,k}\right|_{Z=0}=0
\]
for every admissible \(j,k\), independently of the values of the healthy and primary-virus compartments.

Thus the full vector field is tangent to the coordinate face \(Z=0\). On each time interval on which \(\alpha(t)\) is constant, the finite-dimensional right-hand side is polynomial in the state variables, so solutions are unique. The zero-variant trajectory therefore remains on the face. Continuity across the finitely many switching times used by the source extends the invariance through those switches.

The source also gives a normalized population-conservation relation. The state therefore remains bounded in its population simplex, so the finite-dimensional solution extends globally. This proves
\[
Z(0)=0\Longrightarrow Z(t)=0
\quad\text{for all }t\ge0.
\]

The conclusion is stronger than saying that mutation is slow. No choice of the variant aggressiveness parameter \(\lambda\), transmission modulation \(\alpha(t)\), or primary-virus density can create a positive \(f_5\) component from exactly variant-free initial data, because none of those quantities supplies a source term on the invariant face.

## Verification

The bundled `verify.py` reconstructs the algebraic dependency pattern of the printed variant equations for a finite representative grid and substitutes zero for every variant component. It verifies that every right-hand side vanishes identically while leaving the healthy-state coefficient, transmission coefficient, progression parameters, and time-dependent modulation symbolic.

The checker is only a replay of the displayed algebraic structure. The all-\(m\) result follows analytically from the fact that each term in every variant equation contains a variant component.

## Relationship to prior work

The motivating article states that model (12) accounts for mutations and selection into variants. Its mutation section says that mutations generate the onset of variants, but the same section initializes the simulations with a positive variant state \(\varepsilon_v\). In Figures 6--8 the reported value is
\[
\varepsilon_v=0.005.
\]
The simulations therefore study competition after exogenous seeding, which is consistent with the trajectories shown, but is distinct from endogenous creation of a variant.

Earlier active-particle work by De Lillo, Delitala, and Salvatori explicitly develops mathematical machinery for virus mutation. That broader literature establishes that mutation dynamics can be represented within kinetic active-particle models; it does not imply that the specific 2022 system contains a primary-to-variant creation term.

A closely related 2022 article by Bellomo, Burini, and Outada discusses mutating viruses, variants, vaccination, and within-host competition at the modeling-program level. It does not supply a published correction that inserts a primary-to-variant source into system (12) of the motivating article.

Targeted searches using the source DOI, exact title, variant initialization, invariant-face language, and endogenous-mutation terminology did not locate a published correction of this source-specific structural point.

## Limitations

The result applies to the printed equations. Unavailable simulation code could contain an additional mutation source not shown in the article; no such implementation is asserted here.

The theorem does not say that a very small positive variant seed remains small. Once a variant is present, its transmission and within-host progression can amplify it and allow it to replace the primary strain, exactly as the source's seeded simulations illustrate.

The result also does not prescribe a unique repair. Any endogenous-mutation extension must break the invariance of \(Z=0\) through a genuine coupling from non-variant states, and population conservation would require the corresponding transfers to be balanced.

## References

1. N. Bellomo, D. Burini, N. Outada, “Multiscale models of Covid-19 with mutations and variants,” Networks and Heterogeneous Media 17 (2022), 293--310. DOI: 10.3934/nhm.2022008.
2. S. De Lillo, M. Delitala, M. C. Salvatori, “Modelling epidemics and virus mutations by methods of the mathematical kinetic theory for active particles,” Mathematical Models and Methods in Applied Sciences 19 (2009), 1405--1425. DOI: 10.1142/S0218202509003838.
3. N. Bellomo, D. Burini, N. Outada, “Pandemics of mutating virus and society: a multi-scale active particles approach,” Philosophical Transactions of the Royal Society A 380 (2022), 20210161. DOI: 10.1098/rsta.2021.0161.
