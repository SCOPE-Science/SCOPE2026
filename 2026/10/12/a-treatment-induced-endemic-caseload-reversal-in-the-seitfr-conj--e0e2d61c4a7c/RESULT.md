# A treatment-induced endemic-caseload reversal in the SEITFR conjunctivitis model

## Finding
In the six-compartment conjunctivitis model of Al-Hdaibat et al. [1], increasing treatment initiation can strictly **decrease** the basic reproduction number while **increasing** the fraction of the endemic population occupying the exposed, infectious, treated, or detected treatment-failure classes. There is an exact parameter criterion for this reversal at zero treatment initiation and a strictly positive-parameter example in which the clinical caseload has exactly one interior maximum, although the reproduction number decreases at every treatment rate.

More precisely, fix all parameters other than the treatment-initiation rate \(\kappa\) and let \(\mathcal B(\kappa)=(E^*+I^*+T^*+F^*)/N^*\), where asterisks denote the unique endemic equilibrium when \(\mathcal R_0(\kappa)>1\). With the notation below, if \(\mathcal R_0(0)>1\) and \(b>\epsilon a\), then \(\mathcal R_0'(\kappa)<0\) at every nonnegative rate, whereas
\[
\mathcal B'(0)>0\quad\Longleftrightarrow\quad
\frac{u_1v_0-u_0v_1}{u_0(u_0+v_0)}
>\frac{b-\epsilon a}{ab(\mathcal R_0(0)-1)}.
\]
The derivative at zero is the right derivative of the endemic branch. Thus this inequality is an exact local reversal criterion, not merely a sufficient estimate.

A rational example demonstrates that the criterion is realizable. In that example the endemic branch exists for \(0<\kappa<105/8\), and
\[
\mathcal R_0(\kappa)=\frac{42(\kappa+5)}{5(10\kappa+21)},\qquad
\mathcal B(\kappa)=\frac{(105-8\kappa)(60\kappa+31)}{462(\kappa+5)(10\kappa+21)}.
\]
The latter function increases to its unique maximum at
\[
\kappa_* = \frac{29\sqrt{536655}-8295}{9460}\approx1.36886413194756
\]
and then decreases to zero at the disease-free threshold, even though \(\mathcal R_0\) is strictly decreasing throughout.

## Assumptions and scope
The source model [1, Eq. (2.2)] is defined for \(S,E,I,T,F,R\ge0\), \(N=S+E+I+T+F+R>0\), and
\[
\begin{aligned}
\dot S&=\Pi-(\lambda+\mu)S+\delta R, &
\dot E&=\lambda S-(\Phi+\mu)E,\\
\dot I&=\Phi E-(\alpha_1+\kappa+\mu)I, &
\dot T&=\kappa I-(\alpha_2+\Psi+\mu)T,\\
\dot F&=\Psi T-(\alpha_3+\mu)F, &
\dot R&=\alpha_1I+\alpha_2T+\alpha_3F-(\mu+\delta)R,
\end{aligned}
\]
with standard-incidence force \(\lambda=\beta(I+\epsilon T)/N\). The detected failure class \(F\) is isolated/nontransmitting in this specification. Assume \(\Pi,\mu,\beta,\Phi,\alpha_1,\alpha_2,\alpha_3,\Psi,\epsilon>0\), \(\delta\ge0\), and \(\kappa\ge0\), with \(0<\epsilon\le1\). We vary only \(\kappa\). For \(\kappa>0\) with \(\mathcal R_0>1\), every equilibrium compartment is strictly positive. At \(\kappa=0\), \(T^*=F^*=0\), and the other endemic equilibrium components are positive; all derivative assertions there are understood one-sidedly.

Introduce strictly positive constants
\[
 a=\alpha_1+\mu,\quad b=\alpha_2+\Psi+\mu,\quad
 c=\alpha_3+\mu,\quad C=\frac{\beta\Phi}{\Phi+\mu},
\]
\[
\begin{aligned}
 u_0&=\frac a\Phi+1,&u_1&=\frac1\Phi+\frac1b+\frac\Psi{bc},\\
 v_0&=\frac{\alpha_1}{\mu+\delta},&
 v_1&=\frac1{\mu+\delta}\left(\frac{\alpha_2}b+\frac{\alpha_3\Psi}{bc}\right).
\end{aligned}
\]
Here \(\mathcal B\) is a *snapshot occupancy* of four clinical compartments, **not** incidence, transmission potential, resource utilization weighted by case severity, or cumulative infections. In particular, the failure class contributes to \(\mathcal B\) despite being absent from \(\lambda\).

## Proof
Summing the six equations gives \(\dot N=\Pi-\mu N\), so any equilibrium has \(N^*=\Pi/\mu\). The equilibrium transitions imply
\[
 E^*=\frac{a+\kappa}{\Phi}I^*,\quad
 T^*=\frac\kappa b I^*,\quad
 F^*=\frac{\Psi\kappa}{bc}I^*,\quad
 R^*=(v_0+v_1\kappa)I^*.
\]
For \(I^*>0\), the equilibrium exposed equation and force of infection imply
\[
 \frac{S^*}{N^*}=\frac1{\mathcal R_0(\kappa)},\qquad
 \mathcal R_0(\kappa)=\frac{C(b+\epsilon\kappa)}{b(a+\kappa)}.
\]
The population identity then gives the unique candidate
\[
 \frac{I^*}{N^*}=\frac{1-1/\mathcal R_0(\kappa)}{u_0+v_0+(u_1+v_1)\kappa}.
\]
When \(\mathcal R_0>1\) this is positive, and substitution into the six equilibrium equations (including \(\dot S=0\)) proves existence and uniqueness. Summing \(E^*,I^*,T^*,F^*\) yields the exact occupancy law
\[
\boxed{\displaystyle
\mathcal B(\kappa)=\left(1-\frac1{\mathcal R_0(\kappa)}\right)
\frac{u_0+u_1\kappa}{u_0+v_0+(u_1+v_1)\kappa}.}
\]
Differentiating the reproduction number shows
\[
 \mathcal R_0'(\kappa)=\frac{C(\epsilon a-b)}{b(a+\kappa)^2},
\]
so \(b>\epsilon a\) implies strict decrease for all \(\kappa\ge0\). Logarithmic differentiation of the positive occupancy on the endemic branch gives
\[
\frac{\mathcal B'(0)}{\mathcal B(0)}
=\frac{\epsilon a-b}{ab(\mathcal R_0(0)-1)}
+\frac{u_1v_0-u_0v_1}{u_0(u_0+v_0)},
\]
which proves the exact initial-increase criterion.

For an explicit instance set
\[
\Pi=\mu=\frac1{10},\quad \Phi=1,\quad
\alpha_1=2,\quad\alpha_2=\alpha_3=\frac1{10},\quad
\Psi=\frac3{10},\quad\epsilon=\frac1{10},\quad
\beta=\frac{231}{50},\quad\delta=0.
\]
All positive-rate assumptions hold, with \(\delta=0\) allowed. Direct reduction gives
\[
 (u_0,u_1,v_0,v_1)=\left(\frac{31}{10},6,20,5\right)
\]
and the stated rational functions for \(\mathcal R_0(\kappa)\) and \(\mathcal B(\kappa)\). They satisfy
\[
\mathcal R_0'(\kappa)=-\frac{1218}{5(10\kappa+21)^2}<0.
\]
The endemic condition \(\mathcal R_0>1\) is exactly \(0\le\kappa<105/8\). Differentiating the occupancy yields
\[
\mathcal B'(\kappa)=
-\frac{5(18920\kappa^2+33180\kappa-80871)}
{462(\kappa+5)^2(10\kappa+21)^2}.
\]
The numerator quadratic has exactly one positive zero because its leading coefficient and linear coefficient are positive and its constant coefficient is negative. It is negative at \(\kappa=1\) and positive at \(\kappa=2\), so the unique positive root \(\kappa_*\in(1,2)\) gives a strict interior maximum. The exact formula for that root is given above. In particular, for *two strictly positive treatment rates*,
\[
\begin{array}{c|cc}
\kappa & \mathcal R_0(\kappa)&\mathcal B(\kappa)\\\hline
\frac1{10}&\frac{1071}{550}&\frac{19277}{259182}\\
1&\frac{252}{155}&\frac{1261}{12276}
\end{array}
\]
so \(\mathcal R_0(1)<\mathcal R_0(1/10)\) but \(\mathcal B(1)>\mathcal B(1/10)\), with every equilibrium compartment strictly positive at both rates. This proves the claimed inversion and its one-peak structure.

## Verification
Run `python3 verify.py` using only the Python standard library. It checks exact rational parameter identities, the polynomial coefficients in both derivative formulas, the one-positive-root sign pattern, the exact burden and threshold fractions, the strict reverse ordering between the two nonzero treatment rates, and all six equilibrium residuals plus population normalization at several positive parameter values. Successful replay prints `VERIFY_OK`. The analytic derivation above, not the finite sample of residual checks, establishes the quantified parameter criterion and continuous-treatment assertions.

## Relationship to prior work
Al-Hdaibat et al. [1, Theorems 5 and 9, Eqs. (3.2), (3.18)–(3.20), and (4.6)–(4.10)] establish the reproduction-number formula, endemic equilibrium, and the sign criterion for the effect of treatment initiation on \(\mathcal R_0\). Their complete analysis concerns transmission threshold and equilibrium stability; it does not derive or order the **combined four-stage caseload** \(E^*+I^*+T^*+F^*\) under changes in treatment initiation. The present result supplies a different, occupancy-based comparison and gives an exact counterexample to identifying threshold improvement with declining stage-aggregated occupancy.

Incomplete-treatment models were studied by Huo and Feng [2], but their vaccinated/latent/infectious/treated model allows treatment failure to return cases to infectious or latent states; it does not contain the isolated post-treatment-failure stage whose residence time drives this example. Work on migration-dependent reproduction-number/prevalence relationships [3] likewise addresses a different intervention and compartment structure. Earlier literature on prevalence versus transmission thresholds shows why these indicators should not be conflated; this result makes no priority claim about the general qualitative distinction. No claim of contradiction with [1] is made: its treatment sensitivity concerns \(\mathcal R_0\), not \(\mathcal B\).

## Limitations
The parameter witness is an exact mathematical scenario, not a calibration to a clinical outbreak. A higher equilibrium fraction in the four compartments does not imply more infectious people in the community, increased incidence, or worse clinical outcomes; in the source model the \(F\) compartment is explicitly assumed isolated. The theorem concerns equilibrium branch values and does not prove a dynamical comparative-statics ordering of transient trajectories, intervention costs, or observed treatment data. The sign criterion is local at \(\kappa=0\); the complete unimodality statement is for the specified rational parameter family only. Published background and repository searches cannot exclude all prior unpublished or unindexed work. Independent replication or audit has not been performed.

## References
[1] B. Al-Hdaibat, M. A. Safi, A. Almuneef, Z. Alqahtani, M. H. DarAssi, O. Attoum, *Bifurcation and stability analysis of an SEITFR conjunctivitis model with standard incidence and treatment failure*, AIMS Mathematics 11(8) (2026), 26640–26676, DOI: 10.3934/math.20261069, first public 2026-08-25. Primary MSC2020: 92D30.

[2] H.-F. Huo and L.-X. Feng, *Global Stability of an Epidemic Model with Incomplete Treatment and Vaccination*, Discrete Dynamics in Nature and Society (2012), article 530267, DOI: 10.1155/2012/530267.

[3] *Effects of Dispersal Asymmetry on Disease Spread*, SIAM Journal on Applied Mathematics, DOI: 10.1137/24M1648776 (different multipatch model, consulted for comparison of reproduction number and prevalence).
